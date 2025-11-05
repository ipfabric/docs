---
description: This section describes the IPv4 Managed IP Summary table
---

# IPv4 Managed IP Summary table

The IPv4 Managed IP Summary table provides a comprehensive overview of sites and their IPv4 subnets. For each subnet, it displays:

- Gateway information
- User count
- Total number of unique VLAN IDs
- Total number of unique VRF names

This table includes information about all subnets, regardless of devices they are configured on.

![IPv4 Managed IP Summary table heading](../../../images/technology/IP_Fabric_GUI-technology_tables-addressing_ipv4-managed-ip-summary-table-heading.png)

There is typically a one-to-one relationship between an L3 subnet and its corresponding VLAN ID and VRF name. The `#Vlans` and `#Vrfs` columns help verify this relationship by showing the count of unique VLAN IDs or VRF names associated with each subnet (per site).

However, different vendors use different names for their native VRF:

- Juniper uses `global`
- Cisco NX-OS uses `default`

Simply counting unique VRF names would result in many false positives. To address this, IPF recognizes various native VRF names as equivalent. This ensures accurate VRF counting, even for native VRFs.

For example, if a subnet connects to both a Juniper device (native VRF: `global`) and a Cisco NX-OS device (native VRF: `default`), IPF correctly counts this as one VRF, not two, despite the different native VRF names.

For the complete list of native VRF names, refer to the [Native VRF names section](../../tips/native_vrfs.md).
