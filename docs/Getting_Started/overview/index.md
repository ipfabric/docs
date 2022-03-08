# IP Fabric Overview

The IP Fabric network infrastructure management platform provides on-demand network discovery, advanced analytics, and detailed engineering visibility. The lightweight discovery capabilities (through SSH or telnet) quickly detect the current network state, including detailed data for each address and port. A network model of gathered data reconstructs the topologies for each switching and routing protocol to enable a cross-technology analysis of upstream and downstream relationships. Dependencies and dependents are calculated for each network element, allowing analysis to represent each aspect of the network in the context of productivity impact on the downstream hosts and on network devices, while the immediate productivity impact of performance and capacity is calculated for each user and every element.

## Architecture

A distributed system of micro-service components resides within IP Fabric VM, all based around a multi-model database with a mathematical network model at its core. Operating system-level controls provide high availability, security and log collection. The kernel-level bidirectional traffic shaper and application-level worker flow control mechanisms provide comprehensive traffic management and automatically respond to any sign of network congestion to ensure that only freely available bandwidth is utilized. The user interface is available on port 443 of the VM's IP address through any modern web browser and on any screen. Table output can be exported into CSV format for further processing, and selected reports are exportable into Word format.

![IP Fabric Architecture](architecture.png)

## Operational Requirements

### Hardware Requirements

The IP Fabric platform runs on Intel Xeon Nehalem CPUs or later. The system runs in at least 4 parallel threads, but scheduling can handle operations even down to a single thread. IP Fabric uses less than 4GB of RAM when idle, and an additional 12GB of RAM is required for collected network information. The base installation requires 80GB of HDD space and an additional 50MB per device for the network.

Minimum requirements are:

| CPU | RAM   | HDD  |
| --- | ----- | ---- |
| 4C  | 16 GB | 90GB |

The following table represents the recommended hardware requirements for optimal performance of the platform based on the number of network infrastructure devices in the network.

| Devices | CPU | RAM    | HDD (OS + data)      |
| ------- | --- | ------ | -------------------- |
| 500     | 4   | 16 GB  | 90 GB (80G + 10G)    |
| 1 000   | 4   | 32 GB  | 100 GB (80G + 20G)   |
| 2 000   | 8   | 64 GB  | 200 GB (80G + 120G)  |
| 5 000   | 12  | 64 GB  | 300 GB (80G + 220G)  |
| 10 000  | 16  | 128 GB | 550 GB (80G + 470G)  |
| 20 000  | 18  | 256 GB | 1000 GB (80G + 920G) |

!!! info "Additional resources requirements"

    To make sure you have enough resources, please use the following formulas.

    Data **disk storage** requires 1MB per device per each snapshot (example: 1350 devices, plan is to keep up to 100 snapshots => 135 GB data storage).

    **Memory** requires 5MB of RAM per device per each **loaded** snapshot (example: 1200 devices, up to 100 snapshots but only 3 loaded at a time (1200 x 5 = 6000 x 3) => 18 GB RAM).

!!! note

    The recommended hardware resources may not allow running the most demanding graph traversal functions. These functions may require a sizable memory pool to complete successfully.

### Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth limit which never exceeds an aggregate of set bandwidths in any direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity to managed devices. [Jumphost server](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1384841217/Jumphost+settings) can also be set-up and used. (Jumphost server requires an installation of SSH Python (versions 2.4 to 3.7).)

Inbound flows:

| Source port (remote) | Destination port (local) | Protocol | Description                                                           |
| -------------------- | ------------------------ | -------- | --------------------------------------------------------------------- |
| > 1024               | 443                      | TCP      | User Interface                                                        |
| > 1024               | 8443                     | TCP      | Administrative Interface                                              |
| 443                  | > 1024                   | TCP      | Network Infrastructure Interaction - API; Support, Updates (Optional) |
| 22                   | > 1024                   | TCP      | Network Infrastructure Interaction - SSH                              |
| 23                   | >1024                    | TCP      | Network Infrastructure Interaction - Telnet                           |
|                      |                          | ICMP     | Network Infrastructure Interaction - Traceroute                       |

Outbound flows:

| Source port (local) | Destination port (remote) | Protocol                     | Description                                                                     |
| ------------------- | ------------------------- | ---------------------------- | ------------------------------------------------------------------------------- |
| 443                 | >1024                     | TCP                          | User Interface                                                                  |
| 8443                | >1024                     | TCP Administrative Interface |
| >1024               | 443                       | TCP                          | Network Infrastructure Interaction - API; Technical Support, Updates (Optional) |
| >1024               | 22                        | TCP                          | Network Infrastructure Interaction - SSH                                        |
| >1024               | 23                        | TCO                          | Network Infrastructure Interaction - Telnet                                     |
|                     |                           | ICMP                         | Network Infrastructure Interaction - Traceroute                                 |

Internet connectivity is used to check product updates, upgrades, setup support VPN, send error reports, and submit support tickets.

### Network Access Credentials Requirements

#### Network device access

IP Fabric accesses network-infrastructure devices via CLI (command-line interface) using SSH or TELNET protocols. All device interaction is accounted on the platform and only "read-only" or "operator" group privilege level 1 credentials are required.

The following list contains an example of commands used for Cisco IOS:

```
terminal length 0
show version
show inventory
show etherchannel summary
show interfaces [status|switchport]
show ip int [brief]
show ip vrf
show ip arp
show ip route
show ip cef
show ip access-list
show cdp neighbors detail
show lldp neighbors detail
show mac address-table
show spanning-tree [detail|mst|summary]
show standby [brief]
show vrrp [brief]
show vlan brief
```

In the beginning, IP Fabric fingerprints the device using the "show version" command (or equivalent) to identify a vendor and a system version. A "terminal length" command is optional but highly recommended, as it greatly improves the speed of the device interaction, reduces the load on the network and the device, and improves collection precision.

#### Additional device access

Since firewalls do not follow privilege levels, it may be necessary to
explicitly specify the commands allowed for each user. The following list specifies the exec-mode commands needed for firewall discovery.

```
show version
show interface
show route
show arp
show context
terminal pager 0
```

Turning off paging greatly improves the speed of the discovery and allows a terminal pager command, making it highly recommended although not mandatory. The commands can be allowed through the central `TACACS` or `RADIUS` access control system, or they can be configured locally on a device. The following example adds the necessary commands to a privilege-1 user:

```
privilege show level 1 mode exec command interface
privilege show level 1 mode exec command arp
privilege show level 1 mode exec command route
privilege show level 1 mode exec command context
privilege cmd level 1 mode exec command terminal
```

List of all commands used for CLI discovery can be found [on this page](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/80019486/Used+CLI+commands+for+Discovery) and in this [feature/vendor matrix](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/392003585).
