# Discovery

## IP Scope

### Including and excluding networks from discovery

By default, there are no limitations on discovery and all IP addresses
are allowed (i.e. *Include scope* is 0.0.0.0/0)

Discovery can be limited to one or more subnets using ***Settings →
Advanced → Discovery → IP Scope → **IP networks to include in discovery
and analysis.* Enter one or more subnets to limit the discovery process
to addresses from particular networks.

Specific parts of the network can be also excluded from discovery
using ***Settings → Advanced → Discovery →  IP Scope → **IP networks to
exclude from discovery and analysis.*

<div>

Priority

<div>

Exclude option takes precedence over include.

IP Scope settings are not applied to Vendor API - Meraki (everything is
downloaded and used in discovery)

</div>

</div>

Example:

*IP networks to include in discovery and analysis:* 10.0.0.0/8

*IP networks to exclude from discovery and analysis:* 10.24.0.0/16

*Result:* Only network 10.0.0.0/8 is scanned excluding 10.24.0.0/16
subnet.

  

## Scanner settings

The Scanner intelligently scans the parts of the network which are not
reachable using standard methods by testing the login (SSH/Telnet) to
each IP address from IP networks without any discovered device.

In other words, the Scanner takes each unique route for which there is
no CONNECTED router, and attempts to log in to each IP address by first
logging in to first unicast address of a subnet, then last address,
split the subnet in half and continue the process accordingly (excluding
the already attempted addresses).

For example, if after standard intelligent discovery, there is a network
10.0.0.0/24 in a routing table which does not belong to any of the
interfaces discovered, the scanner will attempt to login to 10.0.0.1,
then to 10.0.0.254, then to 10.0.0.126, then to 10.0.0.129, and so on,
until all of the addresses in the 10.0.0.0/24 network have been
attempted.  
Turn on the Scanner to increase the number of discovered devices.

Go to ***Settings → Advanced → Discovery → Scanner settings*** and turn
on the Use scanner in discovery switch.

Shortest mask of the network to scan - defines maximum size of the
networks in a routing table to be scanned. A smaller prefix length means
larger network and therefore a longer scan time. The minimum prefix
length size is /16.

  

The full routing table, including full BGP, may contain fewer than 700K
records in 2020. Downloading and processing such a large amount of data
is time-consuming and may not provide any relevant information about the
internal IP addressing scheme.  
In cases where we expect to discover a router with a full BGP table, we
can limit the total number of BGP routes stored in the database.

You can find the threshold configuration in the ***Settings → Advanced →
Discovery tab***.

The lower limit available is currently 10000 BGP routes. The IP Fabric
will read the full routing table but will filter BGP routes per the
threshold before storing them in the database.

<img src="attachments/102203417/102629526.png" class="image-left" loading="lazy" data-image-src="attachments/102203417/102629526.png" data-height="139" data-width="524" data-unresolved-comment-count="0" data-linked-resource-id="102629526" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-27 10_46_00-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203417" data-linked-resource-container-version="6" data-media-id="7be21bde-7cd9-4c94-8616-6b6d44813f6b" data-media-type="file" />

  

# DNS resolve

When this option is enabled, IP Fabric performs the IP address to a DNS
name translation. This feature creates many requests to configured DNS
servers during the Discovery process.

To enable this option go to ***Settings → Advanced → Discovery → DNS
resolve*** and click the on on/off switch.

<img src="attachments/102432837/1959395329.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/102432837/1959395329.png" data-height="867" data-width="1910" data-unresolved-comment-count="0" data-linked-resource-id="1959395329" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210204-095307.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102432837" data-linked-resource-container-version="6" data-media-id="16c45637-c95c-4c49-a8d2-6dc3458fdddc" data-media-type="file" width="340" />

  

## Saved configuration check

A saved configuration check is available when a user forgets to save a
changed configuration. IP Fabric compares the actual (running)
configuration with the saved (startup) configuration and the results can
be found in ***Technology → Management → Saved Config***
***Consistency*** table.  

3 statuses available:

1.  ***n/a*** - Saved configuration check is disabled

2.  ***saved*** - configuration is saved (there are no differences
    between running and startup configuration)

3.  ***changed*** - configuration is not saved

To enable/change status go to ***Settings → Advanced → Discovery → Saved
configuration check** *and switch ***Saved configuration check*** to
enable.

<img src="attachments/102662163/1959297025.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/102662163/1959297025.png" data-height="867" data-width="1910" data-unresolved-comment-count="0" data-linked-resource-id="1959297025" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210204-095157.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102662163" data-linked-resource-container-version="5" data-media-id="0f74e697-c0cc-47c2-ae42-de82dd6be7f1" data-media-type="file" width="340" />

  

## Traceroute settings

Traceroute is used when next hop is not available for SSH/telnet.
Devices discovered using traceroute are marked as *unmanaged* in IP
Fabric site diagrams.  More information about traceroute as a protocol
can be found on [Wikipedia](https://en.wikipedia.org/wiki/Traceroute).

For traceroute configuration go to  ***Settings → Advanced → Discovery
→ Traceroute settings.***

Trace scope - limits traceroute scope to the defined subnets. This
prevents scan networks outside an internal network.

***RFC6890*** - this button resets ***Trace scope*** setting to subnets
defined in this RFC.

***Protocol*** - the protocol used for traceroute can be selected from
the options of ICMP (MS Windows like), UDP (Linux like), and TCP.

***Port*** - in case of UDP and TCP, the destination port can be
specified.

  

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

  

  

  
