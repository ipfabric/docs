---
description: Traceroute is used when next hop is not available for SSH/telnet. Devices discovered using traceroute are marked as unmanaged in IP Fabric site diagrams.
---

# Traceroute settings

Traceroute is used when next hop is not available for SSH/telnet.
Devices discovered using traceroute are marked as *unmanaged* in IP
Fabric site diagrams. More information about traceroute as a protocol
can be found on [Wikipedia](https://en.wikipedia.org/wiki/Traceroute).

For traceroute configuration, go to **Settings --> Discovery & Snapshots -->
Discovery Settings --> Discovery --> Traceroute settings**.

**Trace scope** -- limits traceroute scope to the defined subnets. This
prevents scanning networks outside an internal network.

**Use RFC 6890 scopes** -- this button resets the **Trace scope** setting to the subnets
defined in this RFC.

**Protocol** -- the protocol used for traceroute can be selected from
the options of ICMP (MS Windows like), UDP (Linux like), and TCP.

**Port** -- in the case of UDP and TCP, the destination port can be
specified.
