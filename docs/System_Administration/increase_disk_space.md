---
description: Appliance disk space can be extended by extending existing virtual disk or by adding new empty virtual hard drive to IP Fabric VM.
---

# Increase Disk Space

Starting version IP Fabric 5.0.0, appliance is distributed as one hard disk installation instead of two.

IP Fabric appliance is using LVM type for **root** and **swap** partitions.

On default installation **swap** has 16GB and **root** has ~72GB of space.

We automatically resize the **boot** disk as follows:

 * resize primary partition to full size of the disk
 * resize extended partition to full size of primary partition
 * extend `ipfabric-vg/root` to `+100%FREE`
 * online resize `ext4` partition


## Increasing Disk Space On IP Fabric Appliance

If you need any help with a disk space expansion, please contact our [Support Team](../support/index.md)

### Resizing Root/First Disk

The easiest way how to resize IP Fabric system disk is to

1. Shutdown the appliance

2. Resize root/first disk to a desired size

3. Start virtual machine

`cloud-init` will take care of resizing this disk.

### Expanding System Volume By Adding Additional Disk(s)

If you want to add secondary or any additional disk as a system disk, you will need to manually add it to `ipfabric-vg/root` volume.

To do that follow LVM resource:

 * [Debian LVM wiki](https://wiki.debian.org/LVM)
 * [Arch LVM wiki](https://wiki.archlinux.org/title/LVM)


## Local Backup Disk

!!! note "Backup Disk"

    Backup disk is not present by default! Please add a new virtual disk to enable local backups.

When enabling local backups, a [backup](../IP_Fabric_Settings/advanced/system/system_backup.md) tool creates backups to the `/backup` directory.
The tool first checks if the local backup directory exists and then the backups are created.

Any additional disk (see hypervisor specific configuration on the bottom of this page) of your choice can be mounted as the backup directory.
We recommend using for local backups an additional disk that is physically located on a different datastore than the root volume.

!!! warning

    The backup disk has to be partitioned with LVM. Specifically, the `/backup` directory has to be on the logical volume `backup` of the volume group `backup-vg`.

### Example Of A Physical Disk Being Mounted To `/backup` Directory

Find a device which you want to use as the `/backup` directory. In this case, `vdb`.

```
osadmin@ipfabric:~$ lsblk
NAME                    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda                     254:0    0 76,3G  0 disk 
├─vda1                  254:1    0  487M  0 part /boot
├─vda2                  254:2    0    1K  0 part 
└─vda5                  254:5    0 75,8G  0 part 
  ├─ipfabric--vg-swap_1 253:0    0   16G  0 lvm  [SWAP]
  └─ipfabric--vg-root   253:1    0 59,8G  0 lvm  /
vdb                     254:16   0   20G  0 disk             # <- I want to use this device for the /backup directory
```

Create LVM physical volume on the disk `vdb`:

```
osadmin@ipfabric:~$ sudo pvcreate /dev/vdb
  Physical volume "/dev/vdb" successfully created.
```

Create the volume group `backup-vg`:

```
osadmin@ipfabric:~$ sudo vgcreate backup-vg /dev/vdb
  Volume group "backup-vg" successfully created
```

Use the entire size of the volume group `backup-vg` for creating the logical volume `backup`:

```
osadmin@ipfabric:~$ sudo lvcreate -n backup -l 100%FREE backup-vg
  Logical volume "backup" created.
```

Create a filesystem (in this example `ext4`) on the logical volume `backup`:

```
osadmin@ipfabric:~$ sudo mkfs.ext4 /dev/mapper/backup--vg-backup
mke2fs 1.46.2 (28-Feb-2021)
Discarding device blocks: done                            
Creating filesystem with 5241856 4k blocks and 1310720 inodes
Filesystem UUID: 26bf3259-8421-4b67-ad27-71fa55e57af8
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done   
```

Create a new [fstab](https://wiki.archlinux.org/title/fstab) entry (for example with `sudo vi /etc/fstab`):

!!! info

    We strongly recommend only LVM partition, LABEL and UUID in `fstab`, for more info see
    [Persistent block device naming](https://wiki.archlinux.org/title/Persistent_block_device_naming).

```
/dev/mapper/backup--vg-backup   /backup   ext4   defaults   0   0
```

Create the `/backup` directory:

```
osadmin@ipfabric:~$ sudo mkdir /backup
```

The logical volume `backup` on the disk `vdb` can be now mounted with:

```
osadmin@ipfabric:~$ sudo mount /backup
```

Finally, check the output of `lsblk`:

```
osadmin@ipfabric:~$ lsblk
NAME                    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda                     254:0    0 76,3G  0 disk 
├─vda1                  254:1    0  487M  0 part /boot
├─vda2                  254:2    0    1K  0 part 
└─vda5                  254:5    0 75,8G  0 part 
  ├─ipfabric--vg-swap_1 253:0    0   16G  0 lvm  [SWAP]
  └─ipfabric--vg-root   253:1    0 59,8G  0 lvm  /
vdb                     254:16   0   20G  0 disk 
└─backup--vg-backup     253:2    0   20G  0 lvm  /backup
```

## Deprecated Resize Wizard

IP Fabric appliance < 5.0.0 was using two LVM volumes by default. `ipfabic-vg/root` for system and data, `backup-vg/backup` for `/backup`.
System and data volume was extended over two disks (usually first two). For third and onward, one could choose to extend *root* or *backup* volume.
This was dropped in favour of one system/data disk with possibility to add backup disk. The original script is still present in the system,
but is *discouraged* to use it as it is expecting only `boot` disk to be `sda`, `sdb` as extended `ipfabic-vg/root` and one could choose
how `sd[c-z]` would be used. The new approach with one disk is more versatile, and it is not limited to `sd[a-z]` disks. 

!!! error "Deprecated script"

    This script should not be used anymore. You should run only when you are sure you know what you are doing.

Script location: `/opt/nimpee/sys-lvm-resize.sh`


## Increase Disk Space For VMware

### Extend Existing Virtual Disk (For System And Data)

1.  Open VMware vSphere web console.
2.  Right click on VM name and select **Edit Settings**.
3.  Select **Hard disk** and change its size.
4.  Click **OK**.
5.  Restart VM (using CLI or web UI).
6.  Disk space is automatically increased if you resized the first drive.

### Add New Virtual Disk (As An Additional Backup Disk)

1. Open VMware vSphere web console.
2. Right click on VM name and select **Edit Settings**.
3. Click **Add New Device → Hard Disk**
4. Select new size
5. Specify **Location**:
    1.  for system disk expansion is recommended to select **Store with
        the virtual machine**
    2.  for backup volume is recommended to select different datastore
        ideally on a different physical storage
6. Click **OK**
    ![VMWare virtual hardware](vmware_virtual_hardware.png)
7. Launch Remote (Web) Console.
8. Reboot(**Send Ctrl+Alt+Delete** function can be also used) or power on IP
   Fabric VM.
9. Follow [Adding additional disk(s)](#expanding-system-volume-by-adding-additional-disks)
    or [Example adding disk to backup](#example-of-a-physical-disk-being-mounted-to-backup-directory)

## Increase Disk Space For Hyper-V

### Extend Existing Virtual Disk (For System And Data)

1.  Open Hyper-V Manager.
2.  Shutdown VM. (when Started, HyperV won't let you change any
    hardware settings)
3.  Right click on VM name and select **Settings**.
4.  Select **IDE Controller - Hard Drive -
    ipfabric-x-x-x-disk1.vhdx **
5.  Click **Edit** - **Choose Action** - select option **Expand**,
    click **Next**.
6.  Set up required disk size and click **Finish**.
7.  Start VM.
8.  Disk space is automatically increased, if you resized the first disk.

### Add New Virtual Disk (As An Additional Backup Disk)

1. Open HyperV Manager.
2. Shutdown VM. (when Started, HyperV won't let you change any
    hardware settings)
3. Right click on VM name an select **Settings**.
   ![HyperV settings](hyperv_settings.png)
4. Select IDE Controller 1 - Hard Drive - click **Add**
   ![HyperV Add hard drive](hyperv_add_hdd.png)
5. Select **Virtual hard disk** - click **New** - select **Choose
    Disk Format** - select **VHDX** - click **Next**.
   ![HyperV Add hard drive - format](hyperv_add_hdd_format.png)
6. Select **Dynamically expanding** - click **Next**
   ![HyperV Add hard drive - type](hyperv_add_hdd_type.png)
7. Specify name and location of disk.
8. **Configure Disk** - select **Create a new blank virtual hard
    disk** - change **Size** to required value - click
    **Finish**.
   ![HyperV Add hard drive - space](hyperv_add_hdd_space.png)
9. Apply new disk on Settings window - close **Settings**.
10. Start VM.
11. Follow [Adding additional disk(s)](#expanding-system-volume-by-adding-additional-disks)
    or [Example adding disk to backup](#example-of-a-physical-disk-being-mounted-to-backup-directory)
