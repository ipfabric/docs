# Error: AQL: internal error - in index

When any error containing `Error: AQL: internal error - in index` is
shown after any main action after upgrade (for example after Unloading
snapshot or starting Network discovery).

The database got corrupted (no worries all of your data are safely
stored) and is necessary to run maintenance.

This can be done in **_Settings → Advanced → System_** in the main GUI.
For more information see [Schedule System Maintenance](../../../../../IP_Fabric_GUI/settings/advanced/system/Schedule_System_Maintenance)

If this does not help, we recommend restarting ArangoDB process in
System Administration (port `8443`) [System Status](../../../../IP_Fabric_Settings/System_admin_UI/system_status.md) and
running maintenance - see the previous step
