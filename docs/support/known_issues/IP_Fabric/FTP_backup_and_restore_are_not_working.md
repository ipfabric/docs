---
description: This page describes how to resolve issues related to FTP backup and restore.
---

# FTP Backup and Restore Are Not Working

Suppose you have the FTP root directory on the FTP server at `/ftp` and you would like to store backup in `/ftp/backup`.

In that case, you enter `backup` (relative path) while performing an FTP backup.

However, that will fail because the presence of `/backup` (absolute path) is checked instead, even though the backup should actually go to `/ftp/backup`.

So before performing the backup, please also create `/backup` on the FTP server.

The same issue will occur with restore -- please copy the contents of `/ftp/backup` to `/backup` (as the check for files to restore is done on `/backup`, but the actual restore will be done from `/ftp/backup`).

If unsure, please contact IP Fabric Support for assistance.
