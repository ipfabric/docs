---
description: In IP Fabric v4.3.0 a new method for retrieving Snapshot information has been added. This method allows for filtering based on columns.
---

# Snapshot Table

In IP Fabric 4.3.0 a new method for retrieving Snapshot information has
been added. This is a `POST` method to `tables/management/snapshots` which
allows for filtering based on columns.

# Columns

| Name                   | Type | Description                                                                                                                                                                                                                                                                                        |
| ---------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                   | str  | Snapshot ID                                                                                                                                                                                                                                                                                        |
| `status`               | str  | `done` - Loaded<br>`unloaded` - Unloaded<br>`ready` - The snapshot record was created, discovery process not started yet<br>`run` - Discovery or Snapshot Load in progress<br>`finishing` - Almost done, Tasker creating Topology and other calculations like site separation<br>`error` - Errored |
| `finishStatus`         | str  | `done` - Done<br>`error` - Errored<br>'' - Other                                                                                                                                                                                                                                                   |
| `loading`              | bool | `true` if the snapshot is currently loading.                                                                                                                                                                                                                                                       |
| `loadedSize`           | int  | Size of snapshot when loaded                                                                                                                                                                                                                                                                       |
| `unloadedSize`         | int  | Size of snapshot when unloaded                                                                                                                                                                                                                                                                       |
| `isLastSnapshot`       | bool | True if it is the last loaded snapshot `($last)`                                                                                                                                                                                                                                                   |
| `name`                 | str  | Snapshot `name` or `empty` string                                                                                                                                                                                                                                                                  |
| `note`                 | str  | Snapshot `note` or `empty` string                                                                                                                                                                                                                                                                  |
| `sites`                | list | List of Site Names                                                                                                                                                                                                                                                                                 |
| `fromArchive`          | bool | `true` if snapshot was loaded from a file                                                                                                                                                                                                                                                          |
| `locked`               | bool | `true` if snapshot is locked                                                                                                                                                                                                                                                                       |
| `totalDevCount`        | int  | Number of total devices (`licensed` and `unlicensed`)                                                                                                                                                                                                                                              |
| `deviceAddedCount`     | int  | Number of devices added since the previous snapshot                                                                                                                                                                                                                                                |
| `deviceRemovedCount`   | int  | Number of devices removed since the previous snapshot                                                                                                                                                                                                                                              |
| `interfaceCount`       | int  | Number of interfaces<br>Inventory &gt; Interfaces                                                                                                                                                                                                                                                  |
| `interfaceActiveCount` | int  | Number of Active Interface<br>Inventory &gt; Interfaces [Filter L2 State=up]                                                                                                                                                                                                                       |
| `interfaceEdgeCount`   | int  | Number of Edge interfaces<br>Technology &gt; Interfaces &gt; Switchport [Filter Edge=yes]                                                                                                                                                                                                          |
| `userCount`            | int  | Number of hosts<br>Inventory &gt; Hosts                                                                                                                                                                                                                                                            |
| `tsStart`              | int  | Timestamp in milliseconds when the snapshot started                                                                                                                                                                                                                                                |
| `tsEnd`                | int  | Timestamp in milliseconds when the snapshot completed                                                                                                                                                                                                                                              |
| `tsChange`             | int  | Timestamp in milliseconds when the snapshot was last changed                                                                                                                                                                                                                                       |
| `creatorUsername`      | str  | Username who created the Snapshot (New in `6.3.0`)                                                                                                                                                                                                                                                 |

# v4.3.0 Examples

## Get `($last)`

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

## Get Valid Snapshots Newest to Oldest

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

## Get Loaded Snapshots Newest to Oldest

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

## Get Locked Snapshots Oldest to Newest

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

## Get Running Snapshot

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
