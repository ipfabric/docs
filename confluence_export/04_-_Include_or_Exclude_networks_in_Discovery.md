# 04 - Include or Exclude networks in Discovery

## **Include or Exclude networks in Discovery**

By default, there are no limitations on discovery, and all IP addresses
are allowed (i.e. *Include scope* is 0.0.0.0/0)

Discovery can be limited to one or more subnets using ***Settings →
Advanced → Discovery → IP Scope → IP networks to include in
discovery** **and analysis**.* Enter one or more subnets to limit the
discovery process to addresses from particular networks.

Specific parts of the network can be also excluded from discovery
using ***Settings → Advanced → Discovery →  IP Scope → IP networks to
exclude from discovery and analysis**.*

<img src="attachments/2389966860/2390097955.png" class="image-center" loading="lazy" data-image-src="attachments/2389966860/2390097955.png" data-height="301" data-width="708" data-unresolved-comment-count="0" data-linked-resource-id="2390097955" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-124041.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2389966860" data-linked-resource-container-version="3" data-media-id="62d8f0b5-4ded-4738-b13f-b044ec8869a3" data-media-type="file" />

IP Scope settings are not applied to Vendor API (everything is
downloaded and used in discovery)

Exclude option takes precedence over include.

**Example**:

*IP networks to include in discovery and analysis: *10.0.0.0/8

*IP networks to exclude from discovery and analysis: *10.24.0.0/16

*Result:* Only network 10.0.0.0/8 is scanned excluding 10.24.0.0/16
subnet.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-124013.png](attachments/2389966860/2390097948.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-124041.png](attachments/2389966860/2390097955.png)
(image/png)  

</div>
