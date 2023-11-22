---
description: In this section, IP Fabric publishes previous version releases of NIMPEE v2.x.x
---

# NIMPEE v2.x.x

## NIMPEE v2.x.x

### 2.4.0 (27th February 2019)

#### Features - Protocol and technology support

- Collecting SNMP configuration for all vendor/families
  - Technology => Management => SNMP
- Collecting Netflow / IPFIX, sFlow configuration for all
  vendor/families
  - Technology => Management => Flow
- Added VXLAN support for Cisco IOS-XE, NX-OS, Arista EOS
  - Technology => VXLAN
- Added BGP support for Arista EOS
- Added NTP support for Arista EOS, ArubaSW, Huawei, F5
- Added OSPF support for Arista EOS, Check Point Gaia, Cisco ASA,
  Extreme XOS, Fortinet FortiGate, Huawei VRP, PaloAlto
- Added Routing table summary for Arista EOS, Extreme XOS, Huawei VRP,
  Check Point, Cisco ASA
- Added VRRP support for Fortinet FortiGate
- Configuration Management - added support for Fortinet FortiGate,
  Extreme XOS
- Added overview of local and remote logging targets configured on
  network devices
  - Technology => Management => Logging
- BGP address family support (new tables with all session families).
  - Technology => Routing => BGP => Address Families (table is also
    available after click from graph on BGP edge)

#### Features - Visualization

- Significant speedup of graph for big networks
- Added VXLAN as L3 protocol
- Host to GW - "show only active devices" option added, it will
  display only devices in the path
- Path lookup - Asymmetry check is evaluated based on the layer
  instead of a protocol.
- Graph RIB edges - L2 switches have default GW route disabled by
  default. Can be enabled in RIB protocol settings
- Unmanaged devices can now be added and displayed, even if connected
  edges are not visible.

#### Discovery

- Shaper was limited to 10Mb

#### Improvements

- Discovery page - statistic about how many devices were discovered is
  without AP now
- Added support for Cisco Mobility Express WLC detection
- Site separation by regex - you can specify the transformation of
  hostnames before regex separation is used. It solves a situation
  when is used mix uppercase/lowercase hostnames in the network.
- Arista vEOS version detection improvement
- Juniper ISIS - added support for any other level than 1 or 2
- Juniper Loopback interfaces lo0.16384, lo0.16385, lo0.32768 are
  internal auxiliary loopbacks and are not included in discovery.
- Fortinet FortiGate - improved version detection for devices running
  with FortiOS6
- Fortinet FortiGate - improved prompt detection in case that prompt
  ends with $
- Cisco IOS/XE/XR - Updated next-hop evaluation for CEF/MPLS records
- Cisco SG300 - Added support for different show version output
- Huawei - added NTP support on Huawei VRP 8.x
- Huawei - xDP interface names correctly standardized
- Huawei - Routing table sanitation (127.0.0.0 and 0.0.0.0 next-hop
  removed)
- HP Aruba AP, F5 - added missing memory information
- HP Aruba switch/Procurve - OS detection - added support for
  2600/2300/2500 platforms
- HP Aruba switch/Procurve - Localhost routes removed from the routing
  table
- Routing stability table - Added connected routes

#### Bug Fixes

- Virtual gateways count in tables fixed.
- Path lookup - Edge switch must be in the same site as default gw
  (fixes wrong edge switch selection because of virtual mac addresses)
- Router to switch L2 connection - Fix for routers with virtual mac
  addresses
- Cisco IOS - MPLS forwarding table fixed parsing - output for one
  record can be broke to more lines
- Cisco IOS, IOS-XE w/o routing table - default gw entry adds
  interface now
- Cisco IOS - fixed parsing `show environment all` command
- Cisco IOS - ACL - role based trustsec entries are ignored until
  trustsec support will be added.
- Cisco IOS-XR duplicate hsrp virtual addresses fixed
- Cisco NX - improved parsing "show environment fex all" when it
  returns "FEX is not present"
- Cisco ASA - routing table fixed parsing
- Cisco XR - improved parsing for `show mpls ldp vrf \<instance>
neighbor detail` command
- Cisco IOS-XE OSPF interfaces fixed parsing for the unnumbered tunnel
  interface
- Cisco MPLS LDP - updated parsing for LDP neighbor with no source
  interface
- Cisco QOS policy-map interface - improved parsing for different
  command output
- Cisco IOS-XE 3560 - show version stack inventory parsing fix.
- Cisco SG - fixed parsing of different output for STP detail command
- ExtremeXOS - MTU wasn't parsed on ExtremeXOS 22.5.1.7
- Path lookup - FEX on access fixed
- Arista vEOS - missing SN is replaced by system mac address
- Arista vEOS - interface unconfigured speed parsing fix
- Arista vEOS - arp N/A timer parsing fix
- Arista vEOS - interfaces MTU parsing fix
- Arista vEOS - parsing fix when NTP is disabled
- Extreme XOS - memory information fixed parsing
- Check Point Gaia - fixed parsing of different output for command `fw
ctl pstat`
- Fortinet FortiGate - fixed ambiguous command to get info about the
  routing table
- Fortinet FortiGate - fixed parsing for different output about memory
  information on FortiOS6
- HP Aruba switch - fixed NTP associations
- HP Aruba switch - Reported CDP devices without capabilities fix
- HP Aruba switch - Non-complete interface record parsing fix
- HP Aruba switch - show tech buffers command parsing fix
- HP Aruba v8 fixed parsing to get details about AP
- HP Comware fixed parsing of different output for device interfaces
- HP Comware fixed parsing of different output for
  linkAggregationVerbose command
