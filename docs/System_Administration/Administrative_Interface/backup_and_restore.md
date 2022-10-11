---
description: You can schedule an IP Fabric backup to protect your important data locally or remotely. You also have the option to restore a previous backup.
---

# Backup And Restore

## Backup

Use IP Fabric backup to protect your important data.

There are two types of backup:

-   Local backup

-   Remote backup (FTP, sFTP)

!!! tip Security tip

    Backups are encrypted with **osadmin** user password configured during the [first boot wizard](../../Getting_Started/Platform_First_Steps/01-deployment.md#complete-first-time-boot-wizard).
    When you lose **osadmin** user password, backups are also lost!


### Local Backup

Local backup saves database, user and system files locally on a
dedicated backup volume. It's highly recommended placing backup volume
on different datastore ideally on different physical storage.

!!! info "Backup Disk"

	The backup disk is not present by default! Please add a new virtual disk to enable local backups. (See below)

To add a new backup drive and `mount` it as desired, follow instructions in [Increase Disk Space - Local Backup Disk](../../System_Administration/increase_disk_space.md#local-backup-disk).

### Trigger a Backup Manually (On-Demand)

Both types of backup can be also triggered manually on demand. This is
useful for example before a system upgrade.

!!! Warning

	A directory **has to be specified** for FTP and SFTP backups.

	Directory path for **SFTP** has to be defined as **an absolute path** and for **FTP** as a **relative path**. Directory **has to exist** on the remote side. If it does not exist, you will get an error.

Manual backup can be triggered from IP Fabric Administrative interface:

1.  Login to admin interface (for
    example `https://ipfabric.example.com:8443`)

2.  Go to **Restore or Backup**

3.  Select **Backup** from *Do you wish to proceed with a backup or
    restore?* drop-down menu.

4.  For local backup select **Local hard drive** from the **Backup
    files destination**.

5.  For remote backup select **FTP** or **SFTP **from the **Backup
    files destination**.

    1.  Enter remote FTP/SFTP **Server** FQDN or IP address. Make sure
        that your DNS client is configured and working properly in the
        case of FQDN.

    2.  Enter **Username** to access FTP/SFTP server.

    3.  Enter **Password** to access FTP/SFTP server.
		
	!!! Info
		Password can contain only the following characters `A-Za-z0-9.,/-_@%^:=+`

    4.  Specify a **Directory** where FTP/SFTP backup should be
        uploaded.

6.  Click **Next**


## Restore

In case of database or system corruption, IP Fabric can be restored from
a backup.

!!! info

    Restore is supported only to the same version of IP Fabric as source of
    a backup. This is checked automatically during restore.

    The only exception are snapshots which can be restored to any version of
    IP Fabric appliance.


### Restore From Local Hard Drive

1.  Login to admin interface (for
    example `https://ipfabric.example.com:8443`)

2.  Go to **Restore or Backup**

3.  Select **Restore** from *Do you wish proceed a backup or
    restore?* drop down menu.

4.  Select **What restore?** There are four options:

    1.  **Restore data & all system services** - This option restores
        database and system files. It's usable for restore from general
        system failures or upgrade failures.

    2.  **Restore database** - it means that only database data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    3.  **Restore syslog data** - it means that only syslog data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    4.  **Restore snapshot file** - particular snapshot can be
        restored.

5.  For restore from local backup choose **Local hard drive** from
    **Backup files source**.

6.  Click **Next**.

7.  **Select backup file** - there is year, month, day and time when a
    backup file was created in a backup filename.

8.  Click **Restore**.


!!! warning

    Backups are encrypted with **osadmin** user password configured during the [First Boot Wizard](../../Getting_Started/Platform_First_Steps/01-deployment.md#complete-first-time-boot-wizard). When you lose **osadmin** user password, all backups encrypted by this password are lost.


### Restore From Remote Server

1.  Login to admin interface (for
    example `https://ipfabric.example.com:8443`)

2.  Go to **Restore or Backup**

3.  Select **Restore** from *Do you wish proceed a backup or
    restore?* drop down menu.

4.  Select **What restore?** There are four options:

    1.  **Restore data & all system services** - This option restores
        database and system files. It's usable for restore from general
        system failures or upgrade failures.

    2.  **Restore database** - it means that only database data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    3.  **Restore syslog data** - it means that only syslog data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    4.  **Restore snapshot file** - particular snapshot can be
        restored.

5.  For restore from local backup choose **FTP** or **SFTP** from
    **Backup files source**.

6.  Specify **Server** FQDN or IP address. Make sure that your DNS
    client is configured and working properly in case of FQDN.

7.  Enter **Username** to access FTP/SFTP server.

8.  Enter **Password** to access FTP/SFTP server.

9.  If you would like to use different **Directory** than
    FTP/SFTP root please specify.

10. Click **Next**.

11. **Select backup file** - there is year, month, day and time when a
    backup file was created in a backup filename.

12. Click **Restore**.

!!! warning

    Backups are encrypted with **osadmin** user password configured during
    the [First Boot Wizard](../../Getting_Started/Platform_First_Steps/01-deployment.md#complete-first-time-boot-wizard).
    When you lose **osadmin** user password, all backups encrypted by
    this password are lost.
