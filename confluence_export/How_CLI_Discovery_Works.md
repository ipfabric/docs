# How CLI Discovery Works

## Overview

Discovery creates a snapshot of the network, finding all active network
infrastructure devices and collecting the current state of network
protocols and technologies.

The process is controlled from the discovery tab of the web user
interface using the
<img src="attachments/79036476/81494018.png?width=24" loading="lazy" data-image-src="attachments/79036476/81494018.png" data-unresolved-comment-count="0" data-linked-resource-id="81494018" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image18.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="5adf1119-1626-4e2c-aacb-35bc8f6b7953" data-media-type="file" width="24" />
(start)
and <img src="attachments/79036476/81920006.png?width=24" loading="lazy" data-image-src="attachments/79036476/81920006.png" data-unresolved-comment-count="0" data-linked-resource-id="81920006" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image20.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="4a506b5d-4e0d-4a10-ad6d-9602de17a50c" data-media-type="file" width="24" />
(stop) buttons.

The timing of the network discovery snapshots can be automated in
**Settings → Advanced → Snapshots** to collect data in periodic
intervals or at a specific time. It is recommended to do a network
discovery at least once a day to record all network changes.

## Connectivity Report

A connection to every attempted address either succeeds or is recorded
in the Connectivity
Report<img src="attachments/79003743/1891467297.png" loading="lazy" data-image-src="attachments/79003743/1891467297.png" data-unresolved-comment-count="0" data-linked-resource-id="1891467297" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-1-18_16-50-38.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79003743" data-linked-resource-container-version="15" data-media-id="daabb2be-c51b-484f-b353-178deb74ef3b" data-media-type="file" /> which
details the reason for the connection failure. The most frequent reason
for failure is a timeout of the login attempt. A connectivity report can
be useful for troubleshooting failed credentials and other
unreachability reasons. An authentication failure messages denote an
unsuccessful login attempt and provide a description of how the device
has responded.

## Bandwidth Limit

Bandwidth limit controls the amount of traffic sent to and received from
the network infrastructure using bidirectional shaper and application
flow control mechanisms. The traffic rate never exceeds the configured
limit in either direction, allowing discovery and analysis processes to
be run during business hours, thereby not overloading the network
infrastructure devices any more than during standard operational
procedures.

To further distribute the network load and reduce the possibility of the
bottlenecks, the connection scheduler sorts connections attempts to
addresses that are farthest away. For example, in a list of addresses
10.10.10.1, 10.10.10.2, 10.20.10.1, 10.10.20.1, after attempting a
connection to 10.10.10.1, the next IP that will be scheduled is
10.20.10.1, because it shares only 11 bits with 10.10.10.1. This lowest
common mask rule enables statistically distributing the load without
prior topology knowledge.

The selected number of megabits per second also controls the number of
simultaneous connections. Each additional megabit adds 3 parallel
sessions.

## Discovery Process

Discovery is performed via a lightweight interaction with the network
infrastructure using CLI management protocols and ICMP probes. If the
initial seed is not entered, the discovery mechanism attempts to login
to the default gateway and to responders of ICMP probes returning from
the traceroute to the 10.0.0.0 network address.

<img src="attachments/79036476/81952774.png?width=476" class="image-left" loading="lazy" data-image-src="attachments/79036476/81952774.png" data-height="417" data-width="1563" data-unresolved-comment-count="0" data-linked-resource-id="81952774" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image22.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="1cbd7d2a-30fb-400c-b22a-9955450abcdb" data-media-type="file" width="476" />

After a successful login, discovery reads the network protocol state
tables and looks for known neighbours, such as routing protocol next
hops, ARP entries with MAC addresses of supported vendors, and CDP and
LLDP neighbour information. A connection attempt is made to each
potential network infrastructure device. Traceroute is attempted for
each unknown connected router from the discovered networks on the
routing table.

### This is how the discovery process continues after a successful connection to a network device:

1.  IP Fabric looks at LLDP/CDP and other neighbour protocols of the
    discovered device and tries to connect to those devices

2.  IP Fabric tries to connect to a next-hop device from the routing
    table

3.  IP Fabric use the device's ARP table to find hosts and other network
    devices it can connect to with the help of OUI table in IP Fabric
    (Settings → OUI)

4.  Traceroute is attempted for each unknown connected router from the
    discovered networks in the routing table.

Discovery then collects the detailed network state and information from
every discovered device for every supported running protocol. All
collected data is timestamped at the reading time and the timestamps are
used to calculate the rate of change for each element.

Discovery also computes network topology and cross-technology
dependencies by using network graph traversals of upstream and
downstream paths. A topology for each protocol is computed separately.

A managed network is considered to consist of every discovered device
under a coherent administrative domain, as restricted by access
credentials, and the full list of devices is available in the inventory.

The spanning-tree domain is a topology of contiguously connected
spanning-tree instances and signifies a Layer 2 failure domain in the
case of a cascading Layer 2 failure.

The routing domain is a topology of contiguously connected forwarding
hops and signifies a Layer 3 failure domain in the case of a cascading
Layer 3 failure.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2021-1-18_16-50-38.png](attachments/79003743/1891467297.png)
(image/png)  

</div>
