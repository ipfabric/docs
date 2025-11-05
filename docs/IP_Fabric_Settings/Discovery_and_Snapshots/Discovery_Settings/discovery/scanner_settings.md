---
description: After the intelligent discovery completes, the scanner may run to detect devices in distant networks learned from device routing tables. Distant networks are those not reachable by the standard discovery process. Only networks enabled for discovery through the include/exclude policy are eligible.

---

# Network-scanner selection & scanning behavior

After the intelligent discovery completes, the scanner may run to detect devices in distant networks learned from device routing tables. Distant networks are those not reachable by the standard discovery process. Only networks enabled for discovery through the include/exclude policy are eligible.

### How candidate networks are selected

Before scanning begins, the system builds a unique list of candidate networks. A network is qualified for scanning only if all of the following conditions are met:

1. Learned from a routing table
The network appears in the routing table of at least one device discovered during intelligent discovery.

2. Mask is not too broad
The network’s prefix length is equal to or longer than the configured minimum mask for scanning (i.e., it must not have a mask that is lower than the configured minimum).

3. Not directly connected
The network is not a directly connected network. We rely on ARP or equivalent sources - for example, Cisco ACI endpoint tables - to learn about devices on directly connected networks.

4. Has an IP next-hop
The route has an associated IP next-hop. This excludes summary routes, null routes, and any others that do not represent an IP-reachable distant network.

5. No discovered L3 interface in that network
There is no discovered L3 interface connected to that specific network (an exact network/mask match is required).
Example 1: While evaluating 10.10.10.0/24 as a candidate, if an L3 interface 10.10.10.1/24 was discovered, then 10.10.10.0/24 is excluded from scanning.
Example 2: While evaluating 10.10.10.0/24 as a candidate, if an L3 interface 10.10.10.1/25 was discovered, then 10.10.10.0/24 is kept for scanning.


### Uniqueness & VRF considerations
The system builds a final list of unique candidate networks so that each network appears only once.

VRFs are ignored during the selection process: networks in different VRFs are treated as identical. Likewise, the VRF of any discovered L3 interface is not considered when excluding networks.

### Scanning behavior
A qualified network is scanned until either all addresses are tried or a device in the scanned range is found. If a device is found, scanning is paused, and further processing waits until the device is fully discovered. Scanning for that subnet resumes only when the discovered device does not have an L3 or a directly connected route that exactly matches that subnet (an exact prefix and mask match is required to stop scanning).

Scanning proceeds in an alternating outward-in sequence: it probes the minimum usable IP, then the maximum usable IP, then the next lowest (minimum + 1), then the next highest (maximum -  1), and so on - i.e., [min, max, min + 1, max - 1, min + 2, max - 2, …].

Example: For `10.0.0.0/24`, the scanner checks `10.0.0.1`, then `10.0.0.254`, then `10.0.0.2`, then `10.0.0.253`, and continues in that pattern until all usable addresses have been probed.

For each IP that is trying to connect, the Scanner will use the credentials from the global settings to check if it can login with any of them.

If new networks are found in the next scanning iteration, those that have already been scanned in the previous iteration will be filtered out.

### How to use
Turn on the Scanner to increase the number of discovered devices.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Discovery
--> Scanner settings** and turn on the **Use scanner in discovery** toggle.

![Scanner settings](../../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings-discovery_scanner_settings.webp)

**Shortest mask of the network to scan** -- Defines the maximum size of the
networks in a routing table to be scanned. A smaller prefix length means a
larger network and therefore a longer scan time. The minimum prefix length size
is `/16`.
