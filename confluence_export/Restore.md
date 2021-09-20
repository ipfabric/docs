# Restore

# Restore

In case of database or system corruption, IP Fabric can be restored from
a backup.

<div>

<div>

Restore is supported only to the same version of IP Fabric as the source
of a backup. This is checked automatically during restore.  
The only exceptions are snapshots which can be restored to any version
of IP Fabric appliance.

</div>

</div>

## Restore from local hard drive

1.  Login to admin interface (for
    example [https://ipfabric.example.com:8443)](https://ipfabric.example.com:8443))

2.  Go to ***Restore or Backup***

3.  Select ***Restore** *from ***Do you wish proceed a backup or
    restore?*** drop-down menu.

4.  Select ***What restore?***. There are four options:

    1.  ***Restore data & all system services*** - This option restores
        database and system files. It's usable for restore from general
        system failures or upgrade failures.

    2.  ***Restore database*** - it means that only database data are
        restored. It can be sufficient in case of a database failure or
        accidental database drop.

    3.  ***Restore syslog data*** - it means that only syslog data are
        restored. It can be sufficient in case of a database failure or
        accidental database drop.

    4.  ***Restore snapshot file*** - particular snapshot can be
        restored.

5.  For restore from local backup choose ***Local hard drive*** from
    ***Backup files source***.

6.  Click ***Next***.

7.  ***Select backup file*** - there is a year, month, day and time when
    a backup file was created in a backup filename.

8.  Enter IP Fabric user password to ***Specify decryption password
    (same as IP Fabric user)***.

9.  Click ***Restore***.

<div>

<div>

Backups are encrypted with ***osadmin ***user password configured
during [first boot
wizard](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78872592/Deploy+NIMPEE+VM).
When you loose ***osadmin** *user password, backups are also lost.

</div>

</div>

## Restore from a remote server

1.  Login to admin interface (for
    example [https://ipfabric.example.com:8443)](https://ipfabric.example.com:8443))

2.  Go to ***Restore or Backup***

3.  Select ***Restore** *from ***Do you wish proceed a backup or
    restore?*** drop down menu.

4.  Select ***What restore?***. There are four options:

    1.  ***Restore data & all system services*** - This option restores
        database and system files. It's usable for restore from general
        system failures or upgrade failures.

    2.  ***Restore database*** - it means that only database data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    3.  ***Restore syslog data*** - it means that only syslog data are
        restored. It can be sufficient in case of database failure or
        accidental database drop.

    4.  ***Restore snapshot file*** - particular snapshot can be
        restored.

5.  For restore from local backup choose ***FTP*** or ***SFTP*** from
    ***Backup files source***.

6.  Specify ***Server*** FQDN or IP address. Make sure that your DNS
    client is configured and working properly in case of FQDN.

7.  Enter ***Username***** **to access FTP/SFTP server.

8.  Enter ***Password***** **to access FTP/SFTP server.

9.  If you would like to use different ***Directory***** **than
    FTP/SFTP root please specify.

10. Click ***Next***.

11. ***Select backup file*** - there is year, month, day and time when a
    backup file was created in a backup filename.

12. Enter IP Fabric user password to ***Specify decryption password
    (same as IP Fabric user)***.

13. Click ***Restore***.

<div>

<div>

Backups are encrypted with ***osadmin ***user password configured
during [first boot
wizard](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78872592/Deploy+NIMPEE+VM).
When you loose ***osadmin** *user password, backups are also lost.

</div>

</div>
