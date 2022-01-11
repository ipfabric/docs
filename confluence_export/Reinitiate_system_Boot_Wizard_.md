# Reinitiate system 'Boot Wizard'

The Boot Wizard needs to be completed during the IP Fabric virtual
server deployment before the image installation begins. [The Boot Wizard
introduces the configuration of basic network
parameters](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/901808145/Deploying+VMware+OVA+virtual+machine#Complete-first-boot-wizard),
including time zone, NTP, IP address, DNS or Proxy settings.  
In case some of the initial parameters need to be modified after the
installation is complete, the IP Fabric administrator may reinitiate the
Boot Wizard by completing the following procedure.

## **1 - Login as ‘osadmin’ via SSH and re-enable Boot Wizard and reboot**

<img src="attachments/1430192140/1430519821.png" class="image-center" loading="lazy" data-image-src="attachments/1430192140/1430519821.png" data-height="352" data-width="722" data-unresolved-comment-count="0" data-linked-resource-id="1430519821" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200821-131333.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1430192140" data-linked-resource-container-version="3" data-media-id="c0a98798-cd87-4f43-a051-a74f862d7b0e" data-media-type="file" />

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
osadmin@demo4:~$ ipfabric-net-wizard

## Network configuration wizard has been enabled. Please reboot this VM.
## If you do not want to run network configuration wizard during next boot,
## run this command again with parameter "disable" (without quotes)

osadmin@demo4:~$ reboot
```

</div>

</div>

After rebooting the IP Fabric server the virtual machine will
automatically jump into the Boot Wizard.

## **2 - Access the VM hypervisor console and modify parameters in the Boot Wizard**

Follow the Boot Wizard steps to update the settings.

<https://ipfabric.atlassian.net/wiki/spaces/ND/pages/901808145/Deploying+VMware+OVA+virtual+machine#Complete-first-boot-wizard>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200821-131239.png](attachments/1430192140/1430355978.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200821-131333.png](attachments/1430192140/1430519821.png)
(image/png)  

</div>
