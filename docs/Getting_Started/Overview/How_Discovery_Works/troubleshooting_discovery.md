---
description: Documentation on most commonly seen discovery issues and how to resolve them.
---

# Troubleshooting Discovery

## Discovery Settings

This section describes the Global Settings. You can also make adjustments to specific snapshots.
Changes made to the Global Settings do not apply to previously-run snapshots. Here are
two methods for testing snapshot settings:

1. Make your changes in the snapshot **Settings** and then try to
  **Add Devices** (or `Rediscover timed out devices`). If these changes fixed your
  issue, then apply them globally.

  ![Add devices](troubleshooting/add_devices.png)

2. Make your changes globally and then run a new snapshot. In **Settings -->
   Discovery & Snapshots --> Discovery Settings --> Discovery --> IP Scope -->
   IP networks to include in discovery and analysis**, you can also filter the
   allowed discovery scope to a subset of `/32` addresses to lower the discovery
   time. In the example below, we allow only one subnet to be part of the
   discovery:

  ![Limit discovery to subnet](troubleshooting/limit_discovery_to_subnet.png)

### Discovery Seeds

Location: **Settings --> Discovery & Snapshots --> Discovery Settings -->
Discovery Seeds**

![Discovery Seeds](troubleshooting/discovery_seeds.png)

These are **user-defined** IP addresses that IP Fabric will try to connect to and
discover. If a device is successfully discovered, it will check the settings in
the **Discovery tasks settings** to see what technologies to use to discover
neighbors.

If you have remote locations possibly accessed through a WAN that is not owned by you,
this would be the place to put the IP addresses of some of your devices, so IP
Fabric can discover and crawl those.

!!! important

    Adding new devices here will only discover them if `Limit discovery to
    already discovered devices` is not enabled in the **Discovery tasks
    settings**.

### Discovery History

Location: **Management --> Discovery History**

![Discovery History](troubleshooting/discovery_history.png)

The **Discovery History** table is also used by IP Fabric as seed addresses.
Once a device is discovered in a snapshot, it will be placed in this table for
use in other snapshots.

- The **username last successfully used** for a device will be recorded here and be
  the first one tried in a future snapshot. If unsuccessful, IP Fabric will check
  the list in **Settings --> Discovery & Snapshots --> Discovery Settings -->
  Device Credentials** and go back through the decision tree. This
  may cause the next snapshot to take longer due to authentication failures, but
  once this table is updated with the new username, the discovery time will
  return to normal.

- If you have removed devices from your network, IP Fabric will still try to
  connect to them because the IP addresses are defined as seeds in this
  Discovery History table. To speed up discovery, you could delete stale records.
  You can also filter on **Last discovery time** and delete records older than X
  months.

### IP Scope

Location: **Settings --> Discovery & Snapshots --> Discovery Settings -->
Discovery --> IP Scope**

![IP Scope](troubleshooting/ip_scope.png)

**IP Scope** tells IP Fabric which networks to include or exclude in the discovery
process. The default is set to include everything (`0.0.0.0/0`). When IP Fabric
discovers a neighbor in this network, it will try to log in to and discover it. If
the IP address is not in the **include list**, or is in the **exclude list**, then IP
Fabric will not try to connect to and discover the device.

The **exclude list** is a great way to exclude networks managed by a different
department or perhaps vendors or devices that IP Fabric does not currently support.
For instance, a customer had discovery hanging due to it trying to log in to a
terminal server which IP Fabric could not understand; once added to the exclude list,
the discovery completed successfully.

!!! important

    Do not confuse the include list with the seed list. The include list will only
    try to discover an IP if it is found through the Discovery task or the
    IP is in the seeds. Also note IP Fabric does not do any ICMP pings to find
    hosts, so having a `/16` here will not send massive amounts of pings.

### Discovery tasks settings

Location: **Settings --> Discovery & Snapshots --> Discovery Settings -->
Discovery --> Discovery tasks settings**

![Discovery tasks settings](troubleshooting/discovery_tasks_settings.png)

**Discovery tasks settings** is where the magic happens for automated discovery of
new devices on your network.

- If you are not finding new devices in your snapshot, check if
  `Limit discovery to already discovered devices` is not enabled. If this is
  enabled, then only devices in the **Discovery History**
  table will be added to the snapshot, but not new devices (even if those
  devices are manually added to the global discovery seeds in **Settings -->
  Discovery & Snapshots --> Discovery Settings --> Discovery Seeds**).

  If you want to limit to only discovered devices but want to add new
  devices, this is still possible by going to **Discovery Snapshot** and
  manually adding devices into a snapshot. Those will then be added to
  the **Discovery History** table and picked up in future snapshots.

