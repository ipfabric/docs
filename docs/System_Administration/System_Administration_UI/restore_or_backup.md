---
description: This page explains how to manually back up or restore your IP Fabric data in the System Administration UI.
---

# Restore or Backup

!!! warning

    For performing a backup, there needs to be more than 50% free space on the
    `root` filesystem.
    
    You can check the free space with the `df -h` command in the IP Fabric VM's
    shell.

!!! important

    Backups are encrypted with the `osadmin` user password configured during the
    **First Boot Wizard**. If you lose the `osadmin` user password, the backups
    are also lost!

--8<-- "snippets/username_password_regex.md"

## Backup

IP Fabric allows you to back up data it collects with two options:

- local backup
- remote backup (FTP, SFTP)

### Local Backup

Local backup saves the database and user and system files locally on a dedicated
backup volume. It's highly recommended to place the backup volume on a different
datastore, ideally on separate physical storage.

!!! info "Backup Disk"

    The backup disk is not present by default! To enable local backups, please
    add a new virtual disk.

To add a new backup disk, follow the instructions in
[Local Backup Disk](../../System_Administration/increase_disk_space.md#local-backup-disk).

### Trigger a Backup Manually (On-Demand)

Both types of backups can be triggered manually. This is useful, for example,
before a system update. (For automatic backups, see
[Schedule System Backup](../../IP_Fabric_Settings/system/Backup_and_Maintenance/system_backup.md).)

!!! warning

    For FTP and SFTP backups, a directory **must be specified**. It **must
    exist** on the remote side. If it does not, you will get an error.

    For **FTP**, the directory path must be specified as a **relative path**.
    
    For **SFTP**, the directory path must be specified as an **absolute path**.

To proceed with a manual backup, follow these steps:

1. Log in to the **System Administration** UI (for example,
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Backup` from the **Do you wish to proceed with a backup or restore?**
   drop-down menu.

4. For local backup, select `Local hard drive` from the **Backup files
   destination** drop-down menu.

5. For remote backup, select `FTP` or `SFTP` from the **Backup files
   destination** drop-down menu.

   1. Enter the remote FTP/SFTP **Server** FQDN or IP address. If using an FQDN,
      make sure that your DNS client is configured and working properly.

   2. Enter the **Username** and **Password** for accessing the FTP/SFTP server.

   3. Specify the **Directory** where FTP/SFTP backup should be uploaded.

6. Click **Next**.

### Full vs Incremental Backups

The first backup is a full backup. Additional backups are incremental backups.
Incremental backup 1 depends on the full backup, incremental backup 2 depends on
incremental backup 1 and the full backup, and so forth.

By default, a new full backup is created 14 days after the previous full
backup. You may change this behavior by adjusting `--full-if-older-than 14D` in
the following line in `/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for
example, with `sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
STATIC_OPTIONS="--full-if-older-than 14D --allow-source-mismatch --ssl-no-check-certificate"
```

- Possible time values include : `s` (seconds), `m` (minutes), `h` (hours), `D`
  (days), `W` (weeks), `M` (months), and `Y` (years).

By default, only two full backups are retained in the backup directory. You may
modify this behavior by amending the value in the following line in
`/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for example, with
`sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
CLEAN_UP_VARIABLE="2"
```

!!! tip

    As
    [restore does not function properly when two full backups are present](../../support/known_issues/IP_Fabric/restore_not_working_with_2_full_backups.md),
    you may want to set `CLEAN_UP_VARIABLE="1"` (i.e., retaining only one full
    backup and its increments).

    Please note that this approach has a downside -- when a new full backup is
    created, all previous backup files will be removed from the backup
    directory.

If you are unsure, please contact IP Fabric Support for assistance.

!!! example "Examples"

    The first full backup's files (depending on its size, you may have `vol1`,
    `vol2`, ..., `volX` instead of just `vol1`):

    ```shell
    -rw-r--r-- 1 root root  54M Sep 27 11:14 ipfabric-94c370c9-duplicity-full.20230927T111440Z.vol1.difftar.gpg
    -rw-r--r-- 1 root root 3.3M Sep 27 11:14 ipfabric-94c370c9-duplicity-full-signatures.20230927T111440Z.sigtar.gpg
    -rw-r--r-- 1 root root  62K Sep 27 11:14 ipfabric-94c370c9-duplicity-full.20230927T111440Z.manifest.gpg
    ```

    Incremental backup 1's files (referring to / dependent on the full backup):

    ```shell
    -rw-r--r-- 1 root root  28M Sep 27 11:17 ipfabric-94c370c9-duplicity-inc.20230927T111440Z.to.20230927T111735Z.vol1.difftar.gpg
    -rw-r--r-- 1 root root 1.6M Sep 27 11:17 ipfabric-94c370c9-duplicity-new-signatures.20230927T111440Z.to.20230927T111735Z.sigtar.gpg
    -rw-r--r-- 1 root root  11K Sep 27 11:17 ipfabric-94c370c9-duplicity-inc.20230927T111440Z.to.20230927T111735Z.manifest.gpg
    ```

    Incremental backup 2's files (referring to / dependent on incremental backup
    1 and also dependent on the full backup):

    ```shell
    -rw-r--r-- 1 root root  28M Sep 27 11:20 ipfabric-94c370c9-duplicity-inc.20230927T111735Z.to.20230927T112005Z.vol1.difftar.gpg
    -rw-r--r-- 1 root root 1.6M Sep 27 11:20 ipfabric-94c370c9-duplicity-new-signatures.20230927T111735Z.to.20230927T112005Z.sigtar.gpg
    -rw-r--r-- 1 root root  11K Sep 27 11:20 ipfabric-94c370c9-duplicity-inc.20230927T111735Z.to.20230927T112005Z.manifest.gpg
    ```

    The recommended command for sorting all backup files from oldest to newest:

    ```shell
    ls -lahtr <path_to_backup_directory>
    ```

## Restore

In case of a database or system corruption, IP Fabric can be restored from a
backup.

!!! info

    Restore is supported only for the same version of IP Fabric as the backup
    was prepared on. This is checked automatically during restore.

    The only exception is snapshots, which can be restored to any version of the
    IP Fabric appliance.

### Restore From Local Hard Drive

1. Log in to the **System Administration** UI (for example,
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Restore` from the **Do you wish proceed a backup or restore?**
   drop-down menu.

4. Select **What restore?**. There are three options:

  1. `Restore data & all system services` -- This option restores the database
     and user and system files. It is usable for restoring from general system
     failures or upgrade failures.

  2. `Restore database` -- Only the database is restored. This can be sufficient
     in case of a database failure or accidental database drop.

  3. `Restore snapshot files` -- A particular snapshot can be restored.

5. Select `Local hard drive` from the **Backup files source** drop-down menu.

6. Click **Next**.

7. **Select backup file** -- The backup filename includes the year, month, day,
   and time when the backup file was created.

8. Click **Restore**.

### Restore From Remote Server

1. Log in to the **System Administration** UI (for example,
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Restore` from the **Do you wish proceed a backup or restore?**
   drop-down menu.

4. Select **What restore?**. There are three options:

  1. `Restore data & all system services` -- This option restores the database
     and user and system files. It is usable for restoring from general system
     failures or upgrade failures.

  2. `Restore database` -- Only the database is restored. This can be sufficient
     in case of a database failure or accidental database drop.

  3. `Restore snapshot files` -- A particular snapshot can be restored.

5. Select `FTP` or `SFTP` from the **Backup files source** drop-down menu.

   1. Enter the remote FTP/SFTP **Server** FQDN or IP address. If using an FQDN,
      make sure that your DNS client is configured and working properly.

   2. Enter the **Username** and **Password** for accessing the FTP/SFTP server.

   3. Specify the **Directory** where backups are located.

6. Click **Next**.

7. **Select backup file** -- The backup filename includes the year, month, day,
   and time when the backup file was created.

8. Click **Restore**.
