# IP Fabric v3.x.x

## IP Fabric v3.x.x

## 3.8.2 (1st July 2021)

OVA MD5SUM: 3E1B73F76140CBE5726129E3133D8022OVA
SHA256SUM: D9D71C6BACE7FA8AC9913FDD9B6F2ACBE743AB31218C0357BB7A271D0D1E6DE6

### Features - Protocol and technology support

-   AWS - added data to the table Technology / Routing / VRF

### Improvements

-   DNS name resolving, changed the way how we recognize if DNS server
    is available. Don't try to resolve public IP 8.8.8.8 but check if
    any nameserver is set
-   Snapshot management / Inventory table - allowed advanced filtering
    option\\
-   Tables help - API endpoint includes full URL including server name
-   Updated EoL records for Aruba CX
-   System / Advanced settings - Option "Saved configuration check" was
    removed - it can be controlled now from "Discovery Tasks" in
    advanced settings
-   Vendor API setting is part of snapshot settings now
-   Cisco IOS, IOS-XE and NX-OS - Added support for access-classes and
    transport methods on VTY lines to “technology/management/aaa/lines”
    table (as hidden columns Inbound ACL, Outbound ACL, Transport Input,
    Transport Output, Allow VRF login)
-   Transceivers statistics table - round delta low value to two decimal
    places

### Bug Fixes

-   Arista EOS - fixed parsing of different output for command "show ptp
    masters”
-   Arista EOS - fixed parsing of different output for command "show ptp
    local-clock"
-   Aruba CX - Added support for Aruba OS 10.07 routing table output
-   Checkpoint Gaia - fixed API endpoint /show-gateways-and-servers
    errors - VSX clusters & checkpoint host objects
-   CheckPoint Gaia - fixed parsing of bandwidth information for command
    “show virtual-system all“
-   Cisco IOS - exclude OSPFv3 "authentication/confidentiality" IPSec
    tunnels.
-   Cisco IOS - fixed parsing for command "show subscriber session all"
-   Cisco IOS - fixed parsing of command "show ip flow export" in case
    flow export is disabled
-   Cisco IOS - fixed parsing of different output for command "show
    interface switchport"
-   Cisco IOS-XE - fixed parsing of platforms containing dashes in model
    name
-   Cisco IOS-XE - fixed transceiver detection
-   Cisco IOS-XE, NX-OS - fixed parsing of command "show ptp brief" in
    case of ports in 'INITIALIZING' status
-   Cisco IOS-XR - fixed parsing of different output for command "show
    isis interface"
-   Cisco IOS, IOS-XE, IOS-XR - fix parsing of command "show ip route"
    for routes installed years ago. Add parsing for routes pointing to
    Null0
-   Cisco IOS/IOS-XE - VRRP parsing fixed not to fail on IPv6 groups
-   Cisco SX - fixed platform and model detection
-   Dell PowerConnect - Fixed parsing of show "show mac address-table"
    command containing multicast addresses
-   Extreme Xos - changed STP Root and Bridge IDs parsing to contain
    only MAC address part
-   Extreme Xos - Fixed parsing of STP ports with asterisk from command
    "show stpd \<stpDomain> ports detail"
-   Extreme XOS - RIB edges removed for local interfaces
-   Fix of bug "Invalid snapshot format" so snapshot wasn't able to load
-   Fix: Do not download the configuration file multiple times from the
    same IP address.
-   FRR - don’t show error if BGP/OSPF daemon is not running
-   FRR - fixed parsing of different output for command “show version“
-   HP ArubaSw - fix parsing of capabilities from "show lldp info
    remote' command"
-   HP ArubaSw - fix parsing of command "show interface brief" in case
    interface does not have media type
-   HP ArubaSw - improved device model detection
-   HP Comware - Added support for interface status 'STP DOWN'
-   HP Comware - fix parsing of command "show ap bss-table" to allow
    more values in 'phy' column
-   HP Comware - fixed parsing of 'display interface' command for the
    different output format
-   Huawei NE 8000 platforms - version detection fixed
-   Juniper Junos - fixed parsing of command 'show spanning-tree
    statistics interface' to support another output format
-   Juniper Junos - fixed parsing of different output for command "show
    route active-path"
-   Juniper Junos - fixed vrf leak to the main routing table (inet.0).
-   Juniper Junos - Improve error message when the firewall isn’t able
    to provide output for cmd "show security ike security-associations
    detail".
-   Juniper Junos - Improve error message when the firewall isn’t able
    to provide output for cmd "show security ipsec security-associations
    detail".
-   Juniper Junos - MPLS forwarding tables collection fix
-   Mikrotik - fixed ipsec parsing for non-tunnel policies
-   Mikrotik - fixed parsing of interfaces which have an only numeric
    name
-   Palo Alto - Cluster state detection added. Fixes path lookup on
    duplicate IP on both nodes in the cluster.
-   Paloalto - fixed tunnel proposals were not parsed correctly with
    long tunnel names
-   STP edges to Juniper SRX firewalls with virtual mac address fix
-   UI - fixed overflow of items from select boxes used in modals
    dialogs
-   Versa VOS - fixed mapping of API call
    "/vnms/dashboard/appliance/site-a/live?command=arp/all".
-   Versa VOS - fixed mapping of API call
    "api/config/devices/device/\<appliance>/config/networks/network".
-   Versa VOS - fixed mapping of API call
    “/vnms/dashboard/appliance/\<appliance>/live?command=interfaces?deep"
-   Versa VOS - fixed mapping of interfaces without MAC address.

## 3.8.1 (7th May 2021)

OVA MD5SUM: 7788D1E2E6A062F8FE3985A8644E9542OVA
SHA256SUM: 4E7FBA8DF01A787D93B8E6D0E3FE8AED68E3C9F6EABB3D162F84E1F99DADDD3D

### Improvements

-   F5 BigIP - collect configuration from all partitions, not just from
    Common as was before.
-   Cisco IOS, IOS-XE, IOS-XR - add metric and passive properties to
    IS-IS Interfaces table

### Bug Fixes

-   SSH connections could have timeouts on login
-   Arista EOS - fixed parsing of 'show system environment all' command
    in case there are N/A values
-   Cisco ASA - Fixed parsing of snmp location
-   Cisco IOS - fixed parsing for command "show flow exporter"
-   Cisco NX-OS - fixed parsing for command "show flow exporter"
-   Juniper Junos - routing table - fixed parsing of MPLS labels
-   F5 BigIP - new cmd “show sys cluster all-properties“ to add cluster
    management interfaces to interface list.
-   Paloalto IPSec - fixed parsing of tunnels with long names and
    multiple proposals

## 3.8.0 (26th April 2021)

OVA MD5SUM: 2f693acf59d9f31d28507c7edc58234fOVA
SHA256SUM: 2b208eb7584fd5b4708ea56a7f1688f4bf44624c872ef0d6b792576e88f9ff00

### New Vendor Support

-   Added support for Aruba CX
-   Added support for Checkpoint Gaia Embedded platform
-   Added support for AWS - Discovery, inventory and routing support for
    VPC, transit gateway, VPN gateway, nat gateway
-   Added support for Versa VOS - basic discovery process

### Features - Protocol and technology support

-   Cisco ACI - Added NTP support
-   Cisco ACI - DTEP collection added
    -   Tables located at Technology / SDN / ACI / DTEP
-   Added Multi-Chassis LAG support for Arista EOS and Extreme XOS
    -   Tables located at Technology / PortChannel / MLAG
-   Arista EOS - added support for VARP (Virtual-ARP)
    -   Table located ar Technology / FHRP / Virtual Gateways
-   Arista EOS - added PoE support
-   Arista EOS - added support for environment information
-   Cisco NX-OS, IOS-XE, Arista EOS - The Precision Time Protocol
    support added
    -   Tables located at Technology / Management / PTP
-   Cisco IOS, IOS-XE: Add support for PPPoE
    -   Tables located at Technology / Interfaces / PPPoE

### Improvements

-   Table Technology / Platforms / Cisco VSS / Chassis - add column
    Chassis SN
-   More precise parsing of platform identifier for Cisco Catalyst
    series
-   VLAN topology calculation improved for mismatched designatedPortId
    and opposite side portId using xDP
-   Juniper, Palo Alto - add vrf leak support to the routing table.
-   Cisco WLC-AIR - improved pagination handling - backspace is sent to
    display an additional page of command output
-   Table Inventory / Interfaces - added columns about Transceivers (if
    exist, SN, PN, Type - 3 of them hidden by default)
-   Table Technology / Security / IPSec / Tunnels - added column
    "Interface description"
-   Table Technology / Security / IPSec / Gateways - added column
    "Interface description"
-   Table Technology / Platforms / Stacks / Stack Ports - For stack
    technologies that use regular ports for the stack, a new column with
    a list of stack interfaces added.
-   Table Technology / Interfaces / Transceivers / Statistics - added
    column with delta between Value and Low
-   System / Settings / Advanced / Vendor API settings - each setting
    can be enabled / disabled
-   When the application will lose connection with the server then is
    shown "Connection lost" overlay
-   Juniper Junos - filter out VRRP backup virtual IP from the managed
    IP list
-   Managed duplicate IP table - removed for:
    -   Aruba AP - /32 IP on tunnel interfaces taken from another
        interface
    -   Versa - Internal IP
    -   IPv4 link local addresses 169.254.0.0/16
    -   Loopback addresses 127.0.0.0/8
-   The End Of Live database has been updated for Vendors (Cisco, HP,
    F5, PaloAlto, Arista, Extreme)

### Bug Fixes

-   Fix UI - table filters lost when URL is used after authentication
-   Arista EOS - added parsing of interface load and fixed interface
    counters parsing
-   Arista EOS - fix the mapping of multi-lane transceiver physical
    interface names
-   Arista EOS - fixed empty ip address of admin shutdown interfaces
-   Arista EOS - fixed parsing of bandwidth information for command
    "show ip igmp snooping group"
-   Arista EOS - fixed parsing of different output for command "show
    interfaces vxlan 1"
-   Arista EOS - fixed parsing of different output for command "show ip
    igmp snooping groups"
-   Arista EOS - fixed parsing of empty output for command "show ptp
    local-clock"
-   Arista EOS - remove non-existing Router interfaces from Interface
    inventory
-   Arista EOS - sometimes show the wrong VRF for admin shutdown
    interface, fixed.
-   Arista EOS - Spanning tree with MLAG - PeerEthernet ports removed.
-   Avaya/Extreme VOSS - Uptime with years fix
-   CheckPoint Gaia - error about missing router ID was shown even if
    BGP was disabled
-   Checkpoint Gaia - fixed parsing of different output for command
    "show cluster members interfaces all"
-   Cisco - fix parsing switchport mode dot1q-tunnel
-   Cisco - Fixed parsing show running-config command - line password
    with spaces.
-   Cisco - remove non-existing Sup-Eth interfaces from Interface
    inventory
-   Cisco ACI - fixed parsing of different output for command "show coop
    internal info ip-db"
-   Cisco ACI, NX-OS - fixed parsing of interface description.
-   Cisco ASA - fix parsing of not configured tunnels
-   Cisco ASA - fixed parsing of different output for command "show
    crypto ipsec sa"
-   Cisco ASA - fixed parsing of different output for command "show
    crypto isakmp sa detail"
-   Cisco IOS - Allow PIM RP without groups
-   Cisco IOS - fix duplex and media type for C1700
-   Cisco IOS - fix parsing of command "show ip igmp snooping mrouter"
    in case there are no ports configured
-   Cisco IOS - fix parsing of large output from "show mac address-table
    multicast"
-   Cisco IOS - fixed parsing of different output for command "show lldp
    neighbors detail"
-   Cisco IOS - fixed parsing of output for command "show ip igmp
    interface"
-   Cisco IOS - HSRP - fixed preemption detection
-   Cisco IOS-XE - BGP - fixed address family detection
-   Cisco IOS-XE - fixed parsing interfaces without outDrops counter
-   Cisco IOS-XE - fixed parsing of different output for command "show
    ap name \<apName> wlan dot11 5ghz/24ghz"
-   Cisco IOS-XE fixed STP interface - VLAN mapping (TwoGigabitEthernet
    and AppGigabitEthernet)
-   Cisco IOS-XE WLC - Fixed parsing for interfaces with "invalid" as a
    value for speed
-   Cisco IOS-XE WLC - fixed parsing of different output for command
    "show wlan summary"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    mpls forwarding"
-   Cisco IOS, IOS-XE and IOS-XR - Routing table parsing fixed
-   Cisco IOS, IOS-XE, ASA - fixed interface mapping in IPSec task.
-   Cisco IOS, NX-OS - use the full form of commands to avoid ambiguous
    commands - "show spanning-tree summary", "show spanning-tree
    detail", "show port-channel summary", "show etherchannel-summary"
-   Cisco IOS/IOS-XE - Fixed LLDP neighbors parsing in case output is
    split to 2 lines
-   Cisco IOS/IOS-XE - VRF name parsing fixed to disregard ending
    semicolon (if it is present)
-   Cisco NX-OS - added FEX info to inventory
-   Cisco NX-OS - fixed false-positive error emit in case "show monitor
    session all" contains information that destination port is in use in
    other span.
-   Cisco NX-OS - fixed parsing for command "show fex detail" for cases
    fabric port for control traffic is not provided.
-   Cisco NX-OS - fixed parsing of different output for command "show
    vrrp detail"
-   Cisco NX-OS - XDP links for LLDP protocol might have not been
    created in some cases
-   Cisco NX-OS- fixed parsing of show running configuration with some
    specific banner configured.
-   Cisco SG - fixed interface parsing in ARP table
-   Cisco SG - fixed LLDP neighbors detection in multiline output
-   Cisco SG - fixed parsing of different output for command "show sflow
    configuration"
-   Cisco SG - fixed parsing of different output for command "show
    spanning-tree detail"
-   Cisco SG 500 - fixed STP interface - vlan mapping (slash format)
-   Cisco XE - fixed xSR platforms identification
-   Cisco XR - fix parsing for command 'show version' (caused empty
    hostname)
-   Dell Powerconnect - fixed version detection for switches N2048
-   Extreme VOSS - fixed LLDP neighbor parsing
-   Extreme XOS - added reason for administratively down ports
-   Extreme XOS - Fixed STP parsing for multirow vlans output
-   Extreme XOS - Fixed STP parsing for PVST+ mode
-   Extreme XOS - transceivers task execution enabled
-   Fortinet FortiGate - fixed missing description in Interface
    Inventory table
-   HP Aruba - fixed parsing of details for AP which come down during
    discovery
-   HP Arubasw - fixed detection of model
-   HP Arubasw - Fixed error handling for LLDP neighbor with wrong
    format of Chassis ID
-   HP Arubasw - fixed mac-address collecting on some models
-   HP Arubasw - fixed parsing of different output for command "show
    interface brief"
-   HP Arubasw - fixed parsing of different output for command "show
    interfaces transceiver detail"
-   HP Arubasw - fixed parsing of different output for command "show
    interfaces transceiver"
-   HP Comware - fix parsing ARP table for platform 5130
-   HP Comware - fixed parsing of different output for command "display
    clock"
-   Huawei VRP - fixed parsing of different output for command "display
    info-center"
-   Huawei VRP - Fixed ARP parsing in case (SIP/DIP) is shown
-   Huawei VRP - fixed interface clearing time parsing
-   Huawei VRP - Fixed parsing for empty mirroring groups
-   Huawei VRP - fixed parsing of different output for command "display
    mac-address"
-   Huawei VRP - fixed parsing of different output for command "display
    vxlan tunnel"
-   Huawei VRP - fixed parsing of empty output for command "display dhcp
    snooping"
-   Huawei VRP - VXLAN Tunnels - command parsing fix when empty output
    is received
-   Juniper Junos - Configuration parsing fix for “protect protocols
    mstp” command
-   Juniper Junos - fixed parsing of different output for command 'show
    configuration \| display set \| except "^deactivate"'
-   Juniper Junos - fixed parsing of different output for command "show
    chassis environment"