- Huawei VRP - fixed ambiguous command for observer port command
- Juniper - SRX firewall/router mode detection, the default is
  firewall when no relevant output is available
- Tables - FIX filtering in columns where is able to switch property
  for filtering i.e. NAT - Rules
- Tables - Filter rules were inserted randomly after the seventh rule
- Tables - some tables had wrong values for export into CSV (Object
  Object)

### 2.3.1 (7th December)

#### Improvements

- Path lookup - improved calculation for the default gateway
- Cisco ASA serial number detection updated to better support
  virtualized devices
- Cisco NX - improved parsing for FEX information
- Cisco IOS/IOS-XE - improved parsing for `show monitor detail`
  command
- Cisco NX - improved parsing for `show monitor session all` command

#### Bug Fixes

- Cisco NX 7K - fixed parsing of version, VDC wasn't recognized
- Juniper JunOS - fixed parsing pf memory information

### 2.3.0 (5th December)

#### Features - Protocol and technology support

- Added FHRP support for HP Aruba/ArubaSw, Huawei VRP, Arista EOS,
  Cisco XR
- Added support for FEX modules connected to Cisco Nexus 7000 series
  switches
- Added support for environmental information for Cisco Nexus FEX
  modules
- Added support for MPLS & LDP protocol for Cisco
  IOS/IOS-XE/IOS-XR/NX, Juniper
  - New tables in Technology => MPLS
- Added support for Port Mirroring for Cisco IOS/IOS-XE/NX/SG, Juniper
  JunOS, HP Comware, Huawei VRP
  - New table in Technology => Management => Port Mirroring
- Added support for NAT for Cisco IOS/IOS-XE/ASA
  - New tables in Technology => Addressing => NAT

#### Features - Visualization

- Default view - each user can define own default view instead of
  displaying overall network topology
- Added MPLS support in path lookup & LDP protocol for edges
- Enhanced orientation in diagrams - when is graph opened through the
  link on hostname column then the graph will be zoomed in to the
  device.
- Site interconnections are now displayed separately from generic
  transit
- The site can be renamed directly from a graph (only for uses with
  write privilege)
- Window details dialogs are now open in a direction where is more
  space, better UX.
- Protocol CEF was renamed to RIB and CDP to xDP
- Unmanaged neighbors and Transit edge are now the same types of
  neighbors. They can be grouped using prefix length setting under
  Options > Site edge

#### Features - Discovery

- New Settings - OUI, where can be enabled/disabled vendors what will
  be used in discovery from ARP protocol.
- Cisco SG300 family - added support for SF switch line

#### Improvements

- Inventory/devices added columns Total memory, Used memory, Memory
  Utilization %
- Enable to searching in ACL/Zone policies using IP or network

#### Bug Fixes

- Switch to router L2 connections - Mismatch duplicated connections
  created on the router with same mac address on all ports. Fixed when
  xDP exists between switch and router.
- Graph - all graph icons are preloaded into cache now, this fixing
  situation when was generated Site Low-Level design report and graphs
  were without icons.
- Report Site Low-Level graph could be generated as corrupted docx
  (not escape data in XML)
- The app could crash in IE - Inventory/Sites when Site report was
  downloaded and then was tried to load Site Diagram then the App
  crashed - fixed (It's highly recommended to use Chrome, instead IE.
  Chrome has much better performance)
- Cisco NX - LLDP - capabilities 'not advertised' were not parsed
  correctly, some server entries without destination port were added
  incorrectly.
- Cisco NX - fixed parsing of `show fex detail` command
- Cisco NX 5000 - power supply failure from environment fix
- Cisco NX ACL options - generic support for 'divert' option added
- Cisco EIGRP - Ambiguous command fixed on ASR9000
- Cisco EIGRP - Fixed parsing when enabled but no neighbors detected
- Cisco BGP - DMPVPN no families fix
- Cisco IOS-XR OSPF parsing fix when an interface is down
- Cisco IOS-XE OSPF neighbor parsing fix (output may differ per
  version)
- Cisco IOS/IOS-XE: RIP - NVI interfaces are ignored now
- Cisco IOS/IOS-XE - Routing table - added support for default gateway
  detection e.g. on L2 switches
- Cisco AAA - extended support for AAA-related options and setting
- Cisco service object-groups - added support for ICMPv6 params
  parsing
- HP Comware - Ethernet 100Mbps interface parsing fix
- HP Comware - Routing table inactive next-hop removed
- F5 BigIP - VLAN interfaces state is now used from `list net self`
  command only
- xDP - if capability contains IGMP, then the neighbor is recognized
  as a network device
- User edge port and user mac address recognition improved with OUI
  network vendor.
- Scheduling of System Backup could fail and the process wasn't
  executed at all
- System backup - FTP directory was transformed to lowercase it could
  be a problem when the directory on FTP server was in uppercase.
- Dashboard - fixed Snapshot History widget for MAC's
- D-Link and Enterasys wrongly recognized as Aruba switch. Version
  parsing fixed.
- Routing table - recursive lookup for VRF leak fix
- Graphs - Host to gateway and path lookup default gateway selection
  fix (the mask is considered in calculation now)
- 802.1x interface authentication port control mode is now parsed from
  show run if it is not available in show dot1x command output
- Updated RIP neighborship mapping for JunOS routers

### 2.2.9 (31st October 2018)

#### Features - Analytics

- Path verification - you can now save a path for continuous
  verification
  - Saved paths are stored in Technology \\ Routing \\ Path
    verifications
