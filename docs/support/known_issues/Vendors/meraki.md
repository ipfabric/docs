---
description: This page describes known issues with Meraki and how to fix them.
---

# Meraki

**Known affected platforms:** all

**Description:** The Meraki API has limited functionality and doesn't provide
all the necessary data for the IP Fabric model.

These are the known limitations:

- Multiple Meraki devices can have the same public IP address.
- CDP/LLDP might be not linked between devices correctly, as the reported port
  ID doesn't allow it.
- CDP/LLDP timespan is 2 hours, so it might not show the actual state.
- ARP is missing; the MAC table is reconstructed from endpoints.
- DHCP/STATIC doesn't provide an IP mask.
- STP is missing.
- The routing table includes static routes only for firewalls.
- Path lookup is not working because forwarding tables are not provided.
- Can't add a Meraki device into a snapshot (refresh works).
- Limited snapshot -- Meraki tasks will always be downloaded.
- MX firewall uplink ports -- It is not possible to determine if traffic load
  balancing is enabled and/or which port is primary and which is backup.
