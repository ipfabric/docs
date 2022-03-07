# Message: "Error: AQL: internal error - in index"

When any error containing **Error: AQL: internal error - in index** is
shown after any main action after upgrade (for example after Unloading
snapshot or starting Network discovery).

The database got corrupted (no worries all of your data are safely
stored) and is necessary to run maintenance.

This can be done in ***Settings → Advanced → System*** in the main GUI.
For more information see [Schedule System
Maintenance](Schedule_System_Maintenance)

If this does not help, we recommend restarting ArangoDB process in
System Administration (port 8443) [System Status](System_Status) and
running maintenance - see the previous step
