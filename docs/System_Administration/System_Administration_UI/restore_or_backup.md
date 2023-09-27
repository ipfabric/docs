---
description: On this page, we will explain how to manually backup or restore IP Fabric data in the System Administration interface.
---

# Restore or Backup

!!! warning

    For performing a backup, there needs to be > 50 % free space on the `root`
    filesystem.
    
    You can check the free space with the `df -h` command in the IP Fabric VM's
    shell.

!!! important

    Backups are encrypted with the `osadmin` user password configured during the
    **First Boot Wizard**. When you lose the `osadmin` user password, backups
    are also lost!

--8<-- "snippets/username_password_regex.md"

## Backup

IP Fabric allows you to backup data it collects with two options:

- local backup
- remote backup (FTP, SFTP)

### Local Backup

Local backup saves database, user and system files locally on a dedicated backup
volume. It's highly recommended placing the backup volume on a different
datastore, ideally on a separate physical storage.

!!! info "Backup Disk"

    The backup disk is not present by default! Please add a new virtual disk to
    enable local backups.

To add a new backup drive, follow the instructions in
[Local Backup Disk](../../System_Administration/increase_disk_space.md#local-backup-disk).

### Trigger a Backup Manually (On-Demand)

Both types of backup can be triggered manually. This is useful for example
before a system update. (For automatic backups, see
[Schedule System Backup](../../IP_Fabric_Settings/system/Backup_and_Maintenance/system_backup.md).)

!!! warning

    For FTP and SFTP backups, a directory **has to be specified** . It **has to
    exist** on the remote side. If it does not, you will get an error.

    For **FTP**, the directory path has to be specified as a **relative path**.
    
    For **SFTP**, the directory path has to be specified as an **absolute
    path**.

To proceed with manual backup, follow these steps:

1. Log in to the **System Administration** interface (for example
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Backup` from the **Do you wish to proceed with a backup or restore?**
   drop-down menu.

4. For local backup, select `Local hard drive` from the **Backup files
   destination** drop-down menu.

5. For remote backup, select `FTP` or `SFTP` from the **Backup files
   destination** drop-down menu.

   1. Enter the remote FTP/SFTP **Server** FQDN or IP address. Make sure that
      your DNS client is configured and working properly in case of FQDN.

   2. Enter **Username** and **Password** for accessing the FTP/SFTP server.

   3. Specify the **Directory** where FTP/SFTP backup should be uploaded.

6. Click **Next**.

--8<-- "snippets/username_password_regex.md"

### Full vs Incremental Backups

The first backup is a full backup. Additional backups are incremental backups.
Incremental backup 1 depends on the full backup, incremental backup 2 depends on
incremental backup 1 and the full backup etc.

By default, a new full backup is created after 14 days since the previous full
backup. You may change this behavior by changing `--full-if-older-than 14D` in
the following line in `/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for
example with `sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
STATIC_OPTIONS="--full-if-older-than 14D --allow-source-mismatch --ssl-no-check-certificate"
```

- possible time values: `s` (seconds), `m` (minutes), `h` (hours), `D` (days),
  `W` (weeks), `M` (months), `Y` (years)

By default, only 2 full backups are kept in the backup directory. You may change
this behavior by amending the value in the following line in
`/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for example with
`sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
CLEAN_UP_VARIABLE="2"
```

!!! tip

    Due to
    [Restore is not working when 2 full backups are present](../../support/known_issues/IP_Fabric/restore_not_working_with_2_full_backups.md),
    you may consider setting `CLEAN_UP_VARIABLE="1"` (i.e. keeping only 1 full
    backup and its increments).

    Please note that this has a downside -- when a new full backup is created,
    all previous backup files will be removed from the backup directory.

If unsure, please contact IP Fabric Support for assistance.

!!! example "Examples"

    First full backup's files (depending on the backup's size, you may have
    `vol1`, `vol2` ... `volX` instead of just `vol1`):

    ```shell
    -rw-r--r-- 1 root root  54M Sep 27 11:14 ipfabric-94c370c9-duplicity-full.20230927T111440Z.vol1.difftar.gpg
    -rw-r--r-- 1 root root 3.3M Sep 27 11:14 ipfabric-94c370c9-duplicity-full-signatures.20230927T111440Z.sigtar.gpg
    -rw-r--r-- 1 root root  62K Sep 27 11:14 ipfabric-94c370c9-duplicity-full.20230927T111440Z.manifest.gpg
    ```

    First incremental backup's files (they refer to/depend on the full backup):

    ```shell
    -rw-r--r-- 1 root root  28M Sep 27 11:17 ipfabric-94c370c9-duplicity-inc.20230927T111440Z.to.20230927T111735Z.vol1.difftar.gpg
    -rw-r--r-- 1 root root 1.6M Sep 27 11:17 ipfabric-94c370c9-duplicity-new-signatures.20230927T111440Z.to.20230927T111735Z.sigtar.gpg
    -rw-r--r-- 1 root root  11K Sep 27 11:17 ipfabric-94c370c9-duplicity-inc.20230927T111440Z.to.20230927T111735Z.manifest.gpg
    ```

    Second incremental backup's files (they refer to/depend on the first
    incremental backup and also depend on the full backup):

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

    Restore is supported only to the same version of IP Fabric as the backup was
    prepared on. This is checked automatically during restore.

    The only exception are snapshots which can be restored to any version of
    the IP Fabric appliance.

### Restore From Local Hard Drive

1. Log in to the **System Administration** interface (for example
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Restore` from the **Do you wish proceed a backup or restore?**
   drop-down menu.

4. Select **What restore?**. There are three options:

  1. `Restore data & all system services` - This option restores database and
     system files. It is usable for restoring from general system failures or
     upgrade failures.

  2. `Restore database` - It means that only database data are restored. It
     can be sufficient in case of a database failure or accidental database
     drop.

  3. `Restore snapshot files` - A particular snapshot can be restored.

5. Choose `Local hard drive` from the **Backup files source** drop-down menu.

6. Click **Next**.

7. **Select backup file** - There is year, month, day, and time when a backup
   file was created in a backup filename.

8. Click **Restore**.

### Restore From Remote Server

1. Log in to the **System Administration** interface (for example
   `https://ipfabric.example.com:8443`).

2. Go to **Restore or Backup**.

3. Select `Restore` from the **Do you wish proceed a backup or restore?** drop
   down menu.

4. Select **What restore?**. There are three options:

  1. `Restore data & all system services` - This option restores database and
     system files. It is usable for restoring from general system failures or
     upgrade failures.

  2. `Restore database` - It means that only database data are restored. It
     can be sufficient in case of a database failure or accidental database
     drop.

  3. `Restore snapshot files` - A particular snapshot can be restored.

5.  Choose `FTP` or `SFTP` from the **Backup files source** drop-down menu.

   1. Enter the remote FTP/SFTP **Server** FQDN or IP address. Make sure that
      your DNS client is configured and working properly in case of FQDN.

   2. Enter **Username** and **Password** for accessing the FTP/SFTP server.

   3. Specify the **Directory** where backups are located.

6. Click **Next**.

7. **Select backup file** - There is year, month, day, and time when a backup
   file was created in a backup filename.

8. Click **Restore**.
