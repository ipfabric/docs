---
description: This page explains how to manually back up or restore your IP Fabric data via CLI.
---

# How to Backup and Restore IP Fabric via CLI

!!! warning

    For performing a backup, there needs to be more than 50% free space on the
    `root` filesystem.

    You can check the free space with the `df -h` command in the IP Fabric VM's
    shell.

!!! important

    Backups are encrypted with the `osadmin` user password configured with [IPF
    CLI Config](../../IPF_CLI_Config/change_osadmin_pass.md). If you lose the `osadmin` user password, the backups are also
    lost!

--8<-- "snippets/username_password_regex.md"

## Backup via CLI

IP Fabric offers two options for backing up the appliance data:

- Local backup
- Remote backup (FTP, SFTP)

To configure the destination server and backup options, go to the main GUI and navigate to
**Settings --> System --> Backup & Maintenance**. For more details, see
[Schedule System Backup](../../../IP_Fabric_Settings/system/Backup_and_Maintenance/system_backup.md).

!!! Warning

    Ensure that the backup destination and credentials are correctly configured in the main GUI under
    **Settings --> System --> Backup & Maintenance**. These values cannot be adjusted using the
    CLI backup/restore script.

### Trigger a Backup Manually (On-Demand)

To initiate a manual (on-demand) backup, execute the following command in the IP Fabric CLI:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -b
```

Below is an example of a successful local backup output triggered via CLI:

!!! example

    ```shell
    root@system-backup:/# sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -b
    find: ‘/root/.cache/duplicity/’: Permission denied
    Nov 18 14:27:00 [INFO] Backup destination: local
    Nov 18 14:27:00 [INFO] Storage status: OK
    Nov 18 14:27:00 [INFO] ** Backup has started **
    Nov 18 14:27:00 [INFO] Cleaning up backup
    Nov 18 14:27:00 [INFO] Dumping up ArangoDB
    du: cannot access '/opt/ipf-nimpee-update/server/etc/config.json': No such file or directory
    Nov 18 14:27:06 [INFO] Creating backups list
    Nov 18 14:27:14 [INFO] ** Backup has finished **
    Nov 18 14:27:14 [INFO] Removing temp backup files.
    rm: cannot remove '/var/backups/database/': Permission denied
    ```

## Restore via CLI

The same script used for backups is also used for restoring backups.

!!! Warning

    Ensure that the backup destination and credentials are correctly configured in the main GUI under
    **Settings --> System --> Backup & Maintenance**. These values cannot be adjusted using the
    CLI backup/restore script.

There are three options for backup restoration:

1. **Restore data & all system services** -- This option restores the database,
   snapshots, and system files. It is useful for recovering from general system
   failures or upgrade issues.

2. **Restore database** -- Only the database is restored. This option is
   sufficient for database failures or accidental database drops.

3. **Restore snapshot files** -- A specific snapshot can be restored.

To get the list of available backups, use the commands in the following section.

### List Available Backups to Restore

#### Restore data & all system services

To list available backups for restoration, run the following command in the IP Fabric CLI:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l backup
```

!!! example "Output example"

    ```shell 
    root@system-backup:/# sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l backup
    find: ‘/root/.cache/duplicity/’: Permission denied
    Nov 18 13:54:02 [INFO] Backup destination: local
    Nov 18 13:54:02 [INFO] Storage status: OK
    Nov 18 13:54:02 [INFO] Removing temp backup files.
    rm: cannot remove '/var/backups/database/': Permission denied
    
    ## LIST ##
    backup-Full; 2024-11-18T13:49:28
    ## LIST END ##
    ```

#### Restore database

To list available databases for restoration, run the following command in the IP Fabric CLI:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l arangodb
```

!!! example "Output example"

    ```shell
    root@system-backup:/# sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l arangodb
    find: ‘/root/.cache/duplicity/’: Permission denied
    Nov 18 13:54:30 [INFO] Backup destination: local
    Nov 18 13:54:30 [INFO] Storage status: OK
    Nov 18 13:54:30 [INFO] Removing temp backup files.
    rm: cannot remove '/var/backups/database/': Permission denied
    Nov 18 13:54:31 [INFO] Local backup DB same as online list    
    
    ## LIST ##
    arangodb-zsindylek-mq-70-20241118-1349-7_0_4+0; 2024-11-18T13:49:28
    ## LIST END ##
    ```

#### Restore snapshot filesystem

To list available snapshots for restoration, run the following command in the IP Fabric CLI:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l snapshots
```

!!! example "Output example"

    ```shell
    root@system-backup:/# sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -l snapshots
    find: ‘/root/.cache/duplicity/’: Permission denied
    Nov 18 13:54:14 [INFO] Backup destination: local
    Nov 18 13:54:14 [INFO] Storage status: OK
    Nov 18 13:54:14 [INFO] Removing temp backup files.
    rm: cannot remove '/var/backups/database/': Permission denied
    Nov 18 13:54:15 [INFO] Local backup DB same as online list

    ## LIST ##
    snapshot-e71519b9-b7fc-488d-841f-67983a12f6af; 2024-11-18T13:49:28
    snapshot-e09c6b70-b232-4dd1-bec9-97ad1f96d40c; 2024-11-18T13:49:28
    snapshot-d49e9715-3eb3-4b21-b41f-1ef9b6c5bead; 2024-11-18T13:49:28
    snapshot-ab7e4ed6-e07f-47d0-8d95-a7581ec29acc; 2024-11-18T13:49:28
    snapshot-45cf7507-ab1e-42f2-a18d-0ae26d5f4e61; 2024-11-18T13:49:28
    snapshot-41844ce8-cc7a-4b60-b4a5-c59149e42d69; 2024-11-18T13:49:28
    snapshot-12dd8c61-129c-431a-b98b-4c9211571f89; 2024-11-18T13:49:28
    ## LIST END ##
    ```

### Restore a Backup

To restore a backup, you need the output from the previous section, [List Available Backups to Restore](#list-available-backups-to-restore).

!!! example "Example of a full backup list from the previous section"

    ```shell
    ## LIST ##
    backup-Full; 2024-11-18T13:49:28
    ## LIST END ##
    ```

This is the syntax for the list:

```shell
## LIST ##
<item to restore>; <date&time of the item to restore>
## LIST END ##
```

Restoration (full backups, databases, snapshots) is then done using the following command format:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -r <item to restore> -d <date&time of the item to restore>
```

Full backup restoration command example:

```shell
sudo -u autoboss /opt/nimpee/sys-backup-duplicity.sh -r backup-Full -d 2024-11-18T13:49:28
```