-   Juniper Junos - fixed parsing of different output for command "show
    chassis routing-engine"
-   Juniper Junos - IGMP groups fix mapping of 'never' value for expires
    for
-   Juniper Junos fix false-positive err-disabled statuses
-   Meraki - L2 interfaces, reason “connecting” added
-   Palo Alto - an interface that wasn’t associated with any VSYS could
    be missing in the interface inventory
-   Palo Alto - collect list of VRFs from show commands instead of
    configuration
-   Palo Alto - collect transceivers only for interfaces of the
    currently processed virtual system
-   Palo Alto - fixed missing routing tables on single vsys firewalls
-   Palo Alto - fixed parsing of command "show vpn gateway" with
    multiple DH groups
-   Palo Alto - fixed parsing of different output for command “show
    routing route”
-   Palo Alto - fixed parsing of different output for command “show vpn
    flow“
-   Palo Alto - fixed vendor bug where the sessions keep open even the
    connection is correctly closed. Using "exit" cmd for disconnection.
-   Vlan topology calculation - Virtual mac used in switch ID for Cisco
    Nexus fix

## 3.7.6 (8th March 2021)

OVA MD5SUM: a47d9983d046f74a34a17f5025cb7bd8OVA
SHA256SUM: c5972d44b012ff3b3411ea3c6666651e9c6c453a50009c0062df99c11ae29e0b

### Improvements

-   Add support for Cisco Firepower 9000 series SM-24
-   Add indexes to speed up several DB queries
-   Table Technology / Routing / BGP / Neighbors - added "Local
    interface" column
-   Palo Alto - show also unconfigured ports in IPF
-   Cisco Meraki - Zx Teleworker Gateways - extended support for
    interface and routing table discovery (to gather this information Zx
    teleworker gateways processed pretty much the same as MX firewalls).

### Bug Fixes

-   Pathlookup - IGMP snooping fail fix
-   Juniper - IRB L3 interface correct VLAN ID assignement
-   Fortinet FortiGate - zone firewall could be missing in some cases
    since the unit was considered as a HA slave
-   Palo Alto - first configured vsys could be missing in discovery
    result
-   Cisco FTD - fixed detection of service objects with names matching
    ICMP options keywords

## 3.7.5 (22nd January 2021)

OVA MD5SUM: b4c940832cbd592f2653553d72f11f33OVA
SHA256SUM: c16cbac6040e7d07d04c42142ddbb42acc0547c912d726efa1bd1138a58f5be4

### Features - Protocol and technology support

-   Palo Alto - add port channel support

### Improvements

-   API Requests rate limiter counts only unresolved requests
-   Cisco ACI routing edges establish improvements.
-   Cisco NX-OS - Added Route-Target information for VRFs in BGP process
-   Fortinet FortiGate - added support for emac-vlan interfaces
-   Huawei - All send commands expanded to the full syntax
-   Table Technology / Interfaces / Transceivers / Inventory - added
    L1/L2 state columns
-   Frontend - implement request rate limiter

### Bug Fixes

-   CheckPoint Gaia - fixed processing of zone firewall services
    (DCE-RPC, port ranges)
-   Cisco ACI - an unsupported show run command is no longer downloaded
-   Cisco ASA/FTD - L3 interfaces ‘local’ IPs are no longer derived from
    static ARP entries
-   Cisco IOS - fixed parsing of bandwidth information for command "show
    policy-map interface"
-   Cisco IOS - fixed parsing of different output for command "show
    mac-address-table multicast"
-   Cisco IOS - fixed parsing of different output for command "show
    standby"
-   Cisco IOS - Fixed showRun parsing for sections aaa, SNMP
-   Cisco IOS-XE - command "show wireless client mac-address \<mac>
    detail" - filter out clients without ap.
-   Cisco IOS-XE WLC - improved parsing and overall wireless AP
    processing capabilities to better handle erroneous command outputs
-   Cisco IOS, IOS-XE - fixed parsing of source interface for AAA
    servers.
-   Cisco NX-OS - fixed parsing of different output for command "show
    interface transceiver details"
-   Cisco NX-OS - fixed parsing of different output for command "show
    spanning-tree mst"
-   Cisco NX-OS, IOS-XE - fixed parsing of different output for command
    "show version"
-   Cisco NX-OS/ACI - L3 interfaces ‘local’ IPs are no longer derived
    from static ARP entries
-   Cisco SG - Fixed ambiguous commands
-   Cisco SG - Fixed parsing of interface name (SG 500)
-   Documentation - the report was broken when the text included Unicode
    characters
-   Establishing BGP neighborship improved based on VLAN
-   Establishing RIB neighborship between ACI and FW improved based on
    VLAN and neighbor protocol
-   Fortinet FortiGate - fixed missing MAC addresses on all interfaces
    if the modem was active
-   Fortinet FortiGate - L2 data for some of the interfaces could be
    missing, L2 state could be wrong in some specific cases
-   Fortinet FortiGate - show only IP addresses from the active
    (virtual) cluster member
-   HP Aruba switch fix parsing of hostname
-   HP Arubasw - fixed parsing of different output for command "show
    vlans"
-   HP Arubasw - fixed parsing of different output for command “show
    lldp info local-device"
-   HP Comware - fixed parsing of different output for command "display
    arp"
-   HP Comware 1910 - fixed version detection
-   HPE V1910 - Fixed platform detection
-   Juniper Junos - fixed parsing of different output for command "show
    igmp group"
-   Juniper Junos - IRB L3 interface correct VLAN ID assignment
-   Juniper Junos - STP - VLAN specific information parsing fixed for
    VSTP
-   Palo Alto - list only L2 interfaces that belong to the processed
    virtual system
-   Pathlookup - Device connected to ACI LEAF fix
-   Pathlookup - Transit search with tunnel fix (tunnel destination IP
    is now used)
-   System Administration - allows restarting of Discovery services
-   Technology / Addressing / Managed IP - table "DNS name match
    hostname" and "DNS (A/CNAME record)" columns did have correctly set
    failed status.
-   The Discovery process may be stuck when Tacacs is overloaded - fixed

## 3.7.4 (21st December 2020)

### Improvements

-   Topology calculation -  virtual mac calculation optimized
-   Discovery  - Summary of Issues is refreshed every 5mins (from 1min)
    to prevent DB overload
-   Optimized DB queries for Discovery - Summary of issues

## 3.7.3 (17th December 2020)

### Features - Protocol and technology support

-   Cisco ACI - add support for OSPF
-   CheckPoint Gaia - added support for VSX firewalls and switches

### Improvements

-   Checkpoint Gaia - use the default Router ID for BGP if it isn’t
    explicitly configured
-   HP Aruba - (Technology / Wireless / Radios / Radios-detail) improve
    wlans mapping when AP is in monitoring mode
-   Palo Alto - add rebuild property to version.
-   Palo Alto - add support of fqdn objects in Zone FW.
-   Pathlookup - Application of ACL and zone firewall for MPLS links.
-   RIB topology - Down interfaces used as a source for unnumbered
    interfaces filtered from the calculation.

### Bug Fixes

-   Arista EOS - fix parsing of IP route table when IP routing is
    disabled
-   Arista EOS - fixed parsing of different output for command "show ip
    route vrf \<vrfName>"
-   CheckPoint Gaia - fixed mapping of different output for API endpoint
    "/web_api/show-gateways-and-servers"
-   Cisco ACI - fixed parsing of different output for command "show coop
    internal info ip-db"
-   Cisco IOS - fixed parsing of different output for command "show mpls
    forwarding-table detail"
-   Cisco IOS - fixed parsing of different output for command "show vrf
    detail"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    mpls forwarding"
-   Cisco IOS-XR - VRF-based routing information parsing fixed
-   Cisco NX-OS - ACL with IPV4 syntax added
-   Cisco NX-OS - fixed parsing of different output for command "show
    mpls switching"
-   Cisco NX-OS, IOS-XR - fixed parsing of different output for commands
    "show hsrp", "show hsrp detail", "show vrrp detail"
-   Cisco SG - dot1x related commands parsing fixed
-   F5 BigIP - fix “show sys hardware” failure in version detection
-   Fixed Device type detection - One non-connected route is enough for
    router
-   Fortinet FortiGate - fixed missing VIP groups in zone firewall
-   Fortinet FortiGate - fixed parsing of different output for command
    "show firewall service group"
-   HP Arubasw - fixed parsing of different output for command "show
    trunks"
-   HP Comware - fixed parsing of different output for command "display
    device manuinfo"
-   Huawei - Fixed ambiguous commands for arp, dhcp snooping, sflow,
    port-mirroring
-   Huawei - MPLS to RIB transport label mapping - 3 implicit null label
    removed
-   Juniper Junos - fixed parsing of different output for command "show
    vlans detail"
-   Juniper Junos - show route active-path command parsing updated and
    fixed
-   Palo Alto - fixed parsing of different output for command "show
    config merged"
-   Pathlookup - MPLS - nexthop without IP secondary lookup in VRF added
-   Pathlookup - Multiple NH with different link type fix

## 3.7.2 (3rd December 2020)

### Improvements

-   Cisco - IP disabled or unconfigured interfaces excluded from saving
    into L3 interfaces table (IPv4, IPv6)
-   API POST /discovery/trigger-config-backup - config backup is
    possible to execute via API no matter on trigger setting
-   Routing protocols and RIB neighborship establishment improvement for
    unnumbered IP with help of xDP
-   Speed of topology calculation has been improved for networks with a
    lot of XDP records

### Bugfixes

-   Arista EOS - fixed parsing of different output for command "show ip
    ospf interface"
-   Arista EOS - fixed parsing when the device returns empty string for
    command "show ip ospf interface"
-   Arista EOS - fixed parsing when the device returns an empty string
    for command "show logging"
-   Cisco ACI - Edge switch calculation fix (precedence from endpoint
    table on a leaf over ARP on other devices)
-   Cisco ACI - Leaf to switch VLAN topology fix for same access VLAN
    for two different PI VLAN (caused discovery finish calculation fail
    on the unique index).
-   Cisco ACI - Switch to leaf L2 path VLAN translation from access VLAN
    to PI VLAN fix
-   Cisco IOS - fixed parsing of different output for command "show
    crypto ikev2 sa detailed"
-   Cisco IOS - fixed parsing of different output for command "show
    standby"
-   Cisco SG/NX-OS - power supply & fan information processing fixed
-   F5 BigIP - doesn’t run cmd "list /sys management-ip" on vCMP guests,
    it doesn’t return any value on this platform.
-   Fortinet FortiGate - fixed parsing of different output for command
    "show firewall address"
-   Fortinet FortiGate - fixed parsing of different output for command
    “get system status“
-   Fortinet FortiGate - fixed processing of policies with service ALL
    in zone firewall
-   Fortinet FortiGate - neighbor relationships fixed on VDOM links
-   HP Aruba - fixed parsing of different output for command "show ap
    port status ap-name \<apName>"
-   Huawei VRP - fixed parsing of different output for command "display
    sflow"
-   Huawei VRP - fixed parsing of different output for command "display
    transceiver verbose"
-   Huawei VRP - fixed parsing of different output for command "display
    vxlan tunnel"
-   Huawei VRP - Mac address table, add bridge domain number to
    interface if missing
-   Juniper Junos - fixed parsing of different output for command "show
    configuration \| display set \| except "^deactivate""
-   Juniper Junos - fixed parsing of different output for command "show
    configuration security policies \| display set”
-   Juniper Junos - fixed parsing of different output for command "show
    ethernet-switching interface"
-   Juniper Junos - fixed parsing of different output for command "show
    lldp neighbors interface \<int>"
-   Juniper Junos - fixed parsing of different output for command "show
    security ipsec security-associations detail"
-   Juniper Junos - fixed parsing of different output for command "show
    security ipsec security-associations detail"
-   Juniper Junos - fixed parsing of different output for command "show
    vlans detail"
-   Mikrotik RouterOS - fixed parsing of different output for command
    "/ip neighbor print detail"
-   Palo Alto - transceivers - "show system state filter-pretty
    sys.s\*.p\*.phy command" parsing fixed
-   Palo Alto - Zone FW - fix parsing of shared firewall objects on
    multi vsys systems.
-   UI - Settings / Discovery Tasks - button Test in Firefox submit a
    form (save action) instead of Test action
-   Pathlookup - Route to switched interface fix to apply only on SVI
    interfaces.
-   Switch to router VLAN topology calculation - fix for number of MAC
    addresses limitation
-   Bridge domain VLAN topology calculation - fix for recalculation

## 3.7.1 (24th November 2020)

### Features - Protocol and technology support

-   Palo Alto - add support for Syslog

### Improvements

-   The login into the platform was slow - rewritten DB query for GET
    /snapshot endpoint
-   Rewritten DB query to speedup post-discovery topology calculation
-   Technology / Security / Zone firewal / Interfaces - format data in
    Zone column (separate multiple zones by space)
-   Cisco IOS-XE - command "show interfaces transceiver detail" - added
    handling for Cisco bug CSCuw38988 (version 03.07.05E & platform
    cat3k_caa)
-   Fortinet FortiGate - check whether a VDOM still exists before
    switching to it
-   HOTFIX - MERAKI API processing is disabled when the snapshot is
    started from graphs

### Bug Fixes

-   Arista - transceivers - parsing fixed and extended
-   Aruba, Palo Alto - Fixed NTP server parsing when specified by FQDN
-   Checkpoint API data wasn't download on add new devices to the
    snapshot - fixed
-   CheckPoint Gaia - fixed parsing of different output for command
    "show ospf neighbors detailed"
-   CheckPoint Gaia - run command "show security-gateway memory
    statistics" (if available) instead of "fw ctl psat" which is
    deprecated
-   Cisco - IP unnumbered addresses mapped to L3 interfaces
-   Cisco ACI - Too long VRF name over multiple lines parsing fix for
    "show system internal epm vrf all"
-   Cisco ASA - fixed parsing of different output for command "show
    crypto ipsec sa"
-   Cisco ASA - fixed parsing of different output for command "show
    crypto isakmp sa detail"
-   Cisco IOS - fixed parsing of different output for command "show
    crypto ipsec sa"
-   Cisco IOS - fixed parsing of different output for command "show ip
    route"
-   Cisco IOS - fixed parsing of different output for command “show vlan
    brief“
-   Cisco IOS - multicast MAC address table - parsing updated to support
    IOS based routers
-   Cisco IOS XR - fixed platform and model detection for NCS series
-   Cisco IOS-XR - Bundle-Ethernet interface name standardization
    (Bundle-Ether, BE in different outputs, now all is BE).
-   Cisco IOS-XR - Device had incorrectly assigned IP addresses from
    EVPN ARP records
-   Cisco IOS-XR - routing table next hop with vrf leak parsing fix
-   Cisco IOS/XE - fixed parsing of different output for command "show
    lldp neighbors"
-   Cisco WLC-AIR - allow device discovery even if not possible to
    determine device platform and model
-   Fortinet FortiGate - fixed parsing of different output for command
    "diagnose firewall fqdn list"
-   Fortinet FortiGate - fixed parsing of different output for command
    "diagnose netlink aggregate name \<name>"
-   Fortinet FortiGate - fixed parsing of different output for command
    "diagnose vpn tunnel list"
-   Fortinet FortiGate - fixed parsing of different output for command
    "show firewall vip"
-   HP Arubasw - fixed parsing of different output for command "show cdp
    neighbors detail"
-   HP Arubasw - fixed parsing of different output for command "show
    logging server"
-   Huawei ambiguous commands fix - display mac-address, display
    interface, display device manufacture
-   Huawei VRP - ARP - Vlan parsing fix when the record is over multiple
    lines.
-   Huawei VRP - fixed parsing of different output for command "display
    mpls ldp adjacency verbose"
-   Huawei VRP - fixed parsing of different output for command "display
    mpls lsp verbose"
-   Huawei VRP - fixed parsing of different output for command "display
    vxlan tunnel"
-   Huawei VRP - fixed parsing of different output for command "display
    vxlan vni"
-   Huawei VRP - Task VXLAN - Device without VXLAN configuration error
    fix
