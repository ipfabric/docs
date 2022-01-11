# 09 - Schedule System Backup

## Schedule System Backup

<img src="attachments/2396585999/2396454941.png" class="image-center" loading="lazy" data-image-src="attachments/2396585999/2396454941.png" data-height="385" data-width="646" data-unresolved-comment-count="0" data-linked-resource-id="2396454941" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210514-105813.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2396585999" data-linked-resource-container-version="1" data-media-id="3793c36d-e611-49b4-834f-83192f85038b" data-media-type="file" />

# Backup

Use IP Fabric backup to protect your important data.

There are two types of backup:

-   Local backup

-   Remote backup (FTP, sFTP)

<div>

<div>

**Security tip**  
Backups are encrypted with *osadmin *user password configured during
the [first boot
wizard](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78872592).
When you lose *osadmin *user password, backups are also lost!

</div>

</div>

## Local backup

Local backup saves database, user and system files locally on a
dedicated backup volume. It's highly recommended placing backup volume
on different datastore ideally on different physical storage.

<div>

<div>

**Backup Disk**  
The backup disk is not present by default! Please add a new virtual disk
to enable local backups. (See steps below)

</div>

</div>

### Adding a new virtual disk to your IP Fabric VM as a local backup disk

1.  Open your VM platform.

2.  Go to IP Fabric VM settings and add *New* *Hard Disk*

3.  Select size of a new disk

4.  Specify the type of a new disk (for the backup volume it is
    recommended to select a virtual disk on a different datastore
    ideally on different physical storage)  

    <img src="attachments/82116646/1843363848.png?width=136" class="image-left" loading="lazy" data-image-src="attachments/82116646/1843363848.png" data-height="732" data-width="748" data-unresolved-comment-count="0" data-linked-resource-id="1843363848" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (1).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="82116646" data-linked-resource-container-version="25" data-media-id="6d1f2479-499c-4104-8abc-3c3d90be12eb" data-media-type="file" width="136" />

5.  Finish configuration wizard.

6.  Launch Remote (Web) Console.

7.  [Reboot](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79036518/Service+Interfaces) (*Send
    Ctrl+Alt+Delete *function can be also used) or power on IP Fabric
    VM.

8.  During system boot, a *Disk space expansion* wizard appears.  

    <img src="attachments/82116646/1842708519.png?width=136" class="image-left" loading="lazy" data-image-src="attachments/82116646/1842708519.png" data-height="942" data-width="1274" data-unresolved-comment-count="0" data-linked-resource-id="1842708519" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (2).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="82116646" data-linked-resource-container-version="25" data-media-id="0d1e49a9-4c61-4dc5-8e9a-9f61b5f2b392" data-media-type="file" width="136" />

9.  Select *Yes* to start disk space expansion.

10. Expand the new volume as a backup (Backup is used only for local
    backups).

11. Selected volume is extended.  

    <img src="attachments/82116646/1842642960.png?width=136" class="image-left" loading="lazy" data-image-src="attachments/82116646/1842642960.png" data-height="940" data-width="1267" data-unresolved-comment-count="0" data-linked-resource-id="1842642960" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (3).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="82116646" data-linked-resource-container-version="25" data-media-id="3eb203cc-6af3-4d0d-a1cd-0e55b038c49f" data-media-type="file" width="136" />

12. Enter *OK*

## Automatic Local Backups

To schedule automatic local backups do the following steps:

1.  Add dedicated backup volume if not available - see steps above.

2.  Login to the user interface.

3.  Go to ***Settings → Advanced → System → Schedule system backup**.*

4.  Change ***Destination*** to ***Local hard drive***.

5.  Set a backup schedule. See example for "Every day at 3:00".

6.  Enable backup

<img src="attachments/82116646/639172612.png?width=170" class="image-left" loading="lazy" data-image-src="attachments/82116646/639172612.png" data-height="254" data-width="598" data-unresolved-comment-count="0" data-linked-resource-id="639172612" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-14 14_56_37-System settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="82116646" data-linked-resource-container-version="25" data-media-id="5a683fa5-58d5-4068-a2a1-ba5b4cf14f86" data-media-type="file" width="170" />

## Remote backup

Remote backup saves database, user and system files remotely using FTP
or sFTP protocol.

<div>

<div>

This is a recommended type of backup.

</div>

</div>

<div>

<div>

A directory **has to be specified** for FTP and SFTP backups

</div>

</div>

To set up remote backup do the following steps:

1.  Login to the user interface.

2.  Go to ***Settings → Advanced → System → Schedule system backup**.*

3.  Enable backup

4.  Change ***Destination*** to ***FTP*** or ***SFTP**.*

5.  Set a backup schedule. See example for "Every day at 5:15 and 17:15
    (for setting more options, please, hold SHIFT during selection)".  
    <img src="attachments/82116646/82051139.png" loading="lazy" data-image-src="attachments/82116646/82051139.png" data-unresolved-comment-count="0" data-linked-resource-id="82051139" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2018-7-24_17-10-18.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="82116646" data-linked-resource-container-version="25" data-media-id="e5f4d1a7-db4e-42f5-8c42-1a9b6da93102" data-media-type="file" />

6.  Change ***Destination*** to ***FTP*** or ***SFTP**.*

7.  Enter remote FTP/SFTP ***Server*** FQDN or IP address. Make sure
    that your DNS client is configured and working properly in case of
    FQDN.

8.  Enter ***Username*** to access FTP/SFTP server.

9.  Enter ***Password*** to access FTP/SFTP server.

10. Specify a ***Directory*** where FTP/SFTP backup should be uploaded.

11. Click ***Save ***(The IP Fabric platform will immediately test the
    connection)

12. IP Fabric tries to reach FTP/SFTP server with configured parameters.

<div>

<div>

FTP/SFTP user needs read, write, list and delete permissions.

</div>

</div>

<div>

<div>

From version 4.1.1 onward we do not check validity of SSL certificates
during FTP backups.

</div>

</div>

## Trigger a backup manually (on-demand)

Both types of backup can be also triggered manually on demand. This is
useful for example before a system upgrade.

Manual backup can be triggered from IP Fabric Administrative interface:

1.  Login to admin interface (for
    example [https://ipfabric.example.com:8443)](https://nimpee.example.com:8443))

2.  Go to ***Restore or Backup***

3.  Select ***Backup*** from ***Do you wish to proceed with a backup or
    restore?*** drop-down menu.

4.  For local backup select ***Local hard drive*** from the ***Backup
    files destination***.

5.  For remote backup select ***FTP*** or ***SFTP ***from the ***Backup
    files destination***.

    1.  Enter remote FTP/SFTP ***Server*** FQDN or IP address. Make sure
        that your DNS client is configured and working properly in the
        case of FQDN.

    2.  Enter ***Username*** to access FTP/SFTP server.

    3.  Enter ***Password*** to access FTP/SFTP server.

    4.  Specify a **Directory** where FTP/SFTP backup should be
        uploaded.

6.  Click ***Next***

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210514-105651.png](attachments/2396585999/2396454934.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210514-105813.png](attachments/2396585999/2396454941.png)
(image/png)  

</div>
