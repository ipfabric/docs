# Site Separation

# Site Separation

The site represents a separate collection of devices. A site can be a
branch, a factory, a production floor, a campus, or anything that might
represent a logical group for a user.

By default, the Site distribution is generated automatically after the
discovery process ends and is based on the rules described below. It can
also be triggered manually without the need for the whole discovery
process by going to ***Settings → Site separation*** **<u>(</u>In global
or Snapshot settings<u>)</u>**. 

## Routing and switching domain (default)

<div>

<div>

With this setting, you can manually edit the distribution of sites
later. Sites can be also renamed.

</div>

</div>

By default, the site is comprised of the topology of all contiguously
interconnected protocols, and the boundary of a site is formed by the
network protocol relation that is not under management using the
provided authentication credentials. The default separation is useful
for MPLS networks where directly connected routing infrastructure at the
site’s edge is not accessible. For situations where an inaccessible
routed firewall is used at the site (i.e. device under different
management team), an option “***Firewall at site***” can be turned on so
the infrastructure before and behind the firewall is not separated into
two different sites.

For networks that have direct routing connectivity between sites, such
as DMVPN or Leased Lines (usually over Serial or MFR interfaces), an
option to separate the site using ***tunnel*** and/or
***serial** the *interface should be selected.

For configuration go to ***Settings → Site separation***.

<img src="attachments/102203393/802750477.png?width=272" class="image-left" loading="lazy" data-image-src="attachments/102203393/802750477.png" data-height="242" data-width="891" data-unresolved-comment-count="0" data-linked-resource-id="802750477" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-56-3.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="15" data-media-id="0c5c7a43-bae9-4bc5-aa8e-ff64e834f2b7" data-media-type="file" width="272" />

Version 4.3 Example:

<img src="attachments/102203393/2887680008.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/102203393/2887680008.png" data-height="275" data-width="786" data-unresolved-comment-count="0" data-linked-resource-id="2887680008" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-132152.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="15" data-media-id="91e0e2af-4c7d-4295-b61f-54423b4b2b00" data-media-type="file" width="340" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-23 11_37_16-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/102203393/102432769.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-23 12_58_40-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/102203393/102367252.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-02-27 13_45_26-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/102203393/511410180.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-56-3.png](attachments/102203393/802750477.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-57-15.png](attachments/102203393/802652173.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-132152.png](attachments/102203393/2887680008.png)
(image/png)  

</div>
