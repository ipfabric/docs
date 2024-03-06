---
description: In this first step, we will guide you through the deployment of the IP Fabric virtual machine.
---

# Deploying the IP Fabric Virtual Machine (VM)

All VM images are available at  [https://releases.ipfabric.io/ipfabric/#current](https://releases.ipfabric.io/ipfabric/#current). Access is restricted to registered customers only. Please contact our [sales representative](mailto:sales@ipfabric.io) if you are interested in a trial of IP Fabric.

!!! important

    Please remember that IP Fabric uses CLI access (SSH or Telnet) to connect to devices for collecting data. It's important to place the VM in the proper network segment to prevent high ACL or firewall configuration overhead.

## Deploying on VMware OVA Virtual Machine

1. Deploy the OVA to your vSphere environment as described in
   [Deploy an OVF or OVA Template](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html).
2. [Edit VM settings](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-4AB8C63C-61EA-4202-8158-D9903E04A0ED.html) and adjust according to your network size as described in the [Operational Requirements](../overview/index.md#operational-requirements) section.
   1. Change CPU count.
   2. Change memory size.
   3. [Add a new empty virtual disk or resize the main system disk](../System_Administration/increase_disk_space.md).
3. Power on the VM and [complete the First Boot Wizard](#complete-first-time-boot-wizard).

!!! note "Invalid OVF checksum algorithm: SHA256"

    Importing the OVA on older vSphere/ESXi hosts may result in an error stating that the OVF checksum
    is invalid. Please refer to [this documentation](../support/known_issues/IP_Fabric/error_messages/invalid_ovf_checksum.md)
    on how to resolve the issue.

## Deploying on Hyper-V Virtual Machine

The `qcow2` disk image file can be converted to different formats.
Using this method, we will create a `VHDX` usable on Microsoft Hyper-V and manually create a new VM.

1. Download `ipfabric-*.qcow2` from the official source.

2. Convert the `qcow2` image to `VHDX`. (Be sure to change the filenames in the command examples below.)

   - Windows instructions:
     1. Download the [QEMU disk image utility for Windows](https://cloudbase.it/qemu-img-windows/).
     2. Unzip `qemu-img-windows`.
     3. Run: `qemu-img.exe convert ipfabric-<*>.qcow2 -O vhdx -o subformat=dynamic ipfabric-<*>.vhdx`

   - Linux instructions:
     1. Install `qemu-utils`: `sudo apt install qemu-utils`
     2. Run: `qemu-img convert -f qcow2 -o subformat=dynamic -O vhdx ipfabric-<*>.qcow2 ipfabric-<*>.vhdx`

3. Create a new Hyper-V virtual machine and specify its **Name** and **Location**:

   ![Hyper-V - Specify Name and Location](hyperv_create.png)

4. In the **Specify Generation** step, select `Generation 1`:

   ![Hyper-V - Specify Generation](hyperv_generation.png)

5. Assign memory. (Check requirements in the [Operational Requirements](../overview/index.md#operational-requirements) section.)

   ![Hyper-V - Assign Memory](hyperv_memory.png)

6. Configure networking:

   ![Hyper-V - Configure Networking](hyperv_networking.png)

7. Connect a virtual hard disk:

   ![Hyper-V - Connect Virtual Hard Disk](hyperv_harddisk.png)

8. Verify the Summary and click **Finish**:

   ![Hyper-V - Summary](hyperv_summary.png)

9. Wait for the VM to be created.

10. Edit the VM CPU settings. (Check requirements in the [Operational Requirements](../overview/index.md#operational-requirements) section.)

    ![Hyper-V - VM Settings](hyperv_settings.png)

    ![Hyper-V - VM Settings - Hardware - Processor](hyperv_settings_cpu.png)

11. Optionally, increase the disk size based on the [Operational Requirements](../overview/index.md#operational-requirements) section.

    - [Extend the system disk or add a new empty virtual disk](../System_Administration/increase_disk_space.md#increase-disk-space-for-hyper-v) if necessary.

12. Close the VM Settings window.

13. Start the VM.

## Deploying a Virtual Machine to Nutanix

!!! note

    The Nutanix image is based on Virtual Disks of VMware vSphere OVA image. As Nutanix officially supports import of VMware VMs, the instructions below are based on the same image as used in the [VMware deployment](#deploying-on-vmware-ova-virtual-machine) section.

1. Download the `ipfabric-*-.OVA` file from the official source.

2. Extract the downloaded OVA file using 7-Zip or any similar software. The structure of extracted files should look like below:

   ![Unzip OVA](unzip_ova.png)

3. Import the `.vmdk` files to the Nutanix hypervisor and follow Nutanix's official documentation -- [Nutanix import OVA](https://portal.nutanix.com/#page/kbs/details?targetId=kA03200000099TXCAY) and [Quick tip how to deploy a VM from OVF to AHV](https://next.nutanix.com/installation-configuration-23/quick-tip-how-to-deploy-a-vm-from-an-ovf-to-ahv-33613).

4. Edit the VM hardware settings and adjust according to the network environment size. (Check requirements in the [Operational Requirements](../overview/index.md#operational-requirements) section.)

   1. Change CPU count.
   2. Change memory size.
   3. [Extend the system disk or add a new empty virtual disk](../System_Administration/increase_disk_space.md) if necessary.

5. Start the VM and check if the system starts without any interruptions.

## Deploying a Virtual Machine on KVM

We currently have the limitation that drives need to be `/dev/sdx`. Usually, Linux hypervisors use the `virtio-blk` driver, which is represented as `/dev/vdx` in the guest system. To overcome this limitation, use `virtio-scsi` as the drive controller.

1. Download `qcow2` system disk to your KVM hypervisor.

2. Resize the `qcow2` data disk so it corresponds to [your network's needs](../overview/index.md#operational-requirements) if necessary. Use the following command:

   ```shell
   qemu-img resize ipfabric-disk1.qcow2 100G # (up to 1000G for 20 000 devices)
   ```

3. Deploy the VM to your hypervisor with the `virt-install` utility by issuing the following command (chose CPU and RAM size according to the size of your network):

   ```shell
   virt-install --name=IP_Fabric --disk path=<path to the disk>.qcow2 --graphics spice --vcpu=4 --ram=16384 --network bridge=virbr0 --import
   ```

   - This command deploys a new virtual machine with the name `IP_Fabric`, system `qcow2` disk, 4 CPU cores, 16 GB of RAM, and connects the VM to the internet through the `virtbr0` interface. (If your machine has a different bridge interface name or you want to connect it to the internet directly through the device network card, you need to change the `--network` parameter.)
   - This command also starts up the VM.

4. Additionally, you can [create and add a new empty virtual disk](../System_Administration/increase_disk_space.md) if needed.

## Deploying a Virtual Machine on VirtualBox

!!! warning

    Deploying IP Fabric on VirtualBox is currently not officially supported -- it is not tested, and we cannot guarantee that it will work.

1.  Download the `OVA` image.

2.  Import the `OVA` image via **File --> Import Appliance...**:

    ![VirtualBox - Import Virtual Appliance](virtualbox_import-virtual-appliance.png)

3.  In the next step of the **Import Virtual Appliance** guide:

    1. Set **CPU** and **RAM** as per the [hardware requirements](../overview/index.md#hardware-requirements) for your use-case.

    2. Set the **Network Adapter** to `Paravirtualized Network (virtio-net)`.

    3. Keep the `Import hard drives as VDI` option checked for importing the disk image in the default VirtualBox format. (Otherwise, the disk image will be imported as VDMK, the default format of VMware.)

    ![VirtualBox - Import Virtual Appliance - Appliance Settings](virtualbox_import-virtual-appliance-2.png)

4.  Right-click the newly created virtual machine and select its **Settings...**

5.  In the **System** section, select `ICH9` as the **Chipset**:

    ![VirtualBox - VM Settings - System](virtualbox_vm-settings_system.png)

6.  In the **Display** section, select `VMSVGA` as the **Graphics Controller**:

    ![VirtualBox - VM Settings - Display](virtualbox_vm-settings_display.png)

    - Or to what VirtualBox suggests when an invalid Graphics Controller is selected:

    ![VirtualBox - VM Settings - Display - Invalid settings detected](virtualbox_vm-settings_display-2.png)

  !!! warning

      When an invalid Graphics Controller is selected, it can lead to issues in the virtual machine and even on the host machine.

7.  In the **Storage** section, select `virtio-scsi` as the Controller **Type**:

    ![VirtualBox - VM Settings - Storage](virtualbox_vm-settings_storage.png)

8.  In the **Network** section, select `Bridged Adapter` and re-check in **Advanced** that the **Adapter Type** is `Paravirtualized Network (virtio-net)`:

    ![VirtualBox - VM Settings - Network](virtualbox_vm-settings_network.png)

9.  Start the VM.

## Deploying a Virtual Machine on Microsoft Azure

1. Log in to the Microsoft Azure portal and create a resource group.

   In the [Microsoft Azure documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group), a **resource group** is defined as:

   > ... a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. You decide how you want to allocate resources to resource groups based on what makes the most sense for your organization. Generally, add resources that share the same lifecycle to the same resource group so you can easily deploy, update, and delete them as a group.

   Please follow the instructions in [Create resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups).

   ![Create a Resource group](azure-imgs/azure-01-Create-resource-group.png)

2. Create a storage account for IP Fabric.

   A storage account is an Azure Resource Manager resource. Resource Manager is the deployment and management service for Azure. For more information, see [Azure Resource Manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) and [Creating Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#create-a-storage-account-1).

   ![Create a Storage account](azure-imgs/azure-02-Create-storage-account.png)

3. Create a Storage Blob container.

   Azure Blob Storage allows you to store large amounts of unstructured object data. You can use Blob Storage to gather or expose media, content, or application data to users. Because all blob data is stored within containers, you must create a storage container before you can begin to upload data. To learn more about Blob Storage, read the [Introduction to Azure Blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).

   ![Create a Storage blob container](azure-imgs/azure-03-storage-blob-container.png)

4. Convert the `qcow2` image to VHD.

   IP Fabric provides the `qcow2` image. For converting `qcow2` to VHD, you may for instance use a utility from [QEMU](https://www.qemu.org/download/). The recommended way to convert the image is then:

   ```
   qemu-img convert -f qcow2 -o subformat=fixed,force_size -O vpc ipfabric-6-3-1+1.qcow2 ipfabric-6-3-1+1.vhd
   ```

  !!! important

      Please use `qemu-img` version `2.6` or higher. According to the [Azure documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/create-upload-generic#resizing-vhds):

      > There is a known bug in qemu-img versions >=2.2.1 that results in an improperly formatted VHD. The issue has been fixed in QEMU 2.6. We recommend using either qemu-img 2.2.0 or lower, or 2.6 or higher.
      
      You may check the `qemu-img` version that you are using with:
      
      ```
      qemu-img --version
      ```

5. Upload the VHD image to the storage account.

   To [upload the VHD image](https://learn.microsoft.com/en-us/azure/virtual-desktop/set-up-customize-master-image#upload-master-image-to-a-storage-account-in-azure), you need to download and install the [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/).
   The image needs to be uploaded to the previously created Blob container.

   ![Upload the VHD image](azure-imgs/azure-04-uploaded-vhd.png)

  !!! important

      For uploading the VHD image, please use the Azure Storage Explorer (a native Windows app) instead of the Azure web UI. If you upload the VHD image via the Azure web UI, you might encounter the following error:
      
      > The specified cookie value in VHD footer indicates that disk 'ipfabric-6-3-1+1.vhd' with blob https://.../vhd/ipfabric-6-3-1+1.vhd is not a supported VHD. Disk is expected to have cookie value 'conectix'.

6. Create an image from VHD.

   Creating a managed image in Azure is as simple as loading the necessary files. The [Create a legacy managed image of a generalized VM in Azure](https://learn.microsoft.com/en-gb/azure/virtual-machines/capture-image-resource) documentation section contains all the needed clues.

   ![Create an Image from VHD](azure-imgs/azure-05-create-image.png)

7. Deploy a VM from the image.

   Ensure that you follow the [resource requirements matrix](../overview/index.md#hardware-requirements) when sizing the virtual machine on Azure.

  !!! important

      Please note that the Azure serial console might not be accessible for setting the `osadmin` password in the [First Boot Wizard](02-boot_wizard.md). In that case, please contact the IP Fabric Support team or your Solution Architect. We can connect to the appliance via SSH with the default/factory `osadmin` password (that is overwritten during the First Boot Wizard) and run the First Boot Wizard manually with:
      
      ```
      sudo nimpee-net-config -a
      ```
