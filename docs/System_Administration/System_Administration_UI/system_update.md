---
description: This page explains how to update IP Fabric over the internet or using an update file.
---

# System Update

--8<-- "snippets/clear_browser_cache.md"

## Back Up System Before Update

The best practice is to save the virtual machine's state (VM snapshot) using
your hypervisor. Alternatively, you may use an IP Fabric backup. To proceed with
IP Fabric backup, follow these steps:

1. In the top-right corner of the main GUI, click **Support**.
2. Click **System Administration** to access the administrative interface (e.g.,
   `https://ipfabric-ip-address:8443`).
3. Log in with the `osadmin` user and the password configured during the first
   boot.
4. Backup the VM by following the instructions on the
   [Restore or Backup](restore_or_backup.md) page.

!!! info "Backup Disk"

    The local backup disk is not present by default! To enable local backups,
    please add a new virtual disk to your VM. (See
    [Local Backup Disk](../increase_disk_space.md/#local-backup-disk).)

## Online Update

Online updates are automatically available only when the IP Fabric appliance has
connectivity to the following servers:

- `callhome.ipfabric.io` remote port `443/tcp` for update availability check
- `releases.ipfabric.io` remote port `443/tcp` for update package download

--8<-- "snippets/allowlist_fqdn.md"

When a new IP Fabric version is available, a green indicator will appear in the
top-right corner of the main GUI. The image below shows an example of the new
version `6.8.6+0` being available:

![New version 6.8.6+0 available](system_update_new_version.png)

To proceed with an online update, follow these steps:

1. Click the new version indicator. It will navigate you to the **System
   Administration** UI.
2. Log in with the `osadmin` user and the password configured during the first
   boot.
3. Perform the VM backup as described in the section above.
4. Navigate to **System update** and proceed. IP Fabric will automatically
   download the update file, perform the update, and reboot itself.

## Offline Update

If your IP Fabric does not have direct internet connectivity, you may use
offline update:

1. Download the latest update file from
   [https://releases.ipfabric.io/ipfabric/updates/](https://releases.ipfabric.io/ipfabric/updates/).
2. In the top-right corner of the main GUI, click **Support**.
3. Click **System Administration** to access the administrative interface (e.g.,
   `https://ipfabric-ip-address:8443`).
4. Log in with the `osadmin` user and the password configured during the first
   boot.
5. Perform the VM backup as described in the section above.
6. Navigate to **System update**.
7. Select or drag-and-drop the downloaded update file.

![IP Fabric system update in progress](system_update.png)

After a successful package upload, the update process will start automatically,
and the IP Fabric VM will reboot once completed. Afterwards, it is recommended
to create a new discovery snapshot on the latest version.
