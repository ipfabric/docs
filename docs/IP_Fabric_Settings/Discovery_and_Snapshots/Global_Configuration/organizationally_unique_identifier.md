---
description: IP Fabric includes an OUI (Organizationally Unique Identifier) table of network device manufacturers and uses it during the discovery process whenever a network device is discovered through the ARP table or the CDP/LLDP information (if it contains the MAC address of the remote device).
---

# OUI (Organizationally Unique Identifier)

IP Fabric includes an OUI (Organizationally Unique Identifier) table of network
device manufacturers and uses it during the discovery process whenever a network
device is discovered through:

- the ARP table
- the CDP/LLDP information if it contains the MAC address of the remote device

![OUI table](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration_OUI.png)

This table can be found in **Settings --> Discovery & Snapshots --> Global
Configuration --> OUI**.

It contains an OUI (the start of a device's MAC address), the vendor to whom
this OUI belongs, and whether it is enabled (can be used) during the discovery
process.

Custom OUIs can be added with **+ Add OUI**.

All OUIs can be enabled or disabled for discovery with the **Edit** icon (in the
`Actions` column).

**Restore to Factory Settings** reverts the `Enabled for discovery` status of
all non-custom OUIs to default and removes any custom OUIs.

!!! info

    If there are network devices in your infrastructure that were found as hosts
    and IP Fabric did not try to connect to them during discovery, please refer
    to this table and check if OUIs of those devices are enabled for discovery.
