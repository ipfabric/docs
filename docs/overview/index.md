---
description: The IP Fabric network infrastructure management platform provides on-demand network discovery, advanced analytics, and detailed engineering visibility.
---

# IP Fabric Overview

The IP Fabric network infrastructure management platform provides on-demand network discovery, advanced analytics, and in-depth engineering visibility. The lightweight discovery capabilities (through SSH or Telnet) quickly detect the current network state, including detailed data for each address and port. A network model of gathered data reconstructs the topologies for each switching and routing protocol to enable cross-technology analysis of upstream and downstream relationships. Dependencies and dependents are calculated for each network element, allowing analysis to represent each aspect of the network in the context of productivity impact on the downstream hosts and network devices, while the immediate productivity impact of performance and capacity is calculated for each user and every element.

## Architecture

A distributed system of microservice components resides within the IP Fabric VM, all based around a multi-model database with a mathematical network model at its core. Operating system-level controls provide high availability, security, and log collection. The kernel-level bidirectional traffic shaper and application-level worker flow control mechanisms provide comprehensive traffic management and automatically respond to any signs of network congestion to ensure that only freely available bandwidth is utilized. The user interface is available on port `443` of the VM's IP address through any modern web browser and on any screen. Table output can be exported into CSV format for further processing, and selected reports are exportable into Word format.

![IP Fabric Architecture](../images/snapshot-management/overview_architecture.webp)

## Operational Requirements

### Browser Requirements

To access your IP Fabric GUI, we recommend using a browser version that is no older than one year. We support most major browsers, including:

- Google Chrome and Chromium-based browsers (e.g., Brave, Opera, Vivaldi, Edge)
- Mozilla Firefox and its maintained forks (e.g., LibreWolf)
- Safari

For a seamless experience, we recommend using a browser at Full HD (1920 × 1080 px) resolution or higher without custom scaling.

### Hardware Requirements

The IP Fabric platform runs on any x64 CPU with these instructions: `avx`, `popcnt`, `sse`, `sse2`, `sse4.1`, `sse4.2`, `sse4a`, and `ssse3`. The system runs with at least 8 parallel threads, but scheduling can handle operations down to a single thread if necessary. 

!!! info "Single Thread Performance Recommendation"

    We recommend using processors from Intel Cascade Lake or newer, or AMD Zen 2 or newer, as higher single-thread performance is crucial for a smoother user experience. In most cases, it is more beneficial than a high core count with lower per-thread performance.
    
IP Fabric utilizes around 8 GB of RAM when idle, and an additional 24 GB of RAM is required for collected network information. The base installation requires 150 GB of disk space.

The minimum requirements are:

| CPU | RAM   | Disk   |
| --- | ----- | ------ |
| 8   | 32 GB | 150 GB |

Since every network environment is different, we cannot recommend one general setting. Instead, we provide three examples of hardware requirements. Each example assumes 5 loaded snapshots, 1 snapshot being discovered, 100 unloaded snapshots on disk, and disk space overhead for IP Fabric and system logs.

For networks with medium complexity and many access points (>50%) or networks with basic complexity (simple dynamic routing, few or no VRFs, small sites):

| Devices | CPU |    RAM |     Disk |
| ------: | --: | -----: | -------: |
|     500 |   8 |  32 GB |   150 GB |
|   1 000 |  10 |  48 GB |   200 GB |
|   2 000 |  12 |  64 GB |   250 GB |
|   5 000 |  16 |  64 GB |   500 GB |
|  10 000 |  20 |  64 GB |   900 GB |
|  20 000 |  24 |  64 GB | 1 700 GB |

For networks with complex configurations (large routing tables, many VRFs, many STP domains, large MAC and ARP tables, etc.) and few or no access points (<20%):

| Devices | CPU |    RAM |     Disk |
| ------: | --: | -----: | -------: |
|     500 |   8 |  32 GB |   180 GB |
|   1 000 |  10 |  48 GB |   250 GB |
|   2 000 |  12 |  64 GB |   320 GB |
|   5 000 |  16 |  64 GB |   800 GB |
|  10 000 |  20 |  64 GB | 1 500 GB |
|  20 000 |  24 |  64 GB | 3 000 GB |

For managed service provider (MSP) networks:

| Devices | CPU |    RAM |     Disk |
| ------: | --: | -----: | -------: |
|     500 |   8 |  48 GB |   300 GB |
|   1 000 |  12 |  64 GB |   500 GB |
|   2 000 |  16 |  64 GB | 1 000 GB |
|   5 000 |  20 |  64 GB | 2 400 GB |

!!! warning

    If you plan to use FTP/SFTP IP Fabric backup, the recommended disk space must be doubled: 300 GB for 500 devices, 400 GB for 1 000 devices, and so on.

!!! info "Additional Resource Requirements"

    IP Fabric supports increasing both the number of discovery workers and the maximum allocation threshold per worker. Either change can significantly increase total RAM usage.

!!! note

    The recommended hardware resources may not allow for running the most demanding graph traversal functions. These functions may require a sizable memory pool to complete successfully.

#### Minimal IOPS Requirements

| Dedicated IOPS for Cloud Deployments |
| --- |
| 2500 |

##### Approximate `ipf-checker` Results for Minimal IOPS Requirements

| Test | IOPS   |
| --- | ----- |
| IO PSQL WAL Write | 750 |
| IO Data Write | 4400 |
| IO OLTP Mixed Read | 4480 |
| IO OLTP Mixed Write | 1920 |
| IO Fsync Test | 5280 |

However, we recommend using the Recommended hardware resources to ensure optimal performance and stability.

#### Recommended IOPS Requirements

