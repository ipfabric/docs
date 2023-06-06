---
description: If two full backups are present in the backup directory, this article should help you get the backup restore working again.
---

# Restore is not working when 2 full backups are present

When two full backups exist in the backup directory:

```shell
root@ipfabric:/backup/ipfabric# ls -latr
total 206316
drwxr-xr-x 5 root root     4096 Apr 17 08:37 ..
-rw-r--r-- 1 root root 98627303 Apr 18 09:03 ipfabric-94c370c9-duplicity-full.20230418T090304Z.vol1.difftar.gpg
-rw-r--r-- 1 root root  6955417 Apr 18 09:03 ipfabric-94c370c9-duplicity-full-signatures.20230418T090304Z.sigtar.gpg
-rw-r--r-- 1 root root    40632 Apr 18 09:03 ipfabric-94c370c9-duplicity-full.20230418T090304Z.manifest.gpg
-rw-r--r-- 1 root root 98629256 Apr 18 09:06 ipfabric-94c370c9-duplicity-full.20230418T090633Z.vol1.difftar.gpg
-rw-r--r-- 1 root root  6955421 Apr 18 09:06 ipfabric-94c370c9-duplicity-full-signatures.20230418T090633Z.sigtar.gpg
-rw-r--r-- 1 root root    40631 Apr 18 09:06 ipfabric-94c370c9-duplicity-full.20230418T090633Z.manifest.gpg
drwxr-xr-x 2 root root     4096 Apr 18 09:06 .
```

restoring will fail with an error message: `No backups files exists for given source`.

To restore the newer full backup (in this example, `20230418T090633Z`), it is necessary to delete or move the files of the older full backup (`20230418T090304Z`).

Before restoring the backup, please ensure that the backup directory contains only files of one full backup and its related incremental backups. You can sort the files from oldest to newest with this command:

```
ls -latr <path_to_backup_directory>
```

By default, two full backups are kept in the backup directory. A possible hot fix is to keep only one full backup (and its incremental backups) by changing the following line in `/opt/nimpee/conf.d/backup/duplicity-backup.conf` script (as a root):

```
CLEAN_UP_VARIABLE="2"
```

to

```
CLEAN_UP_VARIABLE="1"
```