- Path analysis - added support for Symmetry verification
- Path analysis - added support for L2 flooding
- Path analysis - added overview tab listing all matching filters and
  forwarding
- History - new widget in Dashboard displays the number of discovered
  devices and changes for each snapshot.

#### Features - Protocol and technology support

- Added vendor support for Arista EOS
- Added vendor support for HP Aruba switch / ProCurve
- Added vendor support for Huawei VRP
- Added vendor support for F5 BIG IP
- Detailed information about IS-IS protocol (support for Juniper
  JunOS)
  - New table Technology \\ Routing \\ IS-IS \\ Neighbors
  - New table Technology \\ Routing \\ IS-IS \\ Interfaces

#### Features - Visualization

- Network overview - protocols settings are now persistent
- Added MTU tab into window detail for OSPF, EIGRP, and RIP protocols
- Added IS-IS routing protocol visualization
- Improved wired hosts usability
- Specific routing protocol sessions to transit cloud are now shown
  when "Site edge" is turned on.
- New option added "Show edge devices only" which shows devices
  connecting to edge
- Improved overall graph performance

#### Features - Discovery

- Discovery - Added DNS Name column to Error Report (DNS Resolve has
  to be enabled in Settings).

#### Improvements and Bug Fixes

- Site separation - R&S option site name swapping fix
- Routing table - fixed recursive NH interface lookup
- Graph - position of transit cloud in the network overview is now
  saved
- Graph Path lookup - Forwarding L2 switch to an unknown neighbor
- Router with only one route and ATM interface was recognized as
  'host'
- Path lookup - Default GW forwarding fix
- BGP neighbors uptime column is now properly formatted
- Cisco IOS OSPF neighbors parsing fix
- Cisco IOS/IOS-XE/IOS-XR BGP neighbors parsing fix
- Cisco IOS-XE Auth session parsing fix (different header and no
  session output for interface cmd)
- Cisco IOS-XE 3850 - version parsing fix
- Cisco Catalyst 9300 - version parsing fix
- Cisco IOS-XE VRRP parsing fix
- Cisco IOS fixed ACL parsing
- Cisco IOS BGP dynamic neighbor address parsing fix
- Cisco Updated local IP address information for EIGRP neighbors for
  unnumbered interfaces.
- Cisco - IPv4 Unicast address group for BGP neighbors accepts only
  IPv4 records.
- Juniper JunOS - correctly detects SRX device in packet mode as
  router device type
- HP Comware BGP neighbor idle parsing fix
- HP Comware platform a-msr30 wasn't discovered
- HP Aruba - fixed version detection, enable command now trying all
  combination from enabling password list
- Riverbed CMC - version parsing fix
- Riverbed updated telnet access information.
- Juniper BGP neighbor session time parsing fix
- Scheduled snapshots do not work, wasn't rescheduled on error
- Discovery - enable password list wasn't sorted by priority
- Mac table - NX-OS vPC peer link support added

### 2.2.8 (10th September 2018)

#### Features - Analytics

- Detailed information about all Unmanaged Neighbors
  - New table Technology \\ Interfaces \\ Connectivity Matrix \\
    Unmanaged Neighbors Summary
  - New table Technology \\ Interfaces \\ Connectivity Matrix \\
    Unmanaged Neighbors Detail

**Features - Protocol and technology support**

- BGP protocol support for HP Comware
- Detailed information about EIGRP protocol (support for Cisco IOS,
  IOS-XE, IOS-XR, NX-OS)
  - New table Technology \\ Routing \\ EIGRP \\ Neighbors
  - New table Technology \\ Routing \\ EIGRP \\ Interfaces
- Detailed information about RIP protocol (support for Cisco IOS,
  IOS-XE, IOS-XR, NX-OS, HP Comware, Juniper JunOS)
  - New table Technology \\ Routing \\ RIP \\ Neighbors
  - New table Technology \\ Routing \\ RIP \\ Interfaces

**Features - Visualization**

- The NEW design of edges between the nodes, you can switch between
  "Curved" and "Straight" (new) type in Protocols menu
- Added EIGRP routing protocol
- Added RIP routing protocol
- OSPF & BGP & EIGRP & RIP protocols added into overall network
  overview
- MTU Check - edges are colorized according to colorization rules in
  table Technology / Interfaces / MTU. If there is no colorization
  rule then the color will follow these rules
  - green - MTU is the same on both sides
  - red - MTU is not the same on both sides
  - gray - one if the MTU values are empty.
- Path lookup - Zone Firewall matching rules table
- Path lookup - each forwarding decision can be highlighted in a graph
  for a selected node. See forwarding tab
- Path lookup - the devices where the packet is stopped because
  security rules (ACL, Zone FW) are now red.
- Unmanaged neighbors - also displaying unmanaged neighbors from
  routing protocols
- Additional information can be added for labels, for example,
  Interface Media, Interface IP, Subnet, STP path cost, AS for
  BGP/EIGRP, etc.
- "Non-redundant devices" option has been renamed to "Single points of
  failure"

**Features - System**

- NIMPEE setup wizard added
- NIMPEE UI will inform you when not enough space on disk remaining
- Added SFTP as a destination for backups
- System Update - Added "upload offline upgrade package" button even
  if Callhome server is reachable

**Features - Discovery**

- Riverbed Steelhead - in some cases CLI output had an escape sequence
  what broke a device prompt detection.
- Discovery - Connectivity Report - added column DNS Name - the
  resolved name of the IP address (DNS Resolve has to be enabled in
  Settings).

