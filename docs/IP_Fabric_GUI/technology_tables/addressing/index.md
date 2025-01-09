---
description: The Addressing section provides information about every IP address on every managed network infrastructure device.
---

# Addressing

The **Addressing** section provides information about every IP address on every managed network infrastructure device.

- **ARP Table:** Contains the ARP table from all discovered devices.
- **MAC Table:** Contains the MAC address table from all discovered devices.
- **Managed IP:** List of all interfaces configured with an IP address from all discovered devices.
- **Managed duplicate IP:** Summary of the Managed IP table, where duplicate IP addresses are displayed.
- **NAT:** Contains NAT information from the supported devices.
- **IPv6 Neighbor discovery:** List of the IPv6 neighbors.

![Addressing in Technology menu](menu.png)

## NAT

The **NAT** sub-section contains information about NAT policies and rules configured on a device. Currently, only IPv4 NAT is supported -- in the `NAT44` table.

![NAT44 table](nat44-table.png)

A graphical representation (as shown below) of the policy chain can be accessed by clicking a `Policy Name` or `Sequence` (rule sequence number).

![natPostRouting chain on Forcepoint](forcepoint-natPostRouting.png)

!!! Note

    NAT policies collection for Cisco Firepower 7000 & 8000 Series devices is not supported. To learn more about this limitation, see [Known Issues](../../../support/known_issues/Vendors/cisco/FMC_Firepower_NAT.md).
