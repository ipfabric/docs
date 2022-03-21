# Inconsistent VRF names on Cisco platforms

For different Cisco families, the default VRF name may be inconsistent
in technology tables where the VRF name is present. There are the
following examples:

- Cisco IOS - using ‘default’ string to identify main VRF

- Cisco IOS-XE - using ‘empty’ string to identify main VRF

As per the following example, the excerpt from the
**technology/addressing/managed-ip table**, all records are for Cisco
devices, but different families are involved:

![Inconsistent VRF names](inconsistent_vrf_names.png)

## How the internal algorithms operate

Internally, IP Fabric understands the discrepancy and uses the special
labels to identify default VRF and to simulate the End-to-End path
correctly.
