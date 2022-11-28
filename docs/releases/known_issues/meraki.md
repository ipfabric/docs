---
description: IP Fabric describes known affected issues for Meraki and how to fix them.
---

# Meraki

**Known Affected platforms**: All

**Description**: The Meraki API has limited functionality and doesn’t
provide all the necessary data for the IP Fabric model. The following are known limitations:

* Multiple Meraki devices can have the same public IP
* CDP/LLDP might be not linked between devices correctly as reported port ID doesn’t allow it
* CDP/LLDP timespan is 2h, so it might not show actual state
* ARP is missing, MAC table is reconstructed from endpoints
* DHCP/STATIC doesn’t provide IP mask
* STP is missing
* Routing table static routes only for Firewalls
* Pathlookup is not working because forwarding tables are not provided
* Can't add Meraki device into snapshot (refresh works)
* Limited snapshot - Meraki tasks will be always downloaded
* MX firewall uplink ports - not possible to determine if traffic load balancing is enabled and/or which port is primary and backup
