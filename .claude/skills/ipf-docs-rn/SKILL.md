---
name: ipf-docs-rn
description: Generate IP Fabric patch/major release notes (Improvements + Bug Fixes) from Jira tickets for a given fixVersion, using the connected Atlassian Jira tools instead of OpenAI. Use when the user asks to draft release notes, LLRN/RN summaries, or a changelog for a fixVersion like "7.5.21" or "8.0.10".
metadata:
  origin: ported from jira_ai_agent.py (OpenAI/PydanticAI) to run natively on Claude + the Atlassian MCP connector
---

# Jira Release Notes Agent

Recreates `jira_ai_agent.py` without OpenAI: fetch Jira tickets for a `fixVersion` via the
Atlassian MCP connector, categorize them, and have Claude itself (not an external LLM API)
write the concise "Improvements" / "Bug Fixes" release note items, then refine them with the
user conversationally.

## When to use

The user gives (or you ask for) a `fixVersion`, e.g. `7.5.21` or `8.0.10`, and wants release
notes drafted from the Jira tickets tied to that version.

## Prerequisites

- The Atlassian Jira MCP connector must be available in this session (tools prefixed
  `mcp__<atlassian-connector-id>__...`, e.g. `searchJiraIssuesUsingJql`, `getJiraIssue`).
  These replace the script's raw `requests` calls against `rest/api/3/search/jql` — no
  `JIRA_USER`/`JIRA_PASS` environment variables needed, the connector handles auth.
- No `OPENAI_API_KEY` or PydanticAI `Agent` is used. Claude drafts the summaries itself,
  directly in the conversation.

## Step 1 — Determine release type

```
match = re.match(r"^(\d+)\.(\d+)\.(\d+)", fix_version)
patch = int(match.group(3))
release_type = "major" if patch <= 2 else "patch"
```

- **major** (`patch <= 2`, e.g. `x.y.0`, `x.y.1`, `x.y.2`): focus on new features and
  important improvements — this skill still only emits Improvements/Bug Fixes; for a full
  major-version writeup (Breaking Changes, Known Issues, etc.) tell the user this skill
  covers only the two standard sections and point them at manual authoring for the rest.
- **patch**: fixes and improvements only. This is the common case.

## Step 2 — Fetch issues from Jira

Project keys: `NIM`, `DOS`, `IPF`.

For each project, run this JQL via `searchJiraIssuesUsingJql` (paginate until no more
results; request fields `summary, issuetype, priority, description, labels, issuelinks`):

```
project = {PROJECT} AND fixVersion = "{fix_version}"
{" AND (resolution = Done) " if PROJECT == "NIM" else ""}
AND (resolution IS NOT EMPTY OR statusCategory = Done)
AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY)
ORDER BY key
```

Collect all issues across the three projects into one list. If nothing comes back, tell the
user no issues were found for that fixVersion and stop.

## Step 3 — Categorize

Two buckets only:

- `issuetype == "Bug"` → **Bug Fixes**
- everything else (Story, Task, Improvement, Sub-task, …) → **Improvements**

## Step 4 — Draft release note items (Claude does this directly, no external API)

For each ticket, write **one sentence** using only facts present in that ticket's summary,
description, and labels. Apply this style guide verbatim (it's the same guide the original
script gave to GPT):

1. This is for **patch** release notes — fixes and improvements only.
2. Extract and include specific details actually present in the ticket:
   - Device vendor/family, whenever mentioned (see label conventions below).
   - Specific commands, error messages, field/column/table names, API endpoints.
   - Version numbers **only** if the ticket explicitly says it's a regression and names the
     version that introduced it.
   - Do **not** invent generic consequences or benefits not stated in the ticket
     ("to improve performance", "for better security", etc.).
3. Describe **what was done**, not why — state facts, not assumptions.
4. Identify vendor/family for each ticket by checking, in order:
   1. Labels with `@vendor` (e.g. `@cisco`, `@juniper`, `@arista`, `@fortinet`, `@paloalto`)
   2. Labels with `@family` (e.g. `@nxos`→NX-OS, `@iosxe`→IOS-XE, `@eos`→EOS,
      `@fortigate`→FortiGate)
   3. Labels with `!technology` (e.g. `!aci`→ACI, `!bgp`→BGP, `!vlan`→VLAN)
   4. Vendor names mentioned in the summary (Cisco, Juniper, Arista, Fortinet, Palo Alto, …)
   5. Vendor/family names mentioned in the description (NX-OS, IOS-XE, EOS, FortiGate,
      JunOS, ASA, PAN-OS, …)
