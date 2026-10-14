---
description: Reference for the IP Fabric Application Infrastructure Mapping (AIM) API endpoints that ingest application data from CSV files or a JSON payload and calculate which network devices an application's flows traverse. One of three supported AIM ingestion methods.
---

# Overview

--8<-- "snippets/aim_license_required.md"

Application Infrastructure Mapping (AIM) correlates your application inventory --
applications, workloads, workload interfaces, and flows -- with the network model
that IP Fabric discovers.

IP Fabric currently supports **three ways** of ingesting AIM data into the
appliance:

1. **From external data providers, via API crawling.** IP Fabric connects to an
   external system that holds your application inventory and dependency data and
   retrieves it through that system's API. **Illumio** is the provider supported today. Support for further platform types is planned
   for future releases.
2. **In the Discovery Settings, through the IP Fabric UI.** Create entries
   manually, or import them from CSV files.
3. **Through the AIM API endpoint, using CSV files or a JSON payload.** Described
   on this page.

Of the three ingestion methods above, only **option 3** has a dedicated API
endpoint. This document is an overview and reference of that endpoint together
with the other AIM endpoints available over the API. They fall into four
independent groups:

- **Data ingestion** -- `POST /aim/import/{snapshotId}` writes applications,
  workloads, workload interfaces, and flows into a snapshot, either from
  uploaded CSV files or from a JSON request body.
- **Path-lookup calculation** -- `POST /aim/flow-path-lookups/{snapshotId}`
  calculates on demand which network devices the traffic of an application, or of
  one specific flow, traverses.
- **Data read** -- the AIM inventory tables return the ingested data and the
  devices resulting from the calculation.
- **Integration connection test** -- the `.../verify` endpoints check that an
  external data provider used by ingestion method 1 is reachable and that its
  credentials are accepted.

!!! info "Path-lookup calculation is independent of how the data was ingested"

    The calculation is a separate capability, not a second stage of the API
    ingestion. It operates on the AIM data already stored in a snapshot whatever
    its origin -- retrieved from an external provider, created or imported in the
    Discovery Settings, or ingested through the import endpoint described here.

!!! warning "The Devices inventory is populated only by the path-lookup calculation"

    No ingestion method fills the **Application Devices** table. Until a
    path-lookup calculation has run for a flow, that table stays empty and
    `devices` remains `0` in the Applications inventory.

Both AIM endpoints are asynchronous: each schedules a background job and returns a
`jobId`. For polling those jobs and chaining the calls into an automated sequence,
see [End-to-End Workflow](end_to_end_workflow.md).

## Prerequisites

- A valid **AIM license**. Without it, every endpoint on this page returns `403`.
- An API token whose policy grants access to the endpoint:
    - `/aim/import/{snapshotId}` and the `.../verify` endpoints -- require the
      **Settings** system policy (or a custom policy that includes the endpoint).
    - `/aim/flow-path-lookups/{snapshotId}` and the inventory tables -- require the
      **Tables** system policy.
- A target snapshot:
    - The **import** endpoint only requires the snapshot to exist.
    - The **path-lookup** endpoint requires the snapshot to be **loaded**, because
      it needs the snapshot's device and routing data. Running it against an
      unloaded snapshot returns `404`.

## API Endpoints

Ingesting and calculating:

- `/api/aim/import/{snapshotId}` -- a `POST` method to import AIM data, from CSV
  files or from a JSON payload.
- `/api/aim/flow-path-lookups/{snapshotId}` -- a `POST` method to calculate which
  devices the imported flows traverse.

Testing an external data provider integration:

- `/api/aim/integrations/verify` -- a `POST` method to test an integration
  described entirely by the request body.
- `/api/aim/integrations/{id}/verify` -- a `POST` method to test an integration
  stored in the global settings.
- `/api/snapshots/{snapshotId}/aim/integrations/{id}/verify` -- a `POST` method to
  test an integration stored in a snapshot's settings.

Reading the inventorized data:

- `/api/tables/inventory/applications` -- a `POST` method to list imported
  applications.
- `/api/tables/inventory/applications/workloads` -- a `POST` method to list
  workloads.
- `/api/tables/inventory/applications/flows` -- a `POST` method to list flows and
  whether each one has been calculated.
- `/api/tables/inventory/applications/devices` -- a `POST` method to list the
  devices the flows traverse.

!!! note "API paths are not version-prefixed"

    These endpoints are reached directly under `/api/`, without a
    `/api/{api_version}/` segment. API versioning is negotiated with the
    `X-API-Version` request header instead; both endpoints currently accept
    version `1`, which is also the default. Responses echo
    `X-API-Version-Used`, `X-API-Versions-Supported`, and `X-Product-Version`.

## Header Authentication

Headers must contain:

- `X-API-Token:` -- An API token generated in IP Fabric Settings. See
  [Authentication](../authentication.md) for alternatives such as Basic or Bearer
  token authentication.
- `Content-Type: application/json` -- for every endpoint on this page except a
  **file upload** to the import endpoint.

