# Site Separation

# Site Separation

The site represents a separate collection of devices. A site can be a
branch, a factory, a production floor, a campus, or anything that might
represent a logical group for a user.

By default, the Site distribution is generated automatically after the
discovery process ends and is based on the rules described below. It can
also be triggered manually without the need for the whole discovery
process by going to ***Settings → Advanced → Discovery → Site
separation*** **<u>(</u>In global or Snapshot settings<u>)</u>**. 

## Routing and switching domain

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

For configuration go to ***Settings → Advanced → Discovery → Site
separation***.

<img src="attachments/102203393/802750477.png?width=285" class="image-left" loading="lazy" data-image-src="attachments/102203393/802750477.png" data-height="242" data-width="891" data-unresolved-comment-count="0" data-linked-resource-id="802750477" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-56-3.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="12" data-media-id="0c5c7a43-bae9-4bc5-aa8e-ff64e834f2b7" data-media-type="file" width="285" />

## RegEx based on hostname

<div>

<div>

Site distribution cannot be changed manually when regex rules are used.
Sites cannot be renamed.

</div>

</div>

Alternatively, site separation can follow a specific Regular Expression
(RegEx) where separation will be performed based on portion of a device
hostname.

Go to ***Settings → Advanced → Discovery → Site separation*** and change
***Site boundary calculation*** to ***RegEx based on hostname***.

**Transform hostname** is used to normalize site names based on
hostname:

-   Upper case (default) - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" => result is that both devices in one site named
    "PRAGUE"

-   Lower case - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" => result is that both devices in one site named
    "prague"

-   No transformation - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" =>result is that each device has its own site named
    "PRAGUE" and "prague"

In the last step, introduce the ***Regular Expression***. Use [this
tool](https://regex101.com/) for validation and parentheses to extract
the site from the hostname correctly.

<div>

<div>

If you cannot cover the names of the sites with one regex, you can use
logical ***or***. Use **\|** (pipe) the character between RegEx rules.

</div>

</div>

The change in the regex is displayed as a live preview.

Once the regex is ready, click '***Site overview with this RegEx'*** and
observer results. ***Save*** (in the upper right corner).

<img src="attachments/102203393/802652173.png?width=394" class="image-left" loading="lazy" data-image-src="attachments/102203393/802652173.png" data-height="445" data-width="1350" data-unresolved-comment-count="0" data-linked-resource-id="802652173" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-57-15.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="12" data-media-id="627d2d24-beb4-4fa7-87dd-f187bb50ef7b" data-media-type="file" width="394" />

**RegEx example**:

We have several locations whose name is logically designed as one letter
with one to three numbers. From the point of view of a regex, such a
site can generally be expressed as
"**^(\[a-zA-Z\]\\d{1,3})**". Unfortunately, we have two other sites that
do not fit into this schema. These sites can be defined with their own
regex and this can be added to the original one using the logical
operator ***or***:

***^(\[a-zA-Z\]\\d{1,3}\|HWLAB\|static\\d{1})*** - 1st option OR 2nd
option OR 3rd option  

<div>

<div>

For devices that do not match the RegEx, IP Fabric automatically adds
those to the site based on protocol relation (CDP, LLDP, STP, L3) under
the condition that there's only a single relation to one particular
site. This feature is especially useful for Access Points and similar
devices, that do not follow the standard naming conventions and are
linked to one specific location.

</div>

</div>

## Manual Site Separation

<div>

<div>

With this setting, you can manually edit the distribution of sites.

</div>

</div>

The Manual Site Separation option is complementary to two previous
options and provides the users with full flexibility. It can be enabled
in **Inventory \> Sites \> Manual Separation** where any device's site
can be adjusted based on more attributes.

  

  

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

</div>
