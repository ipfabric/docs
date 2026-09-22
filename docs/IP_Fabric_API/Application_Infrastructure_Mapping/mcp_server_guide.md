---
description: User guide for working with IP Fabric Application Infrastructure Mapping (AIM) data through the IP Fabric MCP Server -- list imported applications, trigger path-lookup calculations on demand, and read the resulting network devices from an AI assistant.
---

# Using AIM Through the MCP Server

--8<-- "snippets/aim_license_required.md"

The [IP Fabric MCP Server](../../IP_Fabric_Settings/integration/mcp.md) lets an AI
assistant work with your AIM data conversationally: check whether an import
finished, list the imported applications and flows, trigger a path-lookup
calculation, and read back the network devices a flow traverses.

This page assumes the MCP server is already enabled and connected to your AI
client. For enabling the server, generating an API token, and configuring Claude
Desktop or VS Code, see
[IP Fabric MCP Server](../../IP_Fabric_Settings/integration/mcp.md).

For the underlying REST endpoints, see
[Overview](index.md) and
[End-to-End Workflow](end_to_end_workflow.md).

## What the MCP Server Can Do With AIM

There are **no AIM-specific MCP tools**. AIM is reached through the MCP server's
three generic API discovery tools, which expose the whole IP Fabric API:

| Tool                       | Purpose                                                                 |
| :------------------------- | :---------------------------------------------------------------------- |
| `ipf_api_endpoint_search`  | Find relevant endpoints from a natural-language description.             |
| `ipf_api_endpoint_details` | Return an endpoint's parameters, request body, and response schema.      |
| `ipf_api_endpoint_invoke`  | Execute an endpoint with path parameters, a JSON body, and headers.      |

Applied to AIM, this yields the following capability matrix:

| Task                                        | Endpoint                                        | Through MCP  |
| :------------------------------------------ | :---------------------------------------------- | :----------- |
| Import AIM data from CSV files              | `POST /aim/import/{snapshotId}`                 | **No** -- see below |
| Check whether an import or calculation ended | `POST /tables/jobs`                             | Yes          |
| List applications                            | `POST /tables/inventory/applications`           | Yes          |
| List workloads                               | `POST /tables/inventory/applications/workloads` | Yes          |
| List flows and their calculation state       | `POST /tables/inventory/applications/flows`     | Yes          |
| Trigger path-lookup calculation              | `POST /aim/flow-path-lookups/{snapshotId}`      | Yes          |
| List traversed devices                       | `POST /tables/inventory/applications/devices`   | Yes          |
| Resolve the snapshot to work with            | `GET /snapshots`                                | Yes          |

