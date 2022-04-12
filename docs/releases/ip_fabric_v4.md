# IP Fabric v4.x.x

!!! warning "Clearing Browser Cache"

    Please force refresh your browser cache after an upgrade. Depending on your operating system all you need to do is the following key
    combination:

      - Windows: CTRL + F5
      - Mac/Apple: Apple + R or command + R
      - Linux: CTRL + F5

## 4.4.0+6 (11th April 2022)

!!! warning "Breaking change -- How is `sn` created for virtual contexts"

    We needed to unify the way how is the device `sn` (Serial Number)
    constructed for devices with virtual context. Following vendors are
    affected with the change:

      - Cisco ASA with virtual contexts
      - Cisco WLC with system access point
      - Cisco NX-OS with VDC
      - Fortigate with VDOM
    
    In 4.4.0 we are migrating device attributes that are necessary for manual site separation but we are not able to migrate snapshots from the older versions. Therefore sites in the older snapshots can be wrong if manual site separation was used. Also, if you compare a snapshot in a version higher or equal to 4.4.0 with a snapshot in a lower version than 4.4.0 that includes affected devices then you might encounter false-positive changes in the snapshot comparison.

!!! important "Changes in licensing model"

    Please note the changes in licensing model. Devices discovered via APIs are
    going to consume license similarly to the physical devices (except Access
    Points). You can find more information at the [dedicated licensing
    page](../Getting_Started/Overview/licensing.md).

### New Vendor Support

- Added support for Cisco Viptela cEdge
- Added support for Juniper Mist
- Added support for Ruckus Virtual Smartzone

### Features -- Protocol and technology support

- HP ArubaCX -- added support for AAA.
- HP ArubaCX -- added parsing for SNMP configuration.
- HP ArubaCX -- Added parsing VXLAN info.
- Extreme XOS -- Add support for AAA.
- Cisco Viptela -- added cEdge support. If cEdge is discovered via cli, discovery ends and notify, that API discovery should be used.
- Cisco -- Added information about device licenses. Tables located at *Technology / Management / License*.
- Added data for Virtual Machines deployed in the network (AWS, Azure, VMware). Tables are located at *Technology / Cloud*.
- Add additional interface counters to most of the vendors. Table are located at *Technology / Interfaces / Counters*.
- Add new table ACL global policies located at *Technology / Security / ACL / Global ACL policies*.

### Bug Fixes

- The discovery process for vendors processed via API can get stuck -- fixed.
- VLAN L3 gateway table -- Access points are removed as they produce false-positive gateways.
- Routing protocols destination interface fix -- path lookup multicast routing was broken because of this.
- The data from global tables are available also when running snapshot is selected.
- Snapshot attributes are now copied when a snapshot is cloned.
- Loading a snapshot could sometimes cause an `Unexpected end of JSON input` error and then the snapshot will get corrupted. The root cause has been fixed.
- Arista EOS -- Fixed false positive error emitting from `show interfaces vxlan 1`.
- Azure -- fixed mapping of network interfaces without MAC address.
- Brocade Fastiron -- Improved parsing hostname from prompt.
- Cisco -- fixed host table for devices reachable with LISP.
- Cisco -- fixed parsing of PIDs containing plus symbol in command `show inventory`.
- Cisco FTD -- `commands/cisco/routingTable` -- fixed parsing for null summarized routes.
- Cisco IOS -- removed text `, wildcard bits` from texts in standard ACL.
- Cisco IOS-XE -- fixed parsing of rebuild version.
- Cisco IOS-XE -- fixed parsing of power supply and fans on Catalyst 9200/9300/9500.
- Cisco IOS/IOS-XE -- Fix transport protocol (telnet) detection.
- Cisco NX-OS -- fixed matching of MAC Addresses interface reference (fabric path) to real interface.
- Cisco NX-OS -- add parsing of port-channel interfaces without members.
- Cisco Meraki, Juniper Mist, Ruckus -- fixed device’s type detection to ensure wireless APs are detected properly.
- Extreme XOS -- fixed parsing of l2Interfaces of missing interfaces.
- Fortinet FortiGate -- fixed executing of cmd `get system password-policy` on VDOM enabled firewalls.
- Fortinet FortiGate -- Fixed missing FQDN in firewall policies unless configured in lower case.
- Fortinet Fortigate -- fixed parsing of `get router info ospf nei detail` for NSSA cases.
- HP Aruba switch -- added parsing of port information.
- HP ArubaCX -- fixed parsing of IGMP query interval.
- HP Comware -- fixed parsing of `display lldp neighbor-information verbose`
- HP Comware -- fixed parsing of `display stp region-configuration` in case vlans list is on multiple lines.
- Juniper Junos -- access-internal routes were removed from routing table.
- Palo Alto -- fixed parsing of empty applications/services in security rules.
- Palo Alto -- fixed parsing of `show high-availability state` for suspended state.
- Versa VOS -- `commands/versa/_vos/vnms/dashboard/appliance/sdWanSites` -- fixed mapping for unsupported IPv6 links.
- Versa VOS -- VRRP -- Allow virtual IP for instances in `Init` status.
- VMware -- NSX-T -- fixed discovery for T0/T1 routers.

## 4.3.5+1 (9th March 2022)

### Bug Fixes

- Routing protocol edges wrong establish to transit fix

### Known issues

  * Discovery with added Vendor API can get stuck and doesn’t finish in some cases. Replicated on NSX-T v2.5, Azure, Meraki

    * ID: NIM-7505, NIM-7479, NIM-7437
    * Root cause: Unlocked resources after calling unsupported API endpoint
    * Status: Fixed in 4.4.0 release
    * Workaround: Stop discovery and disable Vendor API


  * When discovery is stopped after collection from devices is done, API will allow other jobs to run - making them run in parallel. It is especially an issue when running maintenance is started immediately because it re-indexes the DB - making caching take really long time. 

    * ID: NIM-7722
    * Root cause: Discovery allows to run parallel jobs.
    * Status: Fixed in 4.4.0 release
    * Workaround: Do not stop discovery job or do not run maintenance (manually or as a scheduled job).

