# Deploying the IP Fabric Virtual Machine (VM)

All virtual appliance images are available at  [https://releases.ipfabric.io/ipfabric/#current](https://releases.ipfabric.io/ipfabric/#current). Access is restricted to registered customers only. Please contact our [sales representative](mailto:sales@ipfabric.io) if you are interested in a trial of IP Fabric.

!!! important

    Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to connect to devices for data collection. It's important to place the VM in the proper network segment to prevent high ACL or firewall configuration overhead.

## Deploying on VMware OVA Virtual Machine

1.  Deploy OVA to your vSphere environment as described at [Deploy an OVF or OVA
    Template](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html).
2.  [Edit VM settings](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-4AB8C63C-61EA-4202-8158-D9903E04A0ED.html) and adjust according to your network size as described in the [operational requirements section](../overview/index.md#operational-requirements).
    1.  Change CPU count.
    2.  Change memory size.
    3.  [Add a new empty virtual disk](../../system_administration/increase_disk_space.md) if necessary.
3.  Power on VM and [complete Boot Wizard](#complete-first-time-boot-wizard).

## Deploying on Hyper-V Virtual Machine

Hyper-V image has been created using Hyper-V Configuration Version 8.0. Before deploying, please check if your Hyper-V server supports it.[Virtual Machine version on Windows or Windows Server](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/upgrade-virtual-machine-version-in-hyper-v-on-windows-or-windows-server)

1.  Download `ipfabric-*-hyperv.zip` from official source.
2.  Extract previously downloaded archive `ipfabric-*-hyperv.zip`.
3.  Import HyperV image to your hypervisor server. [Export and Import virtual machines (Microsoft docs)](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)
4.  During **Choose Import Type** part, check option **Copy the virtual machine(create a new unique ID)**:

    ![HyperV Import](hyperv_import.png)

5.  Wait until import process ends.
6.  Edit VM hardware settings and adjust according to the network environment size (check requirements in [operational requirements section](../overview/index.md#operational-requirements)). Right click on VM -- choose **Settings**:

    ![HyperV Settings](hyperv_settings.png)

    1.  Change CPU count

        ![HyperV Setting CPU count](hyperv_settings_cpu.png)

    2.  Change memory size

        ![HyperV Setting memory size](hyperv_settings_mem.png)

    3.  Extend system disk if necessary

        ![HyperV Setting disk size](hyperv_settings_disk.png)

    4.  [Add a new empty virtual disk](../../system_administration/increase_disk_space.md) if necessary.

    5.  Close VM Settings window

7.  Start VM.

## Deploying to Nutanix Virtual Machine

!!! note

    Nutanix image is based on Virtual Disks of VMware vSphere OVA image. As Nutanix officially supports import of VMware VM’s, below instructions are based on the same image as used at [VMware deploytment section](#deploying-on-vmware-ova-virtual-machine).

1.  Download `ipfabric-*-.OVA` file from official source.
2.  Extract previously downloaded OVA file using 7-zip or any similar software, structure of extracted files should look like below

    ![Unzip OVA](unzip_ova.png)

3.  Import `.vmdk` files to Nutanix hypervisor, following Nutanix official documentation -- [Nutanix import OVA](https://portal.nutanix.com/#page/kbs/details?targetId=kA03200000099TXCAY) and [Quick tip how to deploy a VM from OVF to AHV](https://next.nutanix.com/installation-configuration-23/quick-tip-how-to-deploy-a-vm-from-an-ovf-to-ahv-33613).

4.  Edit VM hardware settings and adjust according to the network environment size (check requirements in [operational requirements section](../overview/index.md#operational-requirements)).

    1.  Change CPU count
    2.  Change memory size
    3.  Extend system disk if necessary
    4.  [Add a new empty virtual disk](../../system_administration/increase_disk_space.md) if necessary.

5.  Start VM and check if system starts without any interrupts.

## Deploying on KVM Virtual Machine

1.  Download `qcow2` system disk to your KVM hypervisor.
2.  Create a second `qcow2` disk for data with size that corresponds to [your network needs](../overview/index.md#operational-requirements)) with the following command:

    ```shell
    qemu-img create -f qcow2 ipfabric-data.qcow2 10G # (up to 920G for 20 000 devices)
    ```

3.  Deploy VM to your hypervisor through virt-install utility by issuing the following command (chose CPU and RAM size according to size of your network):

    ```shell
    virt-install --name=IP_Fabric --disk path=<path to the first, larger disk with OS>.qcow2 --disk path=<path to the second disk for data>.qcow2 --graphics spice --vcpu=4 --ram=16384 --network bridge=virbr0 --import
    ```

4.  This command deploys a new virtual machine with IP_Fabric name, two `qcow2` disks, 4 CPU cores, 16GB of RAM and will connect VM to the internet through `virtbr0` interface (if your machine has a different bridge interface name or you want to connect it straight through the device network card to the internet you need to change `--network` parameter).

5.  This command also starts up just created VM.

6.  Additionally, you can create and add a new empty virtual disk if [needed](../../system_administration/increase_disk_space.md).

## Deploying to Amazon AWS EC2 instance

### Pre-requisites

Before you begin the deployment, please note the following:

1.  IP Fabric uses SSH, telnet and REST API over http/https in order to access network devices and controllers and carry out its discovery. Please ensure that the VPC subnet chosen for the deployment has the appropriate level of access and routing in order to complete the discovery.

2.  The IP Fabric AMI uses SSH for CLI console access, and HTTPS on ports `443` and `8443` for Web UI and system console access respectively. Security groups will need the appropriate configuration to allow inbound access to the AMI.

### Deployment Steps

1.  Login to the AWS console for the account provided to the IP Fabric support team.

2.  Select the region for the VPC where you want to deploy IP Fabric:

    ![AWS region selection](aws_region.png)

3.  From the **Services** menu at the top left, select **EC2**.

4.  Then choose **Instances** in the left hand menu, and hit the **Launch Instances** button on the right:

    ![AWS Launch instance](aws_launch_instance.png)

5.  Select **My AMIs**, then under **Ownership**, select **Shared with me**. The IP Fabric AMI should show up here. **Select** it.

    ![AWS Select IPF AMI](aws_select_ami.png)

6.  Choose the most appropriate instance type:

    | Devices | CPU | RAM    | HDD     | Example EC2 Instance Type |
    | ------- | --- | ------ | ------- | ------------------------- |
    | 500     | 4   | 16 GB  | 90 GB   | `c5.2xlarge`              |
    | 1 000   | 4   | 32 GB  | 100 GB  | `c5.4xlarge`              |
    | 2 000   | 8   | 32 GB  | 200 GB  | `c5.4xlarge`              |
    | 5 000   | 12  | 64 GB  | 300 GB  | `c5.9xlarge`              |
    | 10 000  | 16  | 128 GB | 550 GB  | `c5.18xlarge`             |
    | 20 000  | 18  | 256 GB | 1000 GB | `d3.8xlarge`              |

    Selecting an appropriate instance type is necessary to achieve a stable and reliable system! Please double-check if your Instance settings are proper for your environment size.

7.  Select **Configure Instance Details**, then ensure the correct VPC and subnet are selected for the IP Fabric instance. (Create a new VPC and subnet if required):

    ![AWS selecting VPC](aws_vpc.png)

8.  Then select **Add Storage**, add 80G to the additional amount from the table above for the root volume. For example, the instance `c5.4xlarge` should have 200G in total.

    ![AWS disk size](aws_disk.png)

9.  Select **Edit Security Groups** to make sure that IP Fabric will have the connectivity it requires to function:

    ![AWS security groups](aws_sec_groups.png)

10. Confirm the details with the [IP Fabric Connectivity Requirements](Network_Connectivity_Requirements). The security group rules should look something like:

    ![AWS security groups configuration](aws_sec_groups_cfg.png)

    !!! note

        Note that you can only select incoming rules at this point! By default the security group allows access to everything over any protocol and port: you will need to revisit once the instance has launched if you need to restrict access at source.

11. Click **Review and Launch**.

12. At this point, if you never used Debian in AWS before, subscription alert can appear. If requires, please follow instruction and open
    hyperlink in Error message: _In order to user this AWS Marketplace product…._

    ![AWS Subscription notification](aws_subscription_notification.png)

13. On new page, please click **Continue to Subscribe**

    ![AWS Subscription continue](aws_subscription_cont.png)

14. When done, please click **Launch** button once again.

15. Please confirm **Key pair** information and click **Launch Instance**.

    ![AWS Launch instance](aws_launch_instance.png)

16. Your Instance appears in the instances list, and it is started automatically by AWS:

    ![AWS instance](aws_instance_booted.png)

17. You can now [access the Web UI, install the license file](Access_User_Interface_and_Install_License) and login to the instance to run the Configuration Wizard.

18. There is a bug in the latest version and you will need to setup `traceroute` in the IPFabric in order to run Discovery. `traceroute` must be setup to -- `127.0.0.1/32`. This is going to be fixed in the future.

    ![AWS tranceroute](aws_traceroute.png)

---

## Complete (first-time) Boot Wizard

The *First Boot Wizard* starts when IP Fabric is run for the first time and configures system options. The wizard can also be re-run later from the service interface to modify basic system parameters.

1.  Assign hostname.
2.  Assign domain name.
3.  Choose IP address acquisition method.
4.  If a static method is used, configure IP address, netmask, default GW, and DNS servers.
5.  Configure NTP servers or just click OK to continue if not using NTP.
6.  Select time zone.
7.  Configure Internet Proxy if used.
8.  Set shell user password of `osadmin` user. The password is used to access the IP Fabric administrative interface and system shell (not for the GUI access, the GUI is accessible with the `admin` username by default, for more information, please, read: [Access User Interface and Install License](Access_User_Interface_and_Install_License) and also for encrypting system backups.
9.  Optionally define organization parameters for the local SSL certificate.
10. After rebooting, the console login screen will display the assigned IP address of the system and provide a link to access the user interface.

!!! warning

    Remember password from step 8! IP Fabric support engineers are able to reset `osadmin` user passwords but **encrypted backups will be lost**!

!!! info

    A trusted certificate can replace a self-signed SSL certificate using IP Fabric web UI.
