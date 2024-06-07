---
description: This section describes how to schedule a local or remote backup to protect your IP Fabric data.
---

# Schedule System Backup

!!! warning

    For performing a backup, there needs to be more than 50% free space on the
    `root` filesystem.
    
    You can check the free space with the `df -h` command in the IP Fabric VM's
    shell.

Use backup to protect your IP Fabric data.

There are two types of backup:

- local backup
- remote backup (FTP, SFTP)

!!! important

    Backups are encrypted with the `osadmin` user password configured during the
    **First Boot Wizard**. If you lose the `osadmin` user password, backups are
    also lost!

## Automatic Local Backups

Local backup saves the database and user and system files locally on a dedicated
backup volume. It's highly recommended to place the backup volume on a different
datastore, ideally on separate physical storage.

!!! info "Backup Disk"

    The backup disk is not present by default! To enable local backups, please
    add a new virtual disk.

To add a new backup disk, follow the instructions in
[Increase Disk Space - Local Backup Disk](../../../System_Administration/increase_disk_space.md#local-backup-disk).

To schedule automatic local backups, follow these steps:

1. If not done yet, add a dedicated backup volume.
2. Log in to the IP Fabric main GUI.
3. Go to **Settings --> System --> Backup & Maintenance --> Schedule system
   backup**.
4. Enable backup.
5. Set a backup schedule. See the example for `Every day at 13:25`.
6. Change the **Destination** to `Local hard drive`.
7. Click **Save**.

![Schedule local backup](system_backup/schedule_local_backup.png)

## Automatic Remote Backups

Remote backup saves the database and user and system files remotely using the
FTP or SFTP protocol.

!!! note

    This is the recommended type of backup.

!!! warning

    For FTP and SFTP backups, a directory **must be specified**. It **must
    exist** on the remote side. If it does not, you will get an error.

    For **FTP**, the directory path must be specified as a **relative path**.
    
    For **SFTP**, the directory path must be specified as an **absolute path**.

To set up remote backup, follow these steps:

1. Log in to the IP Fabric main GUI.
2. Go to **Settings --> System --> Backup & Maintenance --> Schedule system
   backup**.
3. Enable backup.
4. Set a backup schedule. See the example for `Every day at 5:15 and 17:15` (to
   select multiple values, hold `Ctrl` or `Shift` during the selection).
   ![Backup schedule](system_backup/backup_schedule.png)
5. Change the **Destination** to `FTP` or `SFTP`.
6. Enter the remote FTP/SFTP **Server** FQDN or IP address. Make sure that your
   DNS client is configured and working properly in case of FQDN.
7. Enter **Username** and **Password** for accessing the FTP/SFTP server.
9. Specify the **Directory** to which FTP/SFTP backup should be uploaded.
10. Click **Save**.
11. IP Fabric will try to reach the FTP/SFTP server with the configured
    parameters.

--8<-- "snippets/username_password_regex.md"

!!! warning

    The FTP/SFTP user needs the `read`, `write`, `list`, and `delete`
    permissions.

!!! note

    Since version `4.1.1`, we do not check the validity of SSL certificates
    during FTP backups.

## Full vs Incremental Backups

The first backup is a full backup, while subsequent backups are incremental.
Incremental backup 1 depends on the full backup, incremental backup 2 depends on
incremental backup 1 and the full backup, and so forth.

By default, a new full backup is created 14 days after the previous full backup.
You can modify this behavior by adjusting `--full-if-older-than 14D` in
the following line in `/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for
example, using `sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
STATIC_OPTIONS="--full-if-older-than 14D --allow-source-mismatch --ssl-no-check-certificate"
```

- Possible time values include: `s` (seconds), `m` (minutes), `h` (hours), `D`
  (days), `W` (weeks), `M` (months), and `Y` (years).

By default, only two full backups are retained in the backup directory. You can
alter this behavior by adjusting the value in the following line in
`/opt/nimpee/conf.d/backup/duplicity-backup.conf` (for example, using
`sudo vi /opt/nimpee/conf.d/backup/duplicity-backup.conf`):

```
CLEAN_UP_VARIABLE="2"
```

!!! tip

    As
    [restore does not function properly when two full backups are present](../../../support/known_issues/IP_Fabric/restore_not_working_with_2_full_backups.md),
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
