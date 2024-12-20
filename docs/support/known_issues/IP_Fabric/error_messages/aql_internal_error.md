---
description: 'This page describes what to do if you encounter "Error: AQL: internal error - in index".'
---

# Error: AQL: internal error -- in index

When `Error: AQL: internal error - in index` appears after any main action
following an upgrade (for example, after unloading a snapshot or starting
network discovery), it indicates that the database has become corrupted (rest
assured, all your data is safely stored).

To resolve this issue, you need to perform System Maintenance:

1. In the main GUI, navigate to **Settings --> System --> Backup &
   Maintenance**. For more information, see
   [Schedule System Maintenance](../../../../IP_Fabric_Settings/system/Backup_and_Maintenance/system_maintenance.md).

2. If the above step does not resolve the issue, we recommend restarting the
   ArangoDB process in **[System status](../../../../IP_Fabric_GUI/tips/system_status.md)**
   and then running System Maintenance again.
