# Arista

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

**Permanent Fix**: Unknown. Waiting for response from Arista.
