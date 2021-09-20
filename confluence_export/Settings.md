# Settings

# Authentication

Platform interacts with the network infrastructure devices by running
show commands through CLI using SSH or Telnet. Credentials added in the
Authentication section will be used by IP Fabric to access the CLI of
the network devices.

## Credential Selection Logic

If more credentials are specified, a top-down algorithm is used when
trying to login to a network device or the credentials priority can be
changed using drag and drop.  

<img src="attachments/1934983169/1934983181.jpg" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1934983181.jpg" data-height="474" data-width="737" data-unresolved-comment-count="0" data-linked-resource-id="1934983181" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="NIMPEE-login-diagram.jpg" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="a1cac42b-ca9b-4725-aebd-2c776ed12181" data-media-type="file" />

## Configure Network Infrastructure Access

Read-only (Privilege 1) credentials are sufficient for basic
functionality. Security sensitive operations and advanced functionality
might require higher privilege. See the [full list of used command in
the
documentation](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/80019486/Used+CLI+commands+for+Discovery).

When adding new credentials, you can limit the validity of the
credentials just for a part of your network using *Use in subnets*
and *Don't use in subnets* fields.

<img src="attachments/1934983169/1935310852.png?width=142" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1935310852.png" data-height="531" data-width="600" data-unresolved-comment-count="0" data-linked-resource-id="1935310852" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-29_10-58-46.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="319548af-0d3e-4faa-95e3-935203112205" data-media-type="file" width="142" />

Provided credentials can be used for configuration change tracking and
saved configuration consistency (i.e. they allow commands such as *show
run* and *show start*).

To use this credentials for configuration change tracking,
please check [*Use for configuration
management*](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79003762/Configuration)* *box.

## (Optional) Passwords for enable mode

Privileged credentials are generally only necessary for configuration
management. However, some platforms require privileged credentials to
access basic network state information, such as MST spanning-tree state
or 802.1X session information.

<img src="attachments/1934983169/1935245322.png?width=680" class="image-left" loading="lazy" data-image-src="attachments/1934983169/1935245322.png" data-height="272" data-width="1526" data-unresolved-comment-count="0" data-linked-resource-id="1935245322" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-29_12-19-25.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1934983169" data-linked-resource-container-version="3" data-media-id="ff9cd67c-09e6-40f2-b6a9-3e301f30cad8" data-media-type="file" width="680" />

  

# Discovery Seed

If you know a particular starting point for discovering the network, the
information can be entered at *Settings → Discovery Seed*. This option
does not exclude any networks from discovery.

The starting points can be management IP addresses of network devices or
network subnets. Existing inventory data can also be imported.

If no seed information is entered, the discovery will begin from the
current default gateway.

<img src="attachments/1935015957/1936261127.png" class="image-left" loading="lazy" data-image-src="attachments/1935015957/1936261127.png" data-height="168" data-width="453" data-unresolved-comment-count="0" data-linked-resource-id="1936261127" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-29_16-50-54.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1935015957" data-linked-resource-container-version="5" data-media-id="bfec7ad5-d8c9-4e81-8f61-cba93490c6c7" data-media-type="file" />

<div>

<div>

It is recommended to provide multiple IP addresses of core routers as a
starting point for discovery.

</div>

</div>

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

  

  
