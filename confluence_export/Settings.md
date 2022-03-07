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
