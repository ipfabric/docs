---
description: This page describes known issues with Arista and how to fix them.
---

# Arista

## Discovery Task Stops When Encountering VLAN Not Assigned to Any Ports

**IP Fabric version:** all

**Known affected platforms:** Arista EOS, platform `7280sr3`, version `4.26.4M`

**Description:** The `show spanning-tree vlan detail` command stops when it
encounters a VLAN configured on the device but not assigned to any ports (except
for the default VLAN 1). This issue has been observed when running rapid-PVST
spanning tree but could potentially affect other versions.

!!! example

    ```commandline
    arista#show vlan
    VLAN  Name                             Status    Ports
    ----- -------------------------------- --------- -------------------------------
    1     default                          active
    2     BAD_VLAN                         active
    5     GOOD_VLAN                        active    Et1, Et2
    arista#sho span vlan det
    Spanning tree instance for vlan 1
     VL1 is executing the rapid-pvst Spanning Tree protocol
      Bridge Identifier has priority 4096, sysid 1, address 0000.0000.0000
      Configured hello time 2.000, max age 20, forward delay 15, transmit hold-count 6
      We are the root of the spanning tree


    No spanning tree information available for vlan 2
    ```

**Result:** Incomplete IP Fabric path lookups.

**Temporary fix:** Remove the unused VLAN from the configuration using the `no
vlan #` command.

**Permanent fix:** Unknown. Waiting for a response from Arista.

## Wrong End-to-End Path Lookups Due to EOS Bug Assigning Same STP ID to Different Interfaces

**IP Fabric version:** all

**Known affected platforms:** `Arista DCS-7504N` `4.28.6M-30705735.4286M`, `DCS-7280SR-48C6-F` `4.26.4M-25280047.4264M`

**Description:** Arista is assigning the same STP ID to different ports. For
spanning tree port IDs to serve their purpose, they need to be unique within an
L2 domain. Under certain circumstances (such as when a device's operational
requirements exceed its maximum scalability limits or due to a bug in the
device's operating system), a device may assign the same spanning tree port ID
to multiple ports within a single L2 domain. This situation was observed, for
example, on `Arista DCS-7504N` running a software image with internal build
version `4.28.6M-30705735.4286M`. In IP Fabric, this has resulted in incorrect
STP topology calculations and consequent issues in path lookup.

**Result:** Incomplete path lookups in IP Fabric.

**Temporary fix:** None.

**IP Fabric fix version:** To be specified.