!!! warning "The CSV import cannot be performed through the MCP server"

    `POST /aim/import/{snapshotId}` requires a `multipart/form-data` body
    containing file parts. `ipf_api_endpoint_invoke` sends a **JSON** body and has
    no mechanism for attaching files, so the request reaches IP Fabric with no
    file parts and is rejected:

    ```json
    {
      "code": "API_VALIDATION_FAILED",
      "message": "Invalid Input",
      "errors": [
        { "message": "At least one file must be provided" }
      ]
    }
    ```

    Perform the import itself with a normal HTTP client -- see
    [Import AIM Data From CSV Files](index.md#import-aim-data-from-csv-files) --
    and use the MCP server for every step afterwards. Because the request is
    rejected before any job is created, an accidental attempt through the MCP
    server changes nothing.

## Prerequisites

- The MCP server enabled and connected to your AI client.
- An API token whose RBAC scope covers the endpoints you intend to use. The MCP
  server has no implicit access -- every call is authorized solely by that token.
  For the AIM workflow the token needs the **Tables** system policy; the import
  step, performed outside the MCP server, additionally needs **Settings**.
- A valid **AIM license**, otherwise the AIM endpoints return `403`.
- A **loaded** snapshot for path-lookup calculations.

!!! note "The endpoint index may lag behind the appliance"

    The MCP server answers `search` and `details` from an indexed copy of the API
    specification. Immediately after an upgrade that adds endpoints, a valid path
    can still report:

    ```text
    API endpoint not found: POST /aim/flow-path-lookups/{snapshotId}
    ```

    The index is rebuilt in the background, so retrying after a short wait
    usually resolves it. Confirm availability with `ipf_api_endpoint_details`
    before concluding that an endpoint is unsupported.

## Step 1 -- Identify the Snapshot

The AIM endpoints require a snapshot **UUID**. Unlike the table endpoints, they do
not accept the reserved keywords `$last`, `$prev`, or `$lastLocked`.

!!! example "Example Prompt"

    ```text
    List the available IP Fabric snapshots and tell me which one is the latest loaded one.
    ```

The assistant calls `ipf_api_endpoint_invoke`:

```json
{
  "method": "get",
  "path": "/snapshots"
}
```

Each entry includes `id`, `name`, `state`, and `tsEnd`. Pick the `id` of a
snapshot whose `state` is `loaded`; the newest is the one with the highest
`tsEnd`.

## Step 2 -- Confirm the Import Job Finished

After importing the CSV files outside the MCP server, you receive a `jobId`. Ask
the assistant to check it.

!!! example "Example Prompt"

    ```text
    Has AIM import job 177 finished?
    ```

The assistant calls `ipf_api_endpoint_invoke`:

```json
{
  "method": "post",
  "path": "/tables/jobs",
  "body": {
    "columns": ["id", "name", "status", "isDone", "startedAt", "finishedAt", "reason", "snapshot", "username"],
    "filters": { "id": ["eq", "177"] },
    "pagination": { "limit": 1, "start": 0 }
  }
}
```

```json
{
  "data": [
    {
      "id": "177",
      "name": "aimCsvImport",
      "status": "done",
      "isDone": true,
      "startedAt": 1787063861543,
      "finishedAt": 1787063861628,
      "reason": null,
      "snapshot": "{snapshotId}",
      "username": "admin"
    }
  ],
  "_meta": { "limit": 1, "start": 0, "count": 1, "size": 1 }
}
```

The job is finished when `isDone` is `true`. `status` must be `done`; on
`error`, `reason` holds a JSON object naming the file, row, and validation
message. The `snapshot` column confirms **which** snapshot received the data --
worth checking, since the import targets whichever snapshot UUID was used in the
request rather than the one selected in the UI.

!!! tip "Lost the job ID"

    Ask for the most recent import instead -- the assistant can filter on
    `"name": ["eq", "aimCsvImport"]` and sort by `scheduledAt` descending. The
    same works for `aimFlowPathLookup`.

## Step 3 -- List the Imported Data

!!! example "Example Prompt"

    ```text
    List the AIM applications in snapshot <snapshot-id>, with their flow, workload
    and device counts.
    ```

The assistant calls `ipf_api_endpoint_invoke`:

```json
{
  "method": "post",
  "path": "/tables/inventory/applications",
  "body": {
    "columns": ["id", "name", "externalId", "environment", "dataSourceName", "flows", "flowsCalculated", "workloads", "devices"],
    "snapshot": "{snapshotId}",
    "pagination": { "limit": 50, "start": 0 },
    "sort": { "column": "name", "order": "asc" }
  }
}
```

```json
{
  "data": [
    {
      "id": "46",
      "name": "Frontend Service",
      "externalId": "app-001",
      "environment": "prod",
      "dataSourceName": "Manual",
      "flows": 1,
      "flowsCalculated": 0,
      "workloads": 1,
      "devices": 0
    },
    {
      "id": "47",
      "name": "Backend API",
      "externalId": "app-002",
      "environment": "prod",
      "dataSourceName": "Manual",
      "flows": 1,
      "flowsCalculated": 0,
      "workloads": 1,
      "devices": 0
    }
  ],
  "_meta": { "limit": 50, "start": 0, "count": 2, "size": 2, "snapshot": "{snapshotId}" }
}
```

This response is also how you verify the import: `flows` and `workloads` should
match your CSV row counts, and `dataSourceName` distinguishes CSV-imported data
from integration-sourced data.

Two fields matter for the next step:

- **`id`** -- the numeric application ID needed to trigger a calculation.
- **`flowsCalculated`** -- `0` means no path lookups have run yet, which is why
  `devices` is also `0`.

Ask for `/tables/inventory/applications/workloads` or
`/tables/inventory/applications/flows` the same way. The Flows table is where you
get a `flowId` and its `pathLookupsCalculationStatus` boolean:

!!! example "Example Prompt"

    ```text
    Show the AIM flows for application app-001 in that snapshot and whether each
    one has been calculated.
    ```

```json
{
  "method": "post",
  "path": "/tables/inventory/applications/flows",
  "body": {
    "columns": ["id", "srcWorkload", "dstWorkload", "srcApplicationName", "dstApplicationName", "srcIp", "dstIp", "srcPort", "dstPort", "protocol", "pathLookupsCalculationStatus", "devices"],
    "filters": { "or": [
      { "srcApplicationExternalId": ["eq", "app-001"] },
      { "dstApplicationExternalId": ["eq", "app-001"] }
    ]},
    "snapshot": "{snapshotId}",
    "pagination": { "limit": 20, "start": 0 }
  }
}
```

## Step 4 -- Trigger the Path-Lookup Calculation

This is what populates the Devices table. Provide **exactly one** of
`applicationId` or `flowId`.

!!! example "Example Prompt -- Whole Application"

    ```text
    Calculate the path lookups for application "Frontend Service" in snapshot
    <snapshot-id>.
    ```

The assistant calls `ipf_api_endpoint_invoke`:

```json
{
  "method": "post",
  "path": "/aim/flow-path-lookups/{snapshotId}",
  "parameters": { "snapshotId": "{snapshotId}" },
  "body": { "applicationId": "46" }
}
```

```json
{
  "jobId": "184"
}
```

!!! example "Example Prompt -- Single Flow"

    ```text
    Calculate the path lookup for AIM flow 894 only.
    ```

```json
{
  "method": "post",
  "path": "/aim/flow-path-lookups/{snapshotId}",
  "parameters": { "snapshotId": "{snapshotId}" },
  "body": { "flowId": "894" }
}
```

!!! note "Path parameters go in `parameters`"

    Keep the placeholder in `path` (`/aim/flow-path-lookups/{snapshotId}`) and
    supply the value in `parameters`. Substituting the UUID directly into `path`
    prevents the MCP server from matching the endpoint in its index.

Then poll the returned `jobId` exactly as in [Step 2](#step-2-confirm-the-import-job-finished);
the job `name` is `aimFlowPathLookup`.

!!! info "Re-running is harmless"

    Flows with a stored result are skipped, so repeating a calculation finishes
    almost immediately and writes nothing. A flow between two applications
    belongs to both, so calculating one application also covers that shared flow
    for the other -- expect the second application's `flowsCalculated` to rise
    without you asking for it.

## Step 5 -- List the Resulting Devices

!!! example "Example Prompt"

    ```text
    Which network devices do the flows of application "Frontend Service" traverse
    in that snapshot?
    ```

The assistant calls `ipf_api_endpoint_invoke`:

```json
{
  "method": "post",
  "path": "/tables/inventory/applications/devices",
  "body": {
    "columns": ["id", "hostname", "sn", "snHw", "flowId", "srcApplicationName", "dstApplicationName", "applicationFlow"],
    "filters": { "or": [
      { "srcApplicationName": ["eq", "Frontend Service"] },
      { "dstApplicationName": ["eq", "Frontend Service"] }
    ]},
    "snapshot": "{snapshotId}",
    "pagination": { "limit": 200, "start": 0 },
    "sort": { "column": "hostname", "order": "asc" }
  }
}
```

```json
{
  "data": [
    {
      "id": "1749",
      "hostname": "SW-CORE-01",
      "sn": "SN12345678",
      "snHw": "SN12345678",
      "srcApplicationName": "Frontend Service",
      "dstApplicationName": "Backend API",
      "applicationFlow": "web-server-01 → api-server-01"
    }
  ],
  "_meta": { "limit": 200, "start": 0, "count": 1, "size": 1, "snapshot": "{snapshotId}" }
}
```

A device is reached through a flow, not owned by an application, so scoping to one
application means matching **both** sides with an `or` filter. Rows are
`{flow, device}` pairs, so the same device repeats once per traversing flow --
ask the assistant to de-duplicate on `sn` for a unique device list.

Re-running Step 3 afterwards confirms the outcome: `flowsCalculated` and
`devices` should both have increased.

## Worked Example

A complete session, from a finished import to the device list:

```text
You:  List the IP Fabric snapshots and tell me the latest loaded one.
AI:   The latest loaded snapshot is 8366fec8-... (finished 2026-08-18 14:37 UTC,
      41 devices).

You:  Has AIM import job 177 finished?
AI:   Yes -- job 177 (aimCsvImport) completed with status "done", no errors,
      in 85 ms, against snapshot 8366fec8-...

You:  List the AIM applications in that snapshot.
AI:   Two manually imported applications:
        - Frontend Service (app-001), id 46 -- 1 flow, 1 workload, 0 devices
        - Backend API (app-002), id 47 -- 1 flow, 1 workload, 0 devices
      flowsCalculated is 0 for both, so no path lookups have run yet.

You:  Calculate the path lookups for Frontend Service.
AI:   Scheduled job 184. ... Job 184 finished with status "done" in 256 ms.

You:  Which devices does it traverse now?
AI:   One device: SW-CORE-01 (SN12345678), via the flow
      web-server-01 → api-server-01. Frontend Service now reports
      flowsCalculated 1 and devices 1. Backend API also moved to 1/1, because
      both applications share that flow.
```

## Tips

- **Give the assistant the snapshot UUID up front.** The AIM endpoints reject
  `$last`, so a prompt that only says "the latest snapshot" costs an extra
  round-trip while the assistant resolves it.
- **Name the application, not the ID.** Asking for `"Frontend Service"` lets the
  assistant look up the numeric `id` itself from the Applications table.
- **Ask for a CSV export** when you want the result as a file rather than a
  table: adding `"format": { "exportToFile": true, "dataType": "csv" }` to any
  table request works through the MCP server too.
- **Watch the snapshot in job results.** Since the import is snapshot-scoped and
  performed outside the MCP server, the `snapshot` column in the Jobs table is
  the quickest way to catch data that landed in the wrong place.

## Troubleshooting

| Symptom                                                            | Cause and resolution                                                                                                                        |
| :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `400 -- At least one file must be provided` on the import endpoint | The import was attempted through the MCP server, which cannot send file parts. Import with a normal HTTP client instead.                     |
| `API endpoint not found: POST /aim/...`                            | The endpoint is missing from the MCP server's index. Wait for the background reindex and re-check with `ipf_api_endpoint_details`.            |
| `Endpoint ... is not callable with the provided credentials`       | The API token is missing, expired, or lacks the RBAC policy for that endpoint. Verify it under **Settings --> Integration --> API Tokens**.    |
| `403` on an AIM endpoint                                           | No AIM license, or the token's policy does not cover AIM.                                                                                    |
| `404` on the path-lookup endpoint though the snapshot exists       | The snapshot is not loaded. Path lookups need its routing data.                                                                             |
| Endpoint not matched when the UUID is in the URL                   | Keep `{snapshotId}` in `path` and pass the value in `parameters`.                                                                            |
| Path-lookup job `done` but `devices` is still `0`                  | The flow's addresses do not trace a path in this snapshot. `flowsCalculated` and `pathLookupsCalculationStatus` still advance, because a result is recorded even when no device is traversed. |
