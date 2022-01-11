# Discovery

# IP Scope

### Including and excluding networks from discovery

By default, there are no limitations on discovery and all IP addresses
are allowed (i.e. *Include scope* is 0.0.0.0/0)

Discovery can be limited to one or more subnets using ***Settings →
Advanced → Discovery → IP Scope → IP networks to include in discovery**
and analysis.* Enter one or more subnets to limit the discovery process
to addresses from particular networks.

Specific parts of the network can be also excluded from discovery
using ***Settings → Advanced → Discovery →  IP Scope → IP networks to
exclude from discovery** and analysis.*  

<div>

<div>

### Priority

Exclude option takes precedence over include.

IP Scope settings are not applied to Vendor API - Meraki (everything is
downloaded and used in discovery)

</div>

</div>

**Example**:

*IP networks to include in discovery and analysis:* 10.0.0.0/8

*IP networks to exclude from discovery and analysis:* 10.24.0.0/16

*Result:* Only network 10.0.0.0/8 is scanned excluding 10.24.0.0/16
subnet.

# Scanner settings

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
on the ***Use scanner in discovery*** switch.

***Shortest mask of the network to scan*** - defines maximum size of the
networks in a routing table to be scanned. A smaller prefix length means
larger network and therefore a longer scan time. The minimum prefix
length size is /16.

# Limit Download of BGP Routes

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

<img src="attachments/102203417/102629526.png" class="image-left" loading="lazy" data-image-src="attachments/102203417/102629526.png" data-height="139" data-width="524" data-unresolved-comment-count="0" data-linked-resource-id="102629526" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-27 10_46_00-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203417" data-linked-resource-container-version="7" data-media-id="7be21bde-7cd9-4c94-8616-6b6d44813f6b" data-media-type="file" />

# DNS resolve

When this option is enabled, IP Fabric performs the IP address to a DNS
name translation. This feature creates many requests to configured DNS
servers during the Discovery process.

To enable this option go to ***Settings → Advanced → Discovery → DNS
resolve*** and click the on on/off switch.

<img src="attachments/102432837/1959395329.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/102432837/1959395329.png" data-height="867" data-width="1910" data-unresolved-comment-count="0" data-linked-resource-id="1959395329" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210204-095307.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102432837" data-linked-resource-container-version="6" data-media-id="16c45637-c95c-4c49-a8d2-6dc3458fdddc" data-media-type="file" width="340" />

# Discovery Tasks Settings

The Discovery tasks feature was first introduced in **IP Fabric version
3.5.2** as a fast discovery enablement for large scale networks. When
enabled, it will use current ‘Discovery History’ database (in Management
\> Discovery History) only when creating a new snapshot **without
detecting any new network devices** during the discovery process.

If limit is disabled and discovery crawl through whole network is
performed, you can choose which options will be used for new devices
detection (ARP, CDP/LLDP, Routing Table records or a Traceroute).
Default is to use all available options.

<img src="attachments/1157136385/1157300225.png?width=374" class="image-left" loading="lazy" data-image-src="attachments/1157136385/1157300225.png" data-height="134" data-width="610" data-unresolved-comment-count="0" data-linked-resource-id="1157300225" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200519-145530.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1157136385" data-linked-resource-container-version="8" data-media-id="1575dc54-4acc-43d1-8b17-d243b1b1980c" data-media-type="file" width="374" />

The feature is especially helpful for large complex networks with
already defined device scope to avoid multiple repetitive failed
SSH/Telnet attempts that may slow down snapshot creation.

<div class="panel"
style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

When “Limit discovery” is enabled it also ignores all new devices from
the discovery seed and new include lists! If you need to discover new
device(s) with "Limit discovery" please add them manually to the last
(or any other) snapshot.

</div>

</div>

# Traceroute settings

Traceroute is used when next hop is not available for SSH/telnet.
Devices discovered using traceroute are marked as *unmanaged* in IP
Fabric site diagrams.  More information about traceroute as a protocol
can be found on [Wikipedia](https://en.wikipedia.org/wiki/Traceroute).

For traceroute configuration go to  ***Settings → Advanced → Discovery
→ Traceroute settings.***

***Trace scope ***- limits traceroute scope to the defined subnets. This
prevents scan networks outside an internal network.

***RFC6890*** - this button resets ***Trace scope*** setting to subnets
defined in this RFC.

***Protocol*** - the protocol used for traceroute can be selected from
the options of ICMP (MS Windows like), UDP (Linux like), and TCP.

***Port*** - in case of UDP and TCP, the destination port can be
specified.

  

  