**Improvements and Bug Fixes**

- Tables - new advanced filter operator "has the color", so you can
  filtering on column what has some color and add next filter rule for
  the same column to get a specific result.
- Site Separation - the process could fail when using a regex for
  separation, and one of the sites was previously renamed.
- STP - inconsistencies Multiple STP & Vlans without STP: false
  positives fix
- Juniper JunOS - Hostname representing chassis cluster is now derived
  from the active node.
- CDP/LLDP devices with phone capabilities were recognized as a
  network device.
- Host to the gateway - FW as default GW added
- Port-channel with member port XDP is not now edged port
- Fixed mapping of results for BGP tasks
- End to End path lookup - connected host mac address is now taken
  from gateway ARP.
- STP - inconsistencies Multiple STP & Vlans without STP false
  positive fix
- FIXED DNS resolving of Discovered inventory
- Scheduled backup with destination FTP failed, the credentials
  weren't decrypted
- Fixed NTP information - Correct parsing of GNSS reference, stratum
  \< 16 as check for reach-ability
- Cisco Nexus 7000 admin VDC NTP copy to other VDC (system clock is
  controlled only from one VDC)
- Cisco IOS - fixed reported parsing bugs for command `show ip access-list`
- Cisco IOS - fixed reported parsing bugs for command `show bgp all neighbor`
- Cisco IOS - fixed reported parsing bugs for command `show bgp all summary`
- Cisco IOS - parsing fix dynamic cluster-HSRP/NAT acl rules
- Cisco IOS - fixed reported parsing bugs for command `show ip ospf neighbor detail`
- Cisco IOS - auth session parsing fix when no output is available
- Cisco WLC - fixed processing of pagination
- Cisco WLC - fixed reported parsing bugs for command `show ap config
802.11a summary`
- Cisco WLC - fixed reported parsing bugs for command `show ap config
802.11b summary`
- Cisco WLC - fixed reported parsing bugs for command `show ap wlan
802.11a \<apName>`
- Cisco WLC - fixed reported parsing bugs for command `show ap wlan
802.11b \<apName>`
- Cisco WLC - fixed reported parsing bugs for command `show ap
inventory \<apName>`
- Cisco WLC - fixed reported parsing bugs for command `show network
summary`
- Cisco NX-OS - fixed reported parsing bugs for command `show
interface status err-disabled`
- Cisco NX-OS - fixed reported parsing bugs for command `show ip ospf
interface vrf all`
- Cisco NX-OS - fixed reported parsing bugs for command `show
access-list summary` (IPv6 entries).
- Cisco NX-OS - fixed reported parsing bugs for command `show ip ospf
interface vrf all`
- Cisco IOS-XE (Catalyst) - fixed parsing of `show version` when stack
  switch has "Unknown" uptime
- Cisco fixed parsing of command `show ospf neighbor detail`. OSPF
  areas can be represented by either number or CIDR
- Cisco ASA parsing fix for routing table - age and interface for
  dynamic routing protocols
- Cisco IOS - LLDP/CDP neighbor interface for phone fix
- HP Aruba - fixed reported parsing bugs for command `show ap
bss-table`
- HP Comware - fixed reported parsing bugs for command `display ospf
peer verbose`

### 2.2.7 (31st July 2018)

**Features - Analytics**

- Technology / Security / Secure ports - 802.1x / Users - added
  information about authorized user. Columns Username, User MAC, User
  method, User state

**Features - Protocol and technology support**

- Detailed information about BGP protocol (support for Cisco IOS,
  IOS-XE, IOS-XR, NX-OS, Juniper JunOS)
  - New table Technology \\ Routing \\ BGP \\ Neighbors
- Collecting information about MTU on interfaces
  - Added MTU column into Inventory\\Interfaces
  - New table Technology \\ Interfaces \\ MTU
  - Added MTU consistency check into Diagrams
- Collecting information about NTP
  - New tables Management \\ NTP
- Collecting information about Wireless Radios on Wireless Access
  Points
  - New table Technology \\ Wireless \\ Radios/BSSID
- Cisco IOS-XR collecting information about OSPF protocol

**Features - Visualization**

- Host to gateway lookup is part of Network graph now and display the
  path over the network location
- Added option to display/hide Wireless Access Points - AP is disabled
  by default
- Align & Distribute menu which helps to quickly arrange multiple
  selected nodes
- New options "MTU checks" to check MTU consistency
- Path lookup - ACL implicit rules added to a matching table, show
  details button added
- End to end path lookup possibility to specify TCP Flags in packet
- Added BGP routing protocol
- Added OSPF routing protocol

**Features - System**

**Features - Discovery**

- Extreme XOS - in some cases CLI output had an escape sequence what
  broke device prompt detection.

**Improvements and Bug Fixes**

- Tables
  - added button what prepare a link for sharing of current table
    view
  - Table header can be seen as fixed (sticky) when scrolling
  - new advanced filter operator - not equal to a column
- Management / Changes - Speed up of the table for snapshot selection
- Juniper JunOS Description for interfaces is now available in NIMPEE.
- Juniper JunOS added MAC address for logical interfaces.
- Juniper JunOS Fixed parsing of routing table with MPLS records
- Juniper JunOS show ethernet-switching interfaces changed to an
  interface for compatibility with newer platforms
- Juniper JunOS Updated routing engine schema for EX3400
- Cisco - Secured Access ports - fixed parsing for ports with MAB only
  clients, changed command for IOS c2960c405
- Cisco WLC - fixed getting of hostname for HA cluster
- Cisco object-group parsing fix - support for new protocol names
  added
