# Operational Requirements

## Host Hardware Requirements

The IP Fabric platform runs on Intel Xeon Nehalem CPUs or later. The
system runs in at least 4 parallel threads, but scheduling can handle
operations even down to a single thread. IP Fabric uses less than 4GB of
RAM when idle, and an additional 12GB of RAM is required for collected
network information. The base installation requires 80GB of HDD space
and an additional 50MB per device for the network.

|     |       |      |
|-----|-------|------|
| CPU | RAM   | HDD  |
| 4C  | 16 GB | 90GB |


*Table 1: Minimum hardware requirements*

The following table represents the recommended hardware requirements for
optimal performance of the platform based on the number of network
infrastructure devices in the network.

|         |     |        |                      |
|---------|-----|--------|----------------------|
| Devices | CPU | RAM    | HDD (OS + data)      |
| 500     | 4   | 16 GB  | 90 GB (80G + 10G)    |
| 1 000   | 4   | 32 GB  | 100 GB (80G + 20G)   |
| 2 000   | 8   | 64 GB  | 200 GB (80G + 120G)  |
| 5 000   | 12  | 64 GB  | 300 GB (80G + 220G)  |
| 10 000  | 16  | 128 GB | 550 GB (80G + 470G)  |
| 20 000  | 18  | 256 GB | 1000 GB (80G + 920G) |


*Table 2: Recommended hardware requirements*

!!! info
    
    ### Additional resources requirements
    
    To make sure you have enough resources, please use the following
    formulas.

    Data **disk storage** requires 1MB per device per each snapshot
    (example: 1350 devices, plan is to keep up to 100 snapshots => 135 GB
    data storage).

    **Memory** requires 5MB of RAM per device per each **loaded** snapshot
    (example: 1200 devices, up to 100 snapshots but only 3 loaded at a time
    (1200 x 5 = 6000 x 3) => 18 GB RAM).



The recommended hardware resources may not allow running the most
demanding graph traversal functions. These functions may require a
sizable memory pool to complete successfully.

## VMware Requirements

IP Fabric OVA images are built on Hardware Version 13.

ESXi version 6.5 or newer is required.

# Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth
limit which never exceeds an aggregate of set bandwidths in any
direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity
to managed devices. [Jumphost
server](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1384841217/Jumphost+settings)
can also be set up and used.

## Inbound Flow List

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="c4bd1fd9-7fce-440f-8fcf-96adfe6ba2b2">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Source port (remote)</p></th>
<th class="confluenceTh"><p>Destination port (local)</p></th>
<th class="confluenceTh"><p>Protocol</p></th>
<th class="confluenceTh"><p>Description</p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>User Interface</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>8443</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Administrative Interface</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - API</p>
<p>Support, Updates (Optional)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>22</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - SSH</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>23</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - Telnet</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p> n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a </p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>ICMP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - Traceroute</p></td>
</tr>
</tbody>
</table>

</div>

## Outbound Flow List

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="9480f0b6-5fc7-4d3a-8320-13d3f6cf0374">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Source port (local)</p></th>
<th class="confluenceTh"><p>Destination port (remote)</p></th>
<th class="confluenceTh"><p>Protocol</p></th>
<th class="confluenceTh"><p>Description</p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>User Interface</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>8443</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Administrative Interface</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - API</p>
<p>Technical Support, Updates (Optional)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>22</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - SSH</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>23</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - Telnet</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>ICMP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - Traceroute</p></td>
</tr>
</tbody>
</table>

</div>

Internet connectivity is used to check product updates, upgrades, setup
support VPN, send error reports, and submit support tickets.

## Jumphost server requirements

|                    |             |
|--------------------|-------------|
| **Python version** |             |
| 2.7                | supported   |
| 3.5                | supported   |
| 3.6                | supported   |
| 3.7                | supported   |
| 3.8                | unsupported |
| 3.9                | unsupported |

# Network Access Credentials Requirements

## Network device access

IP Fabric accesses network-infrastructure devices via CLI (command-line
interface) using SSH or TELNET protocols. All device interaction is
accounted on the platform and only “read-only” or “operator” group
privilege level 1 credentials are required.

The following list contains an example of commands used for Cisco IOS:

``` text
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

In the beginning, IP Fabric fingerprints the device using the “show
version” command (or equivalent) to identify a vendor and a system
version. A "terminal length" command is optional but highly recommended,
as it greatly improves the speed of the device interaction, reduces the
load on the network and the device, and improves collection precision.

## Additional device access

Since firewalls do not follow privilege levels, it may be necessary to
explicitly specify the commands allowed for each user. The following
list specifies the exec-mode commands needed for firewall discovery.

``` text
show version
show interface
show route
show arp
show context
terminal pager 0
```

Turning off paging greatly improves the speed of the discovery and
allows a terminal pager command, making it highly recommended although
not mandatory. The commands can be allowed through the central TACACS or
RADIUS access control system, or they can be configured locally on a
device. The following example adds the necessary commands to a
privilege-1 user:

``` text
privilege show level 1 mode exec command interface
privilege show level 1 mode exec command arp
privilege show level 1 mode exec command route
privilege show level 1 mode exec command context
privilege cmd level 1 mode exec command terminal
```
