---
description: If the FTP backup is not working, this is how to get it back up again.
---

# FTP backup and restore are not working

Suppose you have the FTP root directory on the FTP server in `/ftp` and you would like to store backup in `/ftp/backup`.

In that case you enter `backup` (relative path) while performing FTP backup.

However, that will fail as the presence of `/backup` (absolute path) is checked instead -- even if the backup should actually go to `/ftp/backup`.

So please also create `/backup` on the FTP server before performing the backup.

The same issue will occur with restore -- please copy the content of `/ftp/backup` to `/backup` (as the check for files to restore is done on `/backup`, but the actual restore will be done from `/ftp/backup`).

If unsure, please contact IP Fabric Support for assistance.