- Cisco IOS - fixed ambiguous command & parsing for Power & Fan
  environment
- Cisco IOS - fixed authentication session interface command for
  version higher than 15.2
- Cisco IOS - fixed mapping of state for HSRP output
- Cisco ASA - fixed parsing of a routing table
- Cisco ASA - fixed parsing of `show version` command, missing SN for
  the particular switch in stacking information
- Cisco ASA - ACL is now read from configuration (using regular
  commands was too expensive)
- Cisco NX-OS - the fixed end to end path lookup for routes with
  default VRF
- Cisco NX-OS - fixed system version parsing
- Cisco NX-OS - fixed parsing of `show access-list summary` command
- Extreme switch SN - if not present chassis or switch in inventory,
  then SN is taken from the first available slot
- FIX: If the server was restarted during the discovery process then
  the discovery process was stuck after server restart.

### 2.2.6 (2nd July 2018)

**Features - Analytics**

- Greatly improved support of security rules interpretation for
  Juniper, Cisco, and HP Comware
- Added default & global policies for Zone-based firewalls

**Features - Protocol and technology support**

- Added collection of ARP and MAC tables for HP Aruba
- Added collection of routing information for Cisco XR
- Added object-groups support for Cisco and HP Comware

**Features - Visualization**

- E2E Path & Site separation no longer reset the view upon close
- Width of the grouped links in the diagram is increased
  logarithmically according to the count
- Details in window components - The component can be moved outside of
  the screen and it will be minimized when it’s released outside of
  the screen
- Graphs - Hub meshing is now restricted to Tunnel and VLAN interfaces

**Features - System**

- Updated EoX reports for Cisco & Juniper
- Customer credentials are no longer needed for updates over the
  Internet

**Features - Discovery**

- Connectivity report - added a new report for Ambiguous or Incomplete
  command error
- Cisco WLC - added support for WLC unit type detection in HA
- Full BGP routing table handling - an Added setting which enables to
  skip downloading of BGP routes if the router has more BGP routes
  than the threshold

**Improvements and Bug Fixes**

- Cisco WLC APs without configured IP address will now appear in
  discovery with IP of 0.0.0.0
- Cisco NX-OS fixed parsing of environment variables
- Cisco SG300 switch port trunk VLAN parsing fix
- Cisco ASA - fixed parsing of SN when Chassis information is not
  available
- Fixed parsing for OSPF neighbors, neighbor ID can be device name.
- HP Aruba allows connecting AP to internal switch (fixing AP
  location)
- HP Comware 850 WLC - AP interface name and VRF fix
- HP Comware 7 fixed processing of L2 interfaces
- HP Comware - display license command is sent only for virtual
  platforms to get the SN
- Juniper JunOS fixed ethernetSwitchningInterfaceDetail parsing error
  when untagged VLAN is unavailable
- Juniper JunOS Command Route - updated parsing of access-internal
  routes
- Juniper JunOS Updated mapping for routing table (multi discard
  flag).
- Juniper JunOS fixed mapping for task SecureAccessPort
- Extreme XOS - fixed parsing of OS version
- Riverbed L3 interfaces fixed task mapping
- Fixed processing of CLI pagination for corner cases and improved
  detection
- Fixed CLI output download, which was not available in some cases
- Fixed Configuration Management scheduling component which didn’t
  remember the selected date(s) for Every week option
- Tasker - fixed memory overflow bug when finishing jobs (Topology
  build could fail in big network with multiple Full BGP routers)
- Updater would fail upon discovered of multi-homed AP with clients
- Diagrams - Grouped protocols had a wrong arrows direction
- Diagrams - Fixed shifted protocol labels in PNG Export
- Table Inventory / Hosts added PoE column (hidden by default)

### 2.2.5 (12th Jun 2018)

**Features - Analytics**

- Added STP pseudo-link between routers and switches not to rely on
  CDP/LLDP
- HSRP, VRRP, and GLBP are now under FHRP menu.
- Added preemption and protocol information to FHRP table.

**Features - Protocol and technology support**

- Added vendor support for Extreme XOS
- Added wireless support for HP830/850
- Added support for CISCO GLBP & VRRP
- Added support for Cisco ASA contexts
- Added voice gateway device type
- Added support for Cisco Nexus environmental parameters

**Features - Visualization**

- E2E Path lookup is part of Network graph now and displays the path
  over the network locations
- The tooltips are replaced with drag & drop windows which enable to
  display more valuable information directly in the graph

**Features - System**

- NIMPEE VM can now be restarted or shut down from System
  Administration interface
- System Administration - added option for restarting API
- New support portal - <http://support.ipfabric.io/>

**Features - Discovery**

- Significantly improved discovery error detection and reporting
- Detailed communication logs are now available in Connectivity Report
  / Error reports & in each table with Hostname detail (only for user
  with Settings privileges)
- XDP (Discovery Protocols) now consider only neighbors with
  capabilities "router" or ("switch" or "bridge" but excluding "phone"
  or "host")

**Improvements and Bug Fixes**

- Juniper/JunOS ARP records weren’t used as discovery targets

- Juniper/JunOS Zone FW is now collected from configuration (fixing
  100% CPU BUG)

- Configuration management no longer attempts to download
  configuration of Wireless APs

- Forms with password field shouldn’t prefill a passwords

- LDAP authentication now supports multiple LDAP servers for a domain

- Firewalls are now included in the routing domain calculation

- STP between switch and router for site calculation and graphs

- Site recalculation - delete STP topology before start

