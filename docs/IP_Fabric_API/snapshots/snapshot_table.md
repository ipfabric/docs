---
description: In IP Fabric 4.3.0, a new method for retrieving snapshot information was added. It allows for filtering based on columns.
---

# Snapshot Table

In IP Fabric `4.3.0`, a new method for retrieving snapshot information was
added. This is a `POST` method to `tables/management/snapshots` that allows for
filtering based on columns.

## Columns

| Name                   | Type    | Description                                                                                   |
| :--------------------- | :------ | :-------------------------------------------------------------------------------------------- |
| `id`                   | string  | Snapshot ID.                                                                                  |
| `status`               | string  | `done` -- Loaded.<br/>`unloaded` -- Unloaded.<br/>`ready` -- The snapshot record was created, but the discovery process has not started yet.<br/>`run` -- Discovery or snapshot load is in progress.<br/>`finishing` -- Almost done, Tasker is creating topology and other calculations like Site Separation.<br/>`error` -- Errored. |
| `finishStatus`         | string  | `done` -- Done.<br/>`error` -- Errored.<br/>'' -- Other.                                      |
| `loading`              | Boolean | `true` if the snapshot is currently loading.                                                  |
| `loadedSize`           | integer | Size of the snapshot when loaded.                                                             |
| `unloadedSize`         | integer | Size of the snapshot when unloaded.                                                           |
| `isLastSnapshot`       | Boolean | `true` if it is the last loaded snapshot (`$last`).                                           |
| `name`                 | string  | Snapshot name or an empty string.                                                             |
| `note`                 | string  | Snapshot note or an empty string.                                                             |
| `sites`                | list    | List of site names.                                                                           |
| `fromArchive`          | Boolean | `true` if the snapshot was loaded from a file.                                                |
| `locked`               | Boolean | `true` if the snapshot is locked.                                                             |
| `totalDevCount`        | integer | Number of total devices (`licensed` and `unlicensed`).                                        |
| `deviceAddedCount`     | integer | Number of devices added since the previous snapshot.                                          |
| `deviceRemovedCount`   | integer | Number of devices removed since the previous snapshot.                                        |
| `interfaceCount`       | integer | Number of interfaces.<br/>**Inventory --> Interfaces**                                        |
| `interfaceActiveCount` | integer | Number of active interfaces.<br/>**Inventory --> Interfaces** [Filter L2 State=up]            |
| `interfaceEdgeCount`   | integer | Number of edge interfaces.<br/>**Technology --> Interfaces --> Switchport** [Filter Edge=yes] |
| `userCount`            | integer | Number of hosts.<br/>**Inventory --> Hosts**                                                  |
| `tsStart`              | integer | Timestamp in milliseconds when the snapshot started.                                          |
| `tsEnd`                | integer | Timestamp in milliseconds when the snapshot completed.                                        |
| `tsChange`             | integer | Timestamp in milliseconds when the snapshot was last changed.                                 |
| `creatorUsername`      | string  | Username of the user who created the snapshot (new in `6.3.0`).                               |

## Version `4.3.0` Examples

### Get `($last)`

```json
{
  "columns": [
    "id",
    "status",
    "finishStatus",
    "loadedSize",
    "unloadedSize",
    "name",
    "note",
    "sites",
    "fromArchive",
    "loading",
    "locked",
    "deviceAddedCount",
    "deviceRemovedCount",
    "interfaceActiveCount",
    "interfaceCount",
    "interfaceEdgeCount",
    "totalDevCount",
    "isLastSnapshot",
    "tsChange",
    "tsEnd",
    "tsStart",
    "userCount"
  ],
  "filters": {
    "and": [
      {
        "isLastSnapshot": ["eq", true]
      }
    ]
  }
}
```

### Get Valid Snapshots From Newest to Oldest

```json
{
  "columns": [
    "id",
    "status",
    "finishStatus",
    "loadedSize",
    "unloadedSize",
    "name",
    "note",
    "sites",
    "fromArchive",
    "loading",
    "locked",
    "deviceAddedCount",
    "deviceRemovedCount",
    "interfaceActiveCount",
    "interfaceCount",
    "interfaceEdgeCount",
    "totalDevCount",
    "isLastSnapshot",
    "tsChange",
    "tsEnd",
    "tsStart",
    "userCount"
  ],
  "filters": {
    "and": [
      {
        "finishStatus": ["neq", "error"]
      }
    ]
  },
  "sort": {
    "order": "desc",
    "column": "tsEnd"
  }
}
```

### Get Loaded Snapshots From Newest to Oldest

```json
{
  "columns": [
    "id",
    "status",
    "finishStatus",
    "loadedSize",
    "unloadedSize",
    "name",
    "note",
    "sites",
    "fromArchive",
    "loading",
    "locked",
    "deviceAddedCount",
    "deviceRemovedCount",
    "interfaceActiveCount",
    "interfaceCount",
    "interfaceEdgeCount",
    "totalDevCount",
    "isLastSnapshot",
    "tsChange",
    "tsEnd",
    "tsStart",
    "userCount"
  ],
  "filters": {
    "and": [
      {
        "status": ["eq", "done"]
      },
      {
        "finishStatus": ["eq", "done"]
      }
    ]
  },
  "sort": {
    "order": "desc",
    "column": "tsEnd"
  }
}
```

### Get Locked Snapshots From Oldest to Newest

```json
{
  "columns": [
    "id",
    "status",
    "finishStatus",
    "loadedSize",
    "unloadedSize",
    "name",
    "note",
    "sites",
    "fromArchive",
    "loading",
    "locked",
    "deviceAddedCount",
    "deviceRemovedCount",
    "interfaceActiveCount",
    "interfaceCount",
    "interfaceEdgeCount",
    "totalDevCount",
    "isLastSnapshot",
    "tsChange",
    "tsEnd",
    "tsStart",
    "userCount"
  ],
  "filters": {
    "and": [
      {
        "locked": ["eq", true]
      }
    ]
  },
  "sort": {
    "order": "asc",
    "column": "tsEnd"
  }
}
```

### Get the Running Snapshot

```json
{
  "columns": [
    "id",
    "status",
    "finishStatus",
    "loadedSize",
    "unloadedSize",
    "name",
    "note",
    "sites",
    "fromArchive",
    "loading",
    "locked",
    "deviceAddedCount",
    "deviceRemovedCount",
    "interfaceActiveCount",
    "interfaceCount",
    "interfaceEdgeCount",
    "totalDevCount",
    "isLastSnapshot",
    "tsChange",
    "tsEnd",
    "tsStart",
    "userCount"
  ],
  "filters": {
    "and": [
      {
        "tsEnd": ["empty", true]
      }
    ]
  }
}
```