-   Juniper Junos - fixed parsing of different output for command "show
    chassis environment"
-   Juniper Junos - fixed parsing of different output for command "show
    chassis routing-engine"
-   Palo Alto - fixed parsing of different output for commands "show vpn
    \*"
-   Palo Alto - fixed parsing of different outputs for command "show
    config pushed-shared-policy vsys \<vsys>"
-   Transceivers statistics table - fixed data for threshold columns
-   Transceivers thresholds and errors tables - show only transceivers
    with some data

## 3.7.0 (9th November 2020)

OVA MD5SUM: 0b44008d783224387c9c894a61a33701OVA
SHA256SUM: 8a3805704b6f4b126d960e3953749f936c67e635d94d387d86ddea6ecf4ea8fc

### Features - Protocol and technology support

-   Adds IPSec support for the following platforms
    -   Cisco IOS, IOS-XE, ASA
    -   Juniper Junos
    -   PaloAlto
    -   Mikrotik
-   Adds detailed IPSec technology tables
    -   Tunnels (/technology/security/ipsec/tunnels)
    -   Gateways (/technology/security/ipsec/gateways)
-   Adds Zone-Based Firewall support for the following platforms
    -   Palo Alto
    -   Checkpoint Gaia
-   Adds Transceiver support for the following platforms
    -   WARNING: Transceiver information collection is intentionally
        disabled by default due to frequent bugs associated with reading
        transceiver status. Please make sure with vendor support about
        presence of such bugs in your code, or contact our support for
        best practices.
    -   Cisco ACI, ASA, FTD, IOS, IOS-XE, IOS-XR, NX-OS, WLC
    -   Arista EOS
    -   Extreme XOS
    -   Fortinet Fortigate
    -   HP Arubasw, Comware
    -   Huawei VRP
    -   Juniper Junos
    -   Paloalto
-   Juniper Junos - Adds support for IGMP snooping
-   Huawei - Adds support for MPLS LDP
-   Huawei - Adds support for MPLS
-   Huawei - Adds support for BGP EVPN
-   Huawei - Adds support for L2 VXLAN
-   Huawei CloudEngine - VBST for version 8 improvement, all STP data
    are now collected
-   Cisco NX-OS - Adds support for VRRPv3
-   Cisco IOS-XE - Adds collection of stack information for switches
    with platform cat9k_lite
-   Settings / API Tokens - API Access Tokens allows you to use IPF API
    easily and secure
-   Settings / Webhooks - Webhooks enable you to send notifications to
    web applications in response to events in IP Fabric platform.
-   Settings / Advanced / Discovery Tasks - possibility to exclude
    specific tasks from the discovery process
-   Settings / Advanced / SSH / Telnet - possibility to set custom port
    for protocol and subnet

### Image

-   Added tcpdump package
-   Installation system wizard - Self-signed certificate with one letter
    country prevented to start all web services. Fixed with the
    requirement for two-letter country

### Improvements

-   Pathlookup - Hairpin routing support added
-   Pathlookup - Do not create host L2 edge to edge switch if the host
    is connected to FEX
-   Pathlookup - ACI endpoint lookup - fix of the search when COOP on
    the spine was introduced in 3.6.0
-   Pathlookup - ACI default GW with non-ACI edge switch, VLAN mapping
    based on access encapsulation VLAN ID
-   Pathlookup - ACI routing on second POD LEAF with endpoint connected
    fix (VNI from the first POD removed)
-   Pathlookup - ACI LEAF to switch connection fix
-   Pathlookup - L2 vxlan multiple tunnel endpoints fix
-   Pathlookup - ACI host to more LEAFs connected fix
-   Pathlookup - Routing proxy spine with multiple VTEP fix
-   Pathlookup - two labels stack processing on PE (PHP disabled)
-   Pathlookup - VXLAN L2 host connected to VTEP over switched network
-   Pathlookup - implicit null label 3 for Huawei support
-   Access-lists - new port translation from name to number added (DHCP,
    DNS)
-   Arista VEOS - add model detection for CVX
-   Cisco ACI - virtual vlan L2 interfaces with connection to L2 stp
    domain added
-   Cisco 6500 & 7600 - IGMP snooping support improvement
-   Cisco Firepower - NTP is now executed on all versions but by default
    disabled in Discovery tasks settings
-   Selected snapshot is remembered, will be automatically selected in
    browser new tabs.
-   F5 BigIP - new cmd "\|list /sys management-ip" to add management
    interface to interface list
-   HP Comware - collect media for L2 interfaces
-   Huawei - L2 STP link added between bridge domain and neighbor switch
-   Palo Alto - management port support added (for VSYS system is placed
    into lowest-numbered VSYS)
-   Table Technology / Platforms / Environment / Power supplies - add
    column Device Model
-   Table Inventory / Devices - Column "Serial number" is renamed to
    "Unique serial number" (includes virtualization unique identifier -
    context/vsys/VDC etc). "Serial number" column now contains real SN
    reported by the device.
-   Table Technology / Multicast / MRoute table - add "Vendor", "Family"
    columns (as hidden by default)
-   Table Technology / Multicast / MRoute / OIL Detail - add "Vendor",
    "Family" columns (as hidden by default)
-   Table Management / Discovery History - the records are updated only
    for new snapshot, not for snapshot load.
-   Table Technology / Platform / Stacks / Members - uptime fixed to
    show members uptime instead of master
-   Table Technology / Platform / Stacks / Stacks - new columns Lowest
    and diff uptime
-   Table Technology / FHRP / Group state - column version added for
    HSRP and VRRP
-   Table Help - the request payload formatted to valid JSON. Added
    button for payload & URL copy.
-   OSPF Area always formatted as an IP address
-   API - added route for device config backup triggering
    -   POST /v1/discovery/trigger-config-backup (payload is JSON with
        IP or SN property)

### Bug Fixes

-   Arista - fixed parsing of different output for command "show lldp
    neighbors detail"
-   Arista - fixed parsing of different output for command "show vrf"
-   CheckPoint Gaia - add cluster virtual IP addresses to the interfaces
-   CheckPoint Gaia - fixed parsing of different output for command
    "show ospf neighbors detailed"
-   Cisco 9800 WLC - Fix parsing when wireless client with "excluded"
    status is contained in output
-   Cisco 9800 WLC - fixed parsing of different output for command "show
    wireless interface summary"
-   Cisco ACI - fixed parsing of different outputs for command "show
    coop internal info ip-db"
-   Cisco ACI - Some show interfaces have 0000.0000.0000 mac, bia is
    taken instead
-   Cisco ASA - fixed parsing of different output for command "show run"
-   Cisco ASA Firepower - Platform detection improvement for 4000 and
    9000 platforms.
-   Cisco Cat9K platforms - fixed parsing of show version output without
    stackwise
-   Cisco Catalyst 3K & 9K - Total output drops bytes/packets handling
    (CSCve59640).
-   Cisco IOS - add correct parameters to the command “show
    storm-control“ on Cat4500 platforms
-   Cisco IOS - fixed parsing of different output for command "show lldp
    neighbors"
-   Cisco IOS - fixed parsing of different output for command "show run"
-   Cisco IOS - fixed parsing of different output for command "show
    udld"
-   Cisco IOS - VSS - Current state time not provided for CAT4500 fix
    (removed as required property)
-   Cisco IOS - VSS - Four supervisor chassis fix
-   Cisco IOS - VSS - VSL link output from both switches fix
-   Cisco IOS 6800 - fixed parsing of different outputs for command
    "show mac address-table multicast"
-   Cisco IOS XR - fixed parsing of different outputs for command "show
    ntp associations"
-   Cisco IOS-XE - fixed parsing of different output for command "show
    run"
-   Cisco NX-OS - CDP capabilities includes phone, so it was wrongly
    classified as phone.
-   Cisco NX-OS - device model is taken from "show inventory"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    ip igmp snooping groups"
-   Cisco NX-OS - OSPF interface fix for unnumbered interface
-   Cisco NX-OS - PIM with unnumbered interfaces fix
-   Cisco NX-OS fixed parsing of different output for command "show cdp
    internal global-info"
-   Cisco NX-OS fixed parsing of different output for command "show ip
    bgp vrf all all nei"
-   Cisco NX1000v - don't execute unsupported cmd "show cdp internal
    global-info"
-   Cisco SG - fixed hostname detection
-   Cisco SG - fixed parsing of different outputs for command "show
    interface status"
-   Extreme Boss - fixed parsing of different output for command "show
    arp-table"
-   Extreme Boss - fixed parsing of different output for command "show
    lldp neighbor-mgmt-addr"
-   Extreme Boss - fixed parsing of different output for command "show
    lldp neighbor"
-   Extreme Boss - fixed parsing of different output for command "show
    mac-address-table"
-   Extreme Boss - fixed parsing of different output for command "show
    port-statistics”
-   Extreme Boss - fixed parsing of different output for command "show
    running-config"
-   Extreme Boss - fixed parsing of different output for command "show
    vlan interface info"
-   Extreme Boss - fixed parsing of different outputs for command "show
    ip"
-   Extreme Boss - fixed parsing of different outputs for command "show
    mlt"
-   Extreme BOSS - fixed parsing of different outputs for command "show
    spanning-tree stp \<args> port vlans"
-   Extreme BOSS - mac address table parsing fixed (caused discovery
    stuck). Fix in library common for more vendors, so this was possibly
    affecting more vendors
-   Extreme Boss - MSTP port role fix for stack
-   Extreme Boss - VLAN interface fix for stack and ports without vlans
-   Extreme Voss - fixed parsing of different output for command "show
    ip vrf"
-   Fortinet FortiGate - fixed collecting device info
-   Fortinet Fortigate - Mac address mapping to aggregate and VLAN
    interfaces (fixes path lookup L2 edge between switch and Fortigate)
-   Fortinet Fortigate - Prompt detection for VDOM with more than 11
    characters fix
-   Fortinet Fortigate - Zone firewall fixes for load balancing VIP
-   HP Aruba - fixed parsing of different output for command "show ap
    port status ap-name \<apName>"
-   HP Aruba - fixed parsing of different output for command “show lldp
    neighbor interface \<intName> detail“
-   HP Arubasw - fixed model detection on stack switches
-   HP Arubasw - fixed parsing of different output for command "show ap
    details ap-name \<apName>"
-   Huawei VRP - ARP table entries with L2 interfaces mapped to L3
    interface to fix path lookup issues
-   Huawei VRP - BGP - Address family in VRF recognition fix
-   Huawei VRP - fixed parsing of different output for command "display
    lldp neighbor"
-   Huawei VRP - fixed parsing of different output for command "display
    mac-address"
-   Huawei VRP - fixed parsing of different output for command "display
    memory"
-   Huawei VRP - Route summary for VPN instances (VRF) fix
-   Juniper Junos - DHCP bindings for private VLANs without VLAN ID
-   Juniper Junos - don’t run discovery on secondary nodes.
-   Juniper Junos - EX3400 sn parsing fix
-   Juniper Junos - fixed parsing of different output for command "show
    ethernet-switching interfaces"
-   Juniper Junos - fixed parsing of different output for command "show
    lldp neighbors interface \<intName>"
-   Juniper Junos - fixed parsing of different output for command "show
    vrrp detail"
-   Juniper Junos - IRB interface support in pathlookup
-   Mikrotik RouterOS - fixed showing duplicated L3 interface in case
    that both IPv4 and IPv6 address is configured
-   Palo Alto - fixed parsing of different outputs for command "show arp
    management"
-   Palo Alto - fixed parsing of different outputs for command "show
    interface management"
-   Palo Alto - Routing table collection in virtual systems fixed
-   Power supplies table - Missing SN can be taken from inventory if
    available
-   UI - Cron component - Sunday as an initial value wasn't selected

### 3.6.3 (10th September 2020)

### Improvements

-   Cisco NX-OS and ACI - show inventory based chassis SN is the
    preferred device SN (otherwise show version based SN is used)

### 3.6.2 (9th September 2020)

### Bug Fixes

-   Configuration Management - fixed getting config file using a
    parallel API requests
-   Configuration Management - fixed unexpected API failure when was
    used advanced filters in API request
-   HP Arubasw - fixed version detection on several platforms.

### 3.6.1 (17th August 2020)

OVA MD5SUM: B4F8C3DCA72657F8A38205D9B1C66626OVA
SHA256SUM: 0FBC098CEE58B7A1F14C6D7DAB822E47788ED2ADB0074DBCC9F745CE7BBEF557

### Improvements

-   Site Separation - Regex rule - Site Name field as select box where
    user can select already created sites or type a new site name
-   Device Explorer - added Model into device detail tab. Also added
    model column into all tables where exists "platform" column
-   Table Technology / Management / SNMP / Summary - added columns
    Vendor, Model
-   Table Technology / Networks / Managed Networks - added VLAN ID
    column
-   Table Technology / Platforms / Cisco VDC - added Device Explorer
    detail for column Device
-   Cisco IOS - don’t run unsupported storm-control commands on Cisco
    C45xx platform
-   Maintenance scheduling - added option WEEK and MONTH to allow
    scheduling to allow job execution on a weekly / monthly basis.
-   Connectivity Report - added MAC address column
-   F5 BigIP - added parsing for model and platform device properties.
-   Added DB index for speed up of table Technology / IP Telephony /
    Phones

### Bug Fixes

-   LDAP - fixed user email when LDAP returns multiple email addresses
    for a given username
-   LDAP - fixed user authentication, domain suffix to be case sensitive
-   UI - Search for page - removed duplicate results for the same page
-   Jumphost - fixed different SSH prompt when the connection is
    established
-   Router to switch L2 STP connection fixed for port channel interfaces
-   Cisco ASA - fix platform detection for FPR models.
-   Cisco IOS-XE - fixed parsing of different outputs for command "show
    ip igmp snooping mrouter"
-   Cisco IOS, IOS-XE - fixed parsing of different output for command
    "show udld"
-   Cisco IOS, IOS-XE - VSS information collecting fix
-   Cisco IOS, IOS-XE - ACLs - added support for packet length option
-   Cisco IOS - fixed Storm Control for C65xx platforms in case that
    storm control limits are not set
-   Cisco IOS - fixed parsing of different outputs for command "show
    switch virtual redundancy"
-   Cisco NX-OS - fixed version detection for models NX-OSv
-   Cisco NX-OS - MDS switches and Nexus 1k Virtual Services Appliance
    servers are flagged as “Unsupported devices”
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    ip igmp interface"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    ip igmp snooping groups"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    cdp global"
-   Cisco NX-OS - fixed getting Fex Power Supply in fail/shutdown state.
-   Cisco IGMP snooping - parsing fixed for disabled IGMP processes on
    NX-OS and ACI
-   Fortinet FortiGate - don’t create xDP relation for VDOM links where
    both ends are in the same VDOM
-   Riverbed Steelhead - in some cases "show version" cmd did not
    provide model, in that case model is taken from "show info".

### 3.6.0 (1st August 2020)

OVA MD5SUM: 5E260AAA1E88BF4BD8523F0634FC3B4E  
OVA
SHA256SUM: 5933E36D0FE6CF8AAD22B8CDCF7EA00A90C0028D6D7CDDF85E005269419A4B34  
Hyper-V MD5SUM: 634428E5722A53F87C4E0BD5C16F6285  
Hyper-V SHA256SUM: 2556A6EB2C7B2DE7318E8FFF1787E5A63D5E5A54BFA1D72F3B416B60DBB8EF78

### New Vendor Support

-   Extreme/Avaya - VSP switch family with VOSS basic discovery support
    added
-   Extreme/Avaya - ERS switch family with BOSS basic discovery support
    added
-   FRRouting - Added support for basic discovery

### Features - Protocol and technology support

-   Device Explorer - Detailed view for each device
    -   When you click on hostname value in every table then you can see
        data from any other table where the data will be automatically
        filtered for that device.
-   Added summarized tables about device inventory. New tabs in
    Inventory / Devices:
    -   Vendors - Vendor overview in the whole network
    -   Families - Vendor / Family overview in the whole network
    -   Platforms - Vendor / Family / Platform overview in the whole
        network
    -   Models - Vendor / Family / Platform / Model overview in the
        whole network