- Voice GW 224 device type

- Added Vendor column to /inventory/hosts table

- Improved Cisco VRRP support

- Translated Cisco NX-OS routing protocol into a standard name

- DOWNLOAD configuration file in
  /technology/management/saved-config-consistency can’t be sanitized.

- Moved Table /reports/end-of-life-milestones to
  /inventory/end-of-life-milestones

- Local IP now inserted into ARP table for a platform which doesn’t
  show local ARP entries

- AP without CDP/LLDP is now connected to switch with pseudo-STP link

- Removed duplicate tables that served as dedicated checks, since now
  each table can have any number of checks using table colors
  (reports)

  - `/dashboard/risk/device-stability` (now a color in `/inventory/devices`)
  - `/dashboard/risk/eox` (duplicate of `/inventory/end-of-life-milestones`)
  - `/dashboard/risk/err-disabled` (duplicate of `/technology/interfaces/errdisabled`)
  - `/dashboard/risk/outbound-balancing` (duplicate of `/technology/port-channels/outbound-balancing-table`)
  - `/dashboard/risk/routing-stability` (duplicate of `/technology/routing/route-stability`)
  - `/dashboard/risk/stp-stability` (now a color in `/technology/spanning-tree/stp-instances`)
  - `/technology/addressing/host-ip` (duplicate of `/inventory/hosts`)
  - `/technology/management/config-register` (now a color in `/inventory/devices`)
  - `/technology/management/os-version-consistency` (duplicate of `/inventory/os-versions`)
  - `/technology/management/unexpected-reloads` (now a color in `/inventory/devices`)

- Fixed Cisco ASA parsing of empty localL4connections

- Fixed parsing of 802.1X details for Cisco IOS-XE

- Fixed parsing of auth sess int \<int> detail command for Cisco
  IOS-XE

- Fixed parsing of 802.1X client list and sessionId for Cisco IOS

- Fixed parsing of ARP entries for HP/Comware

- Fixed processing port security command for HP/Comware when it isn’t
  configured

- Fixed updater failing on validation of Zone FW rules

- Fixed discovery of Juniper/JunOS from ARP entries

- Fixed routing table flags parsing for Juniper/JunOS

- Fixed parsing of non-active routes for Juniper/JunOS

- Fixed ARP parsing of incomplete entries for Palo Alto

- Fixed parsing of Cisco policy-maps under certain conditions

- Fixed parsing of Cisco interfaces and IP interfaces under certain
  conditions

- Fixed parsing of Juniper/JunOS configuration firewall command

- Disabled sanitization of configuration files for Saved Configuration
  Consistency checks

### 2.2.4 (14th May 2018)

Migration to this version can take a long time, depending on the amount
of history collected.

**Features - Analytics**

- End to End path lookups now enable to lookup any IP or Hostname
  directly from the source or destination field
- End to End path lookup now support L4 protocols and ports
- End to End path lookup now supports Zone Firewall rules
- Improved routing next hop analysis in the cumulative routing table
- Improved 802.1x analysis
- Added DNS resolution to hosts
- Added voice VLAN for VoIP phones

**Features - Protocol and technology support**

- Added support for Juniper SRX clusters (platforms)
- Added support for Firewall Zones (security)
- Added support for STP Guards (spanning tree)

**Features - Visualization**

- Small sites (less than 5 devices) are now grouped into redundant and
  non-redundant groups.
- Individual STP instances can now be hidden through Objects diagram
  menu
- L2/L3 boundary is now enhanced through MAC lookup between router and
  switch using VLAN, ARP, and MAC (now still marked as `stp`)

**Features - System**

- Added LDAP support for user authentication (supported Open LDAP,
  Microsoft AD)

**Features - Discovery**

- Discovery connectivity report now contains vendor column for
  connection attempts from ARP entries
- Discovery from XDP protocols now considers only neighbor with
  capabilities "router", "switch", or "bridge"
- SSH/TELNET authentication credentials can now be limited to a
  specific subnet

**Improvements and Bug Fixes**

- Significant performance boost for a historical snapshot comparison
- Fixed Cisco 6500 OS version detection for certain variants
- Fixed parsing of LLDP capabilities for Cisco SG
- Fixed inventory parsing of certain Catalyst 4500 Sup8 IOS-XE
  variants

### 2.2.3 (10th April 2018)

**Features**

- TACACS Authentication failure retries settings -
  SettingsAdvancedSSH-Telnet
- The sites can be separated from the diagram (requires site detection
  using Routing & Switching)
- Site names automatically derived from hostnames when sites detected
  using Routing & Switching
- Discovery service windows have download log button
- Speed improvements for Spanning Tree and QoS information
- Tables now allow filtering using regex using =\~ operator in
  addition to advanced filters
- Diagrams - automatic meshing for sites with over 200 meshable edges
- Diagrams - Spanning Tree tooltips for the failure domain now
  consider VLANs active on a link

**System Features**

- Crypto image option (encrypted disk)
- OS security updates
- Service health check and auto healing for failed application
  services (arangodb, nimpeeAPI, nimpeeUpdate, syslogUpdater,
  syslogWorker)
- Short DNS name in web certificate CSR can be removed

**BugFixes**

- Routing domains are now separated by sites
- Switches with one default route are not calculated into the routing
  domain