!!! warning "Do not set `Content-Type` manually when uploading CSV files"

    Uploading files to `/aim/import/{snapshotId}` requires `multipart/form-data`.
    Let your HTTP client generate the header so that the multipart boundary is
    included. In `curl`, use `-F` and omit `-H 'Content-Type: ...'` entirely.
    Setting `Content-Type: application/json` alongside `-F` parts makes the
    request unparsable: the appliance tries to read the multipart bytes as JSON
    and rejects them with `400 -- Malformed JSON` (`API_MALFORMED_BODY`).

    This does not apply to the JSON variant of the same endpoint, which takes an
    ordinary `Content-Type: application/json` body and no file parts -- see
    [Send the Rows as JSON](#send-the-rows-as-json).

!!! note "TLS certificate verification"

    The `curl` examples on this page omit certificate options. If your appliance
    still uses the default self-signed certificate, `curl` refuses to connect
    with `SSL certificate problem: self signed certificate`. Add `-k` (or
    `--insecure`) to skip verification, or -- preferably -- trust the appliance's
    certificate authority so that verification succeeds:

    ```bash
    curl --cacert /path/to/ipfabric-ca.pem -X POST 'https://{ipf_server}/api/...'
    ```

## Import AIM Data

Writes applications, workloads, workload interfaces, and flows into the given
snapshot. The same endpoint accepts the data in **two interchangeable formats**,
chosen by the request's `Content-Type`:

```text
POST /api/aim/import/{snapshotId}
Content-Type: multipart/form-data   # upload CSV files
Content-Type: application/json      # send the rows in the request body
```

Both formats feed the same import job and apply the same validation rules and
merge behavior. Which one to use:

| Use                          | When                                                                                   |
| :--------------------------- | :------------------------------------------------------------------------------------- |
| `multipart/form-data` (CSV)  | You already have CSV files, or the data set is large -- CSV fits roughly twice as many rows into the same [request size limit](#payload-size). |
| `application/json`           | You are generating the data programmatically, or calling through the [MCP server](mcp_server_guide.md). Row errors are reported immediately. |

!!! important "Through the MCP server, only the JSON format is supported"

    The [IP Fabric MCP Server](mcp_server_guide.md) invokes endpoints with a JSON
    body and has no mechanism for attaching files, so **`application/json` is the
    only format it can use for this endpoint**. `multipart/form-data` requires a
    normal HTTP client.

    This is a limitation of file upload over MCP, not of the endpoint: everything
    the CSV upload can import, the JSON body can import too, within the same
    [request size limit](#payload-size).

### Request Parameters

| Parameter    | In   | Type     | Required | Description                                  |
| :----------- | :--- | :------- | :------- | :------------------------------------------- |
| `snapshotId` | path | `string` | yes      | UUID of the snapshot to import data into, or one of the reserved keywords `$last`, `$lastLocked`, `$prev`. |

!!! tip "Reserved snapshot keywords are accepted"

    `$last`, `$lastLocked`, and `$prev` are resolved by the appliance, so you do
    not have to look the UUID up first. In a shell, quote the value with single
    quotes -- `'https://{ipf_server}/api/aim/import/$last'` -- otherwise the
    shell expands `$last` to an empty string.

### Upload CSV Files

Each form field accepts a **single** CSV file. At least one field must be
present; you do not have to send all four. The files share one request budget --
see [Payload Size](#payload-size).

| Form field     | Type   | Required | Description                          |
| :------------- | :----- | :------- | :----------------------------------- |
| `applications` | file   | no\*     | CSV file with application data.      |
| `workloads`    | file   | no\*     | CSV file with workload data.         |
| `interfaces`   | file   | no\*     | CSV file with workload interfaces.   |
| `flows`        | file   | no\*     | CSV file with flow data.             |

\* At least one of the four fields is required. Omitting all of them returns
`400`.

### CSV File Formats

All files are parsed with a header row; column order does not matter and values
are trimmed. Columns marked optional may be omitted entirely or left empty (an
empty value is stored as `null`).

!!! tip "Downloadable sample data"

    [aim-sample-ingestion-data.zip](aim-sample-ingestion-data.zip) holds a
    working example of both formats, carrying the same data:

    - `csv/` -- the four files shown below, plus a `curl` file with the upload
      command.
    - `json/` -- `import.json`, the equivalent single payload, plus a `curl` file
      with the request, a job-polling call, and two negative checks.

    Both sets import cleanly as they are; point them at a snapshot of your own.

#### `applications.csv`

| Column       | Required | Format / Allowed values | Notes                                          |
| :----------- | :------- | :---------------------- | :--------------------------------------------- |
| `externalId` | yes      | non-empty string        | Unique key for the application. Must be unique within the file. |
| `name`       | yes      | non-empty string        | Display name in the Applications inventory.    |
| `description`| no       | string                  |                                                |
| `environment`| no       | string                  | **Free text** -- not validated against a list. |

!!! example "Sample `applications.csv`"

    ```csv
    externalId,name,description,environment
    app-001,Frontend Service,Web frontend,prod
    app-002,Backend API,REST API service,prod
    ```

#### `workloads.csv`

| Column                  | Required | Format / Allowed values                                        | Notes                                                        |
| :---------------------- | :------- | :------------------------------------------------------------- | :----------------------------------------------------------- |
| `externalId`            | yes      | non-empty string                                               | Unique key for the workload. Must be unique within the file.  |
| `applicationExternalId` | yes      | non-empty string                                               | Must match an `externalId` in `applications.csv` or an application already stored in the snapshot. |
| `name`                  | yes      | non-empty string                                               |                                                              |
| `enforcementMode`       | yes      | `visibility_only`, `selective`, `full`, `idle`, `unknown`       | The column must be present and hold one of these values.      |
| `hostname`              | no       | string                                                         |                                                              |
| `description`           | no       | string                                                         |                                                              |
| `osType`                | no       | string                                                         |                                                              |
| `osDetail`              | no       | string                                                         |                                                              |
| `online`                | no       | `true` or `false`                                              | Any other non-empty value is rejected.                       |
| `managed`               | no       | `true` or `false`                                              | Any other non-empty value is rejected.                       |
| `publicIp`              | no       | IPv4 or IPv6 address                                           | Stored as the workload's IP address.                         |
| `labels`                | no       | comma-separated `key=value` pairs                              | Quote the field so the commas are not read as delimiters.     |

!!! example "Sample `workloads.csv`"

    ```csv
    externalId,applicationExternalId,name,enforcementMode,hostname,online,managed,publicIp,labels
    wl-001,app-001,web-server-01,full,web01.example.com,true,true,203.0.113.10,"tier=web,region=eu-west"
    wl-002,app-002,api-server-01,selective,api01.example.com,true,true,203.0.113.11,"tier=api,region=eu-west"
    ```

#### `interfaces.csv`

| Column               | Required | Format / Allowed values     | Notes                                                        |
| :------------------- | :------- | :-------------------------- | :----------------------------------------------------------- |
| `workloadExternalId` | yes      | non-empty string            | Must match an `externalId` in `workloads.csv` or a workload already stored in the snapshot. |
| `ipAddress`          | yes      | IPv4 or IPv6 address        |                                                              |
| `linkState`          | yes      | `up`, `down`, `unknown`     |                                                              |
| `name`               | no       | string                      | Interface name.                                              |
| `cidrBlock`          | no       | integer                     | Prefix length. Validated against `ipAddress`: `0-32` for IPv4, `0-128` for IPv6. |
| `defaultGateway`     | no       | IPv4 or IPv6 address        |                                                              |
| `network`            | no       | string                      | For example `10.0.1.0/24`.                                   |

!!! example "Sample `interfaces.csv`"

    ```csv
    workloadExternalId,ipAddress,linkState,cidrBlock,network
    wl-001,10.0.1.10,up,24,10.0.1.0/24
    wl-002,10.0.2.20,up,24,10.0.2.0/24
    ```

#### `flows.csv`

| Column                     | Required | Format / Allowed values                                        | Notes                                                        |
| :------------------------- | :------- | :------------------------------------------------------------- | :----------------------------------------------------------- |
| `srcIp`                    | yes      | IPv4 or IPv6 address                                           |                                                              |
| `dstIp`                    | yes      | IPv4 or IPv6 address                                           |                                                              |
| `protocol`                 | yes      | integer                                                        | IANA protocol number, for example `6` for TCP.               |
| `policyDecision`           | yes      | `allowed`, `potentially_blocked`, `blocked`, `unknown`          |                                                              |
| `srcWorkloadExternalId`    | yes      | non-empty string                                               | Must match a workload in `workloads.csv` or in the snapshot. |
| `dstWorkloadExternalId`    | yes      | non-empty string                                               | Must match a workload in `workloads.csv` or in the snapshot. |
| `srcPort`                  | no       | integer                                                        |                                                              |
| `dstPort`                  | no       | integer                                                        |                                                              |
| `flowDirection`            | no       | `intra_app`, `ingress`, `egress`                               | Empty is stored as `null`.                                   |
| `numConnections`           | no       | integer                                                        |                                                              |
| `firstDetected`            | no       | ISO 8601 timestamp                                             | Stored as Unix milliseconds.                                 |
| `lastDetected`             | no       | ISO 8601 timestamp                                             | Stored as Unix milliseconds.                                 |

!!! example "Sample `flows.csv`"

    ```csv
    srcIp,dstIp,protocol,policyDecision,srcWorkloadExternalId,dstWorkloadExternalId,srcPort,dstPort,flowDirection
    10.0.1.10,10.0.2.20,6,allowed,wl-001,wl-002,54321,8080,egress
    ```

### Send the Rows as JSON

Instead of uploading files, send the rows directly in the request body. The body
is an object with up to four arrays, named after the four CSV files. At least one
array must be present and non-empty.

```json
{
  "applications": [ ... ],
  "workloads": [ ... ],
  "interfaces": [ ... ],
  "flows": [ ... ]
}
```

Each array holds one object per row, using the **same field names** as the CSV
columns documented above, with the same required and optional fields. Because
JSON has real data types, four things differ from the CSV encoding:

| Field group                                                        | CSV                                   | JSON                                                    |
| :----------------------------------------------------------------- | :------------------------------------ | :------------------------------------------------------ |
| `protocol`, `srcPort`, `dstPort`, `numConnections`, `cidrBlock`     | `"6"` -- every cell is text            | `6` -- a number                                          |
| `online`, `managed`                                                 | `"true"` / `"false"`                   | `true` / `false` -- a boolean                            |
| `firstDetected`, `lastDetected`                                     | ISO 8601 string                        | ISO 8601 string **or** Unix milliseconds                 |
| `labels`                                                            | `"tier=web,region=eu-west"`            | `[{ "key": "tier", "value": "web" }, ...]`               |

Optional fields may be **omitted entirely** or sent as `null`; both are stored as
`null`.

!!! warning "Use `null` rather than an empty string for non-string fields"

    An empty string is accepted only on the optional fields whose value is
    textual: `description`, `environment`, `hostname`, `osType`, `osDetail`,
    `network`, `publicIp`, `defaultGateway`, the interface `name`,
    `firstDetected`, and `lastDetected` all treat `""` as `null`. Required
    fields reject it, as they reject a missing value.

    `online`, `managed`, `srcPort`, `dstPort`, `numConnections`, `cidrBlock`, and
    `flowDirection` do not: `""` is the wrong type for a boolean, a number, or an
    enumerated value, and the request fails with `422`. This matters when
    converting CSV rows to JSON, where every empty cell starts life as `""`.

!!! tip "Structured labels can hold commas and equals signs"

    The CSV `labels` column packs pairs into `key=value,key=value`, so a label
    whose key or value contains `,` or `=` cannot be expressed. The JSON form has
    no such limit.

!!! warning "Unknown properties are rejected"

    A misspelled array name or row property fails validation rather than being
    ignored, so a typo cannot silently import nothing. `{"aplications": [...]}`
    returns `422`, not `202`.

!!! example "Sample JSON payload"

    The same data as the four sample CSV files above. Note that the flow's
    `dstWorkloadExternalId` is `wl-002`, so the workload defining it has to be in
    the payload as well -- or already in the snapshot.

    ```json
    {
      "applications": [
        { "externalId": "app-001", "name": "Frontend Service", "description": "Web frontend", "environment": "prod" },
        { "externalId": "app-002", "name": "Backend API", "description": "REST API service", "environment": "prod" }
      ],
      "workloads": [
        {
          "externalId": "wl-001",
          "applicationExternalId": "app-001",
          "name": "web-server-01",
          "enforcementMode": "full",
          "hostname": "web01.example.com",
          "online": true,
          "managed": true,
          "publicIp": "203.0.113.10",
          "labels": [
            { "key": "tier", "value": "web" },
            { "key": "region", "value": "eu-west" }
          ]
        },
        {
          "externalId": "wl-002",
          "applicationExternalId": "app-002",
          "name": "api-server-01",
          "enforcementMode": "selective",
          "hostname": "api01.example.com",
          "online": true,
          "managed": true,
          "publicIp": "203.0.113.11",
          "labels": [
            { "key": "tier", "value": "api" },
            { "key": "region", "value": "eu-west" }
          ]
        }
      ],
      "interfaces": [
        { "workloadExternalId": "wl-001", "ipAddress": "10.0.1.10", "linkState": "up", "cidrBlock": 24, "network": "10.0.1.0/24" },
        { "workloadExternalId": "wl-002", "ipAddress": "10.0.2.20", "linkState": "up", "cidrBlock": 24, "network": "10.0.2.0/24" }
      ],
      "flows": [
        {
          "srcIp": "10.0.1.10",
          "dstIp": "10.0.2.20",
          "protocol": 6,
          "policyDecision": "allowed",
          "srcWorkloadExternalId": "wl-001",
          "dstWorkloadExternalId": "wl-002",
          "srcPort": 54321,
          "dstPort": 8080,
          "flowDirection": "egress"
        }
      ]
    }
    ```

### Payload Size

The whole request is limited to **20 MB**, whichever format it uses. For a file
upload that budget covers all four files together, not each one separately.

!!! warning "JSON is roughly twice the size of the same data as CSV"

    JSON repeats every field name on every row, so the format you choose decides
    how many rows fit. As a rough guide, 120,000 flow rows are around 19 MB of
    CSV but around 39 MB of JSON.

    Split anything larger across several requests. The import merges on the keys
    in your data, so importing in batches gives the same result as one request.

### Validation Rules

Both formats apply the same rules. What differs is **when** you find out: a JSON
body is validated before the job is scheduled, while CSV files are parsed inside
the job.

| Validation                                                 | CSV upload                                   | JSON body                                                        |
| :--------------------------------------------------------- | :------------------------------------------- | :--------------------------------------------------------------- |
| Field types, required fields, enumerations, duplicate `externalId` | Job fails; read `reason` for file, row, message | Request fails immediately with `422` and the path to each bad value |
| Cross-references between applications, workloads, and flows | Job fails                                    | Job fails -- these need a database lookup, so they stay in the job  |

A `422` from a JSON body lists every problem it found, each with the array name,
the row index, and the property:

```json
{
  "code": "API_VALIDATION_FAILED",
  "message": "Invalid Input",
  "errors": [
    { "field": ["flows", 0, "protocol"], "message": "Expected number, received string" },
    { "field": ["applications", 2, "externalId"], "message": "field is required" }
  ]
}
```

!!! note "Row numbering differs between the two formats"

    A CSV `reason` counts the header as row 1, so the first data row is `row: 2`.
    A JSON `field` path carries the **array index**, so the same row is `0`.

Whichever format fails, the import is **all or nothing** -- nothing from the
failing data set is applied.

The rules themselves:

- **Required fields** must be present and non-empty.
- **Enumerated fields** must hold one of the listed values.
- **Duplicate `externalId`** values within the applications or workloads data are
  rejected. Interfaces and flows are not de-duplicated.
- **Cross-references** are resolved against the data in the request first and,
  when a section is not part of the request, against data already stored in the
  snapshot:
    - `workloads.applicationExternalId` must resolve to a known application.
    - `interfaces.workloadExternalId` must resolve to a known workload.
    - `flows.srcWorkloadExternalId` and `flows.dstWorkloadExternalId` must
      resolve to known workloads.

This means you can import incrementally -- for example flows alone -- as long as
the referenced workloads already exist in the snapshot.

!!! note "A failing CSV file stops at the first bad row"

    The CSV parser aborts as soon as it hits an invalid row, so `reason` names
    one problem even when the file has several. A JSON body is validated as a
    whole and reports all of them at once, so a payload with five mistakes takes
    one round trip to diagnose rather than five.

### How Data Is Merged

Imported records are attached to the snapshot's **manual** AIM data source, which
is created on the first import. Existing integration-sourced AIM data is not
affected.

Records are either merged in place (inserted when new, updated when the key
already exists) or replaced wholesale:

| Section        | Behavior | Key used for matching                                                            |
| :------------- | :------- | :------------------------------------------------------------------------------- |
| `applications` | merge    | `externalId`                                                                     |
| `workloads`    | merge    | `externalId`                                                                     |
| `interfaces`   | replace  | All interfaces of each referenced workload are deleted and re-created.            |
| `flows`        | merge    | source workload + destination workload + `srcIp` + `dstIp` + `protocol` + `srcPort` + `dstPort` + `policyDecision` + `flowDirection` |

Re-running an import with the same data updates rows in place rather than
duplicating them -- with one exception for flows, described below.

!!! warning "A flow with an empty key field is re-inserted, not updated"

    `srcPort`, `dstPort`, and `flowDirection` are optional, and the database
    treats two empty values as different rather than equal. A flow row that
    leaves any of the three empty therefore never matches the row an earlier
    import created, and re-importing the same data **adds a second copy** of it.

    Send all three on every flow if you intend to re-import the same rows. Flows
    that carry complete keys are unaffected.

!!! warning "Importing workloads clears interfaces and labels"

    A workload's interfaces and labels are replaced from the request, not merged.
    If you send workloads **without** interfaces, the existing interfaces of every
    workload listed are removed. Likewise, an empty `labels` value clears that
    workload's labels. When updating workload attributes, re-send the interfaces
    and the full `labels` value alongside.

!!! note "Every field of the flow key counts"

    The flow matching key covers the addresses, the ports, the protocol,
    `policyDecision`, and `flowDirection`. Two rows between the same workload
    pair that differ in **any** of those -- a different source port, for example
    -- are two distinct flows, not one. Only a row matching on all of them
    updates an existing flow instead of adding one.

    A source system that reports one connection per ephemeral source port
    therefore produces one flow row per connection. Aggregate on the source side
    if that is not what you want.

### Example Requests

!!! example "Import All Four CSV Files"

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/import/{snapshotId}' \
      --header 'X-API-Token: {api_token}' \
      -F 'applications=@applications.csv;type=text/csv' \
      -F 'workloads=@workloads.csv;type=text/csv' \
      -F 'interfaces=@interfaces.csv;type=text/csv' \
      -F 'flows=@flows.csv;type=text/csv'
    ```

    Import only flows, relying on workloads already present in the snapshot:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/import/{snapshotId}' \
      --header 'X-API-Token: {api_token}' \
      -F 'flows=@flows.csv;type=text/csv'
    ```

!!! example "Import a JSON Payload"

    From a file:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/import/{snapshotId}' \
      --header 'X-API-Token: {api_token}' \
      --header 'Content-Type: application/json' \
      --data-binary @aim-import.json
    ```

    Inline, into the latest snapshot. Note the single quotes around the URL, so
    that the shell does not expand `$last`:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/import/$last' \
      --header 'X-API-Token: {api_token}' \
      --header 'Content-Type: application/json' \
      -d '{
            "flows": [
              {
                "srcIp": "10.0.1.10",
                "dstIp": "10.0.2.20",
                "protocol": 6,
                "policyDecision": "allowed",
                "srcWorkloadExternalId": "wl-001",
                "dstWorkloadExternalId": "wl-002",
                "srcPort": 54321,
                "dstPort": 8080,
                "flowDirection": "egress"
              }
            ]
          }'
    ```

### Response

A successful request returns `202 Accepted` with a JSON body containing a single
key:

| Field   | Type     | Description                                                                 |
| :------ | :------- | :-------------------------------------------------------------------------- |
| `jobId` | `string` | Numeric identifier of the scheduled background job, as a quoted string. Use it to poll the job. |

!!! example "Successful Response"

    ```json
    {
      "jobId": "154"
    }
    ```

The scheduled job has the action name `aimImport`. The Jobs table exposes it as
the `name` column, so a script can find the job again by filtering on
`"name": ["eq", "aimImport"]`.

| Code  | Meaning                                                                       |
| :---- | :---------------------------------------------------------------------------- |
| `202` | Import job scheduled. The body contains the `jobId`.                          |
| `400` | Nothing to import -- no files, or a JSON body with no rows in any section. The message reads `At least one file must be provided` for both formats. |
| `400` | `Malformed JSON` (`API_MALFORMED_BODY`) -- the body is declared as `application/json` but is not valid JSON. |
| `401` | Unauthorized.                                                                 |
| `403` | Missing RBAC permissions or no AIM license.                                   |
| `404` | Snapshot not found.                                                           |
| `413` | The request exceeds 20 MB. Returned by the appliance's web server, so the body is an HTML error page rather than the usual JSON envelope. |
| `422` | Invalid `snapshotId`, or a JSON body that failed row validation. `errors[].field` gives the path to each bad value. |
| `500` | Internal server error.                                                        |

!!! info "`202` does not mean the whole import succeeded"

    The response confirms that the job was **scheduled**. Cross-reference checks
    run inside the job in both formats, and for a CSV upload the parsing and row
    validation do too -- so a malformed file still returns `202` here and fails
    later. Always poll the job -- see
    [End-to-End Workflow](end_to_end_workflow.md).

    A JSON body is the exception for row-level problems only: those are caught
    before the job exists and returned as `422`.

### Imported Data Does Not Survive a Snapshot Reload

!!! warning "Current limitation"

    Data ingested through this endpoint is written **directly into the AIM
    inventory tables** of the target snapshot. It is not stored in the snapshot's
    settings, so the snapshot holds no durable copy of it. Unloading and loading
    the snapshot again discards the imported records, and they have to be
    ingested through the endpoint once more.

This is where the endpoint differs from the other two ingestion methods. Records
that come from an integration, or that are maintained in the **Application
mapping** section of the Discovery Settings, are stored as part of the settings
and rebuilt into the inventory tables from there -- so they survive a reload.
Only the API import writes to the tables alone.

If the data needs to persist across reloads, import the same CSV files through
the **Application mapping** section of the global Discovery Settings or of the
snapshot's settings instead of using this endpoint. Note that the two paths do
not share a CSV format -- see
[Application Mapping](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/application_mapping.md#import-from-csv)
for the columns that import expects.

Use this endpoint when the ingestion is repeatable -- driven from a script or a
pipeline that can simply run again -- and the settings-based import when the data
is entered once and expected to stay.

## Calculate Flow Path Lookups

Runs a path lookup for each selected flow and stores the network devices it
traverses, making them visible in the **Application Devices** inventory table.
Any AIM flow present in the snapshot can be calculated, regardless of which
ingestion method produced it.

```text
POST /api/aim/flow-path-lookups/{snapshotId}
Content-Type: application/json
```

### Request Parameters

| Parameter    | In   | Type            | Required | Description                                                       |
| :----------- | :--- | :-------------- | :------- | :---------------------------------------------------------------- |
| `snapshotId` | path | `string` (UUID) | yes      | UUID of the snapshot to run the path lookups against. Must be loaded. |

The request body must contain **exactly one** of `flowId` or `applicationId`.
Sending both is rejected.

| Field           | Type     | Required | Description                                                                                     |
| :-------------- | :------- | :------- | :---------------------------------------------------------------------------------------------- |
| `flowId`        | `string` | one of   | Numeric ID of a single flow, as a quoted string matching `^\d+$`.                                |
| `applicationId` | `string` | one of   | Numeric ID of an application, as a quoted string matching `^\d+$`. Expanded server-side to every flow whose source **or** destination workload belongs to that application. |
| `callbackUrl`   | `string` | no       | Relative path that the completion notification in the UI links to. Maximum 2048 characters.      |

Both IDs come from the AIM inventory tables -- the `id` column of the
Applications and Flows tables respectively. See
[End-to-End Workflow](end_to_end_workflow.md) for how to look them up.

!!! note "`callbackUrl` must be an internal relative path"

    The value is rendered as a link, so it is validated to prevent open
    redirects: it must start with a single `/` and must not contain a scheme,
    host, whitespace, or backslashes. This field only affects the UI
    notification and can be omitted for headless integrations.

### Example Request

!!! example "Calculate Every Flow of One Application"

    Sample payload:

    ```json
    {
      "applicationId": "46"
    }
    ```

    Example cURL command:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/flow-path-lookups/{snapshotId}' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{"applicationId":"46"}'
    ```

!!! example "Calculate a Single Flow With a UI Callback"

    Sample payload:

    ```json
    {
      "flowId": "894",
      "callbackUrl": "/inventory/applications/devices"
    }
    ```

    Example cURL command:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/flow-path-lookups/{snapshotId}' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{"flowId":"894","callbackUrl":"/inventory/applications/devices"}'
    ```

### Response

A successful request returns `202 Accepted` with a JSON body containing a single
key:

| Field   | Type     | Description                                                                 |
| :------ | :------- | :-------------------------------------------------------------------------- |
| `jobId` | `string` | Numeric identifier of the scheduled background job, as a quoted string. Use it to poll the job. |

!!! example "Successful Response"

    ```json
    {
      "jobId": "184"
    }
    ```

The scheduled job has the action name `aimFlowPathLookup`.

| Code  | Meaning                                                                                   |
| :---- | :---------------------------------------------------------------------------------------- |
| `202` | Path-lookup job scheduled. The body contains the `jobId`.                                 |
| `400` | Invalid body, invalid `snapshotId`, or no flows matched the given application.             |
| `401` | Unauthorized.                                                                             |
| `403` | Missing RBAC permissions or no AIM license.                                               |
| `404` | Snapshot not found, or the snapshot is not loaded.                                        |
| `500` | Internal server error.                                                                    |

!!! info "The calculation is idempotent"

    Flows that already have a stored path-lookup result are skipped. Re-running
    the calculation for the same application completes almost immediately and
    writes nothing. Note also that a flow between two applications belongs to
    both, so calculating one application also covers that shared flow for the
    other.

## Verify an AIM Integration Connection

Three endpoints check that an external AIM data provider -- ingestion method 1
above -- is reachable and that its credentials are accepted. No discovery is
started, no job is scheduled, and nothing is written to the settings; the request
is answered synchronously.

They differ only in where the integration definition is read from:

| Endpoint                                                    | Integration read from        | Use when                                                                    |
| :---------------------------------------------------------- | :--------------------------- | :-------------------------------------------------------------------------- |
| `POST /aim/integrations/verify`                             | the request body alone       | The integration is not saved yet, or you have its secret in plaintext.       |
| `POST /aim/integrations/{id}/verify`                         | the global settings          | Testing a saved integration without resending its secret.                    |
| `POST /snapshots/{snapshotId}/aim/integrations/{id}/verify`  | that snapshot's settings     | Same, for an integration on a snapshot's settings page.                      |

`Illumio` is currently the only accepted `platform`.

### Integration Fields

The same field set is used by all three endpoints. It is fully required in the
body-only variant and fully optional in the two stored variants, where each
omitted field falls back to the stored value.

| Field            | Type              | Description                                                                                  |
| :--------------- | :---------------- | :------------------------------------------------------------------------------------------- |
| `platform`       | `string`          | Data provider platform. Must be `Illumio`.                                                    |
| `apiUrl`         | `string`          | PCE base URL, host and port.                                                                  |
| `apiKey`         | `string`          | Illumio API key ID, used as the authentication username.                                      |
| `apiSecret`      | `string`          | Illumio API key secret, in **plaintext**.                                                     |
| `organizationId` | `string`          | Illumio PCE organization ID, used to build the `/api/v2/orgs/{organizationId}/...` path.       |
| `slug`           | `string`          | Unique identifier of the configuration instance. Max 64 characters, `^[a-zA-Z0-9_-]+$`.        |
| `comment`        | `string` \| `null`| Free-form note, or `null`.                                                                    |

No other properties are accepted -- an unknown field fails validation.

!!! warning "`apiSecret` must be plaintext"

    The endpoints reject an encrypted value with
    `apiSecret must be provided in plaintext; omit it to reuse the stored secret`.
    Stored secrets are encrypted, so they cannot be read out and replayed. To
    test a saved integration, use one of the `{id}/verify` variants and **omit**
    `apiSecret` -- the stored value is decrypted server-side and never leaves the
    appliance.

### Test an Integration From the Request Body

Tests an integration described entirely by the body. Nothing is read from or
written to storage, so this covers an integration that has not been saved yet.

```text
POST /api/aim/integrations/verify
Content-Type: application/json
```

All seven fields are required.

!!! example "Verify an Unsaved Integration"

    Sample payload:

    ```json
    {
      "platform": "Illumio",
      "apiUrl": "https://pce.example.com:8443",
      "apiKey": "api_1234567890abcdef",
      "apiSecret": "{api_secret}",
      "organizationId": "12345",
      "slug": "illumio-prod",
      "comment": "Production PCE"
    }
    ```

    Example cURL command:

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/integrations/verify' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{"platform":"Illumio","apiUrl":"https://pce.example.com:8443","apiKey":"api_1234567890abcdef","apiSecret":"{api_secret}","organizationId":"12345","slug":"illumio-prod","comment":"Production PCE"}'
    ```

    A successful test returns `204 No Content` with an empty body.

### Test a Stored Global Integration

Tests an integration stored in the global settings. Every body field is an
optional override applied on top of the stored record, which lets unsaved form
edits be tested before they are saved.

```text
POST /api/aim/integrations/{id}/verify
Content-Type: application/json
```

| Parameter | In   | Type            | Required | Description                              |
| :-------- | :--- | :-------------- | :------- | :--------------------------------------- |
| `id`      | path | `string` (UUID) | yes      | UUID of the stored AIM integration.      |

!!! example "Verify a Stored Integration As-Is"

    Send an empty object to test exactly what is stored:

    ```json
    {}
    ```

    ```bash
    curl -X POST 'https://{ipf_server}/api/aim/integrations/{id}/verify' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{}'
    ```

!!! example "Verify a Stored Integration With Edits"

    Test a changed URL while reusing the stored key and secret:

    ```json
    {
      "apiUrl": "https://pce-new.example.com:8443"
    }
    ```

### Test a Stored Snapshot Integration

The snapshot-scoped counterpart of the previous endpoint. AIM integrations shown
on a snapshot's settings pages belong to that snapshot, so they are read from the
snapshot rather than from the global settings.

```text
POST /api/snapshots/{snapshotId}/aim/integrations/{id}/verify
Content-Type: application/json
```

| Parameter    | In   | Type            | Required | Description                                              |
| :----------- | :--- | :-------------- | :------- | :------------------------------------------------------- |
| `snapshotId` | path | `string` (UUID) | yes      | UUID of the snapshot whose settings hold the integration. |
| `id`         | path | `string` (UUID) | yes      | UUID of the stored AIM integration.                       |

The body is identical to the global variant -- optional overrides, or `{}` to
test the stored record as-is.

!!! example "Verify a Snapshot Integration"

    ```bash
    curl -X POST 'https://{ipf_server}/api/snapshots/{snapshotId}/aim/integrations/{id}/verify' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{}'
    ```

### Response

On success all three endpoints return **`204 No Content`** with an empty body.
There is no `jobId`, because the test runs synchronously.

A failed connection is reported as `400`, not as a `2xx` result with a status
field -- so treat any non-`204` response as a failed test.

| Code  | Meaning                                                                                                     |
| :---- | :---------------------------------------------------------------------------------------------------------- |
| `204` | The connection succeeded.                                                                                   |
| `400` | Invalid body, an encrypted `apiSecret`, or a failed connection test -- unreachable URL or rejected credentials. |
| `401` | Unauthorized.                                                                                               |
| `403` | Missing RBAC permissions or no AIM license.                                                                 |
| `404` | Stored variants only -- no integration with that id, or, for the snapshot variant, an unknown snapshot.       |
| `500` | Internal server error.                                                                                      |

## AIM Inventory Tables

The ingested data is read back through four table endpoints. They share the same
request and response shape and differ only in the columns they return.

```text
POST /api/tables/inventory/applications
POST /api/tables/inventory/applications/workloads
POST /api/tables/inventory/applications/flows
POST /api/tables/inventory/applications/devices
Content-Type: application/json
```

### Common Request Body

| Field        | Type     | Required | Description                                                                                     |
| :----------- | :------- | :------- | :---------------------------------------------------------------------------------------------- |
| `columns`    | array    | yes      | Columns to return. At least one, chosen from the table's column list below.                       |
| `snapshot`   | `string` | yes      | Snapshot UUID, or one of the reserved keywords `$last`, `$prev`, `$lastLocked`.                   |
| `filters`    | object   | no       | Column filters. Omit to return every row.                                                        |
| `pagination` | object   | no       | `{ "limit": 100, "start": 0 }`. **`limit` defaults to 10**, so set it explicitly for full listings. |
| `sort`       | object   | no       | `{ "column": "name", "order": "asc" }`. `order` accepts `asc` or `desc`.                          |
| `format`     | object   | no       | `{ "exportToFile": true, "dataType": "csv" }` returns a downloadable file instead of JSON.        |

!!! note "Reserved snapshot keywords are allowed here"

    Unlike the two AIM endpoints above, which require a UUID, the table endpoints
    also accept `$last`, `$prev`, and `$lastLocked`.

Each filter entry takes the form `"column": [operator, value]`, for example
`["eq", "app-001"]` or `["like", "web"]`. Nest arrays of filter objects under
`and` or `or` to combine conditions.

### Common Response

| Field            | Type      | Description                                                        |
| :--------------- | :-------- | :----------------------------------------------------------------- |
| `data`           | array     | Matching rows. Each object contains exactly the requested columns.  |
| `_meta.count`    | `integer` | Total number of matching rows, ignoring pagination.                 |
| `_meta.size`     | `integer` | Number of rows returned in this response.                          |
| `_meta.limit`    | `integer` | Applied page size.                                                 |
| `_meta.start`    | `integer` | Applied offset.                                                    |
| `_meta.snapshot` | `string`  | Snapshot the data was read from, with any keyword already resolved. |

All timestamp columns are Unix milliseconds.

### Applications

Lists the applications in the snapshot. This is also where you obtain the numeric
`id` used as `applicationId` when calculating path lookups.

| Column            | Type      | Description                                                                    |
| :---------------- | :-------- | :----------------------------------------------------------------------------- |
| `id`              | `string`  | Numeric application ID.                                                        |
| `name`            | `string`  | Application name.                                                              |
| `externalId`      | `string`  | Key supplied in `applications.csv`.                                            |
| `environment`     | `string`  | Free-text environment value. Populated for applications maintained in the Discovery Settings and for those imported from CSV; empty for applications collected through the Illumio integration. Hidden by default in the UI, but unaffected here -- request it like any other column. |
| `dataSourceName`  | `string`  | Origin of the data. Manually ingested data reports the manual source.           |
| `flows`           | `integer` | Number of flows belonging to the application.                                  |
| `flowsCalculated` | `integer` | How many of those flows already have a path-lookup result.                     |
| `workloads`       | `integer` | Number of workloads.                                                           |
| `devices`         | `integer` | Number of traversed devices. `0` until path lookups run.                       |
| `entrypoints`     | `string`  | Reserved for a future release; not populated yet.                              |
| `createdAt`       | `integer` | Creation timestamp.                                                            |
| `updatedAt`       | `integer` | Last change timestamp.                                                         |

!!! example "List Applications"

    Sample payload:

    ```json
    {
      "columns": ["id", "name", "externalId", "environment", "dataSourceName", "flows", "flowsCalculated", "workloads", "devices"],
      "snapshot": "{snapshotId}",
      "pagination": { "limit": 50, "start": 0 },
      "sort": { "column": "name", "order": "asc" }
    }
    ```

    Example cURL command:

    ```bash
    curl -X POST 'https://{ipf_server}/api/tables/inventory/applications' \
      --header 'Content-Type: application/json' \
      --header 'X-API-Token: {api_token}' \
      -d '{"columns":["id","name","externalId","flows","flowsCalculated","workloads","devices"],"snapshot":"{snapshotId}","pagination":{"limit":50,"start":0}}'
    ```

    Example response:

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
          "flowsCalculated": 1,
          "workloads": 1,
          "devices": 1
        }
      ],
      "_meta": { "limit": 50, "start": 0, "count": 1, "size": 1, "snapshot": "{snapshotId}" }
    }
    ```

The remaining tables use identical headers and the same body structure, so only
their columns and payloads are shown below.

### Workloads

Lists the workloads and their interface addresses.

| Column                  | Type     | Description                                              |
| :---------------------- | :------- | :------------------------------------------------------- |
| `id`                    | `string` | Numeric workload ID.                                     |
| `name`                  | `string` | Workload name.                                           |
| `workloadHostname`      | `string` | Hostname from `workloads.csv`.                            |
| `workloadInterface`     | `string` | IP address of a workload interface.                       |
| `applicationName`       | `string` | Owning application.                                       |
| `applicationExternalId` | `string` | Owning application's `externalId`.                        |
| `createdAt`             | `integer`| Creation timestamp.                                       |
| `updatedAt`             | `integer`| Last change timestamp.                                    |

!!! info "One row per workload interface"

    Because interfaces are joined in, a workload with two interfaces returns two
    rows that differ only in `workloadInterface`. Omit that column to get one row
    per workload.

!!! example "List Workloads of One Application"

    Sample payload:

    ```json
    {
      "columns": ["id", "name", "workloadHostname", "workloadInterface", "applicationName", "applicationExternalId"],
      "filters": { "applicationExternalId": ["eq", "app-001"] },
      "snapshot": "{snapshotId}",
      "pagination": { "limit": 100, "start": 0 }
    }
    ```

    Example response:

    ```json
    {
      "data": [
        {
          "id": "88",
          "name": "web-server-01",
          "workloadHostname": "web01.example.com",
          "workloadInterface": "10.0.1.10",
          "applicationName": "Frontend Service",
          "applicationExternalId": "app-001"
        }
      ],
      "_meta": { "limit": 100, "start": 0, "count": 1, "size": 1, "snapshot": "{snapshotId}" }
    }
    ```

### Flows

Lists the flows and whether each one has been calculated. This is where you obtain
the numeric `id` used as `flowId` when calculating a single flow.

| Column                         | Type      | Description                                                                                   |
| :----------------------------- | :-------- | :-------------------------------------------------------------------------------------------- |
| `id`                           | `string`  | Numeric flow ID.                                                                              |
| `srcWorkload`                  | `string`  | Source workload name.                                                                         |
| `dstWorkload`                  | `string`  | Destination workload name.                                                                    |
| `srcApplicationName`           | `string`  | Application owning the source workload.                                                       |
| `srcApplicationExternalId`     | `string`  | That application's `externalId`.                                                              |
| `dstApplicationName`           | `string`  | Application owning the destination workload.                                                  |
| `dstApplicationExternalId`     | `string`  | That application's `externalId`.                                                              |
| `applicationFlow`              | `string`  | Both endpoints as one label, `source → destination`, by workload name or by IP address when the workload is unnamed. |
| `pathLookupsCalculationStatus` | `boolean` | Whether this flow's path-lookup has been calculated.                                           |
| `devices`                      | `integer` | Number of network devices this flow traverses. Empty until the path-lookup is calculated.      |
| `srcIp`                        | `string`  | Source IP address.                                                                            |
| `dstIp`                        | `string`  | Destination IP address.                                                                       |
| `srcPort`                      | `integer` | Source port.                                                                                  |
| `dstPort`                      | `integer` | Destination port.                                                                             |
| `protocol`                     | `integer` | IANA protocol number.                                                                         |
| `createdAt`                    | `integer` | Creation timestamp.                                                                           |
| `lastDetected`                 | `integer` | Value supplied in `flows.csv`, if any.                                                        |

!!! example "List Flows Awaiting Calculation"

    Sample payload:

    ```json
    {
      "columns": ["id", "srcWorkload", "dstWorkload", "srcApplicationName", "dstApplicationName", "srcIp", "dstIp", "srcPort", "dstPort", "protocol", "pathLookupsCalculationStatus", "devices"],
      "filters": { "pathLookupsCalculationStatus": ["eq", false] },
      "snapshot": "{snapshotId}",
      "pagination": { "limit": 100, "start": 0 }
    }
    ```

    Example response:

    ```json
    {
      "data": [
        {
          "id": "894",
          "srcWorkload": "web-server-01",
          "dstWorkload": "api-server-01",
          "srcApplicationName": "Frontend Service",
          "dstApplicationName": "Backend API",
          "srcIp": "10.0.1.10",
          "dstIp": "10.0.2.20",
          "srcPort": 54321,
          "dstPort": 8080,
          "protocol": 6,
          "pathLookupsCalculationStatus": false,
          "devices": null
        }
      ],
      "_meta": { "limit": 100, "start": 0, "count": 1, "size": 1, "snapshot": "{snapshotId}" }
    }
    ```

!!! info "`devices` separates a flow with no result from a genuine zero"

    On this table `devices` is `null` while the flow has no path-lookup result,
    and a number once it has -- including a genuine `0` for a flow whose path
    traverses no device. Use `pathLookupsCalculationStatus` to test whether the
    calculation has run, not the device count.

    The Applications table behaves differently: its `devices` is a total across
    the application's flows, so it reads `0` rather than `null` before anything
    is calculated.

### Devices

Lists the network devices the calculated flows traverse. Populated only by the
path-lookup calculation -- empty until it runs.

| Column                     | Type     | Description                                                                                    |
| :------------------------- | :------- | :--------------------------------------------------------------------------------------------- |
| `id`                       | `string` | Numeric row ID of the flow-device pair.                                                        |
| `hostname`                 | `string` | Device hostname.                                                                               |
| `sn`                       | `string` | Unique serial number assigned by IP Fabric.                                                    |
| `snHw`                     | `string` | Hardware serial number.                                                                        |
| `flowId`                   | `string` | Numeric ID of the flow whose path traverses this device. Filter on it to list one flow's devices. |
| `srcApplicationName`       | `string` | Application owning the flow's source workload.                                                 |
| `srcApplicationExternalId` | `string` | That application's `externalId`.                                                               |
| `dstApplicationName`       | `string` | Application owning the flow's destination workload.                                            |
| `dstApplicationExternalId` | `string` | That application's `externalId`.                                                               |
| `applicationFlow`          | `string` | Both endpoints as one label, `source → destination`, by workload name or by IP address when the workload is unnamed. |
| `srcIp`                    | `string` | The flow's source IP address.                                                                  |
| `dstIp`                    | `string` | The flow's destination IP address.                                                             |
| `srcPort`                  | `integer`| The flow's source port.                                                                        |
| `dstPort`                  | `integer`| The flow's destination port.                                                                   |
| `protocol`                 | `integer`| The flow's IANA protocol number.                                                               |
| `deviceId`                 | `string` | Internal device identifier.                                                                    |
| `devLabels`                | array    | Device labels, when the labels feature is enabled.                                             |

The flow's five-tuple -- `srcIp`, `dstIp`, `srcPort`, `dstPort`, and `protocol` --
is carried here as well as on the Flows table, so a device row is enough to
reconstruct the flow it belongs to.

!!! note "Scoping devices to one application"

    A device is not owned by an application -- it is reached through a flow whose
    source **or** destination workload belongs to one. Match both sides with an
    `or` filter, as below. Rows represent `{flow, device}` pairs, so a device
    repeats once per traversing flow; de-duplicate on `sn` for a unique device
    list.

!!! example "List Devices of One Application"

    Sample payload:

    ```json
    {
      "columns": ["id", "hostname", "sn", "snHw", "flowId", "srcApplicationName", "dstApplicationName", "applicationFlow"],
      "filters": { "or": [
        { "srcApplicationName": ["eq", "Frontend Service"] },
        { "dstApplicationName": ["eq", "Frontend Service"] }
      ]},
      "snapshot": "{snapshotId}",
      "pagination": { "limit": 200, "start": 0 },
      "sort": { "column": "hostname", "order": "asc" }
    }
    ```

    Example response:

    ```json
    {
      "data": [
        {
          "id": "1749",
          "hostname": "SW-CORE-01",
          "sn": "SN12345678",
          "snHw": "SN12345678",
          "flowId": "894",
          "srcApplicationName": "Frontend Service",
          "dstApplicationName": "Backend API",
          "applicationFlow": "web-server-01 → api-server-01"
        }
      ],
      "_meta": { "limit": 200, "start": 0, "count": 1, "size": 1, "snapshot": "{snapshotId}" }
    }
    ```

!!! tip "Listing the devices of one flow"

    Filter on `flowId` instead of the application names:
    `"filters": { "flowId": ["eq", "894"] }`. This is the filter the Flows
    table's own device count links on, and it is exact -- the `applicationFlow`
    workload pair is not unique per flow.

### Response Codes

Common to all four table endpoints:

| Code  | Meaning                                                                     |
| :---- | :-------------------------------------------------------------------------- |
| `200` | Success.                                                                    |
| `400` | Invalid body -- unknown column, malformed filter, or missing `snapshot`.     |
| `401` | Unauthorized.                                                               |
| `403` | Missing RBAC permissions or no AIM license.                                 |
| `500` | Internal server error.                                                      |

## Next Steps

The two AIM endpoints only schedule work. To poll the returned `jobId`, interpret
job failures, and chain all of these calls into a single automated sequence, see
[End-to-End Workflow](end_to_end_workflow.md).
