---
description: In this first step, we will guide you through the deployment of the IP Fabric virtual machine.
---

# Deploying IP Fabric Virtual Machine (VM)

All VM images are available at <https://releases.ipfabric.io/images/>. Access is restricted to registered customers only. Please contact our [sales representative](mailto:sales@ipfabric.io) if you are interested in a trial of IP Fabric.

!!! important

    Please remember that IP Fabric uses CLI access (SSH or Telnet) to connect to devices for collecting data. It's important to place the VM in the proper network segment to prevent high ACL or firewall configuration overhead.

## OVA Distribution Details

The appliance is built on top of Debian 12, which has been officially supported
since
[ESXi version `8.0`](https://compatibilityguide.broadcom.com/search?program=software&persona=live&column=osVendors&order=asc&osFamilyName=%5BDebian+12%5D&activePage=1&activeDelta=20).

The minimal required Virtual Hardware Version is `vmx-20`, supported by ESXi
`8.0`, Fusion `13.6`, Workstation Pro `17.x`, and Workstation Player `17.x`. For
details, see the VMware KB articles
[1003746](https://kb.vmware.com/s/article/1003746) and
[2007240](https://kb.vmware.com/s/article/2007240).

This system type is required because we need the virtio/paravirtualized drivers
for storage and network:

- [`PVSCSI`](https://kb.vmware.com/s/article/1010398) (Paravirtual SCSI)
- [`VMXNET 3`](https://kb.vmware.com/s/article/1001805)

Note that we also have requirements about the processor itself -- see
[Hardware Requirements](../overview/index.md#hardware-requirements). These
cannot be described through the OVA image definition.

!!! danger "If you do not use the virtio/paravirtualized drivers for storage and network, performance will be degraded."

### Setting VM From Scratch -- Importing VMDK Image

!!! success "Importing VMDK is the recommended way."

If you do not have access to an ESXi host for importing, you can try to import
the disk (VMDK) and set up the machine manually. Ensure the following are
configured correctly:

- Virtual Hardware Version is at least `vmx-20`
- virtio/paravirtualized drivers for storage and network
  - [`PVSCSI`](https://kb.vmware.com/s/article/1010398) (Paravirtual SCSI)
  - [`VMXNET 3`](https://kb.vmware.com/s/article/1001805)

See the detailed instructions in
[Deploying VM on VMware ESXi Using VMDK Image](#deploying-vm-on-vmware-esxi-using-vmdk-image).

### Deploying Through vSphere or VxRail -- Converting SHA256 OVA Image to SHA1

You may experience problems deploying through vSphere/VxRail. vSphere/VxRail is
refusing the SHA256 version of our OVA image. When trying to create a virtual
machine using the SHA1-based OVA image, you may experience problems with
importing the image because of unsupported "hardware". In this case, please see
the next paragraph about deploying manually.

VMware's KB article on converting OVA images:
["The OVF package is invalid and cannot be deployed" error when deploying the OVA (2151537)](https://kb.vmware.com/s/article/2151537)

!!! warning "Importing SHA1-Based OVA Image"

    This might lead to unexpected results, such as wrong hardware assignments,
    degraded performance, etc.

!!! tip "`operation not supported on this object`"

    This states the inability to deploy the OVA image with the required hardware
    requirements through itself (vSphere). However, if the same OVA image is
    deployed through ESXi, no warnings are present while creating the virtual
    machine.

## Deploying VM on VMware

### Deploying VM on VMware vSphere Using OVA Image

1. Deploy the OVA to your vSphere environment as described in
   [Deploy an OVF or OVA Template](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html).
2. [Edit VM settings](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-4AB8C63C-61EA-4202-8158-D9903E04A0ED.html) and adjust according to your network size as described in the [Operational Requirements](../overview/index.md#operational-requirements) section.
   1. Change CPU count.
   2. Change memory size.
   3. [Add a new empty virtual disk or resize the main system disk](../System_Administration/increase_disk_space.md).
3. Power on the VM and [complete IPF CLI Config](02-ipf_cli_config.md).

!!! note "Invalid OVF checksum algorithm: SHA256"

    Importing the OVA on older vSphere/ESXi hosts may result in an error stating that the OVF checksum
    is invalid. Please refer to [OVA Distribution Details](#ova-distribution-details)
    on how to resolve the issue.

### Deploying VM on VMware ESXi Using VMDK Image

1. Go to <https://releases.ipfabric.io/images/>, select the folder with the
   highest version number, and download the `ipfabric-<x.y.z+build>.vmdk` file.

2. Log in to the VMware ESXi web interface.

3. Select **Virtual Machines** and click **Create / Register VM**.

4. A `New virtual machine` dialog appears. In its 1st step `Select creation
   type`, select **Create a new virtual machine**:

   ![VMware ESXi - Create a new virtual machine](esxi-vmdk/create-vm.png)

5. In the 2nd step `Select a name and guest OS`:

   1. Specify the VM's **Name**.

   2. In the **Compatibility** field, select at least `ESXi 8.0 virtual
      machine`, which corresponds to the Virtual Hardware Version `20`
      (`vmx-20`). Refer to
      [Virtual machine hardware versions](https://knowledge.broadcom.com/external/article?legacyId=1003746)
      for mapping between Virtual Hardware Versions and ESXi versions.

   3. In the **Guest OS family** field, select `Linux`.

   4. In the **Guest OS version** field, select `Debian GNU/Linux 12 (64-bit)`.

  !!! Info "Deploying VMDK on Older ESXi Systems"
       
      It is possible to deploy VMDK on older ESXi systems that do not support
      Debian 12. Please choose the latest available `Debian (64-bit)` version.
      For the best experience, use a supported version of ESXi.

6. In the 3rd step `Select storage`, keep the default settings.

7. In the 4th step `Customize settings`:

   1. Remove the automatically added hard disk:

      ![VMware ESXi - Remove disk](esxi-vmdk/remove-disk.png)

   2. Change the **SCSI Controller** to `VMware Paravirtual` (`PVSCSI`) and
      the **Adapter Type** under **Network Adapter** to `VMXNET 3`:

      ![VMware ESXi - Change storage and network](esxi-vmdk/storage-and-network.png)

   3. Click **Add hard disk**, select **Existing hard disk**, and import the
      downloaded `ipfabric-<x.y.z+build>.vmdk` file:

      ![VMware ESXi - Add disk](esxi-vmdk/add-disk.png)

  !!! warning "Unsupported and/or invalid disk type while importing VMDK"

      The disk format of the VMDK file may be incomatible with your ESXi version. To convert it to a compatible format, please refer to the [VMware documentation](https://knowledge.broadcom.com/external/article/310567/a-virtual-machine-fails-to-power-on-with.html) for detailed instructions.

8. Power on the VM and [complete IPF CLI Config](02-ipf_cli_config.md).

## Deploying VM on Hyper-V

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

## Deploying VM on Nutanix

1. Go to <https://releases.ipfabric.io/images/>, select the folder with the
   highest version number, and download the `ipfabric-<x.y.z+build>.vmdk` file.

3. Import the `ipfabric-<x.y.z+build>.vmdk` file to the Nutanix hypervisor and
   follow Nutanix's official documentation --
   [Nutanix import OVA](https://portal.nutanix.com/#page/kbs/details?targetId=kA03200000099TXCAY)
   and
   [Quick tip how to deploy a VM from OVF to AHV](https://next.nutanix.com/installation-configuration-23/quick-tip-how-to-deploy-a-vm-from-an-ovf-to-ahv-33613).

4. Edit the VM hardware settings and adjust according to the network environment
   size. (Check requirements in the
   [Operational Requirements](../overview/index.md#operational-requirements)
   section.)

   1. Change CPU count.
   2. Change memory size.
   3. [Extend the system disk or add a new empty virtual disk](../System_Administration/increase_disk_space.md)
      if necessary.

5. Power on the VM and [complete IPF CLI Config](02-ipf_cli_config.md).

## Deploying VM on KVM

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

## Deploying VM on VirtualBox

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

## Deploying VM on Azure

### Uploading IP Fabric Disk File

The first step of deploying to Azure requires creating a VHD file from the `qcow2` image, uploading it to a blob storage container, and then creating an Image to use for a Virtual Machine.

1. Log in to the [Microsoft Azure Portal](https://portal.azure.com/) and create or use an existing Resource Group.

   In the [Microsoft Azure documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group), a **resource group** is defined as:

   > ... a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. You decide how you want to allocate resources to resource groups based on what makes the most sense for your organization. Generally, add resources that share the same lifecycle to the same resource group so you can easily deploy, update, and delete them as a group.

   Please follow the instructions in [Create resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups).

   ![Create a Resource group](azure-imgs/azure-01-Create-resource-group.png)

2. Create or use an existing Storage Account for the IP Fabric VM.

   A storage account is an Azure Resource Manager resource. Resource Manager is the deployment and management service for Azure. For more information, see [Azure Resource Manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) and [Creating Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#create-a-storage-account-1).

   ![Create a Storage account](azure-imgs/azure-02-Create-storage-account.png)

3. Create or use an existing Blob Storage Container.

   Azure Blob Storage allows you to store large amounts of unstructured object data. You can use Blob Storage to gather or expose media, content, or application data to users. Because all blob data is stored within containers, you must create a storage container before you can begin to upload data. To learn more about Blob Storage, read the [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).

   ![Create a Blob Storage container](azure-imgs/azure-03-storage-blob-container.png)

4. Convert the IP Fabric-provided `qcow2` image to VHD using [QEMU](https://www.qemu.org/download/). The recommended way to convert the image:

   ```shell
   qemu-img convert -f qcow2 -o subformat=fixed,force_size -O vpc ipfabric-6-3-1+1.qcow2 ipfabric-6-3-1+1.vhd
   ```

  !!! important "QEMU Version"

      Please use `qemu-img` version `2.6` or higher. According to the [Azure documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/create-upload-generic#resizing-vhds):

      > There is a known bug in qemu-img versions >=2.2.1 that results in an improperly formatted VHD. The issue has been fixed in QEMU 2.6. We recommend using either qemu-img 2.2.0 or lower, or 2.6 or higher.

      You may check the `qemu-img` version that you are using with:

      ```shell
      qemu-img --version
      ```

5. [Upload the VHD image](https://learn.microsoft.com/en-us/azure/virtual-desktop/set-up-customize-master-image#upload-master-image-to-a-storage-account-in-azure) to the storage account blob container created using the [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/).

   ![Upload the VHD image](azure-imgs/azure-04-uploaded-vhd.png)

  !!! warning "Blob Type"

      When uploading the VHD image to Azure, make sure to select `Page Blob` as the Blob Type. Azure images can only be created from a `Page Blob` source.

  !!! important "VHD Upload"

      For uploading the VHD image, please use the Azure Storage Explorer (a native Windows app) instead of the Azure web UI. If you upload the VHD image via the Azure web UI, you might encounter the following error:

      > The specified cookie value in VHD footer indicates that disk 'ipfabric-6-3-1+1.vhd' with blob https://.../vhd/ipfabric-6-3-1+1.vhd is not a supported VHD. Disk is expected to have cookie value 'conectix'.

### Sizing IP Fabric VM

Prior to creating the IP Fabric image, it is necessary to know the type of server required.
Azure Regions contain different server sizes, so performing this step will ensure you select the correct Region in the next step.

#### IP Fabric Hardware Requirements

1. Check the IP Fabric [Hardware Requirements](../overview/index.md#hardware-requirements) documentation.
2. Record the number of CPUs.
3. Record the RAM requirements.

#### Azure VM Finder

For this example, we will use minimum of 16 CPUs and 32 GB memory requirements.

1. Please visit the [Azure Find your VM](https://azure.microsoft.com/en-us/pricing/vm-selector/) website.
2. Select `Find VMs by workload type`.
3. Select all for `Workload type` and click `Next`.
4. Enter minimum and maximum CPU and RAM values.
   1. vCPU: min 16, max 24
   2. RAM: min 32 GB, max 56 GB
5. Select `Premium SSD` for `Disk Storage`.
6. `Data Disk` can be left as default as IP Fabric does not use a separate disk for data.
7. Under `Operating system`: `To use a custom VM image, select Linux and then CentOS to see VM availability and pricing information.`
8. Select your preferred Region(s).
9. Under the `Recommended Virtual Machine(s)`, find an `Instance` with either an **Intel or AMD processor** that will suit your needs.
10. Record the `Instance` and `Region` names you would like to use for the deployment.

### Creating Image

![Search Images](azure-imgs/azure-05-1-images.png)

Search and select `Images` in the portal's search bar, and then `Create` a new Image.

![Create an Image from VHD](azure-imgs/azure-05-create-image.png)

1. Select the correct `Subscription` and `Resource group`.
2. Name the image.
3. Select the `Region` that was recorded from [Azure VM Finder](#azure-vm-finder).
4. Set `OS type` to `Linux`.
5. **Set `VM generation` to `Gen 1`.**
6. Browse the `Storage blob` to find and select your uploaded VHD.
7. Set `Account type` to `Premium SSD`.
8. Set `Host Caching` to `Read/write`.
9. Set `Key management` to `Platform-managed key`.
10. Optional: Add custom `Tags`.
11. Select `Review + create`, wait for validation, and then click `Create`.

### Creating VM

After creating the Image, go to the Resource and select `Create VM`:

![Create VM](azure-imgs/azure-06-create-vm.png)

#### Basics

![VM Details](azure-imgs/azure-07-vm-details.png)

![Basics Continued](azure-imgs/azure-08-basics-cont.png)

1. Fill out the required `Project details` and `Instance details` sections:

   1. Select the correct `Subscription` and `Resource group`.

   2. Name the virtual machine.

   3. Select an `Availability Zone`.

   4. Using the information in [Sizing IP Fabric VM](#sizing-ip-fabric-vm), select the appropriate instance size.

2. Specify an `Administrator account` using Password authentication with a secure password.

  !!! warning "Username"

      Username **must not** be `autoboss`, `osadmin`, or `root`. Optionally, use the default `azureuser`.

  !!! note "SSH Public Key"

      Specifying `SSH public key` authentication will disable SSH Password authentication for the entire VM requiring either:

      - Manually editing `/etc/ssh/sshd_config` to enable password authentication for the `osadmin` user.
      - Using the configured key(s) to SSH into the VM anytime CLI access is required (most secure).

3. `Inbound port rules > Public inbound ports` should be set to `None`.

4. Set `Licensing > License type` to `Other`.

#### Disks

![VM Disks](azure-imgs/azure-09-disks.png)

1. Enabling `Encryption at host` is recommended if it is available.

2. Select the OS disk size based on [resource requirements matrix](../overview/index.md#hardware-requirements).

3. OS disk type can be `Premium SSD (locally-redundant storage)` or `Premium SSD (zone-redundant storage)`.

#### Networking

![VM Networking](azure-imgs/azure-10-networking.png)

1. Select or create a new `Virtual network` and `Subnet`.

2. Please see [Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-overview#network-security-groups) for information on securing access to your VM.

!!! danger "Public IP"

    **IP Fabric contains sensitive information about your network, so it is highly recommended to use private networks only.**

#### Other Configuration Options

1. `Management`: Can be left to defaults.
2. `Monitoring` and `Advanced`:
   - This is outside the scope of a normal IP Fabric deployment.
   - Installing `Extensions` may impact the application, and future upgrades could remove these from the VM.
   - If required, please reach out to your Solution Architect to explore options.
3. `Tags`: Optional, assign custom tags to the resources being created.

#### Review + Create

Ensure validation passed and click `Create`.

### Post Deployment

1. Connect to the IP Fabric VM via SSH with the username created during the deployment:

   ```shell
   # password authentication:
   ssh azureuser@ip_address

   # SSH public key authentication:
   ssh -i identity-file.pem azureuser@ip_address
   ```

2. Run [IPF CLI Config](02-ipf_cli_config.md):

    ```shell
    sudo ipf-cli-config -a
    ```

!!! important "Console Access"

    Please note that the Azure serial console might not be accessible for setting the `osadmin` password in [IPF CLI Config](02-ipf_cli_config.md).
    In that case, please contact the IP Fabric Support team or your Solution Architect.
    We can connect to the appliance via SSH with the default/factory `osadmin` password (that is overwritten during IPF CLI Config) and run IPF CLI Config manually.
