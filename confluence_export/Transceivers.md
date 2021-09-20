# Transceivers

# Transceivers Task

## Task execution control

Executing some commands to get transceiver related information may cause
issues on some devices. In the worst case, a device may crash and
reload. To prevent disruptions of your network, IPF uses a transceiver
task execution control system. The task is only executed on a device if

-   The transceiver task is enabled

-   IPF doesn’t classify the device to be affected by any known bug

### Note:

-   Transceiver task is disabled by default. A user can enable it in IPF
    settings (see the steps below).

-   Even if the transceiver task is enabled, IPF still prevents its
    execution on any device that is classified to be affected by any
    known bug. It is not possible to disable this feature now. See the
    list of known bugs and their corresponding [software and hardware
    versions](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1946583056/Show+Interface+Transceivers).

### Disclaimer

Although we try to prevent task execution on all software and hardware
versions that are known to be affected by any bug, we cannot guarantee
that all bugs are patched. For example, a device manufacturer may update
their list of devices affected by a certain bug in time, but IP Fabric
system may not fully reflect it.

## How To Find Transceivers In IP Fabric

Navigate to ***Technology → Interfaces → Transceivers***

<img src="attachments/1946583045/1946058783.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1946583045/1946058783.png" data-height="1300" data-width="2560" data-unresolved-comment-count="0" data-linked-resource-id="1946058783" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="transcievers_bily_1.PNG" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1946583045" data-linked-resource-container-version="6" data-media-id="d9a0069c-5dca-4dbf-bd42-101f8cb19c0b" data-media-type="file" width="340" />

## How To Enable/Disable Transceivers Task

This function is **enabled by default** for all vendors and product
families. This means that **this command is not executed on any
device**.

The function can be **Enabled/Disabled** in section ***Settings →
Advanced → Discovery task***.

<img src="attachments/1946583045/1946255385.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1946583045/1946255385.png" data-height="868" data-width="2560" data-unresolved-comment-count="0" data-linked-resource-id="1946255385" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="transcievers_bily_2.PNG" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1946583045" data-linked-resource-container-version="6" data-media-id="439d5a14-fdd5-494d-b940-dae8fb160c12" data-media-type="file" width="340" />

To **disable** this task, you need to **delete the default Transceivers
task** or **edit** this default task.

When **editing** this rule, you select by regex expression on which
devices this command **should not** be executed (so for example if you
don't want to run show interface transceivers command for all CISCO
devices, put cisco to the Vendor field. More specific device selection
can be done by Family, Platform, Model and Version fields). You can
simply test your Regex rules by *“Test rules“* button.

<img src="attachments/1946583045/1945829414.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1946583045/1945829414.png" data-height="637" data-width="2024" data-unresolved-comment-count="0" data-linked-resource-id="1945829414" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210201-161336.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1946583045" data-linked-resource-container-version="6" data-media-id="378b906a-d204-4bed-bde0-a30f22f20742" data-media-type="file" width="340" />

#### Related articles:

Known Cisco Bugs: [Show Interface
Transceivers](Show_Interface_Transceivers)

 

 

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210201-104327.png](attachments/1946583045/1936228425.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210201-104346.png](attachments/1946583045/1946222597.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210201-104355.png](attachments/1946583045/1945731095.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[transcievers_bily_1.PNG](attachments/1946583045/1946058783.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[transcievers_bily_2.PNG](attachments/1946583045/1946255385.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210201-161336.png](attachments/1946583045/1945829414.png)
(image/png)  

</div>
