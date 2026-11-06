---
name: ipf-docs-rn
description: Generate IP Fabric release notes (Improvements + Bug Fixes) and low-level release notes (LLRN) from Jira tickets for a given fixVersion, using the connected Atlassian Jira tools instead of OpenAI. Use when the user asks to draft release notes, LLRN/RN summaries, or a changelog for a fixVersion like "7.5.21", "8.0.10" or a new branch like "8.2.0", or asks to refresh/update the LLRN.
metadata:
  origin: ported from jira_ai_agent.py (OpenAI/PydanticAI, since removed from the repo) and jira_release_notes.py (LLRN) to run natively on Claude + the Atlassian MCP connector
---

# Jira Release Notes Agent

Recreates two repo scripts without OpenAI or Jira credentials, using the Atlassian MCP
connector:

- `jira_ai_agent.py` (since removed from the repo; this skill took over its job) — fetch Jira
  tickets for a `fixVersion`, categorize them, and have Claude itself (not an external LLM
  API) write the concise "Improvements" / "Bug Fixes" release note items, then refine them
  with the user conversationally (Steps 1–6).
- `jira_release_notes.py` — generate the low-level release notes (LLRN) from Jira and check
  the last three release branches for LLRN updates (Step 7).

## When to use

The user gives (or you ask for) a `fixVersion`, e.g. `7.5.21`, `8.0.10` or `8.2.0`, and wants
release notes and/or LLRN generated from the Jira tickets tied to that version.

## Step 0 — Pick the workflow

Decide what to run from the requested version and the user's wording, and tell the user which
workflow you picked before fetching anything:

| Request | Run |
|---|---|
| The user says to run only the LLRN ("just LLRN", "only low-level release notes", …) | **LLRN only** — Step 7 |
| New branch, no patch release yet: `x.y.0` (e.g. `8.2.0`) | **LLRN only** — Step 7. The `x.y.0` release notes are a full major-version writeup authored by hand, not by this skill. |
| Patch release: `x.y.z` with `z >= 1` (e.g. `8.1.7`) | **Release notes + LLRN** — Steps 1–6 for the requested version, then Step 7 |

Step 7 always runs the three-branch look back, whichever workflow is picked.

For `x.y.1` and `x.y.2`, check `docs/releases/release_notes/<major>.<minor>.md` first:
early patches usually have no `## vX.Y.Z` heading of their own (they are covered by the
major-version writeup), so ask whether the user wants a release-notes entry or LLRN only.

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

This step does what `jira_release_notes.py` does, through the Jira connector. Do not run
`jira_release_notes.py`: it needs `JIRA_USER`/`JIRA_PASS` in `.env`, only refreshes
the branches its hard-coded filter allows (currently `8.1` and later), and rewrites each
branch file from scratch, which drops any summary that was sanitized by hand. Update the files
by hand instead, in the same format the script produces.

Follow the Branch rule first. In the **Release notes + LLRN** workflow, the LLRN changes go
on the same branch as the release notes. In the **LLRN only** workflow, use a branch such as
`LLRN-<version>`.

### 7.1 — Pick the three branches to check

Always check the three most recent release branches, not only the requested one, because
tickets are often added to (or removed from) a version after its LLRN was written.

1. Read the branch order from `docs/releases/release_notes/.nav.yml`, the **Release Notes**
   section of the site. Its `nav` lists the current branches newest first, e.g. `8.1.md`,
   `8.0.md`, `7.12.md` → `8.1`, `8.0`, `7.12`.
2. If the requested version's branch is not in that list yet (a new branch such as `8.2.0`),
   put it first. Then take the first three: e.g. `8.2`, `8.1`, `8.0`.
3. Otherwise take the first three as they are: requested `8.1.7` → `8.1`, `8.0`, `7.12`.

Tell the user which three branches you will check.

### 7.2 — Find the versions in each branch

