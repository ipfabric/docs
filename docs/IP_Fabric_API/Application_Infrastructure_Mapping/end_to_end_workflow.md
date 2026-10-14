---
description: How to combine the IP Fabric AIM API endpoints into a complete workflow -- import CSV or JSON data, poll the background jobs, calculate flow path lookups, and read the resulting applications, flows, and devices.
---

# End-to-End Workflow

--8<-- "snippets/aim_license_required.md"

The two AIM endpoints described in
[Overview](index.md) are asynchronous: each one
schedules a background job and returns a `jobId`. A complete integration
therefore combines them with the Jobs table and the AIM inventory tables:

1. **Import** the data, as CSV files or a JSON body --
   `POST /aim/import/{snapshotId}`.
2. **Poll** the import job until it finishes -- `POST /tables/jobs`.
3. **Look up** the application or flow ID --
   `POST /tables/inventory/applications` or
   `POST /tables/inventory/applications/flows`.
4. **Calculate** the path lookups --
   `POST /aim/flow-path-lookups/{snapshotId}`.
5. **Poll** the path-lookup job until it finishes -- `POST /tables/jobs`.
6. **Read** the results -- `POST /tables/inventory/applications/devices`.

!!! note "Design the sequence to be repeatable"

    Data ingested through `POST /aim/import/{snapshotId}` is not persisted in the
    snapshot, so unloading and loading that snapshot discards it and the sequence
    has to run again. Both endpoints are safe to re-run -- the import merges on
    the keys in your CSV files, and calculated flows are skipped -- so the whole
    script can simply be executed a second time. See
    [Imported Data Does Not Survive a Snapshot Reload](index.md#imported-data-does-not-survive-a-snapshot-reload)
    for the alternative that persists.

## Supporting API Endpoints

Beyond the two AIM endpoints, the workflow uses the Jobs table to track progress
and the AIM inventory tables to read the results:

- `/api/tables/jobs` -- a `POST` method to poll the status of scheduled jobs.
  Documented on this page.
- `/api/tables/inventory/applications`, `.../workloads`, `.../flows`, and
  `.../devices` -- `POST` methods to read the ingested data. For their columns,
  request fields, and response examples, see
  [AIM Inventory Tables](index.md#aim-inventory-tables).

Headers must contain `Content-Type: application/json` and `X-API-Token:`. See
[Authentication](../authentication.md) for alternatives.

## Monitoring the Job

Poll the `jobId` returned by either AIM endpoint through the Jobs table until
`isDone` is `true`.

```text
POST /api/tables/jobs
Content-Type: application/json
```

!!! warning

    The Jobs table is not snapshot-scoped -- do **not** include a `snapshot` key
    in the request body, or the request is rejected.

!!! example "Polling a Job"

    ```bash
    curl -X POST 'https://{ipf_server}/api/tables/jobs' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{
            "columns": ["id","name","status","isDone","startedAt","finishedAt","reason","snapshot","username"],
            "filters": { "id": ["eq", "184"] },
            "pagination": { "limit": 1, "start": 0 }
          }'
    ```

    ```json
    {
      "data": [
        {
          "id": "184",
          "name": "aimFlowPathLookup",
          "status": "done",
          "isDone": true,
          "startedAt": 1787065241653,
          "finishedAt": 1787065241909,
          "reason": null,
          "snapshot": "8366fec8-da3e-4635-9cb3-97008ca6435b",
          "username": "admin"
        }
      ],
      "_meta": { "limit": 1, "start": 0, "count": 1, "size": 1 }
    }
    ```

The `name` column identifies the job type: `aimImport` for the import and
`aimFlowPathLookup` for the path-lookup calculation. Timestamps are Unix
milliseconds.

!!! tip "Finding a job without its ID"

    If you lose the `jobId`, filter on the action name instead and sort by
    schedule time -- for example
    `"filters": { "name": ["eq", "aimImport"] }` with
    `"sort": { "column": "scheduledAt", "order": "desc" }`.

### Job Status Values

Poll until `isDone` is `true`, then branch on `status`:

| `status`    | Meaning                                                        |
| :---------- | :------------------------------------------------------------- |
| `scheduled` | Queued, not started yet.                                       |
| `running`   | In progress.                                                   |
| `done`      | Completed successfully.                                        |
| `error`     | Failed. `reason` contains the cause.                           |
| `cancelled` | Cancelled before completion.                                   |
| `stopping`  | Stop requested.                                                |
| `stopped`   | Stopped by a user.                                             |

### Reading Validation Errors

Where a validation error surfaces depends on how the data was sent.

**CSV upload.** The job ends with `status: "error"` and `reason` holds a
JSON-encoded object pinpointing the offending row:

```json
{
  "file": "workloads.csv",
  "row": 3,
  "message": "enforcementMode: Invalid enum value. Expected 'visibility_only' | 'selective' | 'full' | 'idle' | 'unknown', received 'strict'"
}
```

`row` counts the header as row 1, so `row: 3` is the second data row. It is
`null` for errors that are not tied to a specific row, such as an unresolved
cross-reference.

**JSON body.** Row-level problems never reach a job -- the request itself is
rejected with `422` before one is scheduled, and the response lists every
problem at once:

```json
{
  "code": "API_VALIDATION_FAILED",
  "message": "Invalid Input",
  "errors": [
    { "field": ["workloads", 1, "enforcementMode"], "message": "Invalid enum value. Expected 'visibility_only' | 'selective' | 'full' | 'idle' | 'unknown', received 'strict'" }
  ]
}
```

The `field` path carries the **array index**, so the row that a CSV reports as
`row: 3` appears here as `1`.

Cross-references between applications, workloads, and flows need a database
lookup, so they are checked inside the job in both formats -- a `202` followed by
a failed job is still possible with a JSON body.

!!! note "`file` follows the format you sent"

    A CSV upload reports the file name, `flows.csv`. A JSON body reports the
    property name instead, so the same cross-reference failure reads:

    ```json
    {
      "file": "flows",
      "row": null,
      "message": "dstWorkloadExternalId 'wl-999' not found in workloads data"
    }
    ```

    Match on the section rather than on the exact string if your client handles
    both formats.

!!! note "Follow-up jobs after a successful import"

    A successful import also schedules the standard post-processing jobs for the
    snapshot, such as topology calculation and intent verification. These appear
    as separate entries in the Jobs table. They do not block the path-lookup
    calculation, so you can proceed as soon as the `aimImport` job reports
    `done`.

## Reading the Results

The four AIM inventory tables -- their columns, request fields, and response
examples -- are documented in
[AIM Inventory Tables](index.md#aim-inventory-tables). This section covers only
what the workflow needs from each of them.

| Purpose                     | Table                                     | What to read                                                                                                         |
| :-------------------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Verify the import           | [Applications](index.md#applications)     | `flows` and `workloads` should match your CSV row counts. `dataSourceName` confirms the data came from the manual source. |
| Obtain an `applicationId`   | [Applications](index.md#applications)     | The `id` column. `flowsCalculated` shows how many of the application's flows already have a result.                    |
| Obtain a `flowId`           | [Flows](index.md#flows)                   | The `id` column. Filter on `"pathLookupsCalculationStatus": ["eq", false]` to list only the flows still needing a calculation. |
| Inspect workload interfaces | [Workloads](index.md#workloads)           | `workloadInterface` holds one interface address per row.                                                              |
| Confirm the outcome         | [Devices](index.md#devices)               | `hostname` and `sn` of each traversed device. Filter on `flowId` for one flow's devices, or de-duplicate on `sn` for a unique device list. |

After a successful calculation, re-reading the Applications table is the quickest
confirmation: `flowsCalculated` and `devices` should both have increased.

## Complete Example Script

The following script imports the CSV files, waits for the import to finish,
calculates the path lookups for one application, waits again, and lists the
resulting devices.

!!! example "Complete Workflow"

    ```bash
    #!/usr/bin/env bash
    set -euo pipefail

    IPF_SERVER="ipfabric.example.com"
    IPF_TOKEN="{api_token}"
    SNAPSHOT="{snapshotId}"
    CSV_DIR="./aim-data"

    api() {
      curl -sk -X POST "https://${IPF_SERVER}/api/$1" \
        -H "X-API-Token: ${IPF_TOKEN}" \
        -H 'Content-Type: application/json' \
        -d "$2"
    }

    # Wait until a job reaches a terminal state; fail on a non-"done" outcome.
    wait_for_job() {
      local job_id="$1" result status
      while :; do
        result=$(api "tables/jobs" "{
          \"columns\":[\"id\",\"name\",\"status\",\"isDone\",\"reason\"],
          \"filters\":{\"id\":[\"eq\",\"${job_id}\"]},
          \"pagination\":{\"limit\":1,\"start\":0}}")
        [ "$(echo "$result" | jq -r '.data[0].isDone')" = "true" ] && break
        sleep 3
      done
      status=$(echo "$result" | jq -r '.data[0].status')
      if [ "$status" != "done" ]; then
        echo "Job ${job_id} finished with status '${status}':" >&2
        echo "$result" | jq -r '.data[0].reason' >&2
        return 1
      fi
      echo "Job ${job_id} completed."
    }

    # 1. Import the CSV files.
    import_job=$(curl -sk -X POST \
      "https://${IPF_SERVER}/api/aim/import/${SNAPSHOT}" \
      -H "X-API-Token: ${IPF_TOKEN}" \
      -F "applications=@${CSV_DIR}/applications.csv;type=text/csv" \
      -F "workloads=@${CSV_DIR}/workloads.csv;type=text/csv" \
      -F "interfaces=@${CSV_DIR}/interfaces.csv;type=text/csv" \
      -F "flows=@${CSV_DIR}/flows.csv;type=text/csv" | jq -r .jobId)
    echo "Import job: ${import_job}"
    wait_for_job "$import_job"
    ```

    To send a JSON payload instead, replace step 1 with the following. The rest
    of the script is unchanged, because both formats return the same `jobId`:

    ```bash
    # 1. Import a JSON payload. A 422 here means a row failed validation, and
    #    no job was created - so check for jobId before waiting on it.
    response=$(curl -sk -X POST \
      "https://${IPF_SERVER}/api/aim/import/${SNAPSHOT}" \
      -H "X-API-Token: ${IPF_TOKEN}" \
      -H 'Content-Type: application/json' \
      --data-binary "@${CSV_DIR}/aim-import.json")

    import_job=$(echo "$response" | jq -r '.jobId // empty')
    if [ -z "$import_job" ]; then
      echo "Import rejected:" >&2
      echo "$response" | jq -r '.errors[]? | "  \(.field | join(".")): \(.message)"' >&2
      exit 1
    fi
    echo "Import job: ${import_job}"
    wait_for_job "$import_job"

    # 2. Resolve the application ID from its externalId.
    app_id=$(api "tables/inventory/applications" "{
      \"columns\":[\"id\",\"name\",\"externalId\"],
      \"filters\":{\"externalId\":[\"eq\",\"app-001\"]},
      \"snapshot\":\"${SNAPSHOT}\",
      \"pagination\":{\"limit\":1,\"start\":0}}" | jq -r '.data[0].id')
    echo "Application ID: ${app_id}"

    # 3. Calculate the path lookups for that application.
    lookup_job=$(curl -sk -X POST \
      "https://${IPF_SERVER}/api/aim/flow-path-lookups/${SNAPSHOT}" \
      -H "X-API-Token: ${IPF_TOKEN}" -H 'Content-Type: application/json' \
      -d "{\"applicationId\":\"${app_id}\"}" | jq -r .jobId)
    echo "Path-lookup job: ${lookup_job}"
    wait_for_job "$lookup_job"

    # 4. List the resulting devices.
    api "tables/inventory/applications/devices" "{
      \"columns\":[\"hostname\",\"sn\",\"srcApplicationName\",\"dstApplicationName\",\"applicationFlow\"],
      \"snapshot\":\"${SNAPSHOT}\",
      \"pagination\":{\"limit\":100,\"start\":0}}" | jq
    ```

## Troubleshooting

| Symptom                                                        | Cause and resolution                                                                                                                     |
| :------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `400 -- At least one file must be provided`                    | Nothing to import. For an upload, send at least one CSV as `multipart/form-data` and do not set `Content-Type` manually. For a JSON body, include at least one non-empty array. |
| `400 -- Malformed JSON`                                        | The request is declared as `application/json` but the body is not valid JSON. Most often `-H 'Content-Type: application/json'` was sent alongside `-F` file parts; drop the header and let `curl` build the multipart one. |
| `422` on the import endpoint                                   | Invalid `snapshotId`, or a JSON row failed validation. `errors[].field` names the array, the row index, and the property. No job was created, so fix the payload and resend. |
| `403` on either AIM endpoint                                   | Missing AIM license, or the API token's policy does not cover the endpoint.                                                               |
| `404` on the path-lookup endpoint, but the snapshot exists     | The snapshot is not loaded. Path lookups need the snapshot's routing data.                                                                |
| `413`, as an HTML page rather than JSON                        | The request exceeds the 20 MB limit, which covers the whole request in both formats. Split the data and import in several requests.       |
| Import job `status: "error"`                                   | Read `reason` for the file, row, and message. Fix that row and re-import -- applications, workloads, and interfaces merge on re-import, so retrying is safe. With a JSON body this indicates a cross-reference failure, since row errors are caught before the job. |
| A flow appears twice after re-importing the same data          | The flow leaves `srcPort`, `dstPort`, or `flowDirection` empty, and empty values do not match on re-import. Send all three -- see [How Data Is Merged](index.md#how-data-is-merged). |
| Import succeeded but the Applications `devices` count is `0`   | Expected. Run the path-lookup calculation.                                                                                               |
| Flows `devices` is empty rather than a number                  | That flow has no path-lookup result yet. On the Flows table such a flow returns `null`, not `0`; check `pathLookupsCalculationStatus` for the state. |
| Path lookup `done` but `devices` is still `0`                  | The flow's addresses do not trace a path in this snapshot. `flowsCalculated` and `pathLookupsCalculationStatus` still advance, because a result is recorded even when no device is traversed. Verify that `srcIp` and `dstIp` exist in the snapshot's routing tables. |
| Workload interfaces disappeared after an import                | `workloads.csv` was uploaded without `interfaces.csv`. Re-send both files together.                                                       |
| All imported AIM data gone after unloading and loading the snapshot | Expected. Data ingested through `/aim/import` is written to the inventory tables only and is not persisted in the snapshot, so a reload discards it. Run the sequence again, or use the settings-based CSV import for data that has to survive a reload -- see [Imported Data Does Not Survive a Snapshot Reload](index.md#imported-data-does-not-survive-a-snapshot-reload). |
| Request to `/api/v8.1/aim/...` returns `404`                   | API paths are not version-prefixed. Use `/api/aim/...` and select the version with the `X-API-Version` header.                            |
