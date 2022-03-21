# Deploying VMware OVA Virtual Machine

## **Deploying IP Fabric OVA Image**

The virtual appliance image is available
at <https://releases.ipfabric.io/ipfabric/#current>

!!! note
    Access to OVA image is restricted to registered customers only. Please
    contact our [sales representative](mailto:sales@ipfabric.io) if you are
    interested in a trial of IP Fabric.

## Deploy And Configure VM

Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to
connect to devices for data collection. It's important to place the VM
in the proper network segment to prevent high ACL or firewall
configuration overhead.


1.  Deploy OVA to your vSphere environment. [Deploy an OVF or OVA
    Template](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html)

2.  Edit VM settings and adjust according to the network environment
    size (check [requirements](http://ipfabric.atlassian.net/wiki/spaces/ND/pages/78938115/Host+Hardware+Requirements)). [Configuring Virtual Machine
    Hardware](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-4AB8C63C-61EA-4202-8158-D9903E04A0ED.html)

    a.  Change CPU count.

    b.  Change memory size.

    c.  Add a new empty virtual disk if necessary > [Increase disk
        space](Increase_disk_space)

3.  Power on VM.

## Complete First Boot Wizard

The *First Boot Wizard* starts when IP Fabric is run for the first time
and configures system options. The wizard can also be re-run later from
the service interface to modify basic system parameters.

1.  Assign hostname.

2.  Assign domain name.

3.  Choose IP address acquisition method.

4.  If a static method is used, configure IP address, netmask, default
    GW, and DNS servers.

5.  Configure NTP servers or just click OK to continue if not using NTP.

6.  Select time zone.

7.  Configure Internet Proxy if used.

8.  Set shell user password of *osadmin *user. The password is used to
    access the IP Fabric administrative interface and system shell (not
    for the GUI access, the GUI is accessible with the '**admin**'
    username by default, for more information, please, read: [Access
    User Interface and Install License](Access_User_Interface_and_Install_License) and also for
    encrypting system backups.

9.  Optionally define organization parameters for the local SSL
    certificate.

10. After rebooting, the console login screen will display the assigned
    IP address of the system and provide a link to access the user
    interface.

!!! danger 
    Remember password from point 8. ! IP Fabric support engineers are able
    to reset *osadmin* user passwords but **encrypted backups will be lost**!

!!! note
    A trusted certificate can replace a self-signed SSL certificate using IP
    Fabric web UI.
