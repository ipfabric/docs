---
description: How to import a label catalog and bulk label assignments into IP Fabric using the API.
---

# Import Labels via API

--8<-- "snippets/labels_experimental.md"

You can use the API to import labels from an external source, such as a CMDB or a spreadsheet. This avoids creating them one by one in the GUI. An import has two steps:

1. [Import the label catalog](#step-1-import-the-label-catalog) -- the label
   names and the values you expect to use with them.
2. [Import label assignments](#step-2-import-label-assignments) -- which
   devices and interfaces carry which labels.

The examples use `curl` with an [API token](../integration/api_tokens.md)
passed in the `X-API-Token` header. The user owning the token must have access
to **Settings**. See [API Authentication](../../IP_Fabric_API/authentication.md)
for other authentication methods.

## Step 1: Import the Label Catalog

Send one `POST /labels` request per label name:

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/labels' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{
  "name": "region",
  "values": ["EMEA", "APAC", "US"]
}'
```

| Field    | Required | Description                                                                                             |
| -------- | -------- | ------------------------------------------------------------------------------------------------------- |
| `name`   | Yes      | Label name, 1--64 characters. Allowed characters: letters, digits, hyphens (`-`), and underscores (`_`). |
| `values` | No       | List of expected values. Each value is 1--128 characters long and cannot contain a colon (`:`).          |

The response (`201 Created`) has the catalog entry, including its `id`:

```json
{
  "id": "<LABEL_ID>",
  "name": "region",
  "values": ["EMEA", "APAC", "US"],
  "createdBy": "<USER_ID>",
  "createdAt": 1758787200000,
  "changedAt": 1758787200000,
  "changedBy": "<USER_ID>"
}
```

`POST /labels` identifies catalog entries by `name`. When an entry with the same name already exists, the call replaces its `values` with the list you send and keeps the same `id`. It does not merge the two lists, so you can run the same import again safely. Always send the full list of values for each label.

To check the imported catalog, list all entries with `GET /labels`:

```shell
curl --location --request GET 'https://<FQDN>/api/<API_VERSION>/labels' \
--header 'X-API-Token: <YOUR_API_TOKEN>'
```

!!! info

    Importing the catalog does not assign any labels. The catalog only drives
    autocomplete in the GUI. You can assign a label in step 2 even if it is not
    in the catalog.

## Step 2: Import Label Assignments

IP Fabric makes label assignments in a specific snapshot. First, find the ID of a loaded snapshot — the latest one — with `GET /snapshots`. The `snapshotId` field must be a snapshot UUID; `$last` is not accepted.

Then assign labels with `POST /labels/assignments`. A single call can assign several labels to many devices and interfaces at once:

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/labels/assignments' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{
  "snapshotId": "<SNAPSHOT_ID>",
  "labels": [
    { "name": "region", "value": "EMEA" },
    { "name": "pci" }
  ],
  "targets": [
    { "type": "device", "sn": "<DEVICE_SN_1>" },
    { "type": "device", "sn": "<DEVICE_SN_2>" },
    { "type": "intL2", "sn": "<DEVICE_SN_3>", "interfaceName": "Gi1/0/1" }
  ],
  "inherit": false,
  "reflectToRules": true
}'
```

| Field            | Required | Description                                                                                                                                                                                                                       |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `snapshotId`     | Yes      | UUID of the snapshot to assign the labels in.                                                                                                                                                                                     |
| `labels`         | Yes      | At least one label. Each label has a `name` and an optional `value`. Omit `value` for labels without a value, such as `pci`.                                                                                                     |
| `targets`        | Yes      | At least one target. A device is `{ "type": "device", "sn": "<SN>" }`. An L2 interface is `{ "type": "intL2", "sn": "<SN>", "interfaceName": "<INTERFACE>" }`. A single request can mix devices and interfaces.                  |
| `inherit`        | No       | When `true`, the labels assigned to devices are also inherited by the devices' L2 interfaces. Corresponds to **Assign also to children** in the GUI.                                                                              |
| `reflectToRules` | No       | When `true`, the system keeps the assignment for future snapshots and it survives label recalculation. When `false` (default), the assignment applies only to this snapshot and disappears at the next label calculation. Corresponds to **Apply to future snapshots** in the GUI. |

A successful call returns `204 No Content`.

!!! important "Set `reflectToRules` for Imports"

    `reflectToRules` defaults to `false` in the API, unlike in the GUI. For an
    import that should persist, always set `"reflectToRules": true`. Otherwise,
    the labels disappear after the next discovery.

Where to get the target values:

- `sn` -- The IP Fabric Unique Serial Number of the device -- the `sn` column
  of **Inventory --> Devices** (`POST /tables/inventory/devices`).
- `interfaceName` -- The interface name -- the `intName` column of
  **Inventory --> Interfaces** (`POST /tables/inventory/interfaces`).

You can also search for targets by hostname, serial number, or interface name
with `GET /labels/assignment-targets?search=<TERM>`.

To import assignments for several label combinations, send one `POST /labels/assignments` call per combination — for example, one call for all `region:EMEA` devices and another for all `region:APAC` devices.

### Removing Assignments

To remove labels, send the same body to `POST /labels/assignments/unassign`.
Set `"reflectToRules": true` to also remove the labels from future snapshots:

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/labels/assignments/unassign' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{
  "snapshotId": "<SNAPSHOT_ID>",
  "labels": [{ "name": "region", "value": "EMEA" }],
  "targets": [{ "type": "device", "sn": "<DEVICE_SN_1>" }],
  "reflectToRules": true
}'
```

## Verify the Import

List every label assignment in the snapshot with `POST /tables/labels`:

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/tables/labels' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{
  "columns": ["type", "hostname", "target", "label", "assignment"],
  "filters": {},
  "snapshot": "<SNAPSHOT_ID>",
  "pagination": { "limit": 100, "start": 0 }
}'
```

Each row has the target type (`device` or `intL2`), the hostname, the target, the label, and the assignment source (`manual`, `auto`, or `inherited`). Imported assignments have the source `manual`.

You can also check the result in the GUI, in **Settings --> Discovery &
Snapshots --> Discovery Data Enrichment --> Assigned labels**.
