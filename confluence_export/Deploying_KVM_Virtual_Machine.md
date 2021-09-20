# Deploying KVM Virtual Machine

## **Deployment of IP Fabric Through Qcow2 Images**

The virtual appliance images are available
at <https://releases.ipfabric.io/ipfabric/#current>

<div>

<div>

Access to qcow2 images is restricted to registered customers only.
Please contact our [sales representative](mailto:sales@ipfabric.io) if
you are interested in a trial of IP Fabric.

</div>

</div>

## Deployment And Configuration Of The VM

<div>

<div>

Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to
connect to the network devices for data collection. It's important to
place a VM into the proper network segment to prevent high ACL or
firewall configuration overhead.

</div>

</div>

1.  Download qcow2 system disk to your KVM hypervisor

2.  Create a second qcow2 disk for data with [**size that corresponds to
    your network
    needs**](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78938115/Host+Hardware+Requirements)
    with the following command:

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
    qemu-img create -f qcow2 ipfabric-data.qcow2 10G (up to 920G for 20 000 devices)
    ```

    </div>

    </div>

3.  Deploy VM to your hypervisor through virt-install utility by issuing
    the following command (CPU and RAM size might need to be [adjusted
    according to your network
    size](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/78938115/Host+Hardware+Requirements)):

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
    virt-install --name=IP_Fabric --disk path=<path to the first, larger disk with OS>.qcow2 --disk path=<path to the second disk for data>.qcow2 --graphics spice --vcpu=4 --ram=16384 --network bridge=virbr0 --import
    ```

    </div>

    </div>

4.  This command will deploy a new virtual machine with IP_Fabric name,
    two qcow2 disks, 4 CPU cores, 16GB of RAM and will connect VM to the
    internet through virtbr0 interface (if your machine has a different
    bridge interface name or you want to connect it straight through the
    device network card to the internet you need to change --network
    parameter)

5.  This command can be altered as needed. For example, you can alter
    hardware resources according to the network environment size (check
    [requirements](http://ipfabric.atlassian.net/wiki/spaces/ND/pages/78938115/Host+Hardware+Requirements)).

6.  This command also starts up just created VM.

7.  Additionally, you can create and add a new empty virtual disk if
    necessary for local backups using the same command found at the step
    2 > [Increase disk space](Increase_disk_space)

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
    User Interface and Install
    License](Access_User_Interface_and_Install_License) and also for
    encrypting system backups.

9.  Optionally define organization parameters for the local SSL
    certificate.

10. After rebooting, the console login screen will display the assigned
    IP address of the system and provide a link to access the user
    interface.

<div>

<div>

Remember password from point 8. ! IP Fabric support engineers are able
to reset *osadmin *user passwords but **encrypted backups will be
lost**!

</div>

</div>

<div>

<div>

A trusted certificate can replace a self-signed SSL certificate using IP
Fabric web UI.

</div>

</div>