The script only includes NIM versions that are **released** and **not archived**. Versions
come from the NIM project (the script's "first project is used as a source of releases");
DOS issues are then matched by the same version name.

For each branch:

1. Collect the versions already in the LLRN file
   `docs/releases/release_notes_low-level/<major>.x/<major>.<minor>.md` (its `## x.y.z`
   headings). For a new branch the file does not exist yet, so start from `x.y.0`.
2. Do not probe versions one by one. Through the connector, Jira returns an **empty result,
   not an error**, for a version name that does not exist. So an empty result cannot tell
   "no such version" apart from "unreleased" or "no issues". Instead, build a candidate
   list from `x.y.0` up to a few patch numbers past the newest version in the file (or the
   requested version, whichever is higher), e.g. `8.1.0` … `8.1.10`, and use it as the
   `IN (...)` list in the 7.3 queries.
3. Read the versions from the results: every issue's `fixVersions` entry carries `name`,
   `released` and `archived`. The branch's versions are the names in the candidate list
   that appear on returned NIM issues with `released: true` and `archived: false`. If a
   NIM issue shows the requested version with `released: false`, tell the user it is not
   released in Jira yet and ask whether to continue.
4. Only NIM and DOS count. Other projects (e.g. MQ, Manual QA; NSD, Support Portal) have
   versions with the same names. They never go into the LLRN, so don't search without a
   `project` clause.

Do not use `fixVersion in releasedVersions(NIM)` in the DOS query: it matches NIM version
IDs, so it would drop every DOS issue.

### 7.3 — Fetch the issues for each branch

Run one query per project for the whole branch, using the script's JQL with the 7.2
candidate list in one `IN (...)` list. Request only the fields `summary, issuetype,
priority, fixVersions` (each issue is 2–3 KB of JSON even then) and paginate with
`nextPageToken` until there are no more results. A branch can have 300–500 issues, so run
each branch's fetch and comparison (7.3–7.4) in its own read-only subagent, in parallel,
and have it return only the differences:

```
project = NIM AND fixVersion IN ("8.1.0", "8.1.1", …) AND (resolution = Done)
AND (resolution IS NOT EMPTY OR statusCategory = Done)
AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY) ORDER BY key

project = DOS AND fixVersion IN ("8.1.0", "8.1.1", …)
AND (resolution IS NOT EMPTY OR statusCategory = Done)
AND (labels NOT IN (skip_LLRN) OR labels IS EMPTY) ORDER BY key
```

IPF is not part of LLRN. Assign each issue to **every** version of that branch listed in its
`fixVersions` field: the script queries per version, so an issue with two fix versions is
listed under both. Versions with no issues get no section, as in the script.

### 7.4 — Compare Jira with the LLRN files and report

For each of the three branches, compare the Jira result with the file, version by version,
by ticket key:

- **Missing version** — a released version with issues but no `## x.y.z` section (e.g.
  `8.1.7` released while the file stops at `8.1.6`).
- **Added tickets** — in Jira for that version but not in its section.
- **Removed tickets** — in the section but no longer returned by Jira (moved to another
  version, `skip_LLRN` label added, resolution changed).
- **Changed priority or issue type** — the ticket is listed with a different priority, or
  under a different `###` type.
- **Changed summary** — the cleaned Jira summary differs from the text in the file. This is
  often a deliberate edit (non-public information removed), so report it but keep the text
  in the file unless the user asks otherwise.

Show the user a short report per branch. If a branch has no differences, say so in one line
("`7.12`: no LLRN updates"). Ask before applying any of the changes; apply only the ones the
user approves.

### 7.5 — Write the changes

**New version section** — insert `## <version>` above the previous patch version (newest
first). Its content:

1. **Group by issue type**, in this order, omitting empty ones, each with its intro sentence
   copied from an existing section of the file: `### Epics`, `### Stories`, `### Bugs`,
   `### Tasks`, `### Sub-Tasks` (Jira `Sub-task`). Other issue types are not listed, as in
   the script.
2. **Item format**: `` - `KEY-123` -- <Priority> -- <summary> `` — here the ticket key **is**
   kept (unlike the customer-facing release notes). Clean the summary like the script's
   `clean_title`: strip team codes (`[DP]`, `[PE]`, …) and version tags (`[7.11]`,
   `[7.11/7.12]`), collapse spaces, trim leading/trailing dashes.
3. **Sort by priority within each type — every time**: Highest, High, Medium, Low, Lowest,
   then by key within the same priority. After writing or changing a version section,
   re-sort its item lists and verify the order (e.g. with `awk`/`uniq -c` on the priority
   column) before showing the diff. Sorting must not add, drop or change any item — compare
   the bullet count before and after.

**Changes to existing sections** — add, remove or move only the approved items, keeping the
same format and sort order. Do not touch anything else in older sections.

**New branch file** (e.g. `8.2.0`, the first LLRN for `8.2`) — create
`docs/releases/release_notes_low-level/<major>.x/<major>.<minor>.md` with the same front
matter, `# LLRN <major>.<minor>` heading and intro paragraph as the previous branch's file,
with the branch number replaced. Then add it to the top of
`docs/releases/release_notes_low-level/<major>.x/.nav.yml`. For the first branch of a new
major version (e.g. `9.0`), the `<major>.x` folder and its `.nav.yml` must be created, and
`docs/releases/release_notes_low-level/.nav.yml` updated — the `README's` "Display Rules"
describe when older majors move to **Previous Releases**; ask the user before changing that.

**Issue count** — the intro paragraph (`...contains a total of N fixed issues.`) uses the
script's count: every issue the NIM and DOS queries return, summed per version. This
includes issue types that are not listed, such as Spikes, so N is usually higher than the
number of list items (7.12: 322 stated, 315 listed, 7 Spikes). Update N by the net change in
returned issues (added minus removed, Spikes included). For a new branch file, N is the
total returned for the branch.

Show the user the diff (`git diff docs/releases/release_notes_low-level`) and ask before
committing.

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
  `[DP]`, `[8.0]`; the `clean_title` cleanup in 7.5 handles the bracketed forms, but check for
  versions written in plain text)

