# 02 - Enable mode passwords

## Enabled Mode Passwords

Those credentials are stored in ***Settings → Authentication***.

Privileged credentials are generally only necessary for configuration
management. However, some platforms require privileged credentials to
access basic network state information, such as MST spanning-tree state
or 802.1X session information.

<div>

<div>

If enable mode is configured with no password and is needed for
discovery, **any enabled password information needs to be set!**
Otherwise, IP Fabric **won’t even try the enable command**.

</div>

</div>

<img src="attachments/2390032390/2390327305.png" class="image-center" loading="lazy" data-image-src="attachments/2390032390/2390327305.png" data-height="256" data-width="800" data-unresolved-comment-count="0" data-linked-resource-id="2390327305" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-104245.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2390032390" data-linked-resource-container-version="4" data-media-id="3b8b9749-7051-4f6d-a251-7f9622713eba" data-media-type="file" />

<div>

<div>

Please **be careful** to configure enable password only for devices
(subnets) that **need the enable command to be included**.  
We encountered some problems with Cisco ISE. When an incorrect enable
password was entered, the user account was locked and IP Fabric wasn't
able to finish the discovery for those devices.

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210401-072201.png](attachments/2390032390/2390425605.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-104245.png](attachments/2390032390/2390327305.png)
(image/png)  

</div>
