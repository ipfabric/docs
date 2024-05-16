---
description: The Scanner intelligently scans the parts of the network which are not reachable using standard methods by testing the login (SSH/Telnet) to each IP address from IP networks without any discovered device.
---

# Scanner Settings

The Scanner intelligently scans the parts of the network which are not reachable
using standard methods by testing the login (SSH/Telnet) to each IP address from
IP networks without any discovered device.

In other words, the Scanner takes each unique route for which there is no
**CONNECTED** router and attempts to log in to each IP address by first logging
in to first unicast address of a subnet, then last address, splitting the subnet
in half and continuing the process accordingly (excluding the already attempted
addresses).

For example, if after standard intelligent discovery, there is a network
`10.0.0.0/24` in a routing table which does not belong to any of the discovered
interfaces, the scanner will attempt to log in to `10.0.0.1`, then to
`10.0.0.254`, then to `10.0.0.126`, then to `10.0.0.129`, and so on, until all
of the addresses in the `10.0.0.0/24` network have been attempted.  

Turn on the Scanner to increase the number of discovered devices.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Discovery
--> Scanner settings** and turn on the **Use scanner in discovery** toggle.

**Shortest mask of the network to scan** -- Defines the maximum size of the
networks in a routing table to be scanned. A smaller prefix length means a
larger network and therefore a longer scan time. The minimum prefix length size
is `/16`.
