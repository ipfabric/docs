# OUI

IP Fabric includes an OUI (organizationally unique identifier) MAC table
of network device manufacturers and uses it during the discovery process
whenever there is a network device discovered through the ARP table.

<img src="attachments/2704179211/2704375830.png" class="image-center" loading="lazy" data-image-src="attachments/2704179211/2704375830.png" data-height="965" data-width="1919" data-unresolved-comment-count="0" data-linked-resource-id="2704375830" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210728-133952.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2704179211" data-linked-resource-container-version="1" data-media-id="ad3e5f3e-b74f-453f-a564-da904de91ff0" data-media-type="file" />

This table can be found in the Settings → OUI menu.

It contains OUI (start of a MAC address of a device), vendor to whom
this OUI belongs and if it is enabled (can be used) during the discovery
process.

Custom OUIs can be added via Add OUI button.

All OUIs can be enabled or disabled for discovery through the Edit
button.

<div>

<div>

If there are network devices in your infrastructure that were found as
hosts and IP Fabric did not try to connect to them during the discovery,
please refer to this table and check if OUIs of those devices are
enabled for discovery.

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210728-133952.png](attachments/2704179211/2704375830.png)
(image/png)  

</div>
