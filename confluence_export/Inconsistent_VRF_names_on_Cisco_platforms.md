# Inconsistent VRF names on Cisco platforms

For different Cisco families, the default VRF name may be inconsistent
in technology tables where the VRF name is present. There are the
following examples:

-   Cisco IOS - using ‘default’ string to identify main VRF

-   Cisco IOS-XE - using ‘empty’ string to identify main VRF

As per the following example, the excerpt from the
**technology/addressing/managed-ip table**, all records are for Cisco
devices, but different families are involved:

<img src="attachments/2859433985/2858778627.png" class="image-center" loading="lazy" data-image-src="attachments/2859433985/2858778627.png" data-height="283" data-width="1391" data-unresolved-comment-count="0" data-linked-resource-id="2858778627" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2022-01-13 at 12.44.01.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2859433985" data-linked-resource-container-version="1" data-media-id="b5b374dd-5135-4664-b981-a470df886568" data-media-type="file" />

## How the internal algorithms operate

Internally, IP Fabric understands the discrepancy and uses the special
labels to identify default VRF and to simulate the End-to-End path
correctly.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Screenshot 2022-01-13 at
12.44.01.png](attachments/2859433985/2858778627.png) (image/png)  

</div>