-   New table Technology => VLANs => L3 Gateways - shows VLANs without
    L3 gateway
-   New table Technology => Platforms => PoE => Modules - shows PoE
    information per module
-   Cisco ACI - Multicast support added
-   Cisco ACI - Add support for FEX & environment
-   Cisco IOS, IOS-XE - UDLD support added - interfaces and neighbors
    tables
    -   Technology / OAM / UDLD
-   Cisco IOS, IOS-XE - VSS support added
    -   Technology / Platforms / Cisco VSS
-   Cisco IOS, NX-OS, HP Comware - Storm Control support added
    -   Technology / Interfaces / Storm Control

### System

-   Jumphost - Intermediary Linux server with SSH can be used to forward
    IPF network discovery traffic. User credentials and SSH key for
    authentication are supported with multiple jumphosts.

### Improvements

-   Site separation - the site separation was rewritten. The multiple
    rules can be defined, Regex rule can be without matching group.
-   Table Technology / Platforms / Stack / Connections - #Known members
    column added to filter false positive down states for provisioned
    switches.
-   Table Technology / Addressing / Managed IP - added column Vlan ID
-   Table Technology / Platforms / Stack / Members - added column Uptime
-   Table Technology / Addressing / Managed duplicate IP - Don't report
    duplicities for Cisco ACI and for "em%", "bme%", "avs%" interfaces
-   Table Inventory - Hosts: Added interface description into Edges
    column
-   Settings / OUI - added enable/disable for multi rows selection
-   ARP discovery - New OUI for HP/Aruba switches added
-   Neighbor protocols CDP/LLDP - deduplication of same neighbor
    improved
-   Intent Verification Rules - added icon for customized rules
-   Settings / Advanced / SNMP - added encryption passphrase into SNMPv3
    settings
-   Arista EOS - collect average packet size for multicast routes
-   Cisco ACI - VTEP and VNI added to RIB for tunnel interfaces (to
    support forwarding to vtep from RIB)
-   Cisco ACI - COOP endpoint database collected on spines
-   Cisco Firepower FTD - L2 connection to switch fix, pathlookup will
    now show L2 path from/to FTD
-   Cisco NX-OS & ACI - local routes /32 are now parsed
-   Cisco NX-OS - fixed parsing of different output for command "show
    interface switchport"
-   Cisco Nexus FEX - support extended to better deal with possibly
    missing SN and model information in show fex detail command outputs
-   Cisco IOS-XE WLC - wireless AP MAC derivation changed to prefer
    MAC-based access point IDs over Ethernet port MACs to better match
    AP MACs provided by wireless clients
-   Cisco IOS & NX-OS - IGMP snooping groups modified to include mrouter
    ports
-   Cisco IOS & Arista - Mrouter port entries are inserted into snooping
    table when no receiver is present
-   Cisco IOS - BGP - add support for Cisco 7300
-   Cisco Firepower ACLs - added support for ‘trust’ action
-   L2 edge port classification improved - tunnel never can be edge port
-   Cisco Nexus - VPC pairs are now connected not only by domain but
    also must be CDP neighbors.
-   Neighbor discovery protocols improvements - Entries without IP
    processed, relationships established based on port id, chassis id
    etc.
-   Pathlookup - WLC detection improved for virtual IP on the management
    interface.
-   Multicast pathlookup
    -   Source MAC taken from any node if not found on connected node in
        ARP
    -   IGMP Snooping L2 path support added
    -   Vlan added to device forwarding summary table
-   Table Technology / Inventory / OS versions
    -   Performance improvement
    -   F5 included
    -   Palo Alto correct calculation fix

### Bug Fixes

-   Pathlookup - Cisco FEX now correctly work in comparison between
    snapshots
-   Pathlookup - Own IP without local ARP entry on default GW fix
-   VLAN information is correctly saved even when STP is missing
-   Arista EOS - changed command for multicast routes counters for
    firmware version 4.23 and higher
-   Arista EOS - fixed version detection on virtual appliance (vEOS)
-   Arista EOS - remove duplicit route, route summary and arp records in
    vrf default. Fix missing vrf default in VRF task.
-   Arista EOS - fixed parsing of different outputs for command "show ip
    interface"
-   Cisco ACI - Endpoint table parsing fix for entries with missing
    flags
-   Cisco IOS & IOS-XE - show ip mroute vrf was on some platforms
    shortened and ambiguous.
-   Cisco IOS - fixed parsing of different outputs for command "show ip
    pim interface"
-   Cisco IOS/IOS-XE - fixed parsing of different outputs for command
    "show ip pim neighbors", entries without flags
-   Cisco IOS/IOS-XE - fixed parsing of different outputs for command
    "show ip mroute"
-   Cisco IOS/IOS-XE - fixed parsing of different outputs for command
    "show interfaces"
-   Cisco IOS C3750 - fixed parsing of provisioned member switches in
    command “show switch detail“
-   Cisco IOS-XE - "show version" stack member parsing fixed
-   Cisco IOS XR - fixed parsing of different outputs for command "show
    cef vrf \<instance> detail"
-   Cisco Meraki - if the proxy is configured then the connection use
    that proxy
-   Cisco NX-OS 5000 - fixed parsing of different outputs for command
    "show nve interface"
-   Cisco NX-OS 5000 - fixed parsing of different outputs for command
    "show nve vni"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    ip pim rp vrf all"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    ip igmp snooping"
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    mac multicast parsing", repeated header in the output
-   Cisco NX-OS - fixed parsing of different outputs for command "show
    vlan brief"
-   Cisco NX-OS - fixed parsing of different outputs for commands "show
    ospfv3 neighbor detail"
-   Cisco NX-OS - Fixed wrong command for IGMP snooping groups
-   Cisco SG - fixed parsing of different output for command "show arp"
-   Dell PowerConnect - fixed parsing of different output for command
    "show interfaces status"
-   Juniper Junos - fixed parsing of different outputs for commands
    "show multicast route extensive"
-   Juniper Junos - fixed parsing of different output for command "show
    connections extensive"
-   Juniper Junos - fixed parsing of different output for command "show
    virtual-chassis"
-   Juniper Junos - fixed parsing of different output for command 'show
    configuration \| display set \| except "^deactivate"'
-   Juniper Junos - fixed parsing of different output for command "show
    lldp neighbors interface \<int>"
-   Extreme Enterasys - fixed parsing of different output for command
    "show spantree stats active sid \<id>"
-   Extreme XOS - fixed parsing of different output for command "show
    edp ports all detail"
-   Extreme XOS - fixed parsing of different output for command "show
    configuration"
-   Fortinet FortiGate - fixed switching between VDOMs
-   HP Arubasw - fixed parsing of different output for command "show ip"
-   HP Arubasw - fixed parsing of different output for command "show
    vlans"
-   HP Arubasw - fixed parsing of different output for command "show
    vlans ports all detail"
-   HP Comware - fixed parsing of different output for command "display
    arp"
-   HP Comware - fixed parsing of different output for command "display
    mac-address"
-   HP Comware - fixed parsing of different output for command "display
    stp region-configuration"
-   HP Comware - fixed parsing of different output for command "display
    interface"
-   HP Comware - fixed parsing of different output for command "display
    fan"
-   HP Comware - fixed parsing of different output for command "display
    ip netstream export"
-   HP Comware - fixed parsing of different output for command "display
    power"
-   Huawei VRP - fixed parsing of different output for command "display
    interface"
-   Huawei VRP - fixed parsing of different output for command "display
    dhcp snooping statistics"
-   Huawei VRP - fixed parsing of different output for command "display
    eth-trunk"
-   Huawei VRP - fixed parsing of different output for command "display
    device"
-   Huawei VRP - fixed parsing of different output for command "display
    current-configuration"
-   PaloAlto - fixed hardware SN for virtual systems

### 3.5.4 (18th June 2020)

OVA MD5SUM: 7BB3D18A74F6D36D94330416C8A5E856OVA
SHA256SUM: 433B2001170341160275044DB430F1EF3F2ED2E1FA9C4E03A68F2A624B677510

**Bug Fixes**

-   Cisco Firepower - NTP disabled for version 6.5 and above due to
    Cisco bug CSCvt01938
-   HP Arubasw - prompt detection fixed - additional chars allow to
    appear in prompt

### 3.5.3 (9th June 2020)

OVA MD5SUM: 59D82DDADAD04C5F160D189A55B23B55  
OVA
SHA256SUM: 3FBA60725BC7261145759AE79DA8E38B54167141F755140D8F67699B5A7F1525

**Improvements**

-   Cisco IOS-XE - Add patch information into version
-   Cisco IOS-XE - show version parsing updated, stack task enabled for
    Cat9k and ct5760
-   End to End path - Gateway mac detection improved
-   Routing edges between devices improved - different VRF established
    if ARP and interface mac is available

**Bug Fixes**

-   End to End path - Multiple lookups on same node optimization fix
-   Arista EOS - fixed collecting of MAC table
-   Arista EOS - MAC multicast - missing multicast table fix
-   Arista EOS - IGMP snooping groups - flood support added
-   Cisco ASA/FTD - ACL evaluation fixed (for cases with inbound global
    ACL only)