## 4.3.4+3 (7rd March 2022)

```
OVA MD5SUM: A5DB9B8C51169216167866C9AD6E951C
OVA SHA256SUM: 2D64A41DF78D3965F70AD80807D788FD12E0F7A1DDCF39A6B23911BF72A8311D
```

### Bug Fixes

- Internet proxy was not working - fixed now
- Snapshot load with F5 device could fail on JSON error. This was hard
  to replicate, happened only occasionally. Fix should work.
- Fortinet FortiGate - fix `get system status` command parsing to
  handle operating system versions without any maintenance ID
- L2 edges from switch to firewall - Multiple wrong edges were created
  because of same virtual mac address on Juniper SRX firewalls (could
  be also case for other vendors). This could cause too problems with
  graph cache calculations. Fixed and firewalls with same virtual mac
  are in different sites, L2 edges will be established properly.
- L2 edges for back-to-back connections - fix for non matching
  switchport modes.
- HP Comware -- fix parsing of Route-Aggregation interfaces.
- HP 3Com - fixed parsing of `display device manuinfo` command
- Duplicate IP on same device on different subinterfaces and different
  sites -- establishing forwarding and routing protocols sessions is
  fixed.
- Some topology calculation speed ups for networks with many routing
  protocols sessions
- Pathlookup - Routing with OIDs, skip checking underlying L2 path
- Fix parsing Virtual Servers and Pool members with routing domains
  and `any` ports.
- VMWare NSX-T -- fixed mapping of empty mac-table
- Error when opening Intent Rule verification in End Of Life
  Milestones page fix
- Arista -- fixed parsing of platform
- Fixed possible crash in syslog worker when collecting device
  configurations
- Fixed POST `/snapshots` endpoint, it failed when `snapshotName` or
  `snapshotNote` was used
- The site names could be wrong when the manual site separation rule
  was disabled - fixed
- Fix load of graph views

## 4.3.3+2 (23rd February 2022)

### Bug Fixes

- Snapshot load time - data preparation before the process started was
  slow, fixed and speed is same as before
- Snapshot settings could overwrite global settings
- Migration of very old snapshot fix

## 4.3.2+2 (22nd February 2022)

### Bug Fixes