- **xDP (neighbors)** signifies using CDP or LLDP information to discover devices
  in your network.

- **ARP** uses the ARP and MAC address OUI information to find devices. If the OUI
  is set to `Enabled for discovery` in the table in **Settings --> Discovery &
  Snapshots --> Global Configuration --> OUI**, then IP Fabric will attempt to
  connect to and discover the device.

- **Routing Table** will try to connect to next-hop devices.

- **Trace** signifies using traceroute to RFC1918 addresses to help discover your
  internal network. This is helpful for the VM as IP Fabric might not be able to log
  in to the default gateway (vRouter), but using traceroute it can find some other
  physical devices in the network to use as starting points.

### Advanced CLI

Location: **Settings --> Discovery & Snapshots --> Discovery Settings -->
Advanced CLI**

![Advanced CLI](troubleshooting/advanced_cli.png)

See [Advanced CLI](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/advanced_cli.md) for
the explanation of these settings.

### Vendors API

Location: **Settings --> Discovery & Snapshots --> Discovery Settings -->
Vendors API**

![Vendors API](troubleshooting/vendors_api.png)

See [Vendors API](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/index.md) as
each vendor has different requirements.

### Device Credentials

Location: **Settings --> Discovery & Snapshots --> Discovery Settings --> Device
Credentials**

![Device Credentials](troubleshooting/device_credentials.png)

**Authentication** is where you define the username and password IP Fabric uses to
connect to a physical device (devices discovered through the API are managed
through **Advanced --> Vendors API**). Ensure that you have a username configured
for all scopes of the network you wish to discover or set to the default
of `0.0.0.0/0`.

!!! tip

    If you are having issues with Configuration Backup not pulling data, ensure
    that you have `Use for configuration management` set on the proper usernames.

Further information can be located
at [Device Credentials](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/device_credentials.md).

## Troubleshooting Missing Devices

There can be numerous reasons why IP Fabric did not discover a
device from Day 0: incorrectly configured devices, AAA outage, insufficient
authorization privileges, just to name a few. First, we will take a look at some tables
to help you find these and then show how to use the **Connectivity Report** to
debug them.

### Vendor Specific Troubleshooting

You may notice that some devices of a certain vendor are not being discovered.
Please read through the [Known Issues](../../../releases/index.md) to ensure a bug has
not been already raised or a fix suggested. For instance, some firewall vendors
require elevated or `admin` profiles in order to pull all data.

### Technology Tables

#### CDP/LLDP --> Unmanaged neighbors

![Unmanaged Neighbors](troubleshooting/unmanaged_neighbors.png)

This is the best table to start as not only you see the local host and
interface names, but also the remote hostname, interface name, and remote IP.
Since devices can connect to multiple other devices, there can be duplicate
remote hostnames in this list.

You are able to export this view to CSV and then remove duplicate hostnames to
get a unique list of devices. For instance in this demo, I see a total of 59
unmanaged neighbors, but only 40 unique remote hostnames.

#### Interfaces --> Connectivity matrix --> Unmanaged Neighbors Detail

![Unmanaged Neighbors Detail](troubleshooting/unmanaged_neighbors_detail.png)

This table shows you unmanaged neighbors based on many protocols and has a built-in
default intent check for you.

- <span style="color:red;">RED</span>: Provides a list of unmanaged CDP/LLDP
  neighbors
  (`cdp|lldp|mndp`). This does not provide you with the remote hostname which is
  why it is recommended to look at this table second.

- <span style="color: orange;">AMBER</span>: Is a list of unmanaged Interior
  Gateway Protocols
  (`eigrp|ospf|rip|isis|pim|vxlan|cef`). It is specified as such because if you
  have a neighbor adjacency with an iGP, it is assumed it is under the control of
  your network.

  !!! tip

      Check this table for help with locating rogue devices in your network.

- <span style="color: blue;">BLUE</span>: Is the default rule if the protocol
  does not match any other regex.

- <span style="color: green;">GREEN</span>: Is defined for the Exterior Gateway
  Protocol BGP.

### Auditing using an External Network Management System