5. Grouping rule — apply after drafting every individual sentence:
   - **Only one** ticket for a given vendor/family → integrate the vendor naturally into the
     sentence, **no prefix**:
     - ✅ `Fixed empty MAC address table issue on Juniper devices`
     - ❌ `Juniper: Fixed empty MAC address table issue` / `Juniper devices fix: ...`
   - **Two or more** tickets for the same vendor/family → group under one parent line with
     sub-bullets:
     ```
     - Cisco NX-OS fixes:
         - Fixed MAC address table parsing
         - Corrected VLAN interface handling
         - Resolved BGP neighbor state tracking
     ```
   - Normalize variant names to one canonical label before grouping/counting, e.g.
     "Cisco NX-OS" / "Cisco Nexus" / "NX-OS" → **Cisco NX-OS**; "Fortinet FortiGate" /
     "FortiGate" → **Fortinet FortiGate**; "Arista EOS" / "EOS" / "Arista" → **Arista EOS**.
   - Never group unrelated vendors/technologies together.
6. Only add a reason/impact clause when the change is complex enough to need context or the
   impact is non-obvious — and even then, only if that context is present in the ticket.
7. Functional-area grouping — once **Improvements** or **Bug Fixes** has enough items to span
   distinct areas of the product, group items under `####` subheadings by functional area
   before applying the vendor grouping rule above within each subheading. Pick subheadings
   from what the tickets are actually about, e.g.:
   - **Path Lookup** — path lookup/E2E path lookup engine, security evaluation, VDOM/zone
     traversal.
   - **Discovery** — discovery jobs, cloud discovery (Azure/AWS/GCP), inventory attribution,
     snapshot handling.
   - **Parsing** — vendor CLI command parsing/regex issues feeding technology tables.
   - **Tables/API** — REST API endpoints, table queries, JSON path/field bugs.
   - **Security/Access** — auth, roles, API tokens, permissions/policies.
   - **Extensions** — extension lifecycle (register/build/run/delete).
   - Add or rename subheadings to fit the actual tickets rather than forcing them into this
     list; skip this step entirely for a short list of tickets that all fall in one area —
     flat bullets are the default and match most existing patch entries in the docs.

Categories to populate (only these two; omit a section if it has no items):

- **Improvements** — enhancements, vendor support additions, GUI changes, path lookup
  improvements, network discovery improvements, experimental features.
- **Bug Fixes** — all bug fixes/corrections: parsing, algorithm, UI, performance, API, or
  any other issue resolution.

## Step 5 — Show a draft, then refine conversationally

Present the drafted Improvements/Bug Fixes lists to the user as normal chat output (not a
separate tool call), with each item linked to its Jira ticket key so the user can trace it
back and ask follow-up questions. Ask if they want changes — added detail, rewording,
reordering, removed items, or questions about a specific ticket key. Since the full ticket
data is already in context, answer directly and produce an updated list; there's no need for
a second "conversation agent" or JSON round-tripping — that machinery in the original script
existed only to work around calling an external API.

## Step 6 — Place the result in the docs

This repo's human-authored release notes live at
`docs/releases/release_notes/<major>.<minor>.md` (e.g. `docs/releases/release_notes/8.0.md`),
with each patch version as its own `## vX.Y.Z (<date>; GA)` heading containing `### Improvements`
and `### Bug Fixes` subsections — see existing entries in that file for the exact style. Once
the user approves the draft, ask whether to insert it under a new version heading in the
relevant file (creating the heading in the right place, newest-first) rather than just leaving
it in chat, and only write the file after they confirm.

**Before writing to the docs file**, strip every internal ticket reference (Jira keys like
`NIM-25309`, and any link to `ipfabric.atlassian.net`) from the text. Ticket keys are useful
in the chat draft for traceability with the user, but release notes are customer-facing and
must not expose internal project/ticket identifiers. Existing entries in this file never
reference ticket keys — match that.

## Key differences from `jira_ai_agent.py`

| Original script | This skill |
|---|---|
| `requests` + Basic Auth (`JIRA_USER`/`JIRA_PASS`) against `rest/api/3/search/jql` | Atlassian MCP connector tools (`searchJiraIssuesUsingJql`) — no credentials to manage |
| PydanticAI `Agent('openai:gpt-5.6', ...)` with a JSON-schema system prompt, manual JSON extraction from the model's reply | Claude drafts the `ReleaseNotes`-shaped content directly in the conversation — no external API key, no JSON parsing/repair step |
| Separate `openai:gpt-4o` "conversation agent" for interactive refinement | Same conversation, same context — just keep talking |
| Saves to a local `release_notes_<version>.md` scratch file | Inserted into the project's actual `docs/releases/release_notes/<major>.md`, matching existing formatting |