- Port-channel members with STP are not considered network edge
- Phone and AP ports are considered network edge
- EOL reports for Juniper had incorrect data
- IP Phones are now detected using MAC in addition to LLDP/CDP
- Discovery pages now always display Connectivity Report button
- Tables - fixed CSV export for colored cells
- Juniper & HP routing protocol types translation to a standard format
- Calculate affected users - fixed root computation
- Cisco - crypto session command - parsing fix
- Cisco SG300 - ARP, L2 interface, and Loopback collection fix
- PaloAlto - environment Power & Fan validation fix
- Juniper - added support for multiple neighbors on a single interface
- Tech support decryption was failing when file size was less than 1MB

### 2.2.2 (26th March 2018)

**Features**

- Dashboard - Table colors - the order of assigned color rules can be
  arranged (use drag&drop)
- Added more predefined verification checks & updated Dashboard view
- Diagrams - more information in the tooltip for STP edges
- Tables - Colorize rules - fade out the background for results with
  value ‘0’

**BugFixes**

- Predefined Advanced Filters was deleted by next Discovery start
- Filtering any tables for the selected site
- Diagrams - export PNG for end2end path lookup and host2gateway
  didn’t work
- Diagrams - the tooltips for ACL/QoS were not showing
- Fixed an error when manually uploading an update package
- Fixed API endpoints for TechnologyPlatformsVDC &
  TechnologyPlatformsVPC
- Wireless access point impact is calculated now only from errors and
  drops on wired interfaces
- Cisco SG300 spanning-tree is now correctly parsed and saved
- FortiGate hostname saved when no authorization is allowed

### 2.2.1 (21st March 2018)

**BugFixes**

- Report - Site Low-Level report - some cases had bug during
  generation
- Report - Network Analysis report showed duplicate percentage under
  radar charts
- Fortinet hostname not visible
- Mac self entries not considered as a switch
- TechSupport file - download doesn’t work
- TechSupport file doesn’t contain discovery and CLI logs
- TechSupport file doesn’t contain the most recent archived CLI logs
- TechSupport file doesn’t contain NIMPEE system logs

### 2.2.0 (19th March 2018)

**Features**

- Colorizing tables using custom filters rules
- The dashboard is fully customizable
- Site separation now allows OR conditions in regex
- Site recalculation can be now performed without a new discovery
  process
- Discovery seed - IP networks can now be added as seed (currently
  limited to /24)
- Diagrams - performance optimizations
- Diagrams - Network - added mask separation option for transit
  networks
- Diagrams - new UI for protocol menu
- Diagrams - moved link grouping and layer grouping options to
  protocol menu
- Diagrams - Network - multiple items can now be selected using CTRL
  key

**System Features**

- Added system interface accessible using system account
- Integrated backup & restore (currently local or FTP target)
- NIMPEE can now be updated over the Internet or by uploading an
  update package

**Vendor Support**

- FortiGate
- Palo Alto
- Juniper - JunOS OS
- Cisco wireless - added support for new wireless access point
  AIR-AP2802I
- HP 830 Unified Wired-WLAN platform - (Interface parsing, without
  wireless features)

**BugFixes**

- Diagrams - Network - nodes without edges now remains visible in the
  graph
- Diagrams - Network - sites can now be added/removed in parallel
- Check Point - Added support for ‘expert’ mode
- Cisco ASA - routing table parsing issue fixed
- Cisco - Wireless added support for clients in ‘start’ state
- Cisco C1900 Routing table parsing issue fixed
- Cisco Environment parsing fix on some IOS platforms
- HP Comware - fixed parsing STP in MSTP mode

### 2.1.2 (19th January 2018)

**Features**

- New audit check **Technology - Spanning Tree - Inconsistencies -
  Neighbors ports VLAN mismatch**
- New audit check **Technology - Spanning Tree - Inconsistencies -
  Ports with multiple neighbors**
- New audit check **Technology - Spanning Tree - Inconsistencies -
  STP/CDP ports mismatch**
- New audit check **Technology - Spanning Tree - Inconsistencies -
  Multiple STP between two devices**
- New audit check **Technology - Interfaces - Duplex** Half duplex
  table replaced with Duplex mismatch table.
- New technology table **Technology - Security - 802.1x -
  Devices** displays grouped data about 802.1x per device.
- New technology table **Technology - Platforms - Stacks** displays
  grouped data about stacks per device.
- Improved overview **Technology - Platforms - Stacks - Members** new
  connectionsCount column, popup with information for hostname, link
  to open site diagram.
- Improved overview **Technology - Platforms - Stacks -
  Connections** new membersCount column, popup with information for
  hostname and interface.
- Added support for relayed Syslog messages
- Improved diagram performance
- Improved diagrams **Diagrams - Network** - added "ignore filters"
  option to allow displaying of a single device with no known
  connections
- Improved diagrams **Diagrams - Network** - added show utilization
  option
- Improved diagrams **Diagrams - Network** - updated site presentation
- Improved diagrams **Diagrams - Network** - tunnels between sites are
  now displayed in the network overview
- Improved diagrams **Diagrams - Network** - added caching for
  redrawing which removes device jumping when redrawing
- Improved Web UI - Enabled searching in quick sites filtering (top
  left corner)
- Improved diagrams UI - enabled searching in the list of sites,
  routing domains, and switching domains
- Settings - Authentication - disable browser popup to save passwords
- Sites calculation type "Routing & Switching domain" change to
  sticky. Now using an intersection of previously found serials
  numbers with new ones. Previously renamed sites before this release
  will be discarded without a migration script.

**BugFixes**

- CLI parsing - Fixed false prompt detection when was used ">" char in
  the interface description
- CLI parsing - Cisco NXOS - fixed parsing of the routing table for
  local routes
