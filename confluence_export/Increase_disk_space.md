# Increase disk space

## Increase disk space (system or backup)

Appliance disk space can be extended simply by extending existing
virtual disk or by adding new empty virtual hard drive to IP Fabric VM.
Same procedure can be also used to add new partition for local system
backup.

<div>

Backup Disk

<div>

Backup disk is not present by default! Please add new virtual disk to
enable local backups. (See option 2 for VMWare or Hyper-V)

</div>

</div>

<div>

Supported hypervisors

<div>

VMware vSphere and HyperV are the only supported platform.

For vShpere, please follow part 'Increase disk space for VMware' 

For Hyper-V, please follow part 'Increase disk space for Hyper-V'

</div>

</div>

## Increase disk space for VMware

#### Option 1 - extend existing virtual disk (for system and data)

1.  Open VMware vSphere web console.
2.  Right click on VM name and select *Edit Settings*.
3.  Select ***Hard disk*** and change its size.
4.  Click OK.
5.  Restart VM (using CLI or web UI).
6.  Disk space is automatically increased.

#### Option 2 - add new virtual disk (as additional backup disk)

1.  Open VMware vSphere web console.
2.  Right click on VM name and select *Edit Settings*.
3.  Click *Add New Device* → *Hard Disk*
4.  Select new size
5.  Specify *Location*:
    1.  for system disk expansion is recommended to select *Store with
        the virtual machine*
    2.  for backup volume is recommended to select different datastore
        ideally on a different physical storage
6.  Click OK  
    <img src="attachments/634060809/634191898.png?height=400" loading="lazy" data-image-src="attachments/634060809/634191898.png" data-unresolved-comment-count="0" data-linked-resource-id="634191898" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-06 16_31_48-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="aed917ec-3df4-42d5-9002-29a0084fd17d" data-media-type="file" height="400" />
7.  Launch Remote (Web) Console.
8.  [Reboot](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79036518/Service+Interfaces)
    (*Send Ctrl+Alt+Delete* function can be also used) or power on IP
    Fabric VM.
9.  During system boot *Disk space expansion* wizard appears.  
    <img src="attachments/634060809/634093592.png?height=250" loading="lazy" data-image-src="attachments/634060809/634093592.png" data-unresolved-comment-count="0" data-linked-resource-id="634093592" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-06 16_39_44-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="694f617d-5e41-4be8-9394-31d8e3d49c82" data-media-type="file" height="250" />
10. Select *Yes* to start disk space expansion.
11. Select which volume to extend:
    1.  System volume is used for all data except local backups.
    2.  Backup is used only for local backups.
12. Selected volume is extended.  
    <img src="attachments/634060809/633995283.png?height=250" loading="lazy" data-image-src="attachments/634060809/633995283.png" data-unresolved-comment-count="0" data-linked-resource-id="633995283" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-06 16_43_21-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="ba26fe14-131c-459e-9743-4646754ab3d3" data-media-type="file" height="250" />
13. Enter *OK*

## Increase disk space for Hyper-V

#### Option 1 - extend existing virtual disk (for system and data)

1.  Open Hyper-V Manager.
2.  Shutdown VM. *(when **Started**, HyperV won't let you change any
    hardware settings)*
3.  Right click on VM name and select ***Settings***.
4.  Select ***IDE Controller - Hard Drive -
    ipfabric-3-x-x-disk1.vhdx ***
5.  Click ***Edit*** - ***Choose Action*** - select option ***Expand***,
    click ***Next***.
6.  Set up required disk size and click ***Finish.***
7.  Start VM.
8.  Disk space is automatically increased.

#### Option 2 - add new virtual disk (as additional backup disk)

1.  Open HyperV Manager.
2.  Shutdown VM. *(when **Started**, HyperV won't let you change any
    hardware settings)*
3.  Right click on VM name an select ***Settings***.   
    <img src="attachments/634060809/869236752.png?height=250" loading="lazy" data-image-src="attachments/634060809/869236752.png" data-unresolved-comment-count="0" data-linked-resource-id="869236752" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-7_10-12-44.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="45ea4b05-3fa6-4a1b-a5ff-b93a6548b9f4" data-media-type="file" height="250" />
4.  Select IDE Controller 1 - Hard Drive - click Add   
    <img src="attachments/634060809/869203982.png?height=250" loading="lazy" data-image-src="attachments/634060809/869203982.png" data-unresolved-comment-count="0" data-linked-resource-id="869203982" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-7_10-17-21.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="e6b2e263-6d23-48fb-9d43-a820675b5b8c" data-media-type="file" height="250" />
5.  Select ***Virtual hard disk*** - click ***New*** - select ***Choose
    Disk Format*** - select ***VHDX*** - click ***Next***.  
    <img src="attachments/634060809/866713658.png?height=250" loading="lazy" data-image-src="attachments/634060809/866713658.png" data-unresolved-comment-count="0" data-linked-resource-id="866713658" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-7_10-19-2.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="9d599457-6b55-44e8-9bca-2a8f3cebe7b6" data-media-type="file" height="250" />
6.  Select ***Dynamically expanding*** - click ***Next***  
    <img src="attachments/634060809/866713663.png?height=250" loading="lazy" data-image-src="attachments/634060809/866713663.png" data-unresolved-comment-count="0" data-linked-resource-id="866713663" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-7_10-21-28.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="f90153d1-a01d-4610-8b98-8856e2e31af6" data-media-type="file" height="250" />
7.  Specify name and location of disk.
8.  ***Configure Disk*** - select ***Create a new blank virtual hard
    disk*** - change ***Size*** to required value - click
    ***Finish***.  
    <img src="attachments/634060809/869269526.png?height=250" loading="lazy" data-image-src="attachments/634060809/869269526.png" data-unresolved-comment-count="0" data-linked-resource-id="869269526" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-2-7_10-24-12.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="65ee302b-f71a-43eb-9c3c-d7922d5005bc" data-media-type="file" height="250" />
9.  Apply new disk on Settings window - close ***Settings***.
10. Start VM.
11. During system boot ***Disk space expansion*** wizard appears.  
    <img src="attachments/634060809/634093592.png?height=250" loading="lazy" data-image-src="attachments/634060809/634093592.png" data-unresolved-comment-count="0" data-linked-resource-id="634093592" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-06 16_39_44-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="694f617d-5e41-4be8-9394-31d8e3d49c82" data-media-type="file" height="250" />
12. Select ***Yes*** to start disk space expansion.
13. Select which volume to extend:
    1.  System volume is used for all data except local backups.
    2.  Backup is used only for local backups.
14. Selected volume is extended.  
    <img src="attachments/634060809/633995283.png?height=250" loading="lazy" data-image-src="attachments/634060809/633995283.png" data-unresolved-comment-count="0" data-linked-resource-id="633995283" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-06 16_43_21-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="634060809" data-linked-resource-container-version="6" data-media-id="ba26fe14-131c-459e-9743-4646754ab3d3" data-media-type="file" height="250" />
15. Enter ***OK***

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-06 16_31_48-Window.png](attachments/634060809/634191898.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-06 16_39_44-Window.png](attachments/634060809/634093592.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-06 16_43_21-Window.png](attachments/634060809/633995283.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-7_10-12-44.png](attachments/634060809/869236752.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-7_10-17-21.png](attachments/634060809/869203982.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-7_10-19-2.png](attachments/634060809/866713658.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-7_10-21-28.png](attachments/634060809/866713663.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-2-7_10-24-12.png](attachments/634060809/869269526.png)
(image/png)  

</div>
