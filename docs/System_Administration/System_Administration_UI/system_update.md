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
2. Click **System Administration** to access the interface on port `8443` (e.g.,
   `https://ipfabric-ip-or-fqdn:8443`).
3. Log in with the `osadmin` user and the password configured during the first
   boot.
4. Backup the VM by following the instructions on the
   [Restore or Backup](restore_or_backup.md) page.

!!! info "Backup Disk"

    The local backup disk is not present by default! To enable local backups,
    please add a new virtual disk to your VM. (See
    [Local Backup Disk](../increase_disk_space.md/#local-backup-disk).)

## Update

The system update functionality has been moved to a separate service, accessible
at `https://ipfabric-ip-or-fqdn/ipf-system-upgrade/`.

![IP Fabric System Upgrade](ipf-system-upgrade.jpg)

### Online Update

Online updates are automatically available only when the IP Fabric appliance has
connectivity to the following servers:

- `callhome.ipfabric.io` remote port `443/tcp` for update availability check
- `releases.ipfabric.io` remote port `443/tcp` for update package download

--8<-- "snippets/allowlist_fqdn.md"

When a new IP Fabric version is available, a green indicator will appear in the
top-right corner of the main GUI.

To proceed with an online update, follow these steps:

1. Go to `https://ipfabric-ip-address/ipf-system-upgrade/` and log in with the
   `osadmin` user and the password configured during the first
   boot.
2. In the **Upgrade remotely** section, select the IP Fabric version to which you
   want to upgrade your instance.
3. IP Fabric will automatically download the update file, perform the update,
   and reboot itself.
4. It is recommended to create a new discovery snapshot on the latest version
   afterwards.

--8<-- "snippets/no_proxy_localhost.md"

### Offline Update

If your IP Fabric instance does not have direct internet connectivity, you may
use offline update:

1. Download the latest update file from
   <https://releases.ipfabric.io/updates/>.
2. Go to `https://ipfabric-ip-address/ipf-system-upgrade/` and log in with the
   `osadmin` user and the password configured during the first
   boot.
3. In the **Upload upgrade package** section, choose the update file from your
   computer.
4. After a successful upload, the update process will start automatically, and the
   IP Fabric VM will reboot once completed.
5. It is recommended to create a new discovery snapshot on the latest version

--8<-- "snippets/no_proxy_localhost.md"