- Palo Alto - Fixed discovery of multi vsys firewalls.
- Mikrotik RouterOS - Fixed parsing of MTU in case it has value ”auto”
  in output of command ``/interface print detail`
- Fortinet FortiGate - Fixed wrongly assigned MAC address to link
  aggregation interfaces on HA primary units
- Jumphost - Jumphost was broken in 4.3.0 release, fixed.
- Graphs - Fail on hidden transit or clouds fixed.
- `/platforms/vdc/devices` table fail when snHw column was included

### Improvements

- Check Point Gaia - improved pairing of gateways with management
  server data to fix missing zone firewall policies

## 4.3.1+1 (17th February 2022)

```
OVA MD5SUM: 0ab89eb2127d5a83f806876b438dcd95
OVA SHA256SUM: 3d07c8f1a51497eae671a43130cbf536b7e7bdf9ae6ba9030ebc50c981328119
```

### Bug Fixes

- Missing hostname on Cisco devices with non standard transceivers

### Features - Protocol and technology support

- HP ArubaCX - Added syslog support

## 4.3.0+4 (16th February 2022)

### New Vendor Support

- Added support for [Microsoft Azure Cloud
  infrastructure](Azure_Networking)
- Added support for [Silverpeak SD-WAN networks](Silver_Peak_SD-WAN)
- Added support for [VMware NSX-T](VMware_NSX-T)
- Added support for Brocade FastIron

### New Features

- Added Single sign-on (SSO), read how to set it up [Enabling SSO
  Providers](Enabling_SSO_Providers)
- Device Attributes - the table is located in Settings / Device
  Attributes, where you can set attribute per device (SN) and the
  value for a specific attribute. [Device
  Attributes](Device_Attributes). We support following attributes

  - `siteName` - set a site name (location) for a specific
    device and in case you have enabled the
    _Manual site separation_ rule in Site Separation settings
    then the name will be used in future snapshots for that
    device.

  - `stpDomain` - set a name of the STP domain for a specific
    device and this domain name will be used in future snapshots
    for that device. But also other members that belong to the
    same STP domain and don't have an attribute set will be
    moved there automatically.

  - `routingDomain` - same as STP domain, but for Routing domain

- Added support for [AWS Assume
  Role](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/2691563521/AWS+API#AWS-AssumeRole)
  that can be configured in Vendor API settings

- Graphs - Path Lookup - Added simulation for Cloud / SD-WAN networks.
  Simulate packets between legacy and next-gen networks!

- Graphs - Path Lookup - Added detection of packets in the loop - the
  option is on Visualization Setup.

- Graphs - Path Lookup - The packet can be traced hop by hop in "Show
  Detail" by Next/Prev buttons

- Graphs - Path Lookup - added more options into path lookup form like
  L7 applications, ICMP options, IP Regions, TTL, and everything can
  be saved to setting preset

- Graphs - Path Lookup - added "First hop algorithm" option, this will
  allow you to simulate external networks by specifying where the
  packet should start (device/interface)

  - unfortunately, all the above Path lookup changes cause a
    breaking change in the API request payload.

  - See [Tech Notes for Path Lookup](../../IP_Fabric_API/path_lookup-4.x/)

### Features - Protocol and technology support

- HP ArubaCX - Implement IGMP/PIM
- F5 BigIP - Added support for virtual servers and pools. New tables
  added:

  - Technology / Load-balancing / Virtual Servers
  - Technology / Load-balancing / Virtual Servers Pools
  - Technology / Load-balancing / Virtual Servers - Pool members
  - Technology / Load-balancing / F5 Partitions

- Added new table Technology/ Port channels / MLAG / Cisco VPC
- Extreme Xos - Added POE support

### Improvements

- [Site Separation](../../IP_Fabric_Settings/Settings_UI/site_separation) has been rewritten, it respects Device Attributes
  (see New Features)
  - there was added an algorithm to determine the site name based on
    SNMP location.
  - also added an option that will try to assign devices without
    site name to the site based on device neighborship.
- Discovery classification improved - only IP addresses with
  interfaces in UP state go to the discovery process.
- Router to switch connection with some members of port-channel in
  state down could prevent STP edge establishment.
- Updated EoL information for F5
- Router with no VLAN tag on the interface to ACI leaf connection over
  L2 with xDP added.
- Table Technology / Security / IPSec / IPSec tunnels - add new column
  "Tunnel interface description"
- Table Technology / Addressing / Manage IP - add new columns
  "Interfaces L1 state", "Interfaces L2 state"
- Table Technology / Security / DMVPN - add interface column
- Zone Firewall and Access lists security tables are now broken to
  rule level with columns that are string searchable for all values
  (some of the columns are hidden by default). Tables also allow the
  application of intent checks.
  - Table Technology / Security / Access lists
  - Table Technology / Security / Zone firewall
- The date and time values are now displayed in ISO8601 format
- Cisco Firepower - Change collecting data to use FMC API and add
  support for application rules: More [Dropping support for ACL on
  Cisco Firepower](Dropping_support_for_ACL_on_Cisco_Firepower)
- Added API endpoint POST `/v1/tables/management/snapshots` for the
  possibility to get information about all snapshots (loaded,
  unloaded) via [API](../../IP_Fabric_API/path_lookup-4.x/)
- Path Lookup inspector - cosmetic improvement of ACI endpoint lookup
  reporting
- Path Lookup - Forwarding for explicit label 0 fix
- Check Point Gaia - added collecting of static ARP
- Cisco - IOS, IOS-XE, IOS-XR, NX-OS and Juniper Junos - change BGP
  route max threshold evaluation to be done on a per VRF basis.
- Extreme XOS - Added new reason of disabled port `port not present`
- Fortinet FortiGate - configured virtual IPs and IP pools were
  missing in the list of managed IP addresses

### Bug Fixes

- If Snapshot Settings had stored credentials without username
  then credentials from the Global setting were taken
- Graph - The detail for XDP link between two devices could include
  records that pointed from one device to the Transit cloud.
- Table Management / Changes - fixed export of CSV that didn't work
- Table Technology / MPLS / Forwarding - nexthop label 0 value was not
  previously shown. Fixed now
- Arista EOS - Fix parsing of the routing table.
- Arista EOS - fix subinterfaces parsing from command `show ip ospf neighbor detail`
- Arista Eos- Fix parsing of command `show lldp neighbors detail`.
- AWS - Fix mapping of `aws/_ec2/describeRouteTables`
- AWS - Fix parsing for a command that shows tunnelOptions which can
  be empty.
- Checkpoint Gaia - Fix parsing for Alias interfaces.
- Checkpoint Gaia - Fix parsing for command `show cluster members interfaces all`.
- Checkpoint Gaia - Fix parsing for empty management interface entry.
- CheckPoint Gaia - collect only relevant SNMP configuration according
  to agent version
- Checkpoint Gaia - Fix parsing for command `show ospf interfaces detailed`
- CheckPoint Gaia - fixed error when only a virtual IP was assigned on
  an interface
- CheckPoint Gaia - fixed missing zone firewall policies on gateways
  with VPN tunnel interfaces
- CheckPoint Gaia - fixed parsing of physical interfaces from command
  `show cluster members interfaces all`
- Cisco - fixed PID parsing for nonstandard Cisco transceivers from
  command `show inventory`
- Cisco - Fix duplicate entries for lldp and cdp discovery.
- Cisco - Fix parsing of nexthop list from routing table
- Cisco - IOS/IOS-XE fixed parsing of `show ip mroute count` command
- Cisco ASA - the discovery of firewall contexts fixed
- Cisco ASA - fixed MTUs and IP addresses parsing on tunnels.
- Cisco ASA - fixed parsing of named ip addresses from `show running-config`
- Cisco IOS - add support for portgroups in ACL
- Cisco IOS - fix N/A value in current traffic from command `show storm-control`
- Cisco IOS - Fix parsing of speed, duplex and tunnel type.
- Cisco IOS - fix state when two (current and trap) are outputed in
  command `show storm-control`
- Cisco IOS - fixed parsing of tunnels in case source/destination IP
  address is missing
- Cisco IOS - Remove emitting error for bgp neighbors in state 'idle'
- Cisco IOS-XE - Add missing vlanId for the command `show interfaces`.
- Cisco IOS-XE - added support for another output format of the `show env/environment status` command
- Cisco IOS-XE - Fix parsing for no transceivers in command `show interfaces transceiver`
- Cisco IOS-XE - Fix parsing of interface counters for command `show wireless client mac-address <int> detail`
- Cisco IOS-XE - Fixed parsing for virtual IPv6 addresses in command
  `show standby`
- Cisco IOS-XE - Removed PTP related errors throwing in case `show ptp clock dataset default` does not provide any results
- Cisco IOS-XR - `commands/cisco/isis/neighborsDetail` - fixed parsing
  with different neighbors format.
- Cisco IOS-XR - `commands/cisco/routingProtocols/ipRouteSummaryVrf` -
  fixed parsing with different format.
- Cisco IOS-XR - Exclude parsing of monitor sessions in L2VPNs.
- Cisco IOS-XR - Fix parsing for the command `show bgp all neighbors`
- Cisco IOS, IOS-XE - Fix parsing for command `show subscriber session all`.
- Cisco IOS, IOS-XE, IOS-XR some routes with MPLS label were not used
  correctly even when next hop is known.
- Cisco NX-OS - `show vlan brief` parsing updated to handle error
  message displayed due to Cisco bug CSCvr88898
- Cisco NX-OS - Fix parsing of command `show password strength-check`
- Cisco NX-OS - Fix parsing of ospf state for the command `show ip ospf interface vrf all`.
- Cisco NX-OS - Fixed parsing for negative DHCP snooping values in
  command `show ip dhcp snooping statistics`, probably bug on device.
- Cisco NX-OS - fixed parsing of command `show mac address-table` that
  were containing fabric path SWID.
- Cisco NX-OS - fixed parsing of different output for command `show snmp user`

- Cisco viptela - Fix parsing of uptime from command
  `/device/bfd/sessions?deviceId=`
- F5 Big-IP - added support for IPv6 NTP source addresses in command
  `run util bash -c "ntpq -np"`
- F5 Big-IP - `commands/f5/_big-ip/showSysHardware` - fix parsing
  various sections of command
- F5 Big-IP - Fix parsing of translated ports in command `list /sys sflow receiver all-properties`
- F5 BIG-IP 2000 - Fix parsing if the output of the command `list /sys management-ip` is empty.
- F5 Big-IP - Fix parsing of invalid interfaces for command `show cm device`.
- F5 Big-IP fix prompt detection - add the possibility for "(Sync
  Only)"
- Fortinet FortiGate - Added another parsing option of src-filter for
  command `show firewall VIP`.
- Fortinet FortiGate - Fix parsing for command `show system ha`
- Fortinet Fortigate - Fix parsing for the command `get router info bgp nei`
- Fortinet FortiGate - MAC address on link aggregation interfaces
  could be missing in some cases
- HP 3Com - Fix device detection from `display version` command
- HP 3Com - remove ip address reference from directly connected
  routes.
- HP Comware - Added support for tunnel protocol: UDP_ADVPN/IP.
- HP Comware - Fix parsing for command `display arp`
- HP Comware - Fix parsing for command `display fan`
- HP Comware - Fix parsing of BGP peer instance regex for localID.
- HP Comware - Fix regex splitting of state and age for command
  `display ip routing-table verbose`.
- HP Comware - Fixed parsing of M-Ethernet and TwentyGigE interfaces
- HP Comware - fixed parsing of power supplies from command `display power`
- HP Comware - Fixed parsing of Route-Aggregation interface in the
  command `display interfaces`.
- HP Comware: fix routing relation on own address.
- Juniper - fixed parsing firewall rules - added nonterminating
  actions.
- Juniper Junos - Add an exception for infinite values while parsing
  the command `show interfaces diagnostics optics`
- Juniper junos - `commands/juniper/junos/configurationDisplaySet` -
  added from `dscp`, `ttl`, `is-fragment` (with except actions if
  applicable) action to firewall parsing.
- Juniper junos -
  `commands/juniper/_junos/interfacesStatisticsDetail` - fix parsing
  errors on interfaces - added support for a type of output.
- Juniper Junos - `commands/juniper/_junos/route` - Removed Service to
  routes, unable to resolve next hop for those routes
- Juniper Junos - Fix parsing of no output from command `show sflow`
- Juniper Junos - fixed parsing for fans which don't have tray
  information from command `show chassis environment`
- Juniper Junos - fixed parsing of "null" encryption in command `show security ipsec security-associations detail`
- Juniper Junos - improved information parsing of deactivated and
  protected configuration
- Juniper Junos - removed management interfaces with configured ip
  `128.0.0.1/2` or `10.0.0.1/8`
- Juniper Junos- fixed parsing of command `show interfaces statistics detail` for logical-unit-number larger than 4095
- Paloalto pan-os -
  `commands/paloalto/showConfigPushedSharedPolicyVsys` - fixed parsing
  of none zone in security rule.
- Paloalto pan-os - fix services parsing from command `show config merged`

## 4.2.0 (20th December 2021)

```
OVA MD5SUM: E50411AF79A1990249FA9D041809302E
OVA SHA256SUM: 8D773667434B4C27C9C199E84784312864E01C08D51DAA158B7C07C9B99BFD8F
```

### New Vendor Support

- Added support for HP 3Com

### New Features

- Graphs - New layout option - Radial Tree: Use this layout for tree
  topologies to expand outward from center.
- New table - Technology / Management / AAA / Password Strength
- Added timezone support - every user can set his preferred time zone
  and each cron job has also its own timezone settings. The logs are
  always in UTC.

### Improvements

- Arista EOS - added support for another output format of `show vrf`
  command
- Cisco ASA/FTD - added support for local syslog targets and fixed
  parsing of `show logging` in case there are ifNames containing
  special characters
- Cisco ASA/FTD - syslog - `show logging` command replaced with a more
  efficient `show logging setting`
- Fortinet FortiGate - fixed missing policies with configured profile
  group
- HP ArubaCX - Add parsing of reload reason
- HP ArubaCX - added support for parsing of interface load.
- Juniper Junos - added missing community string in table
  technology/management/snmp/trap-hosts.
- Juniper Junos - `commands/juniper/\_junos/configurationDisplaySet` -
  add parsing for firewall tcp-established `from` action

### Bugfixes

- The users with Read privileges weren't able to open Device Explorer
- The path lookup form wasn't correctly filled with data from the
  loaded view
- Arista 7010t - fixed parsing of different output for command `show inventory`
- Arista eos - `commands/arista/_eos/ntp` - fixed parsing with
  different `refid`
- Arista eos - fixed parsing of `default-control-plane-acl` by command
  `show ip access-lists` in case it contains `cvx-license` port
- Cisco ACI - fixed parsing of backbone area in `show ip ospf interface vrf all`
- Cisco ASA - added support for another output format of `show bgp neighbors`
- Cisco csr1000 - MPLS - added support for an additional type of `show mpls forwarding-table detail` command output
- Cisco IOS - Fix parsing of interface tunnel protocol.
- Cisco IOS-XR, NX-OS - MPLS forwarding - shortened commands `sh mpl for` and `sh mpl switch` extended to their full syntax to prevent
  ambiguous command error
- Cisco IOS/IOS-XE - tasks/vrf - use `show ip vrf detail` if `show vrf detail` is not available.
- Cisco MS - Fixed parsing of Meraki device clients.
- F5 BIG-IP i800 - Fix parsing of NTP data.
- Fortinet FortiGate - Fix for bad parsing of command `diag hard dev nic`.
- Fortinet FortiGate - Fix parsing for command show full application
  list.
- Fortinet FortiGate - fixed missing zoneFw data for geography address
  objects and application profile data
- Fortinet Fortigate - fixed transceiver value parsing.
- HP Comware - fixed parsing of `display lldp neighbor-information verbose` command in case there are no neighbors
- HP Comware - Fixed parsing of TwentyGigE interfaces.
- HP Comware 5130 - AAA - fixed parsing of server parameters
- Huawei VRP - fixed parsing of different output for command `display info-center`
- Juniper Junos - Fix parsing firewall filter section - problem with
  unsupported `from` action
- Palo Alto - fix parsing of interface secondary IPs.

## 4.1.1 (3rd December 2021)

```
OVA MD5SUM: 9487074E08641A8FD1C7F0E887B92EA4
OVA SHA256SUM: 901018EE369B630CD80C6438B3A4D0C54F0F3D7BCD9156B9F93087C9B5147ECE
```

### New Features

- Graphs - allow for selection for nearest neighbors (1st, 2nd, 3rd
  level of neighbors)

### Breaking changes

- Changed format of payload for API Endpoints
  `/tables/management/changes/*`

### Improvements

- Site Separation - HOTFIX - added button to disable paging, this will
  allow drop rules among pages.
- Management / Configuration - can be used only for users with
  "Discovery" & "Read" privileges.
- End of Life milestones tables - add URL into CSV export
- Configuration Management - respect if Telnet is disabled/enabled now
- Graphs - the nodes can be also searched by SN now
- Pathlookup - support for Cisco VXLAN anycast gateway added
- Graphs - Intent Checks overlay - the data in "Show detail" have
  colored only one column based on the applied report
- Services - webhook service is correctly started and enabled
- FTP backup - dropped SSL certification validation for FTP backup,
  please use SFTP for more secure file transfer

### Bug fixes

- Tables - Management / Changes - fixed filtering in all changes
  tables.
- Fixed name of tech support file
- Graph requests might fail when an incomplete payload was sent.
- FIX Rediscover action in Connectivity Report
- Fixed filename of downloaded Techsupport file
- Routing to Cisco ACI pervasive address fix
- Fortinet FortiGate - prevented to execute command `get system interface transceiver` if transceivers task is disabled
- Cisco - SUP32 based Catalyst platforms - fixed to use `show ip igmp interface” comman` to gather IGMP snooping interface related
  information
- Cisco ASA/FTD - added `show failover` command to detect
  Active/Standby status of unit/context in HA cluster
- Cisco ASR routers - added support for PTP related commands `show ptp clock dataset default`, `show ptp clock dataset parent domain <domainId>` and `show ptp`
- CheckPoint Gaia - fix of missing zoneFw rules for some of the
  managed firewalls
- Juniper Junos - fixed parsing for security with no address books.
- Cisco - NX-OS - fixed parsing of interface speed on for some nexus
  switches
- Cisco NX-OS - commands/cisco/stpMstMapList fixed parsing when mapped
  vlans are on multiple lines
- Juniper - fixed parsing of ethernet switching table on QFX switches
- Fortinet FortiGate - fixed discovery of VDOMs with long name
- Huawei VRP - Fix OS detection for NetEngine 8000

## 4.1.0 (15th November 2021)

```
OVA MD5SUM: 70CF5FCD46262EF621BFC2DCA8895B17
OVA SHA256SUM: DD5F1F0F701974CC8367336DDB7B3877CAAF3BD6DC114BB37C178CD104CA8BA7
```

!!! important

    If you’re migrating from 4.0.2 to 4.1.0 then you have to reload all your snapshots manually

### New Vendor Support

- Added support for Cisco Viptela

### Improvements

- Add hostname to Detail tab in the Device Explorer component
- Changes in POST `/snapshots` endpoint - the snapshot `snapshotName`
  and `snapshotNote` can be set now
- End of life database has been updated for Juniper, HP, Cisco, and
  Fortinet. Also, EOL dates for Cisco Meraki were fixed.
- Fortinet FortiGate - show `Possible device error` message in the
  `Discovery issues` tab in case that all VDOMs can’t be discovered on
  FortiGate because of wrong permissions
- Graphs - the Transit cloud has a different icon now
- Inventory / Interface - add new column "Original Name" -
  Non-standardized interface name (hidden by default)
- Inventory / Interface - column IP now shows the physical address of
  the interface (instead of virtual IP)
- Paloalto pan-os - `tasks/_helpers/security/preProcess` - added
  support for application-filter
- Significant optimization of DB queries for snapshots where exists
  hundreds of interfaces for a single device.
- Snapshot download - the file name now consists from following
  `<snapshotName>-<snapshotTime>-<snapshotKey>.tar`
- Snapshot download - the UI has been improved, added snapshot name
  and snapshot timestamp
- Snapshot name in the UI - the order of labels was changed, the
  timestamp is first and the custom name is below that.
- SSH connection to PaloAlto - confirmation for
  _Do you accept and acknowledge the statement above?_ fixed. It will
  allow the discovery of PaloAlto with this confirmation. SSH library
  was upgraded to new version.

### Bug Fixes

- API `/graphs/png` endpoint - the PNG export didn't work - fixed.
- Arista EOS - added support for rules with DSCP in command `show ip access-lists`
- Arista EOS - fixed parsing of `show ip virtual-router` for another
  output format
- Arista EOS - fixed parsing of interface ranges in command `show ip access-lists summary`
- Arista EOS - fixed parsing of logging and snmp information in
  command `show running-config`
- CheckPoint Gaia - fixed missing zone firewall data for VSX clusters
- CheckPoint Gaia - fixed version detection for OS versions
- CheckPoint Gaia - policy rule was missing if `Install On` was set to
  a group object
- CheckPoint SMS - fixed processing of nested inline rulebase layers
- Cisco - ASA - added support for FWSM detection (support for `show version` command parsing)
- Cisco - fixed ACLs parsing in case they contain multiple white
  characters between keywords
- Cisco - QoS fixed parsing for nested child service policies
- Cisco IOS - commands/cisco/vxlan/nvePeers - added support for an
  additional type of `show nve peers` command output
- Cisco IOS-XE - Added exclusion for ACL rule
  `system-cpp-energywise-disc` containing bug (CSCue04444) in `show ip access-list`
- Cisco IOS-XE - fixed parsing of assigned ACLs from `show ip interface` command in case of different output format
- Cisco IOS-XE - fixed parsing of recursive routes with MPLS label.
- Cisco IOS/IOS-XE - routing table - added support for ICMP redirects
  and filtering out of `possibly down` routes
- Cisco NX-OS - an icon of Nexus 9000 changed to match the icon of
  Nexus 7000.
- Fixed advanced filtering in Snapshot Management / Inventory table
  (OR condition didn't work)
- Fixed Interface edge classification for tunnel interfaces.
- Fixed PNG export for graphs via API request
- Fortinet FortiGate - fixed empty MAC table
- HP ArubaCX - added support for another output format of command
  `show interface`
- HP ArubaCX - added support for another output format of command
  `show ip ospf neighbor detail`
- HP ArubaCX - Added support for task `vrf`
- HP ArubaCX - Fix parsing for command `show ip route all-vrfs`
- HP ArubaCX - fixed parsing of platform in command `show system`
- Path lookup - ACI and firewall routing to duplicate IP addresses
  fix.
- Router to switch L2 edges - same mac on multiple interfaces fix
- Table Management / Changes - the column `#IP Addresses` had always 0
  as a value - fixed
- Versa - standardize duplex values

## 4.0.2 (11th October 2021)

```
OVA MD5SUM: 7b23502208cbffe07584e31ccd48f29e
OVA SHA256SUM: 045123c5ccfeeb0f89eb1af8fb6a1dd3de1d91a109f0024a281da2d788db6c40
```

### Features - Protocol and technology support

- Arista - added ACL support
- CheckPoint Gaia - added VRRP support
- Cisco - AAA - new local users table added, located at Technology /
  Management / AAA / Local users
- Cisco IOS-XR - added ACL support
- Cisco IOS-XR - added support for port channels
- Extreme XOS - Add support for switchport
- Juniper Junos - added support for OSPFv3
- Juniper Junos - added VXLAN support

### Breaking changes

- Table **Technology->Security->Object Groups** was dropped. All
  object groups are now part of the new security model. API calls to
  URL `/v1/tables/security/acl/object-groups` will no longer be
  working.

- For tables **Technology->Security->Access lists**
  (`/v1/tables/security/acl`) and **Zone Firewall**
  (`/v1/tables/security/zone-firewall/policies`), all columns except
  `name` were dropped
  (`seq`, `srcAddresses`, `dstAddresses`, `inAcl`, `outAcl`, `term`, `action`, `actionName` and `matches`
  for ACL table and
  `type`, `fromZone`, `toZone`, `seq`, `src`, `dst`, `appNames` and `actions` for
  Zone Firewall table) as new security model is represented by a tree.
  Because of that, it can't be fitted into a table format.

- Snapshot cannot be refreshed from the graph in this release. This
  function will come back in the following release 4.1.

- API for pathlookup has changed see [API Documetation](../../IP_Fabric_API/path_lookup-4.x/)

### Improvements

#### The visualization part of the application was fully rewritten to boost performance and capabilities.

- The brand new UI
- Visualize your topology with a range of built-in layouts (or layout
  only selected nodes)
- Intent-based networking has never been easier, the results are shown
  in the context of visualized devices.
- Define your own preset, change colour or labels for any protocol
- Use API to share visualizations with your wider ecosystem
- Highlight device neighbour relationship
- Share the view with your team
- Export to SVG, PNG
- Enhanced search capabilities
- Collapse or hide devices

#### The path lookup simulation was also completely rewritten to packet-based path-lookup simulation.

- The unicast simulation also supports subnets now
- Improved ACI topology simulation
- Added hairpin switching in different VLANs
- Multicast options for filtering receivers added
- Improved simulation through transit cloud including tunnelled
  traffic
- New packet inspector - understand all forwarding decisions at every
  layer
- Reworked security model - visualized in a tree
- Change path lookup edge colours according to packet header
  priorities

#### Other improvements

- Cisco ASA/FTD - added support for ‘show DNS’ command and use it for
  translation of FQDNs in objects/ACLs
- Cisco WLC IOS-XE - Added parsing of wireless client IP address.
- CheckPoint Gaia - added support for Link Aggregation (Bond
  interfaces)
- Allow to use `-` or `.` characters in username
- Device type classification for a router with unused switch module
  changed. Now is recognized as a router, not a layer 3 switch.
- Host table - IP host classification improved (OUI vendor check is
  removed).
- Table Technology / Interfaces / Transceivers / Statistics - add
  Delta High-Value column
- Fortinet FortiGate - added missing Part Numbers to Inventory
- Add support for `onep-plain` port name to number (15001) translation
- Table Technology / CDP/LLDP / All Neighbors - show _Device Explorer_
  component for values in Remote Neighbor column
- Updated End of life records for Cisco, Arista, Fortinet, Juniper,
  ProCurve, Extreme
- End of Life summary table improved - table now shows also records
  that don't have introduced EoL data yet, data are grouped per vendor
  and add new column `Replacement`
- Routing edge improvement for tunnel interfaces with unnumbered IP
  addresses.
- Make LDAP group matching case insensitive.
- Inventory host table - hosts connected to ACI with default gateway
  on the non-ACI device have now edge switch.
- Pathlookup - ACI to FW connection added
- Table Management / Changes - added column `Snapshot name` for better
  orientation
- Tables - CSV Export - the format was changed and it's fully
  compliant with [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180)
- Site separation - added pagination when exists a lot of regex rules

### Bug Fixes

- Fix for snapshot clone process in a stuck state
- Site separation - preview results now respect transformation
  settings.
- Snapshot Management - fixed empty status of the snapshot
- Table component - `Reset table settings` didn't work - fixed
- The toggle `Allow using telnet protocol` didn't work - fixed
- Transceivers statistics table - delta column calculation fix
- Arista EOS - `/commands/arista/_eos/switchport` - full cmd syntax
  used to prevent ambiguous command errors
- Arista EOS - add support for another format output of the `show poe`
  command
- Arista EOS - ARP in some cases was not parsed whole interface name
  for ARP record
- Arista EOS - fixed false-positive error regarding VPN/VRF in `show ip interface` command
- Arista EOS - fixed missing IP phones on some devices
- Arista EOS - fixed parsing of `show interfaces vxlan 1` for
  interfaces with description
- Arista EOS - fixed parsing of `show ip route` command in case VRF
  Leaks are in it
- Arista EOS - fixed parsing of different output for command `show mlag detail`
- Arista EOS - fixed parsing of different output for command `show ntp ass`
- Arista EOS - Syslog - information is parsed from `show running-config` instead of `show logging`
- Aruba CX - commands/arubacx/interface - fixed parsing for ip address
  / mask
- Aruba switch - standardize port speed units with other vendors
- Checkpoint Gaia -
  `commands/checkpoint/_gaia/cluster/members/interfacesAll` - fixed
  parsing for different command output
- CheckPoint Gaia - fixed collecting of nested network / service
  groups in security policies
- CheckPoint Gaia - fixed discovery on devices where the command `show management interface` is not available
- CheckPoint Gaia - fixed parsing of different output for command
  `show cluster members interfaces all`
- CheckPoint Gaia - fixed parsing of OSPF InterArea and External
  routes
- CheckPoint Gaia (Security Management) - don’t download policy
  packages without configured installation target
- Cisco - fix error created by calling ambiguous command (`show interface switchport`, `show interface status err-disabled`, `show ip interface`, `show spanning-tree bpdu`)
- Cisco - fixed ambiguous command `sh mpl interf` by `show mpls interfaces`
- Cisco - fixed parsing of commands `show mac address-table multicast`
  and `show mac-address-table multicast` for cases there are
  unexpected lines at the beginning of the output
- Cisco - Fixed parsing of VRF Route-Targets in an IP format
- Cisco - various platforms - suppress error messages when tunnel
  present on port.
- Cisco ACI - fixed parsing of 'inherit' speed value from `show interface` command
- Cisco ACI, NX-OS - fixed parsing of `show environment` command in
  case power supply’s column model is empty
- Cisco HSRP - fixed preemption
- Cisco IOS - add stacking support for catalyst 2960-s platform
- Cisco IOS - commands/cisco/mcast/macMulticast - add parsing support
  for MAC table records with multiple interfaces per row
- Cisco IOS - commands/cisco/mcast/pimNeighbor - fixed missing PIM
  version & different output structure on old IOS version
- Cisco IOS - commands/cisco/vrrp - fixed parsing of preempt parameter
- Cisco IOS - Fixed parsing for AAA section from running config.
- Cisco IOS - fixed parsing of `show power inline` command for cases
  of empty device name
- Cisco IOS - fixed parsing of ”show version” command in case of
  faulty master switch
- Cisco IOS - Fixed parsing of command `sh ip mroute vrf \<vrfName>`
  that would get translated by the DNS server
- Cisco IOS - fixed parsing of command ”show ip igmp snooping groups”
  in case port list does not contain any interface for a group
- Cisco IOS - fixed parsing of the different output for command `show ip flow export command`
- Cisco IOS - fixed parsing of the different output format of command
  `show ip mroute count`
- Cisco IOS - removed false positive error emitting in `show monitor detail` command
- Cisco IOS - `tasks/deviceConfig/current` - allow empty configuration
  when device return it
- Cisco IOS + IOS-XE - fixed false-positive error detection in command
  `show dot1x all details` in case of Tacacs session expiration.
- Cisco IOS cat9300 - commands/cisco/vxlan/nveVni - fixed parsing for
  new command output format
- Cisco IOS-XE - added parsing of another format of `show env all` and
  `show env status`
- Cisco IOS-XE - Fixed parsing of command `show interfaces transceiver detail` for another output format
- Cisco IOS-XE fixed parsing of `show environment all` command for
  devices with multiple PSU
- Cisco IOS-XR - ACL add suport for networks in CIDR format
- Cisco IOS-XR - fixed parsing for dot1x interfaces configured as
  authenticator and supplicant
- Cisco IOS-XR - Removed backup (FRR) routes from routing tables.
- Cisco IOS-XRv - fixed platform, model and uptime parsing
- Cisco IOS/IOS-XE - fixed parsing of _CVTA phone port_ and _Two-port
  Mac Relay_ CDP capabilities
- Cisco ISA - `commands/_osVersions/showVersion` - fixed parsing of ISA
  platform
- Cisco Meraki - API v0 input validation updated for endpoint
  `switch-ports/get-device-switch-port-statuses`
- Cisco Meraki - `commands/cisco/_meraki/v0/devices/switch/ports` -
  Unexpected stp guard value: root guard.
- Cisco Meraki - fixed parsing of Meraki device clients.
- Cisco Nexus - commands/cisco/mac - Added support for FabricPath MAC
  entries
- Cisco Nexus - commands/cisco/switchport - fix parsing for VLAN ID
  ranges that are split over multiple lines
- Cisco Nexus - fixed parsing of `show policy-map system type network-qos` command to support another output format
- Cisco Nexus - `show environment fex all` cmd - added support of
  `absent` PSU parsing
- Cisco Nexus - added parsing of another output format of `show logging server` command
- Cisco Nexus - fixed parsing of FEX environment information
- Cisco Nexus - fixed parsing of in/out bytes, multicasts and
  broadcasts from `show interface` command
- Cisco Nexus - Fixed parsing of STP port status on STP broken ports.
- Cisco Nexus, ACI - fixed Device Mode value for FEX devices in
  Technology/Platforms/Environment
- Cisco nx9000-aci - `commands/cisco/igmp/group` - Group IP parsing fix
- Cisco SG - `commands/_osVersions/showVersion` - Add OS discovery
  support for cisco Sg220.
- Dell Powerconnect - added MTU and MAC for interfaces
- Dell Powerconnect - fixed parsing of MAC address from `show interfaces` command
- Dell Powerconnect - fixed parsing of speed and duplex from `show interfaces status` command to support also N/A and unknown values
- Dell Powerconnect n1500 - Fixed parsing for the command `show spanning-tree detail`.
- Duplicate IP table - false-positive unnumbered IP removed
- Extreme XOS - added support for another output format of `show sharing` command
- Extreme XOS - `show ports transceiver information detail` fixed
  parsing of `-infinity` value
- Extreme XOS - fixed parsing of port names for `show stpd <stpdDomain> ports counters` command
- Extreme Enterasys - tasks/portChannel - port state fix
- Extreme XOS - Fixed parsing of command 'show ip-security
  dhcp-snooping vlan' to allow more or none ports in Trusted ports
  section
- Extreme XOS - fixed parsing of command `show ports transceiver information detail` to allow transceivers without any statistics
- F5 - commands/f5/\_big-ip/listNetSelf - add support of ipv6
  addresses
- F5 BigIP - fixed parsing of Cluster members if they don't have
  Failover Unicast configured.
- Fortinet FortiGate - `commands/fortinet/diagSysNtpStatus` - fixed
  parsing if all configured servers are unresolved
- Fortinet FortiGate - fixed parsing of `get system status` command
  for FortiGateRugged platform to allow IPF device discovery
- Fortinet FortiGate - LLDP link wasn’t established for HA ports
- Fortinet FortiGate - Routed port classification fix for L2 edges
- HP Aruba - `commands/_osVersions/showVersion` - fixed parsing for
  Aruba Mobility Master and Mobility Controller.
- HP Aruba - Mobility Master - platform and LLDP parsing fixed
- HP Aruba 7200 - Fix parsing for APs that dont respond to
  `show ap debug system-status ap-name <apName> command`.
- HP Aruba CX - fixed memory parsing
- HP Aruba CX - fixed parsing for `show vsx brief` with state in
  sync-primary
- HP Aruba CX - fixed parsing of `show interface` command with
  different output structure
- HP Aruba CX - fixed parsing of different output for command `show vsx status`
- HP Aruba CX - fixed parsing of property LAST in command `show ntp association`
- HP Aruba S3500-24P - `commands/hp/_aruba/inventory` - Fixed parsing
  of serial number for Aruba switch.
- HP Aruba switch - added parsing of the different output format of
  `show tech buffers` command
- HP Aruba switch - fixed parsing of different output for command
  `show spanning-tree`
- HP Aruba switch - fixed STP task mapping for RPVST for cases
  designated bridge ID is missing.
- HP ArubaCX - fix parsing of `show ip ospf neighbor detail` command
  in case priority is missing
- HP ArubaCX - fix parsing of command `show ip ospf interface` for
  cases local IP address is missing
- HP ArubaCX - fix parsing of command `show ip ospf interface` from
  Aruba OS version 10.07 and higher
- HP ArubaCX - fixed parsing of `show interface mgmt` in case mgmt
  interface is disabled
- HP ArubaCX - fixed parsing of `show ip ospf interface all-vrfs` and
  `show ip ospf neighbor detail` to not change VRF name to lower case
- HP ArubaCX - fixed uptime parsing (it isn't always provided)
- HP Comware - added support for another output format of `display arp` command
- HP Comware - fixed parsing of `display fan` command for the
  different output format
- HP Comware - fixed parsing of `display ip interface` command
- HP Comware - fixed parsing of `display power` command for the
  different output format
- HP Comware - fixed parsing of `display ospf interface verbose`
  command to support multiple areas for process ID and removed false
  positive error emitting in case there is configured process without
  any area
- HP Comware - fixed parsing of commands with large output (added cli
  clearing for Comware 3 format)
- HP Comware - tasks/l2Interfaces - fixed mapping of interfaces in
  case trunk doesn't contain any permitted vlans
- HP Comware 5130 - commands/hp/\_comware/currentConfiguration - AAA
  scheme fixed parsing for test-profile in aaa server configuration
- Juniper Junes - fixed parsing of different output for command `show configuration | display set`
- Juniper Junos - added parsing for another output format of command
  `show lldp neighbor`
- Juniper Junos - fixed false-positive error emitting in STP task for
  STP disabled interfaces
- Juniper Junos - fixed mapping of stacking for cases switch is not
  present (disconnected)
- Juniper Junos - fixed parsing of `show chassis environment` command
  to support different output format of fans
- Juniper Junos - fixed parsing of `show route` command for discarded
  routes
- Juniper Junos - fixed parsing of `show vrrp detail` command in case
  `version` is missing
- Juniper Junos - Fixed parsing of LLDP neighbors.
- Juniper Junos - fixed parsing of the routing table to parse
  correctly Administrative Distance and Metric
- Juniper Junos - fixed parsing of secondary address for command `show interfaces statistics detail`
- Juniper Junos - removed duplicates in the routing table
- Mikrotik RB1100 - Fixed parsing for command `ip ipsec installed-sa print detail`
- Mikrotik RouterOS - fixed parsing of IP addresses of
  actual-interface in command 'ip address print detail'
- Palo Alto - fixed parsing of different output for command `show routing route`
- Palo Alto, F5 clusters - Fix for establishing routing protocol edges
- Paloalto - fixed parsing for the routing table.
- PaloAlto 5200 - `commands/paloalto/showConfigMerged` - fix parsing,
  when vsys has no configuration
- Pathlookup - STP edge between switch and firewall in a cluster with
  virtual mac fix
- Routing table recursive lookup for VXLAN and other forwarding
  properties fix
- STP topology fix for port role master
- Versa VOS - Fixed BGP task mapping for cases total received Pfx is
  not available.
- Versa VOS - fixed mapping of API endpoint
  `/vnms/dashboard/appliance/<appliance>/live?command=ospf/interface/int-extensive`
- Wrong MAC address classification as a phone for proxy ARP fix.
