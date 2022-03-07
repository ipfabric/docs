# API Tech Note - Snapshot Table

In IP Fabric v4.3.0 a new method for retrieving Snapshot information has
been added. This is a POST method to “tables/management/snapshots” which
allows for filtering based on columns.

# Columns

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="4a39fe69-bd28-4d1e-a079-73443b10b918">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Name</strong></p></th>
<th class="confluenceTh"><p><strong>Type</strong></p></th>
<th class="confluenceTh"><p><strong>Description</strong></p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>id</p></td>
<td class="confluenceTd"><p>str</p></td>
<td class="confluenceTd"><p>Snapshot ID</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>status</p></td>
<td class="confluenceTd"><p>str</p></td>
<td class="confluenceTd"><p>‘done’ - Loaded</p>
<p>‘unloaded’ - Unloaded</p>
<p>‘ready’ - The snapshot record was created, discovery process not started yet</p>
<p>‘run’ - Discovery or Snapshot Load in progress</p>
<p>‘finishing’ - Almost done, Tasker creating Topology and other calculations like site separation</p>
<p>‘error’ - Errored</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>finishStatus</p></td>
<td class="confluenceTd"><p>str</p></td>
<td class="confluenceTd"><p>‘done’ - Done</p>
<p>‘error’ - Errored</p>
<p>'' - Other</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>loading</p></td>
<td class="confluenceTd"><p>bool</p></td>
<td class="confluenceTd"><p>True if the snapshot is currently loading.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>loadedSize</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Size of snapshot when loaded</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>unloadedSize</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Size of snapshot when loaded</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>isLastSnapshot</p></td>
<td class="confluenceTd"><p>bool</p></td>
<td class="confluenceTd"><p>True if it is the last loaded snapshot ($last)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>name</p></td>
<td class="confluenceTd"><p>str</p></td>
<td class="confluenceTd"><p>Snapshot name or empty string</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>note</p></td>
<td class="confluenceTd"><p>str</p></td>
<td class="confluenceTd"><p>Snapshot note or empty string</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>sites</p></td>
<td class="confluenceTd"><p>list</p></td>
<td class="confluenceTd"><p>List of Site Names</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>fromArchive</p></td>
<td class="confluenceTd"><p>bool</p></td>
<td class="confluenceTd"><p>True if snapshot was loaded from a file</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>locked</p></td>
<td class="confluenceTd"><p>bool</p></td>
<td class="confluenceTd"><p>True if snapshot is locked</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>totalDevCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of total devices (licensed and unlicensed)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>deviceAddedCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of devices added since the previous snapshot</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>deviceRemovedCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of devices removed since the previous snapshot</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>interfaceCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of interfaces</p>
<p>Inventory &gt; Interfaces</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>interfaceActiveCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of Active Interface</p>
<p>Inventory &gt; Interfaces [Filter L2 State=up]</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>interfaceEdgeCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of Edge interfaces</p>
<p>Technology &gt; Interfaces &gt; Switchport [Filter Edge=yes]</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>userCount</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Number of hosts</p>
<p>Inventory &gt; Hosts</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>tsStart</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Timestamp in milliseconds when the snapshot started</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>tsEnd</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Timestamp in milliseconds when the snapshot completed</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>tsChange</p></td>
<td class="confluenceTd"><p>int</p></td>
<td class="confluenceTd"><p>Timestamp in milliseconds when the snapshot was last changed</p></td>
</tr>
</tbody>
</table>

</div>

# v4.3.0 Examples

## Get $last

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
    "columns": ["id", "status", "finishStatus", "loadedSize", "unloadedSize", "name", "note", "sites", "fromArchive", "loading", "locked", "deviceAddedCount", "deviceRemovedCount", "interfaceActiveCount", "interfaceCount", "interfaceEdgeCount", "totalDevCount", "isLastSnapshot", "tsChange", "tsEnd", "tsStart", "userCount"],
    "filters": {
        "and": [{
                "isLastSnapshot": [
                    "eq",
                    true
                ]
            }
        ]
    }
}
```

</div>

</div>

## Get Valid Snapshots Newest to Oldest

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
    "columns": ["id", "status", "finishStatus", "loadedSize", "unloadedSize", "name", "note", "sites", "fromArchive", "loading", "locked", "deviceAddedCount", "deviceRemovedCount", "interfaceActiveCount", "interfaceCount", "interfaceEdgeCount", "totalDevCount", "isLastSnapshot", "tsChange", "tsEnd", "tsStart", "userCount"],
    "filters": {
        "and": [{
                "finishStatus": [
                    "neq",
                    "error"
                ]
            }
        ]
    },
    "sort": {
        "order": "desc",
        "column": "tsEnd"
    }
}
```

</div>

</div>

## Get Loaded Snapshots Newest to Oldest

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
    "columns": ["id", "status", "finishStatus", "loadedSize", "unloadedSize", "name", "note", "sites", "fromArchive", "loading", "locked", "deviceAddedCount", "deviceRemovedCount", "interfaceActiveCount", "interfaceCount", "interfaceEdgeCount", "totalDevCount", "isLastSnapshot", "tsChange", "tsEnd", "tsStart", "userCount"],
    "filters": {
        "and": [{
                "status": [
                    "eq",
                    "done"
                ]
            }, {
                "finishStatus": [
                    "eq",
                    "done"
                ]
            }
        ]
    },
    "sort": {
        "order": "desc",
        "column": "tsEnd"
    }
}
```

</div>

</div>

## Get Locked Snapshots Oldest to Newest

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
    "columns": ["id", "status", "finishStatus", "loadedSize", "unloadedSize", "name", "note", "sites", "fromArchive", "loading", "locked", "deviceAddedCount", "deviceRemovedCount", "interfaceActiveCount", "interfaceCount", "interfaceEdgeCount", "totalDevCount", "isLastSnapshot", "tsChange", "tsEnd", "tsStart", "userCount"],
    "filters": {
        "and": [{
                "locked": [
                    "eq",
                    true
                ]
            }
        ]
    },
    "sort": {
        "order": "asc",
        "column": "tsEnd"
    }
}
```

</div>

</div>

## Get Running Snapshot

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
    "columns": ["id", "status", "finishStatus", "loadedSize", "unloadedSize", "name", "note", "sites", "fromArchive", "loading", "locked", "deviceAddedCount", "deviceRemovedCount", "interfaceActiveCount", "interfaceCount", "interfaceEdgeCount", "totalDevCount", "isLastSnapshot", "tsChange", "tsEnd", "tsStart", "userCount"],
    "filters": {
        "and": [{
                "tsEnd": [
                    "empty",
                    true
                ]
            }
        ]
    }
}
```

</div>

</div>