Perhaps you would like to audit IP Fabric with an NMS (or vice versa). This can
be done as all the tables can return the data in CSV format via the UI or JSON
using the API. This would perhaps help you find other missing devices IP Fabric
could not discover.

!!! tip

    Don't forget to audit your NMS or alarming system's inventory with what IP
    Fabric discovered on the network. Many customers have found devices that
    were not being monitored.

!!! Note "Note on Management IP"

    In IP Fabric `4.3.5` or lower, the UI in many places has a `Management IP` column;
    since `4.4`, this has been renamed to `Login IP` to avoid confusion and to match
    the API column name `loginIp`.

    Since IP Fabric is an automated discovery process, it will try to log
    in to any IP address found during the discovery tasks processes. This
    value could be a loopback, management, physical, or virtual interface.
    Auditing your external NMS will need extra care as in many cases, the
    IPs will not match.

    One solution is to export your NMS inventory to Excel and the
    **Technology --> Addressing --> Managed IP** table to CSV and then perform
    vlookups between the two datasets. Since the **Managed IP** contains all
    the IP addresses found on devices, the NMS data should find a match.

    Another option is to use the device's Serial Number. Serial numbers are
    not always unique and there is a chance of overlap, so please take this
    into account.

!!! Note "Note on Serial Numbers"

    IP Fabric records two serial numbers for a device. The column named
    `Serial Number` is the actual hardware serial number of the device which
    is why it is labeled as `snHw` in the API.

    The column named `Unique serial number` is an IP Fabric-unique identifier
    and primary key for the device. This column is labeled as `sn` in the API, so it is
    easy to confuse the two if you were not aware. The main occasion there are
    differences between the two is seen in firewalls with virtual contexts,
    vdoms, etc.

### Connectivity Report

![Connectivity Report button](troubleshooting/connectivity_report_button.png)
![Discovery Connectivity Report](troubleshooting/discovery_connectivity_report.png)

The **Connectivity Report** is a per-snapshot report stating successes or
errors for IP addresses that IP Fabric tried to discover. Once you have a list of
IP addresses from the unmanaged neighbor tables above or perhaps an external
Network Management System, this is where you would start your troubleshooting
process.

The most common reason why a new installation of IP Fabric will not connect is
due to the `connect ECONNREFUSED XX.XX.XX.XX:22` error which signifies the
traffic is being blocked by an ACL or firewall. This is why it is recommended
having IP Fabric in your management subnet which is already allowed for remote
access to devices, so you do not have to re-configure all your ACLs. Another
option is to use a jumphost as described
at [Jumphost](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Global_Configuration/jumphost.md).

Another common error is due to authentication or authorization errors. Please
ensure that the configured username has the correct permissions. There is also
[a list of CLI commands](https://matrix.ipfabric.io) used which can help ensure
authorization is correct.

If you find other errors, you can refer to
[Connectivity report - Type of Error](common_problems/connectivity_report.md)
and the CLI output of the device is usually helpful as well.

If you need further assistance, please feel free to reach out to your IP Fabric Solution
Architect or open a ticket following
the [Technical Support](../../../support/techsupport.md) instructions.

Finally, another option for testing devices is to log in to the IP Fabric CLI
using the `osadmin` account and manually trying SSH'ing into your devices,
preferably using the username and password the system was configured to use. If
you cannot open a connection, this is due to an external reason.

Further information can be found
at [No Devices Discovered](common_problems/no-devices-discovered.md).

## Troubleshooting Configuration Management

![Configuration Management](troubleshooting/configuration_management.png)

**Configuration Management** is a separate process from discovery. First, a device
must be discovered in a snapshot and placed in the **Management -->
Discovery History** table. Once in this table, next time IP Fabric is scheduled
to pull configs, the device should be populated in the **Configuration
Management** list.

!!! example

    - **Settings --> Discovery & Snapshots --> Snapshot Retention --> Create
      Snapshots Periodically** is set to create snapshots every day at 6AM.

    - **Settings --> Configuration Management --> Schedule** is set to
      create device configuration backups every day at 11PM.

    - New device will be found at 6AM, but since its configuration backup is
      scheduled for 11PM, you will need to wait until the next day to be sure
      that its configuration is pulled.

!!! tip

    Please ensure that in **Settings --> Discovery & Snapshots --> Discovery
    Settings --> Device Credentials**, you have enabled the correct usernames to
    `Use for configuration management`. If no usernames have been enabled for
    configuration management, then configurations will not be backed up.
