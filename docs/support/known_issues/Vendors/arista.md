---
description: This page describes known issues with Arista and how to fix them.
---

# Arista

## Discovery task stops when it hits a VLAN that is not assigned to any ports
**IP Fabric Version:** All

**Known Affected platforms**: Arista EOS, Platform 7280sr3, Version 4.26.4M

**Description**: The command `show spanning-tree vlan detail` stops when it hits
a VLAN that is configured on the device but is not assigned to any ports (exception
is the default VLAN 1). This has been seen when running `rapid-pvst` spanning-tree
but could possibly affect other versions.

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

**Result**: Incomplete IP Fabric Path Lookups.

**Temporary Fix**: Remove the unused VLAN from the configuration using the `no vlan #` command.

**Permanent Fix**: Unknown. Waiting for a response from Arista.

## Wrong E2E Path Lookups due to bug in EOS which assigns the same STP ID to different interfaces

**IP Fabric Version:** All

**Known Affected platforms**: `Arista DCS-7504N`, `4.28.6M-30705735.4286M`, `DCS-7280SR-48C6-F`, `4.26.4M-25280047.4264M`

**Description**: Arista is assigning the same STP ID to different ports. To serve its purpose spanning tree port ID needs to be unique in a L2 domain. Under some circumstances, e.g. when device operational requirements break its maximum scalability limits or due to a bug in device operating system, a device may assign the same spanning tree port ID to more ports in a single L2 domain. This situation was observed e.g. on `Arista DCS-7504N` running software image with internal build version `4.28.6M-30705735.4286M`. In IP Fabric this has resulted in wrong STP topology calculation and consequent issues in path lookup.

**Result**: Incomplete IP Fabric Path Lookups.

**Temporary Fix**: None.

**IP Fabric fix Version**: To be specified.
