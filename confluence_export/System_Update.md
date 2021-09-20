# System Update

<div>

<div>

**Clearing Cache Memory**  
Please force refresh your browser cache after an upgrade!

Depending on your operating system all you need to do is the following
key combination:

Windows: ctrl + F5  
Mac/Apple: Apple + R or command + R  
Linux: F5

</div>

</div>

## Access Administrative interface and backup the system

Access administrative interface by clicking "**Support**" button at the
top right of the main user interface and then clicking "**System
Administration**". You can also access administrative interface directly
by connecting to HTTPS port 8443 of the IP Fabric VM, e.g.
<https://ipfabric.company.com:8443>

Use the user **osadmin** with password configured during the first boot
wizard.

On [Restore and Backup](Backup_and_restore) page perform system backup.

<div>

<div>

**Backup Disk**  
Local backup disk is not present by default! Please add a new virtual
disk to your VM to enable local backups. (See Restore and Backup page)

</div>

</div>

## Online upgrade

At the **System update** page of the administrative interface, click the
**Update** button. (In releases earlier than 2.2.6 additional release
credentials are required).

<div>

<div>

**Network requirements**  
An online upgrade requires access to:

-   [*callhome.ipfabric.io*](https://callhome.ipfabric.io) (194.228.111.170)
    remote port 443/TCP for upgrade availability check

-   [*releases.ipfabric.io*](https://releases.ipfabric.io) (194.228.111.172)
    remote port 443/TCP for upgrade package download

</div>

</div>

In the following screenshot, the green 3.7.5 button in the right top
corner indicates that a new version of Ip Fabric is available (if the
system has Internet connectivity).

<img src="attachments/79069223/1906245681.png" class="image-center" loading="lazy" data-image-src="attachments/79069223/1906245681.png" data-height="380" data-width="1161" data-unresolved-comment-count="0" data-linked-resource-id="1906245681" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210122-115335.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79069223" data-linked-resource-container-version="22" data-media-id="ecaf8b7c-d676-4bff-8550-9e546b2f7dc6" data-media-type="file" alt="Green 3.7.5 button on the right top indicates that new version is available." />

## Offline upgrade

Download the latest upgrade package from the updates folder on the
distribution page <https://releases.ipfabric.io/ipfabric/#updates>

<div>

<div>

When performing offline upgrade IP FABRIC v2.2.2 or lower, load the
patch for large offline updates first using
<https://releases.ipfabric.io/nimpee/updates/nimpee-offline-update-fix.tar.gz.sig>

</div>

</div>

Go to **Support \> System Administration** (use 'osadmin' user to
access). At the **System update** page of the administrative interface,
upload the package. The following screenshot depicts the actual upgrade
process in the System Administration.

<img src="attachments/79069223/1907589121.png" class="image-center" loading="lazy" data-image-src="attachments/79069223/1907589121.png" data-height="432" data-width="1267" data-unresolved-comment-count="0" data-linked-resource-id="1907589121" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210122-115013.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79069223" data-linked-resource-container-version="22" data-media-id="cb313681-e18d-446f-992a-96577e2c5b32" data-media-type="file" alt="Performing upgrade in System Administration" />

The upgrade will start automatically after a successful package upload,
after which the IP Fabric VM will reboot. Once the IP Fabric VM is
rebooted, please run a new discovery so all of the new calculations can
take place.

Make sure to refresh the browser cache using CTRL+F5 when accessing IP
Fabric VM user interface after an upgrade.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210122-115013.png](attachments/79069223/1907589121.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210122-115335.png](attachments/79069223/1906245681.png)
(image/png)  

</div>
