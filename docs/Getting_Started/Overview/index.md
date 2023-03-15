---
description: The IP Fabric network infrastructure management platform provides on-demand network discovery, advanced analytics, and detailed engineering visibility.
---

# IP Fabric Overview

The IP Fabric network infrastructure management platform provides on-demand network discovery, advanced analytics, and detailed engineering visibility. The lightweight discovery capabilities (through SSH or Telnet) quickly detect the current network state, including detailed data for each address and port. A network model of gathered data reconstructs the topologies for each switching and routing protocol to enable a cross-technology analysis of upstream and downstream relationships. Dependencies and dependents are calculated for each network element, allowing analysis to represent each aspect of the network in the context of productivity impact on the downstream hosts and on network devices, while the immediate productivity impact of performance and capacity is calculated for each user and every element.

## Architecture

A distributed system of micro-service components resides within the IP Fabric VM, all based around a multi-model database with a mathematical network model at its core. Operating system-level controls provide high availability, security and log collection. The kernel-level bidirectional traffic shaper and application-level worker flow control mechanisms provide comprehensive traffic management and automatically respond to any sign of network congestion to ensure that only freely available bandwidth is utilized. The user interface is available on port `443` of the VM's IP address through any modern web browser and on any screen. Table output can be exported into CSV format for further processing, and selected reports are exportable into Word format.

![IP Fabric Architecture](architecture.png)

## Operational Requirements

### Browser Requirements

To access your IP Fabric GUI, we recommend using a browser version that is at most 1 year old or newer. We support most major browsers. Below is a list of supported browsers:

- Google Chrome and Chromium-based browsers (e.g. Brave, Opera, Vivaldi, Edge)
- Mozilla Firefox and maintained forks (e.g. LibreWolf)
- Safari

For seamless experience, we recommend using a browser at Full HD (1920 × 1080 px) resolution or higher without custom scaling.

### Hardware Requirements

The IP Fabric platform runs on any x64 CPU with the following instructions: `avx,popcnt,sse,sse2,sse4.1,sse4.2,sse4a,ssse3`. The system runs in at least 4 parallel threads, but scheduling can handle operations even down to a single thread. IP Fabric uses less than 4 GB of RAM when idle, and an additional 12 GB of RAM is required for collected network information. The base installation requires 80 GB of HDD space and an additional 50 MB per device for the network.

The minimum requirements are:

| CPU | RAM   | HDD   |
| --- | ----- | ----- |
| 4   | 16 GB | 90 GB |

The following table represents the recommended hardware requirements for optimal performance of the platform based on the number of network infrastructure devices in the network.

| Devices | CPU |    RAM |      HDD |
| ------: | --: | -----: | -------: |
|     500 |   4 |  16 GB |    90 GB |
|   1 000 |   8 |  32 GB |   100 GB |
|   2 000 |  12 |  64 GB |   200 GB |
|   5 000 |  16 |  64 GB |   300 GB |
|  10 000 |  20 | 128 GB |   550 GB |
|  20 000 |  24 | 256 GB | 1 000 GB |

!!! warning

    If you are planning to use FTP/SFTP IP Fabric backup option, recommended disk space has to be doubled.

    For 500 devices 180 GB, for 1 000 devices 200 GB and so on.
    

!!! info "Additional resources requirements"

    To make sure you have enough resources, please use the following formulas:

    Data **disk storage** requires 1 MB per device per each snapshot (example: 1350 devices, plan is to keep up to 100 snapshots => 135 GB data storage).

    **Memory** requires 5 MB of RAM per device per each **loaded** snapshot (example: 1200 devices, up to 100 snapshots but only 3 loaded at a time (1200 x 5 = 6000 x 3) => 18 GB RAM).

!!! note

    The recommended hardware resources may not allow running the most demanding graph traversal functions. These functions may require a sizable memory pool to complete successfully.

### Supported Virtualization Platforms

We recommend using either VMware ESXi or vSphere platform to deploy the IP Fabric appliance.

Appliance is built on the top of Debian 11 which is officially supported since [ESXi 7.0](https://www.vmware.com/resources/compatibility/detail.php?deviceCategory=Software&productid=54075&vcl=true&supRel=396,448,508,518,578,589,615,617,649,650&testConfig=16). In order to get the best performance we strongly recommend using latest ESXi with [`pvscsi`](https://kb.vmware.com/s/article/1010398) storage driver and [`VMXNET 3`](https://kb.vmware.com/s/article/1001805) networking driver.

It might be possible to deploy OVAs on earlier versions of ESXi with some effort. As our OVAs use SHA256 cryptographic
hashing algorithm, we recommend deployment of IP Fabric via the vSphere Web Client or ESXi Embedded Host Client version
6.5 or newer because both support SHA256. The 6.0.0 and 5.5.0 versions of ESXi do not support SHA256 and require the OVA to be hashed with SHA1, see [Error: Invalid OVF checksum algorithm: SHA256](../../support/known_issues/IP_Fabric/error_messages/invalid_ovf_checksum.md).

It is also possible to run IP Fabric on any other virtualization platform using our qcow2/OVA images, but we can provide only limited support for those platforms.

### Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth limit which never exceeds an aggregate of set bandwidths in any direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity to managed devices. [Jumphost server](../../IP_Fabric_Settings/advanced/SSH_telnet.md#setting-up-jumphost) can also be set-up and used. (Jumphost server requires an installation of SSH Python version 3.6+.)

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

#### Network Device Access

IP Fabric accesses network-infrastructure devices via CLI (command-line interface) using SSH or Telnet. All device interaction is accounted on the platform and only `read-only` or `operator` group privilege level 1 credentials are required.

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

In the beginning, IP Fabric fingerprints the device using the `show version` command (or equivalent) to identify a vendor and a system version. A `terminal length` command is optional but highly recommended, as it greatly improves the speed of the device interaction, reduces the load on the network and the device, and improves collection precision.

#### Additional Device Access

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

List of all commands used for CLI discovery can be found in this [feature/vendor matrix](https://matrix.ipfabric.io).

### Staging vs Production Deployment

IP Fabric is a complex solution with multiple moving parts. We thoroughly test every release before it is made available to our customers. Testing comprises of the automated unit testing on the code level and automated tests run against various physical and virtual lab environments. These emulate complex networks with many devices from multiple vendors. Despite these efforts, issues can still arise after deploying a new version of IP Fabric to the customer's environment. For example, it is not feasible to replicate the entire network or a combination of particular device models.

Therefore, we suggest 2-stage deployment of the new IP Fabric releases for complex or critical implementations. The first stage is _staging_ deployment, used to verify the functionality of the new release within the customer's environment.

!!! info

    You will need a valid license for the staging deployment. Please contact our sales team to check eligibility for a free complimentary license.

The second stage is the deployment to the production / live environment. The staging environment's sizing follows the suggestions mentioned above for a standard deployment. We don't provide special staging builds. These are regular production builds, which are just deployed separately not to potentially disrupt the day-to-day use of IP Fabric within the organization.

We suggest that you make staging as close as possible to the final production environment. The staging environment should discover the same devices as the production (e.g., there is only a limited value if the staging environment "sees" only 500 network devices, while the whole network consists of thousands of devices). On the other hand, it is perfectly fine to provision the staging environment dynamically if your deployment environment allows it. Also, a typical "acceptance test" on the staging environment lasts only a couple of days to verify overall functionality.