- CLI parsing - fixed WLC platform AIR-C25xx
- Updater service - heap out of memory fixed
- port with CDP AP considered as an edge
- Remove phone capability in CDP/LLDP send from some Nexus platforms
- Configuration Management - Fixed false positives, which erroneously
  showed changes in configuration, when in fact none have occurred.
  (Line break n vs rn)
- Diagrams - Fixed label boxes disappeared after hiding
- Diagrams - Fixed search
- Diagrams - Fixed link overlapping in the network view
- Diagrams - Network - removed impact option
- Diagrams - labels in the export image are always visible
- Table **Technology - Interfaces - Switchport** Edge column displayed
  wrong values
- Table **Reports - Site Low-Level Design** column siteName was wrong
  after the site renaming
- Site Low-Level Design - Report: siteName was wrong after the site
  renaming
- Site Low-Level Design - Report: if user arranges a site diagram then
  the diagram in a report also rendered according to this positions.
- Web UI - Fixed generation of TechSupport file, which could fail with
  a large data set
- Web UI - Some messages of informative character was displayed as
  critical messages (red color).
- Routing domains calculation fix - protocols forming domains were not
  correctly filtered

### 2.1.1 (5th January 2018)

**Features**

- The component for scheduling **snapshots** and **configuration
  management**
- **Technology - Management - Saved config consistency** display diff
  directly in the table, instead of on a new page
- **Technology - Interfaces - Switchport** added columns **Access Mode
  Vlan**, **Voice Vlan**
- **Technology - Wireless - Access points** added
  column **Mac**, **Impact**
- The columns labels & help is now used in the search.
- HP Aruba - more detailed error & drop counters

**BugFixes**

- HP Aruba - fixed parsing of wireless clients
- The discovery process stuck when DNS resolve was enabled.
- Telnet client - fixed negotiation for IOS XR
- Cisco IOS-XE 3.04.06 fixed parsing of environment/stuck command
- Cisco IOS-XR fixed parsing of age for arp command
- Cisco IOS 870 fixed parsing of crypto session command
- Cisco IOS-XE fixed parsing of OSPF neighbor command
- Cisco IOS 2500, IOS-XE cat4500e fixed parsing of OSPF interfaces
  command
- Cisco IOS - fixed parsing of switchport command, trunk allowed VLAN
  list
- Cisco IOS 2950 - fixed parsing of a serial number
- HMM protocol removed from CEF

### 2.1.0 (15th December 2017)

**Platforms**

- Check Point Gaia
- HP Aruba (Wireless)

**Features**

- NX-OS Routing summary support
- **Technology - Addressing - Managed IP** added
  columns **VRF**, **DNS name**, **DNS matched**, **DNS
  reverse** *(check if DNS record correspond with a hostname of the
  device, including DNS reverse lookup))*
- **Technology - Management - Saved config consistency** *(check if a
  device have unsaved configuration)*
- **Technology - Security - IPsec**
- **Technology - Security - DMVPN**
- **Technology - Platforms - Environment** (Power Supplies & Fans)
- **Technology - Interfaces - Switchport**
- **Technology - Spanning Tree - Neighbors**
- **Technology - Routing - OSPF - Neighbors & Interfaces**
- **Technology - Security - 802.1x**
- **Technology - Wireless - Clients** add new column **SSID**
- **Technology - Wireless - Access points** add new columns **Average
  Signal Strength**, **Average Signal to Noise Ratio** *(Clients with
  a weak signal, Access points with problematic clients)*
- **Settings - Advanced - SSH/Telnet** *(customer can define retries
  limit for failures)*

**BugFixes**

- SSH & Telnet clients - fixed false prompts detection *(Cisco ASA
  timeouted on \<—More—>)*
- Cisco WLC - `show client summary` command timeout fix *(reply "y"
  on display more entries? y/n)*
- Cisco WLC - `show port detailed info` fixed parsing
- Cisco `show spanning-tree detail` STP instances with no interfaces
  removed
- IP Phones - fixed LLDP & CDP different destination interfaces
- L2 edge port & user mac address detection improvement
- NX-OS OTV interface supported
- IE11 better performance

### 2.0.0 (9th November 2017)

**Platforms**

- Riverbed Steelhead
- HP Comware 5 and Comware 7

**System BugFixes**

- FEX parsing when description includes non-alphanumeric characters
- OS Versions VDC fix (the only chassis are included)
- STP parsing logic fix
- Duplicate IP not reported for /30-32 networks
- Fixed telnet negotiation

**Features**

- Combined Discovery & Analysis
- Network Change Management
- New diagrams
- New central API
- Added IP telephony
- Added QoS
- Added PoE
- Added StackWise
- Added routing protocols summary table
- Added Interfaces - Transceivers
- Added Interfaces Rate (inbound, outbound, bidirectional) tables
- Added Spanning Tree - Inconsistencies table
- Added Wireless controllers, access points, clients tables
- Added End of life reports for 3COM, HP Enterprise, ProCurve,
  Riverbed + Cisco reports updated
- Better TACACS controls
- FEX-FABRIC port-channel type
- Export encrypted tech support file
- Jumphost support
- Connectivity matrix based on protocol direction
- Access List - new filter for source & destination port (searching in
  port range, filter values can be separated by ",")
- Tables improvements (Automatic calculation of rows per page, Table
  rows size, Sticky first column, better pagination design)
- User management including roles
- Option to create a CSR (Certificate Signing Request)
- CLI authentication records importance can be changed by drag & drop,
  the upper record will be used first.
- Search - user can simply find the related page using search
- User with settings privileges can clear DB
