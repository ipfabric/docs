---
description: The Addressing section provides information about every IP address on every managed network infrastructure device.
---

# Addressing

The Addressing section provides information about every IP address on every managed network infrastructure device.

- ARP Table: contains the ARP table from all discovered devices
- MAC Table: contains the MAC address table from all discovered devices
- Managed IP: list of all interfaces configured with an IP address from all discovered devices
- Managed duplicate IP: summary of the Managed IP table, where duplicate IP addresses are displayed
- NAT: contains NAT information from the supported devices
- IPv6 Neighbor discovery: list of the IPv6 neighbors

![main menu](addressing/menu.png)

## NAT

This section contains information about NAT policies and rules configured on a device. Currently, only IPv4 NAT is supported -- tab NAT44.

![NAT 44 table](addressing/nat44-table.png)

A graphical representation (as shown below) of the policy chain can be access by clicking on a "Policy Name" or a "Sequence number".

![natPostRouting chain on Forcepoint](addressing/forcepoint-natPostRouting.png)