Vendor/product/platform names (Cisco NX-OS, FortiGate, AWS) are fine. If unsure, ask the user.
Descriptions often contain such data even when the summary does not — never copy description
text into the notes beyond the specific technical facts allowed in Step 4.

## Key differences from `jira_ai_agent.py` (removed)

| Original script | This skill |
|---|---|
| `requests` + Basic Auth (`JIRA_USER`/`JIRA_PASS`) against `rest/api/3/search/jql` | Atlassian MCP connector tools (`searchJiraIssuesUsingJql`) — no credentials to manage |
| PydanticAI `Agent('openai:gpt-5.6', ...)` with a JSON-schema system prompt, manual JSON extraction from the model's reply | Claude drafts the `ReleaseNotes`-shaped content directly in the conversation — no external API key, no JSON parsing/repair step |
| Separate `openai:gpt-4o` "conversation agent" for interactive refinement | Same conversation, same context — just keep talking |
| Saves to a local `release_notes_<version>.md` scratch file | Inserted into the project's actual `docs/releases/release_notes/<major>.md`, matching existing formatting |

## Key differences from `jira_release_notes.py`

| Original script | This skill |
|---|---|
| `requests` + Basic Auth against `rest/api/3/project/NIM/versions` and `rest/api/3/search/jql` | JQL through the Atlassian MCP connector; released versions found with `releasedVersions(NIM)` |
| Refreshes every branch allowed by a hard-coded filter (currently `8.1` and later) | Checks the three most recent branches from the Release Notes nav |
| Rewrites each branch file from scratch, including hand-sanitized summaries | Reports the differences and edits only the approved items |
| One query per version | One query per project per branch, split by `fixVersions` |
| Recounts the issue total from Jira (all returned issue types, including Spikes) | Adjusts the stated total by the net change, counted the same way |
