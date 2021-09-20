# Deploying Hyper-V Virtual Machine

## **Deploying IP Fabric Hyper-V Image**

The virtual appliance image is available
at <https://releases.ipfabric.io/ipfabric/#current>

<div>

<div>

Access to Hyper-V image is restricted to registered customers only.
Please contact our [sales representative](mailto:sales@ipfabric.io) if
you are interested in a trial of IP Fabric.

</div>

</div>

### Deploy And Configure VM

<div>

<div>

Hyper-V image has been created using Hyper-V Configuration Version 8.0.
Before deploying, please check if your Hyper-V server supports
it.[Virtual Machine version on Windows or Windows
Server](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/upgrade-virtual-machine-version-in-hyper-v-on-windows-or-windows-server)

</div>

</div>

<div>

<div>

Please bear in mind that IP Fabric uses CLI access (SSH or telnet) to
connect to devices for data collection. It's important to place the VM
in the proper network segment to prevent high ACL or firewall
configuration overhead.

</div>

</div>

1.  Download **'ipfabric-3-x-x-hyperv.zip'** from official source.

2.  Extract previously downloaded
    archive **'ipfabric-3-x-x-hyperv.zip'** 

3.  Import HyperV image to your hypervisor server. [Export and Import
    virtual machines (Microsoft
    docs)](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)

4.  During ***Choose Import Type*** part, check option ***Copy the
    virtual machine(create a new unique ID)***

    <img src="attachments/899285029/902103087?width=142" class="image-center" loading="lazy" data-image-src="attachments/899285029/902103087" data-height="533" data-width="704" data-unresolved-comment-count="0" data-linked-resource-id="902103087" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-6_13-11-2.png?version=1&amp;modificationDate=1580991063487&amp;cacheVersion=1&amp;api=v2&amp;height=250" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="899285029" data-linked-resource-container-version="6" data-media-id="6fb68c52-335b-4a49-ba53-a05db888dee4" data-media-type="file" width="142" />

5.  Wait until import process ends.

6.  Edit VM hardware settings and adjust according to the network
    environment size (check requirements in [Host Hardware
    Requirements](Host_Hardware_Requirements) ). Right click on VM -
    choose **Settings **

    <img src="attachments/899285029/902103080?width=142" class="image-center" loading="lazy" data-image-src="attachments/899285029/902103080" data-height="586" data-width="871" data-unresolved-comment-count="0" data-linked-resource-id="902103080" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-6_14-37-47.png?version=1&amp;modificationDate=1580996268890&amp;cacheVersion=1&amp;api=v2&amp;height=250" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="899285029" data-linked-resource-container-version="6" data-media-id="93c5df0c-83fa-4c82-be05-ea80838b83dc" data-media-type="file" width="142" />

    1.  Change CPU count

        <img src="attachments/899285029/899121199?width=136" class="image-center" loading="lazy" data-image-src="attachments/899285029/899121199" data-height="687" data-width="722" data-unresolved-comment-count="0" data-linked-resource-id="899121199" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-6_14-37-8.png?version=1&amp;modificationDate=1580996229761&amp;cacheVersion=1&amp;api=v2&amp;height=250" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="899285029" data-linked-resource-container-version="6" data-media-id="23c18fb1-7d6b-4330-8655-d32c4f6ff95b" data-media-type="file" width="136" />

    2.  Change memory size

        <img src="attachments/899285029/901546014?width=136" class="image-center" loading="lazy" data-image-src="attachments/899285029/901546014" data-height="687" data-width="722" data-unresolved-comment-count="0" data-linked-resource-id="901546014" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-6_14-39-26.png?version=1&amp;modificationDate=1580996367798&amp;cacheVersion=1&amp;api=v2&amp;height=250" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="899285029" data-linked-resource-container-version="6" data-media-id="7b635c38-e3ec-40f5-9462-cc164a725bf0" data-media-type="file" width="136" />

    3.  Extend system disk if necessary

        <img src="attachments/899285029/901546020?width=136" class="image-center" loading="lazy" data-image-src="attachments/899285029/901546020" data-height="843" data-width="719" data-unresolved-comment-count="0" data-linked-resource-id="901546020" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-6_17-37-31.png?version=1&amp;modificationDate=1581007052427&amp;cacheVersion=1&amp;api=v2&amp;height=250" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="899285029" data-linked-resource-container-version="6" data-media-id="bfba825b-f696-4399-a699-9464ed90ae2f" data-media-type="file" width="136" />

    4.  Add a new empty virtual disk if necesery > [Increase disk
        space](Increase_disk_space)

    5.  Close VM Settings window

7.  ***Start*** VM.

<div>

<div>

Proper hardware setup is necessary to achieve stable and reliable
system ! Please double-check if your VM settings are proper for your
environment size !

</div>

</div>

### Complete First Boot Wizard

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

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_14-37-47.png?version=1&modificationDate=1580996268890&cacheVersion=1&api=v2&height=250](attachments/899285029/902103080)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_13-11-2.png?version=1&modificationDate=1580991063487&cacheVersion=1&api=v2&height=250](attachments/899285029/901808182)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_13-11-2.png?version=1&modificationDate=1580991063487&cacheVersion=1&api=v2&height=250](attachments/899285029/902103087)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_14-37-8.png?version=1&modificationDate=1580996229761&cacheVersion=1&api=v2&height=250](attachments/899285029/899121199)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_14-39-26.png?version=1&modificationDate=1580996367798&cacheVersion=1&api=v2&height=250](attachments/899285029/901546014)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-6_17-37-31.png?version=1&modificationDate=1581007052427&cacheVersion=1&api=v2&height=250](attachments/899285029/901546020)
(image/png)  

</div>
