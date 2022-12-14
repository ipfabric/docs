---
description: In this first step we will guide you through the deployment of the IP Fabric virtual machine (VM).
---

# Deploying the IP Fabric Virtual Machine (VM)

All virtual appliance images are available at  [https://releases.ipfabric.io/ipfabric/#current](https://releases.ipfabric.io/ipfabric/#current). Access is restricted to registered customers only. Please contact our [sales representative](mailto:sales@ipfabric.io) if you are interested in a trial of IP Fabric.

!!! important

    Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to connect to devices for data collection. It's important to place the VM in the proper network segment to prevent high ACL or firewall configuration overhead.

## Deploying on VMware OVA Virtual Machine

1. Deploy OVA to your vSphere environment as described at [Deploy an OVF or OVA
    Template](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html).
2. [Edit VM settings](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-4AB8C63C-61EA-4202-8158-D9903E04A0ED.html) and adjust according to your network size as described in the [operational requirements section](../Overview/index.md#operational-requirements).
   1. Change CPU count.
   2. Change memory size.
   3. [Add a new empty virtual disk or resize the main system disk](../../System_Administration/increase_disk_space.md)
3. Power on VM and [complete Boot Wizard](#complete-first-time-boot-wizard).

!!! note "Invalid OVF checksum algorithm: SHA256"

    Importing OVA on older vSphere/ESXi hosts may error stating the OVF checksum
    is invalid.  Please see [this documentation](../../support/known_issues/IP_Fabric/error_messages/invalid_ovf_checksum.md)
    on how to resolve this.


## Deploying on Hyper-V Virtual Machine

The `QCOW2` disk image file can be converted to different formats.
Using this method we will create a `VHDX` usable on Microsoft Hyper-V and manually create a new VM.

1. Download `ipfabric-*.qcow2` from the official source.
2. Convert `QCOW2` image to `VHDX` (Be sure to change the filenames in the command examples below.) 
   * Windows instructions:
     1. Download [qemu-img-windows](https://cloudbase.it/qemu-img-windows/)
     2. Unzip `qemu-img-windows`
     3. Run `qemu-img.exe convert ipfabric-<*>.qcow2 -O vhdx -o subformat=dynamic ipfabric-<*>.vhdx`
   * Linux instructions:
     1. Install qemu-utils `sudo apt install qemu-utils`
     2. Convert file: `qemu-img convert -f qcow2 -o subformat=dynamic -O vhdx ipfabric-<*>.qcow2 ipfabric-<*>.vhdx`
3. Create New Hyper-V Virtual Machine and Specify Name and Location

    ![HyperV Create](hyperv_create.png)

4. Specify Generation as `Generation 1`

   ![HyperV Generation](hyperv_generation.png)

5. Assign Memory (check requirements in [operational requirements section](../Overview/index.md#operational-requirements))

    ![HyperV Memory](hyperv_memory.png)

6. Configure Networking

    ![HyperV Networking](hyperv_networking.png)

7. Connect the Virtual Hard Disk

   ![HyperV Hard Disk](hyperv_harddisk.png)

8. Verify the Summary and Finish

   ![HyperV Summary](hyperv_summary.png)

9. Wait for the VM to be created

10. Edit the VM CPU settings (check requirements in [operational requirements section](../Overview/index.md#operational-requirements))

    ![HyperV Settings](hyperv_settings.png)

    ![HyperV Settings CPU](hyperv_settings_cpu.png)

11. Optionally increase Hard Disk Size based on [operational requirements section](../Overview/index.md#operational-requirements)
    1. [Extend the system disk or add a new empty virtual disk](../../System_Administration/increase_disk_space.md#increase-disk-space-for-hyper-v) if necessary.

12. Close the VM Settings window

13. Start the VM.

## Deploying a Virtual Machine to Nutanix

!!! note

    The Nutanix image is based on Virtual Disks of VMware vSphere OVA image. As Nutanix officially supports import of VMware VM’s, below instructions are based on the same image as used at [VMware deployment section](#deploying-on-vmware-ova-virtual-machine).

1. Download the `ipfabric-*-.OVA` file from official source.
2. Extract the previously downloaded OVA file using 7-zip or any similar software. The structure of extracted files should look like below

    ![Unzip OVA](unzip_ova.png)

3. Import `.vmdk` files to Nutanix hypervisor and follow Nutanix' official documentation -- [Nutanix import OVA](https://portal.nutanix.com/#page/kbs/details?targetId=kA03200000099TXCAY) and [Quick tip how to deploy a VM from OVF to AHV](https://next.nutanix.com/installation-configuration-23/quick-tip-how-to-deploy-a-vm-from-an-ovf-to-ahv-33613).

4. Edit VM hardware settings and adjust according to the network environment size (check requirements in [operational requirements section](../Overview/index.md#operational-requirements)).

   1. Change CPU count
   2. Change memory size
   3. [Extend the system disk or add a new empty virtual disk](../../System_Administration/increase_disk_space.md) if necessary.

5. Start the VM and check if the system starts without any interrupts.

## Deploying a Virtual Machine on KVM 

We have currently the limitation that drives need to be `/dev/sdx`. Usually Linux hypervisors are using the `virtio-blk` driver which is represented as `/dev/vdx` in the guest system. To overcome this limitation use the `virtio-scsi` as drive controller.

1.  Download `qcow2` system disk to your KVM hypervisor.
2.  Resize the `qcow2` data-disk that corresponds to [your network needs](../Overview/index.md#operational-requirements) if necessary. Use the following command:

    ```shell
    qemu-img resize ipfabric-disk1.qcow2 100G # (up to 1000G for 20 000 devices)
    ```

3.  Deploy the VM to your hypervisor with the virt-install utility by issuing the following command (chose CPU and RAM size according to the size of your network):

    ```shell
    virt-install --name=IP_Fabric --disk path=<path to the disk>.qcow2 --graphics spice --vcpu=4 --ram=16384 --network bridge=virbr0 --import
    ```

4.  This command deploys a new virtual machine with IP_Fabric name, system `qcow2` disk, 4 CPU cores, 16GB of RAM and will connect VM to the internet through the `virtbr0` interface (if your machine has a different bridge interface name or you want to connect it straight through the device network card to the internet you need to change the `--network` parameter).

5.  This command also starts up the VM.

6.  Additionally, you can [create and add a new empty virtual disk if needed](../../System_Administration/increase_disk_space.md).