| Dedicated IOPS for Cloud Deployments |
| --- |
| 5000 |

##### Approximate `ipf-checker` Results for Recommended IOPS Requirements

| Test | IOPS   |
| --- | ----- |
| IO PSQL WAL Write | 1500 |
| IO Data Write | 8800 |
| IO OLTP Mixed Read | 9600 |
| IO OLTP Mixed Write | 4000 |
| IO Fsync Test | 11200 |

!!! info "NVMe Storage Recommendation"

    For optimal performance, we recommend using directly attached Non-Volatile Memory express drives (NVMe) storage for virtual machine. Replacing traditional spinning disks NVMe will significantly improve the performance of database-intensive operations, such as [System Maintenance](../IP_Fabric_Settings/system/Backup_and_Maintenance/system_maintenance.md) and post-discovery calculations.

### Supported Virtualization Platforms

For deploying the IP Fabric appliance, we recommend using either VMware ESXi or vSphere. For more information, please see [Deploying IP Fabric Virtual Machine (VM) -- OVA Distribution Details](../platform_first_steps/01-deployment.md#ova-distribution-details).

It is also possible to run IP Fabric on any other virtualization platform using our qcow2/OVA images, but we can provide only limited support for those platforms.

### Network Connectivity Requirements

During snapshot operations, you can control the network bandwidth limit, which never exceeds the aggregate of set bandwidths in any direction, providing an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity to managed devices. A [jumphost server](../IP_Fabric_Settings/Discovery_and_Snapshots/Global_Configuration/jumphost.md#setting-up-jumphost) can also be set up and used. (A jumphost server requires an installation of SSH Python version 3.6+.)

Inbound flows:

| Source port (remote) | Destination port (local) | Protocol | Description                                                            |
| -------------------- | ------------------------ | -------- | ---------------------------------------------------------------------- |
| > 1024               | 443                      | TCP      | User Interface                                                         |
| 443                  | > 1024                   | TCP      | Network Infrastructure Interaction -- API; Support, Updates (Optional) |
| 22                   | > 1024                   | TCP      | Network Infrastructure Interaction -- SSH                              |
| 23                   | >1024                    | TCP      | Network Infrastructure Interaction -- Telnet                           |
|                      |                          | ICMP     | Network Infrastructure Interaction -- Traceroute                       |

Outbound flows:

| Source port (local) | Destination port (remote) | Protocol                     | Description                                                            |
| ------------------- | ------------------------- | ---------------------------- | ---------------------------------------------------------------------- |
| 443                 | >1024                     | TCP                          | User Interface                                                         |
| >1024               | 443                       | TCP                          | Network Infrastructure Interaction -- API; Support, Updates (Optional) |
| >1024               | 22                        | TCP                          | Network Infrastructure Interaction -- SSH                              |
| >1024               | 23                        | TCP                          | Network Infrastructure Interaction -- Telnet                           |
|                     |                           | ICMP                         | Network Infrastructure Interaction -- Traceroute                       |

Internet connectivity is used to check for product updates, perform upgrades, setup the Support VPN, send error reports, and submit support tickets.

### Network Access Credentials Requirements

#### Network Device Access

IP Fabric accesses network infrastructure devices via CLI (command-line interface) using SSH or Telnet. All device interactions are recorded on the platform, and only `read-only` or `operator` group privilege level 1 credentials are required.

Below are examples of commands used for Cisco IOS:

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

At the beginning, IP Fabric fingerprints the device using the `show version` command (or equivalent) to identify the vendor and system version. A `terminal length` command is optional but highly recommended, as it greatly improves the speed of the device interaction, reduces the load on the network and the device, and improves collection precision.

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

Turning off paging greatly improves the speed of discovery and allows a terminal pager command, making it highly recommended although not mandatory. The commands can be allowed through the central `TACACS` or `RADIUS` access control system, or they can be configured locally on a device. The following example adds the necessary commands to a privilege-1 user:

```
privilege show level 1 mode exec command interface
privilege show level 1 mode exec command arp
privilege show level 1 mode exec command route
privilege show level 1 mode exec command context
privilege cmd level 1 mode exec command terminal
```

A list of all commands used for CLI discovery can be found in the [feature/vendor matrix](https://matrix.ipfabric.io).

### Staging vs Production Deployment

IP Fabric is a complex solution with multiple moving parts. We thoroughly test every release before making it available to our customers. Testing comprises automated unit testing at the code level and automated tests run against various physical and virtual lab environments. These environments emulate complex networks with many devices from multiple vendors. Despite these efforts, issues can still arise after deploying a new version of IP Fabric to the customer's environment. For example, it is not feasible to replicate the entire network or a combination of particular device models.

Therefore, we suggest a 2-stage deployment of new IP Fabric releases for complex or critical implementations. The first stage is a _staging_ deployment, used to verify the functionality of the new release within the customer's environment.

!!! info

    You will need a valid license for the staging deployment. Please contact our sales team to check your eligibility for a complimentary license.
The second stage is the deployment to the production/live environment. The staging environment's sizing follows the suggestions mentioned above for a standard deployment. We don't provide special staging builds; these are just regular production builds, which are deployed separately to potentially avoid disrupting the day-to-day use of IP Fabric within the organization.

We suggest making the staging as close as possible to the final production environment. The staging environment should discover the same devices as the production (e.g., there is only a limited value if the staging environment "sees" only 500 network devices, while the whole network consists of thousands of devices). On the other hand, it is perfectly fine to provision the staging environment dynamically if your deployment environment allows it. Also, a typical "acceptance test" on the staging environment lasts only a couple of days to verify overall functionality.