-   Cisco ASA/FTD - "internal-only” interfaces are not parsed anymore
    (names like "Internal-Data”, "Internal-Control” or "Virtual” with
    nameif "\_internal_loopback”)
-   Cisco IOS - fixed parsing of different output for command "show ip
    igmp snooping"
-   Cisco IOS - IGMP snooping - parsing fix for EOL comma, multiple
    versions, and different headers
-   Cisco IOS - MAC multicast - parsing fix for no ports or no VLAN
    entries, 6500 new header fix
-   Cisco IOS - fixed parsing of different outputs for commands "show ip
    pim rp vrf all" and "show ip pim rp mapping"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show wlan summary"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show wireless client mac-address \<mac> detail"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show ap name \<apName> wlan dot11 5ghz"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show ap name \<apName> wlan dot11 24ghz"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show ap cdp neighbors"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different outputs for
    commands "show ap name \<apName> ethernet statistics"
-   Cisco IOS-XE - show version - stack member parsing fixed to deal
    with missing system sn
-   Cisco NX-OS - fixed parsing of different outputs for commands "show
    ip pim rp vrf all" and "show ip pim rp mapping"
-   Cisco NX-OS - MAC multicast - different platform heading parsing fix
-   Cisco NX-OS - MAC address table - VTEP IP parsing fixed
-   Cisco Nexus VPC - STP virtual bridge ID mac fix, CDP to establish
    STP links for virtual bridge ID is required.
-   Fortinet FortiGate - fixed parsing of different output for command
    "show system zone"

### 3.5.2 (1st June 2020)

OVA MD5SUM: 2985C13C8185B470F4BD65A05826FCA2  
OVA
SHA256SUM: 84CF13C1266B0FC690765C2E547C61DF9679DF2B4CEC023CBEB3DEA06F46220F

**Features - Protocol and technology support**

-   Arista EOS - Added AAA support
-   Juniper Junos - add ISIS IPv6 neighbors support
-   Cisco FTD added support for AAA, ACL, NAT, NTP, Object groups,
    Routing table, SNMP, Syslog
-   Cisco IOS, IOS-XE, NX-OS & Arista - New IGMP Snooping and mac
    multicast tables
    -   Technology / Multicast / Mac table
    -   Technology / Multicast / IGMP Snooping / Vlans Configuration
    -   Technology / Multicast / IGMP Snooping / Global Configuration
    -   Technology / Multicast / IGMP Snooping / Groups
-   Cisco IOS, IOS-XE, IOS-XR, NX-OS & Arista & Juniper - Add info about
    PIM Rendezvous Points (RP) and Bootstrap servers
    -   Technology / Multicast / RP / Overview
    -   Technology / Multicast / RP / BSR
    -   Technology / Multicast / RP / Mappings
    -   Technology / Multicast / RP / Mappings Groups

**Improvements**

-   Settings - Advanced - new setting for discovery tasks
    -   The discovery process can be limited only to devices that were
        already discovered in the past.
    -   The number of tasks for discovery process can be also limited by
        "What information is used to identify neighbors"
-   Pathlookup - Multicast over unreachable transit support added.
-   Mikrotik RouterOS - remove syslog messages from command output +
    fixed processing of tunnel interfaces
-   Table Technology / Management / AAA / Servers - added columns
    "Destination hostname", "Config name" - (hidden by default)
-   Table Technology / IP Telephony / Phones - added columns "Vendor"
-   Cisco Nexus - Mroute table counters (incoming packets and avg.
    packet size) added
-   Cisco Nexus - routes with “pending only” parameters are not put into
    the routing table
-   Cisco FTD - uptime parsing fixed for device in failover cluster
    (device uptime is used now)
-   Added Voice VLAN parameter from Arista switchports.
-   Cisco ASA/FTD - added support for "show interface detail" command to
    better parse vlan IDs on interfaces (cmd "show interface" still kept
    as backup cmd)
-   Host-to-gateway - STP instance added not only based on ROOT ID (can
    be same for virtual mac) but also STP domain ID.
-   CSV export - export is limited to 2M rows to improve performance. We
    will introduce a separate Export job in the near future

**Bug Fixes**

-   Managed duplicate IP false positive removed for
    -   VXLAN virtual address
    -   VXLAN source loopback address
-   Fixed detection of some entry-level FortiGate models (e.g. 30D)
-   Unable to discover Meraki with automated snapshot
-   Enable discover HP ProCurve in the stack
-   The user with read priviliges could update intent verification
    rules.
-   Arista EOS - fixed collecting of multicast routing table for all
    VRFs
-   Arista EOS - fixed parsing of different output for command "show
    vlan"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf neighbor detail"
-   Arista EOS - fixed parsing of different output for command "show
    port-channel summary"
-   Arista EOS - fixed parsing of different output for command "show
    interfaces vxlan 1"
-   Arista EOS - collect PIM commands for all configured VRFs
-   Cisco ASA - fixed parsing of different output for command "show
    context"
-   Cisco NX-OS - fixed parsing of different output for command "show ip
    igmp group vrf all"
-   Cisco NX-OS 9000 - MTU information is now taken from port
    configuration instead of QoS policy.
-   Cisco IOS - fixed parsing of different output for command "show ip
    vrf"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different output for
    command "show wireless client summary"
-   Cisco Firepower Threat Defense - fixed mapping of mac address table
-   Extreme XOS - get ARP records from all vr
-   HP Comware - fixed parsing of different output for command "display
    dhcp-snooping packet statistics"
-   HP Comware - fixed parsing of different output for command "display
    device manuinfo"
-   Huawei VRP - fixed parsing of different output for command "display
    bgp peer"
-   Huawei VRP - fixed parsing of different output for command "display
    bgp peer verbose"
-   Juniper Junos - fixed parsing of different output for command "show
    ldp neighbor extensive instance \<vpnName>"
-   Juniper Junos - fixed parsing of different output for command "show
    spanning-tree bridge detail"
-   Juniper Junos - fixed parsing of various output for command “show
    interfaces terse"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration \| display set"
-   Juniper Junos - fixed parsing of different output for command "show
    ethernet-switching interface"
-   Juniper Junos - fixed showing of RPs in multicast routing table
-   Huawei VRP - fixed parsing of different output for command "display
    ospf peer"
-   Palo Alto - fixed parsing of different output for command "show arp
    all"
-   Cisco IOS-XE WLC 9800 - fixed parsing of different output for
    command "show ap summary"

### 3.5.1 (20th April 2020)

**Features - Protocol and technology support**

-   New multicast first-hop routers table - all routers which have
    connected sources ( Technology / Multicast / MRoute / First hop
    router)

**Improvements**

-   Improved system update procedure
    -   Allow downloading logs from an update process
    -   Progress bar for manual package upload
-   At the user's request, we increased CLI session timeout to a maximum
    of 600s (Warning: a high timeout can significantly prolong the
    discovery time)
-   Cisco ASA - ACLs and object groups - added support for ‘names’

**Bug Fixes**

-   Graph protocols - VXLAN VTEP sessions with virtual IP fix
-   Pathlookup - Default GW - prefer devices with host ARP entry
-   Pathlookup - Vxlan multiple router lookup in different VRF fix
-   Pathlookup - Encapsulation into VXLAN first edge RIB tunnel fix
-   Pathlookup - Multicast sources and receivers in snapshot comparison
    fix
-   Pathlookup - Multicast source connected to multiple routers with
    same mac is now represented by one source
-   Pathlookup - Multicast source and first-hop routers detection
    improved
-   Pathlookup - Multicast forwarding - do not send back from to
    incoming interface included in OIL
-   Multicast sources table - (\*, G) false entries removed
-   Mikrotik RouterOS - in some cases getting xDP neighbors could fail
    (fixed)
-   Arista EOS - parse transceivers information from command "show
    inventory"
-   Arista EOS - parse transceivers information from command "show
    port-channel dense"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf interface"
-   Arista EOS - fixed parsing of different output for command "show ip
    route"
-   Arista EOS - fixed parsing of different output for command "show
    interfaces vxlan 1"
-   Arista EOS - several multicast fixes regarding PIM neighbors &
    interfaces, IGMP
-   Cisco - showRun - parsing fixed and extended (ASA AAA, IOS NAT)
-   Cisco IOS-XR - fixed parsing of different output for command "show
    route summary detail"
-   Cisco IOS-XR version 5 - fixed OSPF task mapping, add new commands
    "show ospf interface", "show ospf vrf all interface"
-   Cisco IOS-XR - several multicast fixes regarding PIM neighbors &
    interfaces, IGMP
-   Cisco IOS-XE - WLC 9800 - fixed parsing of different output for
    command "show version"
-   Cisco Firepower Threat Defense - fixed mapping of L2 management
    interface
-   Cisco NX-OS - fixed parsing of different output for command "show ip
    bgp vrf all all neighbor"
-   Cisco NX-OS - fixed parsing of different output for command "show
    nve vni"
-   Cisco NX-OS - several multicast fixes regarding PIM neighbors &
    interfaces, IGMP
-   Cisco Nexus - correctly detect "Error: AAA authorization failed for
    command" as Authentication fail error
-   Cisco Meraki - added support for 'failed' interface state, counters
    load parsing extended
-   Cisco SG - fixed parsing of different output for command "show
    system"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    system"
-   Cisco WLC - fixed parsing of different output for command "show ap
    wlan 802.11a \<apName>"
-   Cisco WLC - fixed parsing of different output for command "show ap
    wlan 802.11b \<apName>"
-   Juniper Junos - several multicast fixes regarding PIM neighbors &
    interfaces, IGMP
-   Juniper Junos - fixed remote IP’s mapping of CCC with long LSP names
-   Juniper Junos - fixed parsing of different output for command "show
    connections extensive"
-   Palo Alto - fixed missing routing table on some of devices
-   CDP/LLDP - Meraki neighbor parsing fixed

### 3.5.0 (1st April 2020)

OVA MD5SUM: A129A0FD9359105E9C637ADC332459AE  
OVA
SHA256SUM: 9A3713121B9072882F8332618594F4BAB566697D52544FEBB737DAD528321203  
Hyper-V MD5SUM: 698E5DF7D7A945EE2FABCA4DA1EA845C  
Hyper-V SHA256SUM: 29E185591D87B327B50D791F8916C6FC08C399984C5AE392902E9EF6418EA8F3

**Features - Protocol and technology support**

-   Add support for Cisco Meraki (REST API provides limited set of
    information)
    -   Setup REST API connection at Settings / Advanced / Vendors API
-   Add support for L2VPN technologies: CCC, VPWS and VPLS. (Cisco
    IOS's, Juniper)
    -   Tables in Technology / MPLS / L2 VPN
-   Add support BGP over IPv6 for Cisco XR
-   Add support for Multicast (IGMP, PIM, MROUTE) for Cisco IOS, IOS-XE,
    IOS-XR, NX-OS, Arista EOS, Juniper Junos
    -   Tables in Technology / Multicast

**Features - System**

-   Techsupport file - added option to make database dump without
    devices data (only system tables + settings)

**Improvements**

-   Technology / FHRP tables improved to be VRF aware
-   CSV export - removed first line with "sep=;" and escape all value
    (stop forcing auto-format in excel
-   Pathlookup
    -   MPLS explicit null label support added
    -   MPLS swap and push label support added
-   Count of total rows for some table can be a big performance problem,
    so this feature is disabled for some tables. "unknown" is used
    instead of total rows.
    -   Technology / MPLS / L3 VPN / PE Routes
-   Juniper Junos - Get import/export route targets to VRF from policies

**Bug Fixes**

-   Configuration management - syslogTrigger option didn't work, fixed
-   Tables - fixed updating of rule for Advanced Filters
-   Techsupport page - fixed issue when techsupport failed, then the UI
    still displayed that the process is in progress
-   Host to gateway - fixed Host in VRF
-   Arista EOS - keep domain name in hostname
-   Arista EOS - fixed mapping for VXLAN task
-   Arista EOS - fixed parsing of different output for command "show
    interfaces"
-   Arista EOS - fixed parsing of different output for command "show
    interfaces vxlan 1"
-   Arista EOS - fixed parsing of different output for command "sho ip
    bgp neighbor vrf all"
-   Arista EOS - fixed parsing of different output for command "show ip
    bgp neighbor"
-   Cisco IOS-XE Catalyst 9000 - fixed parsing of stacking information
-   Cisco ASA - fixed parsing of different output for command "show ipv6
    interface"
-   Cisco ASA - fixed parsing of different output for command "show run"
-   Cisco ASA - fixed parsing of different output for command "show
    route", add name alias to IP mapping
-   Cisco ASA - fixed parsing of different output for command "show run
    all object"
-   Cisco ASA - fixed parsing of different output for command "show ipv6
    ospf neighbor detail"
-   Cisco IOS - fixed parsing of different output for command "show vrf
    detail"
-   Cisco IOS - fixed parsing of different output for command "show ip
    protocols"
-   Cisco IOS/IOS-XE - fixed parsing of capwap interfaces
-   Cisco ASR9K/10K - show version parsing fix
-   Cisco IOS-XE cat3K - stack member without HW version and empty stack
    parsing fixes
-   Cisco IOS-XE - fixed parsing of different output for command "show
    monitor detail"
-   Cisco IOS-XE - fixed parsing of different output for command "show
    authentication sessions"
-   Cisco IOS-XE - fixed parsing of different output for command "show
    run"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    mpls forwarding-table detail"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    ospfv3 vrf all-inclusive neighbor detail"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    ospf vrf all-inclusive neighbor detail"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    mpls forwarding"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    hsrp"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    isis neighbor detail"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    snmp host"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    run"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    ospfv3 vrf all-inclusive interface"
-   Cisco NX-OS - fixed parsing of different output for command "show
    ospfv3 vrf all neighbors detail"
-   Cisco NX-OS - fixed parsing of different output for command "show
    ipv6 interface vrf all"
-   Cisco NX-OS - fixed parsing of different output for command "show
    fex detail"
-   Cisco NX-OS - fixed parsing of different output for command "show
    ospfv3 vrf all"
-   Cisco NX-OS - keep domain name in hostname
-   Cisco NX-OS - try to use 2 different commands for routing table per
    VRF instance
-   Cisco SG - fixed parsing of different output for command "show
    system"
-   Cisco SG - fixed parsing of different output for command "show run"
-   Cisco SG - fixed parsing of different output for command "show
    interface switchport \<intName>"
-   Cisco SG - Secure access ports - port auth.state fix
-   Cisco WLC Air - fixed parsing of different output for command "show
    wlan \<wlanId>"
-   Cisco WLC Air - fixed parsing of different output for command "show
    port detailed-info"
-   Cisco WLC Air - fixed parsing of different output for command "show
    ap wlan 802.11a \<apName>"
-   Cisco WLC Air - fixed parsing of different output for command "show
    ap wlan 802.11b \<apName>"
-   Cisco WLC Air - fixed parsing of different output for command "show
    lag summary"
-   Checkpoin Gaia - fixed parsing of different output for command "show
    ospf interfaces detailed"
-   Extreme XOS - fixed mapping for L2 interfaces
-   Extreme XOS - fixed parsing of different output for command "show
    stpd detail"
-   Fortinet Fortigate - fixed parsing of different output for command
    "diag netl agg name \<aggregate>"
-   F5 BigIP - fixed parsing of different output for command "show cm
    device"
-   Fortinet FortiOS - fixed parsing BGP neighbors which are in active
    state for a long time
-   Fortinet FortiGate - Zone FW - FQDN address object couldn’t be found
    if it was defined with upper case letters
-   HP ArubaSW - fixed parsing of different output for command "show ap
    lldp neighbors"
-   HP Comware - fixed parsing of different output for command "display
    stp"
-   HP Comware - fixed parsing of different output for command "display
    wlan ap all verbose"
-   Huawei VRP - fixed parsing of different output for command "display
    ospf interface all"
-   Huawei VRP - fixed parsing of different output for command "display
    eth-trunk"
-   Huawei VRP - fixed parsing of different output for command "display
    lldp neighbor"
-   Huawei VRP - fixed parsing of different output for command "display
    snmp-agent community read"
-   Huawei VRP - fixed parsing of different output for command "display
    snmp-agent community write"
-   Huawei VRP - fixed parsing of different output for command "display
    ip routing-table vpn-instance \<name> statistics"
-   Huawei VRP - fixed parsing of different output for command "display
    ntp sessions"
-   Huawei VRP - fixed parsing of different output for command "display
    observe-port"
-   Huawei VRP - fixed parsing of different output for command "display
    esn"
-   Huawei VRP - fixed parsing of different output for command "display
    vrrp"
-   Huawei VRP - fixed parsing of different output for command "display
    mac-address"
-   Huawei VRP - fixed parsing of different output for command "display
    port-mirroring"
-   Huawei VRP - imporved parsing for command "display ip vpn-instance"
    to support long names of VRF
-   Huawei VRP - "display device" and "display device manufacture-info"
    parsing fixed and extended to better support modular chassis
-   Checkpoint Gaia - improved OS version detection, support for new
    versions outputs.
-   Mikrotik RouterOS - fixed command to get bridge hosts table
-   Juniper Junos - fixed parsing of different output for command "show
    lacp interfaces"
-   Juniper Junos - fixed parsing of different output for command "show
    spanning-tree interface detail"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration security policies \| display set"
-   Juniper Junos - fixed getting VRRP group in idle state
-   Juniper Junos - fixed parsing of different output for command "show
    vrrp detail"
-   Juniper Junos - fixed parsing of different output for command "show
    interfaces statistics detail"
-   Juniper Junos - fixed parsing of different output for command "show
    ldp neighbor extensive instance \<ipv4VpnName>"
-   Palo Alto - interfaces: n/a duplex and speed are not parsed as
    unknown but as n/a
-   Quagga - fixed parsing of different output for command "show bgp
    summary"
-   Quagga - fixed parsing of different output for

### 3.4.4 (11th March 2020)

OVA MD5SUM: EF151028D7F0DABFC556F87F3696E1C1  
OVA
SHA256SUM: 40449CAC066CF91A7934514DE870A86B5CDAD09D486C1863F8578259635E471A

**Bug Fixes**

-   Maintenance job - fixed memory leak in reading snapshots details.

### 3.4.3 (4th March 2020)

**Improvements**

-   Removed automatic sanitization for LDAP Settings
-   Added new option to disable LDAP nested groups for AD (speedup login
    process)
-   Added ldap-search tool into image for troubleshooting purposes

### 3.4.2 (27th February 2020)

OVA MD5SUM: 2B16E83667672944095CEC1BA6FCE92A  
OVA
SHA256SUM: 5652274E1678A40ADF03945F95FA174C0F06245CB213DB7CDBF9AD4FFDF65B40  
Hyper-V MD5SUM: 43D8EDCDE98F7F176306B1529DDC32EE  
Hyper-V SHA256SUM: AF8A6B44963C71E7FE28FB08D4D474FD2B18F93E17265C4F3CE5C6051984E017

**Improvements**

-   Added NGINX logs into techsupport file

**Bug Fixes**

-   LDAP Groups - the user groups are always determined using "member"
    and also using "memberOf" attribute, no matter on LDAP server type.
-   User management - fixed fail to create user with any capital letters
-   FIX API service isn't restarted when DB service isn't alive - only
    message in UI will be displayed
-   Cisco IOS - fixed parsing of different output for command "show
    crypto session brief"
-   Juniper - Add protocol isis parameter to cmd for route summary task
    (protection before downloading full bgp table)
-   Fixed several problems with Backup/Restore

### 3.4.1 (5th February 2020)

**Improvements**

-   Quagga Routing Suite - replaced command "show interfaces vrf all"
    with "show interfaces"
-   Quagga Routing Suite - replaced command "show ip route vrf all" with
    "show ip route"
-   Quagga Routing Suite - replaced command "show ip route summary vrf
    all" with "show ip route summary"

**Bug Fixes**

-   LDAP - fixed sanitization of DN information, improved LDAP logs
-   Arista EOS - fixed parsing of different output for command "show ip
    route \<protocol>"
-   Arista EOS - fixed parsing of different output for command "show ip
    bgp neighbors"
-   Juniper Junos - fixed parsing of different output for command "show
    version" - missing hostname in output

### 3.4.0 (28th January 2020)

OVA MD5SUM: 0eba4cf8e164ce267ce6edd0677f8dda

OVA
SHA256SUM: 17d733e041c2726bc0dd74d88573f88525c0a3ba9cfbb65ad4faafe0de4ce7b0

**Features - Protocol and technology support**

-   Added support for Cisco Converged Access WLCs and “Next-Gen” WLCs
    9800
-   Added support for Quagga Routing Suite
-   Added basic support for Virtual Systems on Palo Alto firewalls
-   New VRF tables (Technology => Routing => VRF)
    -   Summary - to get a quick overview of configured VRF in your
        network.
    -   Detail - configured VRF per device.
    -   interfaces - configured VRF on device and interface.
-   New L3 VPN tables (Technology => MPLS => L3 VPN)
    -   PE Routers in network
    -   VRF configured on PE routers with summary of routes in VRF
    -   Route targets import and export configured in VRF
    -   Routes on PE in VRF including originating source PE

**Features - System**

-   implemented LDAP groups - now is possible set permissions per LDAP
    domain group.
-   compare feature now working also for STP instances
-   FIX: L3 protocols edges disappeared after transit cloud expansion

**Visualization**

-   FIX: Positions of FEX's weren't correctly restored for next snapshot
    (or reloaded snapshot) - all views with FEX's have to be saved again
    after rearranging positions.
-   Pathlookup - Cisco ACI support added
-   Pathlookup - possibility to track packet path in specific VRF,
    including VRF auto detection.

**Improvements**

-   Added column Mac address into Technology => Management => Manage IP
-   Arista - ARP and RIB tables support for non-vrf devices
-   Arista - BGP and ISIS support for non-vrf devices
-   Cisco ASA cluster auto-generated MAC starting with A2 - when IP is
    learned from ARP, it’s included to discovery.
-   Fortinet Fortigate - added verstion detection for fortigate with
    Wifi module
-   Snapshot Management - Settings detail can be closed on ESC
-   Juniper Junos - VRRP groups were assigned to wrong subinterface. Now
    groups are assigned properly.
-   End of Life table improvement - One summary table per unique PID,
    one detail table showing all PID and their SN
-   Technology / Routing / Summary - BGP, IS-IS, OSPF, OSPFv3 added VRF
    column
-   CLI Authentication - allow to save duplicit usernames
-   L2 Edge port - xDP protocols on void are removed from decisions
    process as they can lie with their capabilities (e.g. OPX send it’s
    router)

**Bug Fixes**

-   Fixed problem with resolving DNS names - some IP didn't have to be
    translated.
-   Arista - fixed missing native VRF in OSPF
-   Arista EOS - fixed parsing of different output for command "show
    interfaces vxlan 1"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf neighbor detail"
-   Cisco ACI - Interface vlan mac address parsing fix
-   Cisco ACI - fixed parsing of different output for command "show vlan
    extended"
-   Cisco ASA routing table - nexthop IP to outgoing interface mapping
    fixed
-   Cisco IOS - fixed parsing of different output for command "show ip
    cef detail"
-   Cisco IOS - fixed parsing of different output for command "show mpls
    forwarding-table detail"
-   Cisco IOS - fixed parsing of different output for command "show
    spanning-tree mst"
-   Cisco IOS - fixed parsing of different output for command "show
    power inline"
-   Cisco IOS - fixed parsing of different output for command "show cdp
    neighbors detail"
-   Cisco IOS XE - fixed parsing of different output for command "show
    vlan brief"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    mpls forwarding"
-   Cisco NX-OS - fixed parsing of different output for command "show
    nve vni"
-   Cisco NX-OS - fixed parsing of different output for command "show
    system internal l2fwder mac"
-   Cisco NX-OS - fixed parsing of different output for command "show
    logging server"
-   Cisco NX-OS - fixed parsing of different output for command "show
    interface switchport"
-   Cisco NX-OS - fixed parsing of different output for command "show
    environment fex all"
-   Cisco SG350 - fixed version detection
-   Cisco SG - fixed parsing of different output for command "show
    interface switchport"
-   Extreme Enterasys - fixed parsing of different output for command
    "show system"
-   Extreme Enterasys - fixed parsing of different output for command
    "show neighbors"
-   Extreme Enterasys - fixed parsing of different output for command
    "show lacp"
-   Extreme Enterasys - fixed parsing of different output for command
    "show port status"
-   Extreme Enterasys - fixed parsing of different output for command
    "show ip route"
-   Extreme Enterasys - fixed parsing of different output for command
    "show port counters"
-   Extreme Enterasys - improved version detection
-   F5 BigIP - fixed parsing of different output for command "show sys
    hardware"
-   Fortigate - fixed missing VIP address objects in FortiGate policies
-   Fortinet Fortigate - fixed parsing of different output for command
    "get router info ospf interface"
-   Fortinet Fortigate - fixed parsing of different output for command
    "get router info vrrp"
-   Fortinet Fortigate - fixed parsing of different output for command
    "show firewall policy"
-   HP ArubaSW - fixed parsing of different output for command "show
    trunks"
-   HP ArubaSW - fixed parsing of different output for command "show ip"
-   HP ArubaSW - fixed parsing of different output for command "show
    spanning-tree instance \<instance>"
-   HP ArubaSW - fixed parsing of different output for command "show
    interface all"
-   HP ArubaSW - fixed parsing of different output for command "show
    interface brief"
-   HP ArubaSW - fixed parsing of different output for command "show
    vlans ports all detail"
-   HP Comware - fixed parsing of different output for command "display
    mac-authentication"
-   HP Comware - fixed parsing of different output for command "display
    isis peer ver \<processId>"
-   HP Comware - fixed parsing of different output for command "display
    clock"
-   HP Comware - fixed parsing of different output for command "display
    mirroring-group all"
-   HP Comware - fixed parsing of different output for command "display
    link-aggregation verbose"
-   Juniper Junos - fixed parsing of different output for command "show
    route active-path"
-   Juniper Junos - fixed parsing of different output for command "show
    interfaces terse"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration forwarding-options sampling"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration interfaces \| match sampling \| display set"
-   Juniper Junos - fixed parsing of different output for command 'show
    configuration \| display set \| except "^deactivate"'
-   Juniper Junos - fixed parsing of different output for command "show
    route active-path"
-   Juniper - SNMP & Logging parsing fix when deactivated part was in
    config
-   Juniper - fixed getting ACL from device configuration
-   Juniper Junos - fixed route summary calculations, now corresponds
    correctly to number of routes in routing table
-   Juniper Junos - BGP summary parsing fix

### 3.3.3 (10th December 2019)

OVA MD5SUM: 3849bcf518ac89ea987f70af48ed88fa

OVA
SHA256SUM: cf360ee8379b73591a1c7790004e11aa49f02f1da5bdaa101a933d251a71f3b5

**Visualization**

-   Comparison of routing protocols in the graph was fixed - added links
    were not displayed
-   FIX: OSPFv3 edges weren't displayed

**Improvements**

-   Snapshot Management - Inventory tab - added column platform
-   Cisco ACI - RIB recursive lookup fix
-   Cisco IOS/XR - RIB to MPLS forwarding for global table improved
-   Cisco MPLS forwarding table parsing updated to better support per
    VRF aggregate labels

**Bug Fixes**

-   Discovery didn't work without any configured "enable" password
-   Snapshot locking / unlocking fix
-   Cisco IOS - BDI interface is standardized to BD so all outputs
    provides same interface name
-   FIX - Discovery process can be stuck (with enabled DNS resolving)
-   Cisco ACI - fixed parsing of different output for command "show vlan
    extended"
-   Cisco NX-OS - fixed ambiguous command for show routing table
-   Configuration Management worker - if serial number of the device
    included "/" character then the config file wasn't saved

### 3.3.2 (28th November 2019)

OVA MD5SUM: 351f8829c6a6d8106519958b60cc3074

OVA
SHA256SUM: 422a095b590301074049b489722be1a03729d00401d4d4e73de483c2b12fe82e

**Features - Protocol and technology support**

-   PortChannel - added support HP ArubaSW
-   New table Management => Discovery History
    -   This table shows all discovered devices in history (no matter
        which snapshot is selected).

**Visualization**

**Improvements**

-   Settings - Advanced - System - Clear DB: Don't delete main inventory
    data table on keep settings option.
-   Pathlookup - Default GW selection - prefer arp entry over virtual
    address.
-   Pathlookup - Destination site behind transit cloud recognition
    improvement
-   HP Comware WLC - removed WLAN-DBSS interfaces
-   Snapshot Connectivity report - allow rediscover IP addresses what
    were excluded or weren't included before
-   Settings / Authentication / credentials list for CLI - added field
    to exclude specific CIDR ranges
-   Settings / Authentication / credentials list for enable commands -
    added include / exclude specific CIDR ranges, username

**Bug Fixes**

-   Management / Changes - the changes could be wrong after ADD or
    REFRESH actions in that snapshot
-   Diagrams - if the site was opened from network overview diagram then
    "single point of failure" or "Nonredundant links" didn't work
-   System - Backup - backup to FTP/FTPS server didn't work without
    directory specification
-   Add devices into snapshot - if the IP addresses were already tried
    before then it weren't inserted as a new tasks
-   Cisco NX-OS - fixed parsing of different output for command "show
    interface status err-disable"
-   HP ArubaSW - improved prompt detection
-   HP ArubaSW - MSTP fixed to use only enabled vlans on ports
-   HP ArubaSW - fixed parsing of different output for command "show cdp
    neighbors detail"
-   HP ArubaSW - fixed parsing of different output for command "show
    lldp info remote-device \<intName>"
-   HP ArubaSW - fixed parsing of different output for command "show
    lldp info remote-device detail"
-   HP ArubaSW - L2 interfaces - not all interfaces were correctly
    parsed
-   Juniper Junos - fixed parsing of different output for command "show
    interfaces statistics detail"

### 3.3.1 (18th November 2019)

OVA MD5SUM: 962ebf98db27d514ec993a7e8d2c0735

OVA
SHA256SUM: 18e5df2c5ab44756d790b47ced322a138a62dc075c81c4fbe4ffcfe786909e17

**Features - Protocol and technology support**

-   New table Technology => CDP/LLDP => Endpoints neighbors
    -   This table shows all endpoints found by XDP protocols.

**Improvements**

-   TechSupport & Snapshot Download is generated via API jobs and the
    result (link for download) will be in Jobs menu now.
    -   Those links will be there until user confirm it with X button
        (user can safely reload the page)
-   Allow to save credentials with empty username (for telnet purposes)
-   Discovery remember used protocol now and this protocol is preferred
    for next discovery (improved speed of discovery)
-   Improved "Save historical data" job which is run after discovery -
    precalculation of data is much faster now
    -   WARNING - all snapshots should be reloaded otherwise you will
        get false changes in Management / Changes tables.
-   Maintenance page is displayed also during job "Clean DB" - during
    this time API don't responding to any request returns HTTP status
    503
-   Device hostname should be never empty - if command for getting
    hostname will fail, then we're getting hostname from CLI prompt
-   HP Aruba switches - MSTP mode detection improvement
-   WLC HP Comware - Wireless service interfaces WLAN-DBSS removed from
    discovery
-   WLC Aruba - Wireless service interfaces Aruba removed from discovery
-   Site Separation using regex - new button for result preview
    (optimization for big networks)
-   Discovery - processing of small snapshots will be much faster now

**Bug Fixes**

-   Fix for corrupted CLI log files
-   HP Aruba - hotfix for enable mode (sending enter for Username:
    prompt)
-   CDP/LLDP - Parsing fix of some AP and IP Phone reported interface.
    Improved aggregation of multiple CDP & LLDP entries from same device
-   Manual site separation - didn't work correctly for already loaded
    snapshot
-   Diagrams - fixed Cisco nx7000 wrong icon
-   Fixed cases where UI shown "\[object response\]" instead of errors
-   Settings - Advanced - System - Clear DB: The jobs weren't correctly
    rescheduled
-   Arista EOS - fixed Switchport on L2 interfaces
-   Arista EOS - fixed parsing of different output for command "show ntp
    ass"
-   Arista EOS - fixed parsing of different output for command "show ip
    dhcp snooping counters debug"
-   Cisco IOS & NX-OS - fixed parsing of different output for command
    "show ip dhcp snooping binding"
-   Cisco IOS & NX-OS - fixed parsing of different output for command
    "show ip dhcp snooping statistics"
-   Cisco IOS & NX-OS - “show vlan brief” support for long names and
    spaces in names added
-   Cisco IOS use "show vlan-switch brief" command (instead of show vlan
    which gives ambiguous command).
-   Cisco IOS / IOS-XR / IOS-XR - fixed ISIS system type L1/L2
-   Enterasys fixed device prompt detection
-   Enterasys minor fixes regarding CDP & LLDP bindings
-   F5 Big-IP - fixed parsing of different output for command "show cm
    device"
-   HP ArubaSW - fixed parsing of different output for command "show
    dhcp-snooping"
-   HP ArubaSW - fixed parsing of different output for command "show
    spanning-tree detail"
-   HP Comware WLC - client AP mac detection improved so it’s correctly
    tied to AP
-   Juniper Junos - fixed parsing of different outpur for command "show
    vlans detail"
-   Mikrotik - fixed parsing of different output for command "/interface
    print detail"
-   Mikrotik - fixed parsing of different output for command "/ip route
    print detail"
-   Mikrotik - fixed parsing of different output for command "/system
    ntp client print"

### 3.3.0 (4th November 2019)

OVA MD5SUM: 5fe5fbba70252dcc60ed76a33ebb9eed

OVA
SHA256SUM: 2dc27c1de2d3bb664359e9906cec80bf685bff0e6cb25c68f0933dfe29867f1c

**Features - Protocol and technology support**

-   Added support for Mikrotik routers (please read known issue
    <https://ipfabric.atlassian.net/wiki/spaces/ND/pages/735248385/Mikrotik>)
-   Added basic support for Enterasys vendor
-   Every snapshot has own settings which can be extended from global
    settings.
-   SSID Summary table for wireless (Technology / Wireless /
    Radios/BSSID / SSID Summary)
-   Vlan database collection with new vlan detail and summary tables
    -   Technology -> Vlans -> Device Summary - Number of VLANs
        configured per device
    -   Technology -> Vlans -> Device Detail - Detail for specific vlan
        and device
    -   Technology -> Vlans -> Network Summary - List of all vlans
        configured in network. Grouped by VLAN ID
    -   Technology -> Vlans -> Site Summary - List of all vlans
        configured on the site
-   Collecting information about DHCP snooping
    -   Technology -> Security -> DHCP Snooping

**Visualization**

-   Diagrams - display results from intent verification rules
-   Diagrams - Host to gateway & Pathlookup form - the last used values
    are remembered
-   Diagrams - Protocols can be expanded / collapsed on double click
-   Performance improvements - loading of graph should be faster
-   Comparing was improved to display changes for edges pointing into
    transit cloud + changes for interconnected sites edges (If the site
    have more than 400 ummanaged neighbors then it can't be compared)
-   If transit cloud have more than 100 devices then it can't be
    expanded.

**Improvements**

-   Improved network credential management - you can set expiration for
    credentials, more subnet for individual credential, update password.
-   Cisco ASA - object-groups added support for system pre-defined
    objects
-   Cisco Nexus - transceivers added to inventory.
-   Settings / Advanced / System - Clear DB - now you can choose if you
    want to keep settings or restore initial settings.
-   Settings / Advanced / SSH/Telnet - added new option to disable
    discovery using telnet protocol
-   Settings / Advanced / Maintenance - a new job which is necessary to
    run on daily to keep the system healthy (The job can be run also
    manually)
-   Reserverd IPv4 prefixes are automatically excluded from discovery
    (0.0.0.0/8, 127.0.0.0/8, 224.0.0.0/4, 240.0.0.0/4)
-   Pathlookup - Gateway selection algorithm will consider only /8 and
    smaller networks.
-   Diagrams - don't navigate into overall network view when leaving or
    entering pathlookup or host2gateway mode

**Bug Fixes**

-   Configuration management didn't work correctly from 3.2.0 - the
    changes in settings wasn't applied without a service restart
-   CLI - pagination text wasn't correctly cleared from CLI output (bug
    introduced in 3.2.1)
-   Diagrams - options "Show edge" wasn't correctly restored for loaded
    view
-   Diagrams - The saved views with long names couldn't be deleted
-   Diagrams - Saved view (including ViewBuilder) keep the position of
    transit cloud
-   Discovery could stuck on stop action when scanner was enabled.
-   LDAP Authentication - new ldap admin didn't have set privileges
    correctly
-   LDAP Authentication - case sensitivity issue Fixed
-   Certification Authorities - fixed verification if uploaded file is
    correct certificate
-   Snapshot uploading - the second attempt to upload a snapshot leads
    to deleting a snapshot from the hard drive.
-   Downloaded snapshot what was later uploaded had a problem that the
    refresh or add new devices didn't work. Used CLI credentials were
    sanitized on download, the user is prompted to set new credentials
    now.
-   Inventory - Interfaces table: IP column, preferring virtual IP as
    first (previously virtual IP was not shown).
-   Arista EOS - fixed parsing of different output for command "show
    sflow"
-   Arista EOS - fixed parsing of different output for command "show ntp
    ass"
-   Arista EOS - fixed parsing of different output for command "show ip
    arp vrf \<vrfName>"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf nei det"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf interface"
-   F5 - Hostname for both devices in cluster was same. Now it's fixed,
    each member has correct hostname.
-   F5 Big-IP - fixed parsing of different output for command 'run util
    bash -c "ntpq -np"'
-   HP Aruba WLC - duplicit client output fixed - it caused that no
    access point was saved (unique index duplicity)
-   HP Aruba switch - fixed parsing of different output for command
    "show mac-address"
-   Cisco ASA - fixed parsing of different output for command "show bgp
    summary"
-   Cisco ASA - fixed parsing of different output for command "show run"
-   Cisco IOS - startup config can be empty fix
-   Cisco IOS - fixed parsing of different output for command "show isis
    neighbor detail"
-   Cisco IOS - fixed parsing of different output for command "show
    dot1x all details"
-   Cisco IOS - fixed parsing of different output for command "show
    interface"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    inventory all"
-   Cisco IOS-XR - fixed parsing of different output for command "show
    run"
-   Cisco IOS-XR NCS - inventory, hostname and SN fixes
-   Cisco NX-OS - fixed parsing of different output for command "show
    logging server"
-   Cisco NX-OS - fixed parsing of different output for command "show
    inventory"
-   Cisco NX-OS - fixed parsing of different output for command "show
    interface"
-   Cisco NX-OS - fixed parsing of different output for command "show
    monitor session all"
-   Cisco NX-OS - RIB HSRP entry removed from RIB edges
-   Dell FTOS - fixed parsing of different output for command "show ip
    interface"
-   Dell FTOS - fixed parsing of different output for command "show
    interface"
-   Dell FTOS - fixed parsing of different output for command "show ntp
    associations"
-   Dell Powerconnect - fixed parsing of different output for command
    "show interfaces status"
-   Dell Powerconnect - When "show system" hostname is empty, hostname
    is taken from prompt
-   F5 Big-IP - fixed parsing of different output for command "show sys
    tmm-info raw"
-   F5 Big-IP - fixed parsing of different output for command "list net
    trunk all-properties"
-   F5 Big-IP - fixed parsing of different output for command "list sys
    snmp all-properties"
-   F5 Big-IP - Recursive RIB interface lookup fix
-   F5 Big-IP - IP on L3 interfaces fix
-   F5 Big-IP - Duplicit IP in cluster as RIB nexthop fix (active node
    IP used)
-   HP Comware - fixed parsing of different output for command " display
    ip routing-table verbose"
-   Juniper Junos - fixed parsing of different output for command "show
    ldp neighbor extensive instance \<vpnName>"
-   PaloAlto- fixed parsing of different output for command "show system
    resources"

**API Changes**

-   Following endpoints have changed 'vlan' column to 'vlanId', next new
    column added 'vlanName'
    -   /tables/spanning-tree/ports
    -   /tables/spanning-tree/instances
    -   /tables/spanning-tree/topology
    -   /tables/spanning-tree/neighbors
    -   /tables/spanning-tree/vlans

### 3.2.1 (19th September 2019)

OVA MD5SUM: 362052f0fc1cecb4c9fefcb0c0cd76e2

OVA
SHA256SUM: 237754a2d2594c7ee096c6d90f00a7833bb8f6159e40bb9b5f303b5674d30ce6

**Improvements**

-   Cisco ACL - added support for more complex rules combining several
    service object-groups
-   HP Arubasw - LLDP information gathering extended to support switches
    not supporting “show lldp info remote-device detail” command

**Bug Fixes**

-   FIXED: Discovery process can be stuck
-   Pathlookup - Object groups on firewalls in path fix
-   Cisco IOS/IOS-XE - netflow version mapping fix
-   Cisco Nexus - Power supply fans are moved from Fans to Power
    supplies fans tab
-   Extreme XOS- fixed parsing of different output for command "show
    isis neighbors detail"
-   Juniper EX4300 - fixed parsing for "show version"
-   F5 Big-IP - fixed parsing of different output for command 'run util
    bash -c "ntpq -np"'
-   F5 Big-IP - fixed parsing of different output for command "run util
    bash -c uptime"
-   F5 Big-IP - fixed parsing of different output for command "list sys
    snmp all-properties"
-   Fortinet - NTP task fixed for case when NTP is disabled and command
    “diagnose sys ntp status“ is not available
-   HP Aruba switch - fixed parsing of different output for command
    "show system"
-   HP Comware - Interface with lag down state parsing fix
-   HP Comware - fixed parsing of different output for command "display
    fan"
-   FIXED: Riverbed: Uptime does not consider days, parameter is read
    incorrectly

<div class="post has-merged read">

<div class="post-body">

-   System - Disk expansion was not working properly in some cases
-   Juniper – Firewall Filters (ACLs) – QoS related actions like
    loss-priority, forwarding-class or policer are considered to be
    traffic allowing actions (i.e. permit actions). Actual traffic rate
    vs. policing max rate is not taken into account anyhow.

  

<div class="items">

3.2.0 (10th September 2019)

</div>

</div>

</div>

OVA MD5SUM: 822ae7794b420242aa0d9db6dd2d62df

OVA
SHA256SUM: 03073bc8ecedfac612354a1fbf1695e08808a75366cc433f5fc4d78641c02c60

<div>

<div>

Warning already loaded snapshot may not work correctly, they should be
unloaded and loaded again.

</div>

</div>

#### Features - Protocol and technology support

-   Arista EOS - added support for PortChannel task
-   Cisco ACI - added support for discovering
    -   New tables in Technology => SDN => ACI
-   Cisco IOS - Added Flexible flow support
-   Dell FTOS (ver 8 & 9 only) - add support for discovering
-   Dell PowerConnect - add support for discovering
-   Fortinet Fortigate - Added MAC address tables support on transparent
    VDOMs and software switches
-   HP Aruba switch stacking support added

#### Visualization

-   Compare feature - allows compare topology changes between snapshots
-   Refresh data directly from the graph:
    -   New snapshot from devices in the view - allows you to create a
        network snapshot containing only devices in the view to quickly
        refresh data for troubleshooting, path lookup, or other
        purposes.
    -   Refresh devices in the view - refreshes and overwrites collected
        information in the current snapshot for devices in the view.
    -   Add devices into this snapshot - allows adding new devices into
        current snapshot in the same way as from snapshot management but
        directly from the diagram.
-   Site separation implemented in graphs - use drag&drop to move
    devices into new site (use CTRL/SHIFT to select multiple)
-   ViewBuilder
    -   Added "expand" icon to add all devices what are connected to
        parent device
    -   Added "collapse" icon to remove all devices what are connected
        to parent device
    -   Multiple devices can be also selected with CTRL or SHIFT holding
        and those devices can be then added or removed from ViewBuilder
        view.

#### Improvements

-   Snapshot management - new snapshot allows to create snapshot with
    customized global settings
-   Snapshot management - Connectivity report - user can select specific
    IP addresses to rediscover them (only IP with status "stopped",
    "error")
-   Size of loaded or unloaded snapshot was decreased
-   Settings - Authentication - Notes can be set per credentials record
-   F5 BGP - devices with Virtual Clustered Multiprocessing (vCMP)
    should be correctly discovered (fixing error - Device already in
    queue)
-   HPE WLC - Exclude command 'display irf topology' - it may cause high
    CPU
-   Host table - removed Juniper’s localhost addresses
-   Zone FW policy processing updated to support multi-zone interfaces

#### Bug Fixes

-   Snapshot older than 3.1.0 couldn't be loaded
-   Visualization - IS-IS edges wasn't correctly restored for saved
    views, including ViewBuilder
-   Arista EOS - fixed parsing of different output for command "show
    vrf"
-   Arista EOS - fixed parsing of different output for command "show ip
    bgp neighbors vrf all"
-   Arista EOS - fixed parsing of different output for command "show ip
    roout vrf \<vrfName>"
-   Arista EOS - fixed parsing of different output for command "show
    vxlan address-table"
-   Cisco ASA - fixed parsing of different output for command "show ipv6
    interface"
-   Cisco ASA - fixed parsing of different output for command "show
    route"
-   Cisco ASA - fixed parsing of different output for command "show
    context"
-   Cisco IOS 2960 NTP sources parsing fix
-   Cisco IOS - fixed parsing of different output for command "show snmp
    host"
-   Cisco IOS - fixed parsing of different output for command "show ipv6
    interface"
-   Cisco IOS - fixed parsing of different output for command "show
    object-group"
-   Cisco IOS - do not run “show flow interface” command on devices
    where is no exporter (ambiguous cmd fix).
-   Cisco IOS-XE & IOS-XR MPLS forwarding table parsing fixes
-   Cisco IOS-XE - fixed parsing of different output for command "show
    ip cef vrf \<instance> detail"
-   Cisco NX-OS - fixed parsing of different output for command "show
    run"
-   Cisco NX-OS - fixed parsing of different output for command "show
    object-group"
-   Cisco NX-OS - fixed Nexus 5000 interface MTU was wrong due to Cisco
    bug.
-   Cisco WLC - fixed parsing of different output for command "show
    run-config commands"
-   Cisco - fixed parsing of different output for command "show snmp
    user"
-   Checkpoit GAIA - fixed parsing of different output for command "show
    ospf neighbors detailed"
-   Checkpoit GAIA - fixed parsing of different output for command "fw
    ctl pstat"
-   Juniper - Corrected BGP neighbor uptime if the uptime is less than
    60 minutess
-   Juniper Junos - fixed parsing of different output for command "show
    vrrp detail"
-   Juniper Junos - fixed parsing of different output for command "show
    ethernet-switching interfaces"
-   F5 Big-IP - fixed parsing of different output for command "show net
    trunk all-properties" (unsupported counters units)
-   F5 Big-IP - fixed parsing of different output for command 'run util
    bash -c "ntpq -np"'
-   F5 Big-IP - fixed parsing of different output for command "show sys
    hardware"
-   F5 Big-IP fixed get uptime from TMSH
-   Fortinet Fortigate - fixed parsing of different output for command
    "diagnose sys ntp status" (IPv6 ntp sources)
-   Fortinet Fortigate - fixed parsing of different output for command
    "show firewall policy"
-   Fortinet Fortigate - fixed parsing of different output for command
    "show system interface"
-   HP Aruba switch - fixed parsing of different output for command
    "show tech buffers"
-   HP Aruba switch 2920 modules parsing fix
-   HP Aruba switch inventory parsing fix
-   HP Aruba switch - MST instance interface parsing updated to better
    detect disabled ports
-   HP Aruba - standalone access points are not supported, will be
    reported as "Can't detect version" - AP can be discovered only via
    controllers now
-   Huawei Vrp - fixed parsing of different output for command "display
    lldp neighbor"
-   Huawei Vrp - fixed parsing of different output for command "display
    stp"
-   Huawei Vrp - fixed parsing of different output for command "display
    ntp sessions"
-   Huawei Vrp - fixed parsing of different output for command "display
    vrrp"
-   Paloalto - fixed parsing of different output for command "show
    interface \<intName>"
-   Paloalto - fixed parsing of different output for command "show
    routing proto ospf interface"
-   Riverbed - fixed collecting information about memory & device
    platform
-   STP on portchannel to Cisco VSS fix
-   STP to transit for known neighbors fix
-   STP inconsistency - port vlan mismatch for router to switch
    connection fix
-   STP inconsistency - Ports with multiple neighbors, fix for Cisco VPC
    and switch to router connections.
-   STP inconsistency - CDP/STP port mismatch for router to switch
    connection fix
-   Bad device icon in graph - router with NVI interface is recognized
    as a router even without #routes > 1
-   RIB recursive lookup - fix for local IP on own interface in RIB when
    used for recursive lookup
-   Pathlookup - Router to switch connection, multiple next hop with
    different MAC on one interface fix

#### Changes

-   Syslog functionality has been reduced for triggering configuration
    changes only. IP Fabric no longer stores incoming syslog messages
    due to misalignment with product direction.

#### API Changes

-   Datatype changed for column vlanId from string to number in
    following endpoints
    -   /tables/addressing/arp
    -   /tables/interfaces/inconsistencies/details
-   Datatype changed for column vlan from string to number in following
    endpoints
    -   /tables/addressing/mac
    -   /tables/addressing/hosts
    -   /tables/reports/capacity/hosts
    -   /tables/reports/performance/users
    -   /tables/spanning-tree/neighbors
    -   /tables/spanning-tree/instances
    -   /tables/spanning-tree/ports
    -   /tables/spanning-tree/topology
    -   /tables/spanning-tree/vlans
-   Routes changes
    -   POST /start/discovery was replaced with:
        -   POST /snapshots for starting a new discovery / creating a
            new snapshot
        -   POST /snapshots/:key/devices for adding a new device
        -   DELETE /snapshots/:key/devices for removing a device

### 3.1.2 (22nd July 2019)

OVA MD5SUM: 99e9f0518be8cc3a6bc662df89a91617

OVA
SHA256SUM: c32f726930ffd80d9433888510315c8ed1d5509a3f70b2f98f34b3cab472ef50

<div>

<div>

Please be patient during the upgrade to IPF version 3.1.2, it may take
longer than expected due to the migration of its ArangoDB from 3.3.19 to
version 3.4.7.

</div>

</div>

  

#### Improvements

-   BGP - Added support for 4-byte ASN
-   User Interface Security - TLSv1.2 is now the only allowed HTTPS
    protocol
-   Network Assurance Dashboard loading speedup
-   Cisco WLC - Syslog related information is now parsed from “show
    run-config commands” instead of “show logging” which provided a lot
    of unnecessary data
-   Fortinet FortiGate - added support for any-any zone firewall
    policies
-   Juniper memory information is now taken from “show chassis routing“
    command instead of “show system memory“
-   F5 BigIp Improved prompt detection
-   Settings - Advanced - SSH/Telnet - Maximum number of parallel
    sessions can be limited to a single session (Warning: Discovery
    speed will be extremely slow)
-   Settings - Advanced - SNMP - Added support for multiple SNMP pollers
    in

#### Bug Fixes

-   Tables - CSV export - some columns may not have been exported
    correctly
-   UI - the tooltips sometimes left visible artifacts
-   UI - Inventory / Host table - could crash when it was stored with
    old settings
-   UI - Fixed selection of an item in the menu - Diagrams / Site
    Diagrams - Menu Inventory/sites was selected instead of Site
    Diagrams
-   Building network topology - could fail on deadlock in DB
-   Cisco ASA – ACL to L3 interface mapping fixed
-   Cisco ASA - fixed parsing of different output for command "show
    route"
-   Juniper – L2 interfaces and STP related information parsing fixed
    and updated. Command ‘show ethernet-switching interfaces detail’ is
    no longer used and was substituted by other commands including ‘show
    ethernet-switching interfaces’.
-   Juniper - discovery failed when root was used as username
-   Juniper VLAN parsing fixed to include even vlans with names starting
    and ending with double underscores.
-   Juniper - some platform did not correctly set IP as virtual
-   Juniper Junos - fixed parsing of different output for command "show
    vlans detail"
-   Arista EOS - fixed parsing of different output for command "show
    lldp neighbors detail"
-   Arista EOS - fixed parsing of different output for command "show
    interfaces switchport"
-   Extreme XOS - fixed parsing of different output for command "show
    ospf interface detail enabled"
-   Extreme XOS - fixed parsing of different output for command "show
    edp ports all detail"
-   Fortinet FortiGate - fixed parsing of different output for command
    "get router info bgp neighbors"
-   Fortinet FortiGate - fixed parsing of different output for command
    "diag sys ntp status"
-   Fortinet FortiGate - fixed parsing of different output for command
    "diag hard dev nic \<intName>"
-   Huawei - fixed parsing of different output for command "display bgp
    \<addressFamily> \<vpnInstance> peer verbose'"
-   Paloalto - fixed parsing of different output for command "show ntp"
-   Palo Alto - L2 connection to switches fix
-   Palo Alto - routing table parsing fix
-   Palo Alto - L3 connection on cluster fix

### 3.1.1 (28th June 2019)

OVA MD5SUM: 1c8a3b4de12d9a2a3c15ceea4005080e

OVA
SHA256SUM: 138b25ae8b4b1b1f29b6e01a2e15d619a0eddfd610fcbaa042a22a9a8b80f0e0

#### Bug Fixes

-   Snapshot Management - fixed cloning of snapshot
-   F5 BigIP - improved OS version detection

### 3.1.0 (27th June 2019)

#### Features - Protocol and technology support

-   Cisco Firepower Threat Defense - Added basic support
-   Fortinet FortiGate - added support for vDOMs (please follow our [KB
    article](https://ipfabric.atlassian.net/wiki/spaces/NK/pages/676003845/Fortinet+FortiGate+-+IP+Fabric+prerequisites))
-   Fortinet FortiGate - added support for Zone Firewall
-   Added PortChannel support for Fortinet/FortiGate (802.11ad only)
-   Added support for OSPF v3 (Cisco).
    -   Technology -> Routing -> OSPF v3
-   Added basic support of firewall policies on FortiGate firewalls (UTM
    security profiles, load balancing, NAT and user auth objects are not
    supported in this release)

#### Visualization

-   View Builder - enables to define custom views
-   Added OSPFv3 protocol
-   Improved object manipulation in the diagrams
-   Improved non-redundancy and single point of failure checks in the
    diagrams
-   Manual site separation replaced the previous method of site
    separation.

#### Improvements

-   Snapshot management
    -   Discovery page was merged with snapshot management
    -   Services logs are now included in the snapshot data file.
    -   Added ability to remove devices from the snapshot

-   Added Manual site separation (for now only from table) Inventory =>
    Sites => Manual Separation

-   Host table speed up - the table is pre-calculated in the topology
    build process

-   The API documentation is now directly in UI
    -   Each table has API documentation accessible through the "?"
        button

-   Improved site separation by regex
    -   After regex separation is completed, all devices in the unknown
        site (not matched by regex) are moved to the site where they are
        directly connected, if such a connection exists.

-   Backup and restore have been rewritten from scratch. IP Fabric
    backup now supports incremental backup, local backup to separate
    datastore, DB restores, snapshot restore and full restore.

    <div>

    Backup has changed!

    <div>

    Please reconfigure your backup in Settings -> Advanced -> System.
    Restoring backup from versions earlier than 3.1.0 into version 3.1.0
    must be done with the assistance of the support team. Alternatively,
    the earlier backup can be restored to a version 3.0.7 or older, and
    then the version can be upgraded to 3.1.0.

    </div>

    </div>

-   Added support for IP Fabric appliance monitoring via SNMP (CPU, RAM,
    storage, network)

-   Advanced Filtering
    -   Added new operators "is empty" and "is not empty" to able to
        filter for empty values
    -   Array datatypes is able to specify filtering rules for a
        specific item in the array or for all items in the array.

-   Path lookup - Protocol menu can now display available protocols
    according to the path

-   Path lookup - MPLS link type is now based on the presence of label
    stack

-   Path lookup - routing to connected devices (e.g. for WLC) is
    improved

-   Discovery - Multiple CLI credentials - system now remember what
    credentials works and these credentials will be prioritized for next
    attempt to connect to individual devices.

-   TechSupport file
    -   DB dump can be executed only for selected snapshot

-   Technology -> Routing -> IS-IS - added VRF column

-   Technology > Networks > Gateway redundancy - added VRF column

-   Cisco ASA - improved hostname for clusters & contexts

-   Cisco WLC - improved hostname for clusters

-   NTP - Cisco WLC sync unknown state added. NTP summary table now
    considers the unknown state as reachable and is not reported as a
    violation

#### Bug Fixes

-   Host to gateway graph - missing RIB L3 edge to gateway added
-   Host to the gateway - Host was not visible when connected to Cisco
    FEX
-   Path lookup - Connected routes VRF leak to BGP fixes (don't create
    RIB edge to transit, a route to connected network with a leak).
-   AP with GLPB gateway - RIB to all forwarders
-   Path lookup - ACL & Zone FW icons weren't displayed on the path
-   Discovery - Summary of Issues - Authentication errors -
    false/positive reports for this error could be displayed when was
    used multiple credentials
-   Discovery - Tasker process - fixed include/exclude list, sometime
    could be discovered IP addresses what wasn't in included or was in
    excluded list.
-   Juniper Junos - fixed parsing of different output for command "show
    interfaces statistics detail"
-   Arista EOS - fixed mapping for Task STP - when STP is disabled on
    the device
-   Arista EOS - fixed parsing of different output for command "show mac
    address-table"
-   Arista EOS - fixed parsing of different output for command "show
    lldp neighbors detail"
-   Arista EOS - fixed parsing of different output for command "show ip
    interfaces"
-   Arista EOS - fixed parsing of different output for command "show ip
    ospf interface"
-   Arista EOS - fixed parsing of different output for command "show ntp
    ass"
-   Arista EOS - fixed parsing of different output for command "show
    vrf"
-   Cisco ASA - fixed parsing of different output for command "show
    route"
-   Cisco IOS-XE - fixed parsing of different output for command "show
    isis neighbor detail"
-   Cisco IOS - fixed parsing of different output for command "show
    environment all"
-   Cisco IOS - fixed parsing of different output for command "show run"
-   Cisco NX-OS - fixed parsing of different output for command "show
    spa detail"
-   Cisco NX-OS - fixed parsing of different output for command "show
    flow export"
-   Cisco WLC - fixed mapping for Task WLC Access points lists
-   Cisco WLC - fixed parsing of different output for command "show wlan
    \<wlanId>"
-   Cisco WLC - fixed parsing of different output for command "show ap
    stats ethernet summary"
-   Cisco WLC - fixed parsing of NTP
-   Extreme XOS - fixed parsing of different output for command "show
    stpd"
-   Extreme XOS - fixed parsing of different output for command "show
    log configuration"
-   HP Aruba - fixed parsing of different output for command "show ap
    debug system-status ap-name \<apName>"
-   HP Aruba - fixed parsing of different output for command "show
    system"
-   HP Aruba - fixed parsing of different output for command "show ap
    bss-table"
-   HP Comware - fixed parsing of different output for command "display
    ip interface"
-   Checkpoint Gaia - fixed parsing of different output for command
    "show ospf neighbors detailed"
-   HP ArubaSW - fixed parsing of different output for command "show
    spanning-tree debug-counters instance \<mstpInstanceId> ports all"
-   F5 BigIP - fixed parsing of different output for command "show cm
    device"
-   Fortinet FortiGate - fixed parsing of different output for command
    "diag hard dev nic \<intName>"
-   Fortinet FortiGate - fixed parsing of different output for command
    "get system arp"
-   Juniper Junos - fixed parsing of different output for command "show
    spanning-tree interface detail"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration interfaces \| match sampling \| display set"
-   Juniper Junos - fixed parsing of different output for command "show
    lacp interfaces"
-   Juniper Junos - fixed parsing of different output for command "show
    ethernet-switching interface detail"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration \| display set"
-   Juniper Junos - fixed parsing of different output for command "show
    sflow"
-   Juniper Junos - fixed parsing of different output for command "show
    lldp neighbors interface \<intName>"
-   Juniper Junos - fixed parsing of different output for command "show
    interfaces statistics detail"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration forwarding-options sampling"
-   Juniper Junos - fixed parsing of different output for command "show
    configuration firewall"
-   Site Low-level design report - table Interfaces in the HALF duplex
    was wrongly reported

### 3.0.7 (30th April 2019)

#### Features - Protocol and technology support

-   Extreme/Xos - EDP support added

#### Improvements

-   MPLS Cisco IOS, XR - VPN aggregate label support added
-   Routing table - VRF leak information added to next hop column
-   Connected routes leaked to other routing protocols are now removed
    from RIB edges (caused path lookup false routing to transit)
-   Path lookup - Support for VPN aggregate labels added
-   Path lookup - Support for multiple default gw (GLBP)
-   Path lookup - Possible ACL fail on switches with Cisco FEX fixed
-   Host to Gateway - If IP is a network device, show this device only
-   Path lookup - MPLS transit support added. For incoming MPLS
    interface from transit lookup in MPLS table based on prefix is
    checked.
-   Cisco IOS-XE - MPLS was not collected for 15.4 version, added

#### Bug Fixes

-   Manual site separation fixed, it didn't work in certain diagrams.
-   MPLS Cisco IOS - Nexthop mapping fix when only VPN label is present
-   Cisco Blade FEX modules - parsing of FEX related environment
    information fixed
-   Cisco MPLS forwarding with multiple next-hop including route and
    label fixed parsing
-   Juniper Junos - fixed parsing issue for command "show vlans
    detail" - VPLS VLANs aren't supported
-   Juniper Junos - fixed parsing for command "show sflow" when SFlow
    isn't configured
-   Juniper Junos - fixed parsing of different output for command "show
    vrrp detail"
-   Juniper Junos - fixed parsing of different output for command "show
    virtual-chassis device-topology"
-   Juniper Junos - fixed parsing of different output for command "show
    virtual-chassis vc-port all-members"
-   Juniper Junos - fixed parsing of different output for command "show
    spanning-tree interface detail"
-   Juniper Junos - fixed parsing of different output for command "show
    spanning-tree statistics interface"
-   Juniper Junos - fixed parsing of different output for command "show
    route active-path"
-   Fixed RIB edges with duplicate GLBP addresses for devices without
    ARP table (AP) or without
-   Checkpoint Gaia - fixed parsing of different output for command
    "show ospf interfaces detailed"
-   Cisco ASA - fixed parsing of different output for command "show bgp
    summary"
-   Cisco 6500/7600 routing table parsing fix - some entries were split
    into a new line in CLI output.
-   Cisco WLC - fixed parsing of different output for command "show port
    detailed-info"
-   Cisco WLC - fixed parsing of different output for command "show ap
    config general \<apName>"
-   Cisco IOS - fixed parsing of different output for command "show
    dot1x all details"

### 3.0.6 (10th April 2019)

#### Features - Protocol and technology support

-   HP/Aruba switch - STP support added

#### Improvements

-   UI - Added "Reload required" notification - when the system is
    updated the UI has to be reloaded. (A manual reload is still
    required at the moment, use CTRL+SHIFT+R)
-   System and application logs are now available in CLI (/var/log)
-   HP/Aruba switch - improved LLDP protocol parsing & mapping

#### Bug Fixes

-   FIX Critical BUG - when VM doesn't have a DNS server set, the
    discovery process can get stuck and a new discovery process can't be
    started.
-   Hosts table - Host DNS name column was always empty
-   Cisco IOS - fixed parsing of different output for command "show vrrp
    brief"
-   Cisco NX-OS - fixed parsing of different output for command "show
    monitor session all"
-   Cisco NX-OS - fixed parsing of different output for command "show
    flow export"
-   HP/Aruba switch - fixed parsing of different output for command
    "show lldp info remote-device detail"
-   Path lookup - flooding fix for virtual mac
-   fixed color report results refreshing when multiple snapshots are
    loaded
-   fixed various color reports patching scenarios (removing a rule,
    changing a color column)

### 3.0.5 (2nd April 2019)

#### Features - Protocol and technology support

-   Added BGP support for Checkpoint Gaia, Cisco ASA, Extreme XOS,
    Fortinet Fortigate, F5 Big-IP, Huawei VRP, Palo Alto
-   Added ISIS support for Arista EOS, Cisco IOS / IOS-XE / IOS-XR,
    Extreme XOS, HP Comware, Huawei VRP
-   Added STP support for Extreme XOS
-   Added Routing table support for Cisco WLC

#### Visualization

-   Path lookup for Wireless clients has been added for Cisco WLC.
-   Path lookup now supports Riverbed in path transparent mode with
    CDP/LLDP enabled.
-   Protocols menu - added new option "Hide unconnected devices",
    enabled by default.
-   Position of transit cloud is now correctly stored for loaded view.
-   Path lookup speed has been improved for large networks.
-   Path lookup - Protocol menu - all protocols that are in the path are
    visible by default.
-   Site separation - RIB edges for default gateway are now displayed
    automatically.

#### Discovery

-   Protocol relationship on with the same IP in multiple VRFs is now
    supported if VRF on both sides matches the name.

#### Improvements

-   Added version detection for HP1910 and 1950, including switch into
    CLI mode
-   Improved snapshot loading speed (depending on the number of
    available CPUs)
-   Spanning tree edge to router links are no longer created based on
    MAC for multiple destination ports.
-   AP on switch port is now recognized as edge port (based on incoming
    CDP message).
-   Cisco terminal server router now recognized as a router (based on
    serial sync/async interfaces), which was previously recognized as
    host.

#### Bug Fixes

-   Cisco WLC - fixed parsing of various output for command "show system
    interfaces"
-   HP Aruba - fixed parsing of various output for command "show
    inventory"
-   HP Aruba - fixed parsing of various output for command "show ap lldp
    neighbors"
-   HP Aruba switch - fixed parsing of various output for command "show
    tech buffers"
-   HP Aruba switch - fixed parsing of various output for command "show
    ip"
-   HP Aruba switch - fixed parsing of various output for command "show
    system"
-   HP Aruba switch - fixed parsing of various output for command "show
    vlans"
-   HP Aruba switch - fixed parsing of various output for command "show
    interface all"
-   Cisco - fixed parsing of various output for command "show run"
-   Cisco XR - fixed parsing of various output for command "show eigrp
    vrf all interfaces detail"
-   Arista EOS - fixed parsing of various output for command "show bgp
    neigh vrf all"
-   Extreme XOS - fixed parsing of various output for command "show
    ip-fix"
-   Juniper Junos - fixed parsing of various output for command "show
    spanning-tree interface detail"

#### Known issues

-   Graphs - Link groups which have more than 25 links (edges) can no
    longer be un-grouped due to performance impact on the client.

### 3.0.4 (12th March 2019)

#### Features - Visualization

-   Host to the gateway - displays only the path by default
-   Path lookup - displays only the path by default
-   Hub messaging is disabled by default
-   LDP & MPLS protocols are now part of the L3 group
-   Window details - external links are removed from tables

#### Discovery

-   all changes from the latest release v2.4.0 are included now

#### Improvements

-   Site reports
    -   STP domains graph has only STP protocol now
    -   Routing domains graph has only L3 protocols
    -   Overall site graph - access points were removed
-   Tables - sort by color was removed
-   Tables - filtering using simple filters isn't triggered
    automatically when you typing, you have to confirm filtering by
    hitting Enter
-   Tables - filtering is disabled if data loading is still in progress
-   DB indexes optimizations
-   Added support for 802.1x interface monitor mode detection for Cisco
    IOS/IOS-XE (auth. open)
-   Cisco CDP and LLDP neighbors with the same hostname and IP that are
    connected through the same local interface are considered to be the
    same regardless of their interface name
-   Port is now recognized as edge port when network device mac address
    (without any protocol relations) is associated
-   Cisco Nexus & 6500 - Virtual mac addresses spanning tree edges fix
    (CDP between switches is required).
-   Device type - Device is recognized as a switch if has mac table and
    VLANs (previously STP mode was enough)
-   STP domain - Devices without STP edges are not considered as part of
    STP domain (even when they have some STP mode set).

#### Bug Fixes

-   Fixed number of total rows in tables
-   Fixed Duplicate IP Table - Don't report GLBP virtual addresses
-   Discovery topology build may fail when WLC device data was refreshed
-   Wireless clients table didn't display data for the selected snapshot
-   Cloned snapshot didn't have wireless clients
-   Changes - Managed IP table was empty
-   Cisco NX fixed parsing of different output for command "show
    interface fex-fabric"

### 3.0.3 (22nd February 2019)

#### Improvements

-   Snapshot with 0 devices aren't automatically deleted (revert)
-   Fixed issue when server has set a proxy then API server can't be
    reached
-   DB indexes optimizations
-   Discovery - Refresh data for specific devices - access points was
    removed from table
-   Discovery - Refresh data for specific devices - overide device
    output in snapshot
-   Discovery - Fixed - Cannot be started when proxy is configured.
-   Initial network configuration wizard - Fixed - NTP configuration
    hangs.

### 3.0.2 (19th February 2019)

#### Improvements

-   API service can fails, because Redis service wasn't started
-   Snaphosts with 0 devices are automatically deleted
-   Automatically remove latest snapshot, when scheduled discovery start
    fails on not enough disk space
-   Fixed services status in status page
-   Tech Support file - you are able to choose if a snapshot will be
    included
-   Maximum BW limit changed to 10Mbps

### 3.0.1 (12th Fabruary 2019)

#### Improvements

-   Fixed an error in Site Separation by regex
-   Tech Support file now contains CLI logs

### 3.0.0 Release Candidate 1 (6th Fabruary 2019)

-   A complete overview of network history through individual network
    "Snapshots"
-   Visualization and analysis for any point in time
-   Discovery page now enables to add devices to a snapshot, refresh
    devices in a snapshot, or to create a new snapshot.
-   Snapshot management tab enables to download/upload,
    activate/deactivate, clone or delete snapshots.

The Release Candidate is currently in active development.  
The RC1 version is designed to collect feedback about functionality for
practical situations, such as making changes, tracking history, creating
reference snapshots, and more.  
Please post any ideas for improvement to <https://ideas.ipfabric.io> and
in case of any problems contact our support team, either via the
<https://support.ipfabric.io> portal or through <support@ipfabric.io>.
