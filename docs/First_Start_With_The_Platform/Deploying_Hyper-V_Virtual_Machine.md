# Deploying Hyper-V Virtual Machine

## **Deploying IP Fabric Hyper-V Image**

!!! info Usefull info
    The virtual appliance image is available at [releases.ipfabric.io/ipfabric/#current](https://releases.ipfabric.io/ipfabric/#current)

    Access to Hyper-V image is restricted to registered customers only. Please contact our [sales representative](mailto:sales@ipfabric.io) if you are interested in a trial of IP Fabric.

### Deploy And Configure VM

Hyper-V image has been created using Hyper-V Configuration Version 8.0. Before deploying, please check if your Hyper-V server supports it.[Virtual Machine version on Windows or Windows Server](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/upgrade-virtual-machine-version-in-hyper-v-on-windows-or-windows-server)

Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to connect to devices for data collection. It's important to place the VM in the proper network segment to prevent high ACL or firewall configuration overhead.

1.  Download **'ipfabric-3-x-x-hyperv.zip'** from official source.

2.  Extract previously downloaded archive **'ipfabric-3-x-x-hyperv.zip'** 

3.  Import HyperV image to your hypervisor server. [Export and Import virtual machines (Microsoft docs)](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)

4.  During ***Choose Import Type*** part, check option ***Copy the virtual machine(create a new unique ID)***
    ![hyper v import type](./hyper_v_import_type.png)

5.  Wait until import process ends.

6.  Edit VM hardware settings and adjust according to the network environment size (check requirements in [Host Hardware Requirements](Host_Hardware_Requirements) ). Right click on VM - choose **Settings **
![hyper v settings](hyper_v_settings.png)

!!! info Image configuration
    1.  Change CPU count
    ![hyper v procesor selection](hyper_v_procesor_selection.png)
    2.  Change memory size
    ![hyper v ram](hyper_v_ram.png)
    3.  Extend system disk if necessary
    ![hyper v hard drive](hyper_v_hard_drive.png)
    4.  Add a new empty virtual disk if necesery > [Increase disk space](Increase_disk_space)
    5.  Close VM Settings window

7.  ***Start*** VM.

Proper hardware setup is necessary to achieve stable and reliable system ! Please double-check if your VM settings are proper for your environment size !


### Complete First Boot Wizard

The *First Boot Wizard* starts when IP Fabric is run for the first time and configures system options. The wizard can also be re-run later from the service interface to modify basic system parameters.

1.  Assign hostname.

2.  Assign domain name.

3.  Choose IP address acquisition method.

4.  If a static method is used, configure IP address, netmask, default GW, and DNS servers.

5.  Configure NTP servers or just click OK to continue if not using NTP.

6.  Select time zone.

7.  Configure Internet Proxy if used.

8.  Set shell user password of *osadmin *user. The password is used to access the IP Fabric administrative interface and system shell (not for the GUI access, the GUI is accessible with the '**admin**' username by default, for more information, please, read: [Access User Interface and Install License](Access_User_Interface_and_Install_License) and also for encrypting system backups.

9.  Optionally define organization parameters for the local SSL certificate.

10. After rebooting, the console login screen will display the assigned IP address of the system and provide a link to access the user interface.


Remember password from point 8. ! IP Fabric support engineers are able to reset *osadmin *user passwords but **encrypted backups will be lost**!


A trusted certificate can replace a self-signed SSL certificate using IP Fabric web UI.