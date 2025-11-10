---
description: This page describes known issues with Meraki and how to fix them.
---

# Meraki

**Known affected platforms:** all

**Description:** The Meraki API has limited functionality and doesn't provide
all the necessary data for the IP Fabric model.

These are the known limitations:

 - Multiple Meraki devices can share the same public IP address.
 - CDP/LLDP data has a timespan of 2 hours, so it may not always reflect the current state.
 - ARP and MAC tables are available only for switches.
 - Firewalls use the client table as the source of ARP-like data, which includes only records related to the LAN side of the firewall.
 - Path lookup has certain limitations — it works correctly through switches, but for firewalls and access points (APs), functionality depends on available data (limited ARP and no MAC table).
 - The device must have a statically configured management interface for the management mask and gateway to be available — DHCP provides only the IP address.
 - STP data is partially available for switches.
 - The LAN side of a firewall includes switch ports that do not support STP.
 - The routing table includes only static routes for firewalls.
 - A Meraki device cannot be added to a snapshot (only refresh operations are supported).
 - Limited snapshot functionality — Meraki tasks are always downloaded.
 - For MX firewall uplink ports, it is not possible to determine whether traffic load balancing is enabled, or which port is primary and which is backup.
