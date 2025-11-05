---
description: This section describes how to clear the IP Fabric database, which might be necessary in some rare cases.
---

# Clear DB

!!! warning

    Before clearing the database, make sure that you have access to a recent
    backup!

!!! important

    After clearing the database, we highly recommend rebooting the IP Fabric
    appliance. This is especially important if you have experienced issues with
    a low amount of available RAM and a lot of memory data was moved to the disk
    swap.

In rare cases, it might be necessary to delete and recreate the IP Fabric
database. To do that, navigate to **Settings --> System --> Backup &
Maintenance** and click **Clear DB**.

When running Clear DB, all loaded snapshots are automatically unloaded, and the
database recreated.

![Clear DB](../../../images/settings/IP_Fabric_Settings-system-Backup_and_Maintenance-cleardb_cleardb.png)

There are two-way confirmations.

![First confirmation](../../../images/settings/IP_Fabric_Settings-system-Backup_and_Maintenance-cleardb_cleardb_first_confirmation.png)

In the second screen, you can choose between **Reset Settings** and **Keep
Settings**:

![Second confirmation](../../../images/settings/IP_Fabric_Settings-system-Backup_and_Maintenance-cleardb_cleardb_second_confirmation.png)

We recommend selecting **Keep Settings**. If you select **Reset Settings**, all
system and discovery settings will be lost, including login credentials, Site
Separation rules, saved views, shared URLs, filters, and API tokens. The system
settings will be reset to defaults **except for**:

- Certificate authorities
- User settings
- LDAP settings
- Reports settings
- Dashboard settings
