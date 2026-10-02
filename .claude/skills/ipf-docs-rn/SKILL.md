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

## Branch rule — never change `main`

Never make changes directly on `main`. Check the current branch (`git branch --show-current`)
before editing any file (including this skill and the release notes). If `main` is checked out
and the user requests changes:

1. Tell the user that changes cannot be made directly on `main`.
2. Ask the user for a name for a new branch.
3. Create and switch to that branch (`git switch -c <name>`).
4. Apply the requested changes only on the new branch.

Read-only work (fetching Jira tickets, showing a draft in chat) is fine on `main`; the rule
applies as soon as a file would be written.

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
separate tool call). **Do not include Jira ticket keys (e.g. `NIM-25309`) or hyperlinks of any
kind in the draft** — the user does not need them; show plain item text only. Keep the key
mapping in your own context so you can still answer follow-up questions about a specific item
(the user can refer to an item by its wording), and mention a ticket key only if the user
asks for it. Ask if they want changes — added detail, rewording, reordering, or removed
items. Since the full ticket
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

The text written to the docs file must contain no internal ticket references (Jira keys like
`NIM-25309`, or any link to `ipfabric.atlassian.net`). The Step 5 draft already omits them, so
there should be nothing to strip — but double-check before writing. Release notes are
customer-facing and must not expose internal project/ticket identifiers; existing entries in
this file never reference ticket keys — match that.

## Step 7 — Low-level release notes (LLRN)

When the user asks to update the low-level release notes (LLRN) for a version, **do not run
`jira_ai_agent.py`** (that is the patch release-notes generator). The script that regenerates
LLRN is `jira_release_notes.py` (needs `JIRA_USER`/`JIRA_PASS` in `.env` and rewrites every 8.x
file), so instead update the file by hand from the Jira connector data, in the same format the
script produces. Follow the Branch rule first (e.g. `LLRN-<version>`, branched from `main` so
it doesn't mix with the release-notes branch).

1. **Fetch** NIM and DOS issues for the `fixVersion` with the Step 2 JQL (fields `summary,
   issuetype, priority, labels`). IPF is not part of LLRN. The Step 2 data can be reused.
2. **File**: `docs/releases/release_notes_low-level/<major>.x/<major>.<minor>.md`. Insert a
   new `## <version>` section directly above the previous patch version (newest first).
3. **Group by issue type**, in this order, omitting empty ones, each with its intro sentence
   copied from an existing section of the file: `### Epics`, `### Stories`, `### Bugs`,
   `### Tasks`, `### Sub-Tasks` (Jira `Sub-task`).
4. **Item format**: `` - `KEY-123` -- <Priority> -- <summary> `` — here the ticket key **is**
   kept (unlike the customer-facing release notes). Clean the summary like the script's
   `clean_title`: strip team codes (`[DP]`, `[PE]`, …) and version tags (`[7.11]`,
   `[7.11/7.12]`), collapse spaces, trim leading/trailing dashes.
5. **Sort by priority within each type**: Highest, High, Medium, Low, Lowest, then by key
   within the same priority.
6. **Update the issue count** in the page's intro paragraph (`...contains a total of N fixed
   issues.`) by adding the number of issues fetched for the new version.
7. **Do not touch** older version sections.
8. Show the user the diff (`git diff <file>`) and ask before committing.

### Check for non-public information before writing

LLRN pages are public, and ticket summaries are copied verbatim. Before writing, scan every
summary (and the release-note items in Step 4) for non-public data and **tell the user about
each hit** — quote the ticket and the offending text, and propose a sanitized wording — instead
of silently publishing or silently altering it:

- Customer, partner or company names (e.g. in `Found on <customer>` or `<customer> prod` style
  text)
- IP addresses, hostnames/device names from a real network, MAC addresses, serial numbers,
  usernames, credentials, tokens
- Internal URLs (SharePoint, Slack, privatebin, `atlassian.net`) and support-case IDs such as
  `NSD-1234`
- Version or team information that the README says to remove from ticket summaries (e.g.
  `[DP]`, `[8.0]`; the cleanup in step 4 handles the bracketed forms, but check for
  versions written in plain text)

Vendor/product/platform names (Cisco NX-OS, FortiGate, AWS) are fine. If unsure, ask the user.
Descriptions often contain such data even when the summary does not — never copy description
text into the notes beyond the specific technical facts allowed in Step 4.

## Key differences from `jira_ai_agent.py`

| Original script | This skill |
|---|---|
| `requests` + Basic Auth (`JIRA_USER`/`JIRA_PASS`) against `rest/api/3/search/jql` | Atlassian MCP connector tools (`searchJiraIssuesUsingJql`) — no credentials to manage |
| PydanticAI `Agent('openai:gpt-5.6', ...)` with a JSON-schema system prompt, manual JSON extraction from the model's reply | Claude drafts the `ReleaseNotes`-shaped content directly in the conversation — no external API key, no JSON parsing/repair step |
| Separate `openai:gpt-4o` "conversation agent" for interactive refinement | Same conversation, same context — just keep talking |
| Saves to a local `release_notes_<version>.md` scratch file | Inserted into the project's actual `docs/releases/release_notes/<major>.md`, matching existing formatting |
