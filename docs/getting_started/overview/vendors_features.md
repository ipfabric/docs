# Supported vendors and features

[Vendor-Feature matrix](https://docs.ipfabric.io/matrix){ .md-button .md-button--primary }

## CLI commands used during Discovery

Following commands are used during the discovery of a network device.

!!! warning

    Commands marked with asterisk at the beginning of the line are mandatory for basic discovery process.

### Cisco

#### cisco asa

```
*changeto context <contextName>
*changeto system
*enable
*show arp
*show context
*show curpriv
*show interface
*show inventory
*show ipv6 interface
*show memory
*show route
*show version
*terminal pager 0
show running-config
changeto context <name>
changeto context system
show bgp neighbors
show bgp summary
show ipv6 ospf interfacel
show ipv6 ospf neighbor detail
show logging
show nat detail
show ntp associations
show ospf interface
show ospf neighbor detail
show route summary
show run
show sflow-export counters
show startup-config
```

#### cisco sg

```
*enable
*show arp
*show cdp neighbors detail
*show interface counters
*show interface description
*show interface status
*show interface switchport <int>
*show inventory
*show ip interface
*show ip route
*show line telnet
*show lldp neighbors
*show lldp neighbors <int>
*show mac address-table
*show privileges
*show spanning-tree detail
*show system
*show version
*terminal datadump
show running-config
show access-list
show dot1x
show dot1x users
show errdisable interfaces
show interfaces access-lists
show interfaces port-channel
show ports monitor
show power inline
show sflow configuration
show snmp users
show spanning-tree bpdu
show startup-config
```

#### cisco ios

```
*show cdp neighbors detail
*show glbp brief
*show interface
*show interface switchport
*show inventory
*show ip arp
*show ip arp vrf <vrf>
*show ip cef <vrf> detail
*show ip interface
*show ip route [<protocol>]
*show ip route vrf <vrf> [<protocol>]
*show ipv6 interface
*show lldp neighbors detail
*show mac address
*show mac-address
*show memory statistics
*show mpls interfaces
*show privileges
*show running-config
*show spanning-tree
*show spanning-tree detail
*show spanning-tree mst
*show spanning-tree summary
*show standby brief
*show version
*show vrrp brief
*terminal length 0
show authentication sessions
show authentication sessions interface <int>
show authentication sessions interface <int> detail
show bgp all neighbors
show bgp all summary
show crypto session brief
show dmvpn
show dot1x all details
show environment all
show environment stack
show environment status
show etherchannel summary
show flow exporter
show flow interface
show flow monitor
show interface status err-disabled
show interface transceivers detail
show ip access-list
show ip eigrp vrf * interfaces detail
show ip eigrp vrf * neighbor
show ip flow export
show ip flow interface
show ip ospf interface
show ip ospf neighbor detail
show ip protocols
show ip protocols vrf <vrfName>
show ip route summary
show ip route vrf <vrf> summary
show ip vrf interface
show ipv6 ospf interface
show ipv6 ospf neighbor detail
show isis hostname
show isis neighbors detail
show isis protocol
show mab all details
show monitor detail
show mpls forwarding-table
show mpls ldp neighbor all detail
show ntp associations
show object-group
show ospfv3 vrf * interface
show ospfv3 vrf * neighbor detail
show policy-map interface
show power inline
show run
show snmp users
show startup-config
show switch detail
show vrf interfaces
```

#### cisco ios-xe

```
* show bridge-domain
*show cdp neighbors detail
*show glbp brief
*show interface
*show interface switchport
*show interfaces
*show inventory
*show ip arp
*show ip arp vrf <vrf>
*show ip cef <vrf> detail
*show ip interface
*show ip route [<protocol>]
*show ip route vrf <vrf> [<protocol>]
*show ipv6 interface
*show lldp neighbors detail
*show mac address
*show mac-address
*show memory statistics
*show mpls interfaces
*show privileges
*show running-config
*show spanning-tree detail
*show spanning-tree mst
*show spanning-tree summary
*show standby brief
*show version
*show vrrp brief
*terminal length 0
show authentication sessions
show authentication sessions interface <int> detail
show bgp all neighbors
show bgp all summary
show crypto session brief
show dmvpn
show dot1x all details
show environment all
show environment stack
show environment status
show etherchannel summary
show flow exporter
show flow interface
show flow monitor
show interface status err-disabled
show interface transceivers detail
show ip access-list
show ip eigrp vrf * interfaces detail
show ip eigrp vrf * neighbor
show ip flow export
show ip flow interface
show ip ospf interface
show ip ospf neighbor detail
show ip protocols
show ip protocols vrf <vrfName>
show ip route summary
show ip route vrf <vrf> summary
show ip vrf interface
show ipv6 ospf interface
show ipv6 ospf neighbor detail
show isis hostname
show isis neighbors detail
show isis protocol
show mab all details
show monitor detail
show mpls forwarding-table
show mpls ldp neighbor all detail
show ntp associations
show nve interface <intName>
show nve peers
show nve vni
show object-group
show ospfv3 vrf * interface
show ospfv3 vrf * neighbor detail
show policy-map interface
show power inline
show run
show snmp users
show startup-config
show switch detail
show vrf interfaces
```

#### cisco ios-xr

```
*show arp
*show arp vrf <vrf>
*show cdp neighbors detail
*show hsrp
*show interface
*show inventory
*show inventory all
*show ipv4 vrf all interface
*show ipv6 vrf all interface
*show lldp neighbors detail
*show memory summary
*show mpls interfaces
*show route
*show route vrf <vrf>
*show running-config
*show version
*show vrrp
*terminal length 0
show bgp neighbors
show bgp summary
show bgp vrf all neighbors
show bgp vrf all summary
show eigrp interfaces detail
show eigrp neighbor
show ip interface
show isis hostname
show isis neighbors detail
show isis protocol
show mpls forwarding
show mpls ldp vrf <vrf> discovery detail
show mpls ldp vrf <vrf> neighbor detail
show ntp associations
show ospf vrf all-inclusive interface
show ospf vrf all-inclusive neighbor detail
show ospfv3 vrf all-inclusive interface
show ospfv3 vrf all-inclusive neighbor detail
show rip
show rip interfaces
show rip interfaces vrf all
show rip vrf all
show route summary detail, show route vrf <vrf> summary detail
show snmp host
show vrf all detail
```

#### cisco nx-os

```
*show cdp neighbors detail
*show glbp brief
*show hostname
*show hsrp brief
*show interface
*show interface switchport
*show interfaces
*show inventory
*show ip arp
*show ip arp vrf <vrf>
*show ip interface vrf all
*show ip route detail
*show ip route detail vrf <vrf>
*show ip route vrf <vrf> detail
*show ipv6 interface vrf all
*show lldp neighbors detail
*show mac address
*show mpls interfaces
*show mpls switching
*show nve vni
*show policy-map system type network-qos
*show running-config
*show spanning-tree detail
*show spanning-tree mst
*show spanning-tree summary
*show system internal l2fwder mac
*show system resources
*show user-account
*show vdc
*show vdc current-vdc
*show version
*show vpc
*show vrrp
*terminal length 0
*terminal width 256
show access-list summary
show environment
show environment fex all
show feature
show fex detail
show flow export
show flow interface
show flow monitor
show interface fex-fabric
show interface status err-disabled
show ip access-list
show ip bgp vrf all all neighbors
show ip bgp vrf all all summary
show ip eigrp neighbor vrf all
show ip interface
show ip ospf interface vrf all
show ip ospf neighbor detail vrf all
show ipv6 ospfv3 interface vrf all
show ipv6 ospfv3 neighbors detail vrf all
show logging server
show monitor session all
show mpls ldp neighbor detail
show ntp peer-status
show nve interface
show nve peers
show object-group
show ospfv3 vrf all
show ospfv3 vrf all interface
show ospfv3 vrf all neighbors detail
show port-channel summary
show rip interfaces vrf all
show rip neighbors vrf all
show rip vrf all
show routing summary vrf all
show snmp users
show startup-config
show vrf interface
show ip eigrp interfaces vrf all
```

#### cisco wlc-air

```
*config paging disabled
*show cdp neighbors detail
*show interface detailed <name>
*show interface summary
*show inventory
*show lag summary
*show memory statistics
*show network summary
*show port detailed-info
*show port summary
*show redundancy summary
*show run-config commands
*show stats port summary <portId>
*show sysinfo
*show system interfaces
*show version
show advanced 802.11a summary
show advanced 802.11b summary
show ap cdp neighbors all
show ap config 802.11a summary
show ap config 802.11b summary
show ap config general <apName>
show ap inventory <apName>
show ap stats ethernet <apName>
show ap stats ethernet summary
show ap summary
show ap wlan 802.11a <apName>
show ap wlan 802.11b <apName>
show client detail
show client detail <clientMac>
show client summary
show flow monitor summary
show interface detail <int>
show snmpcommunity
show snmptrap
show snmpv3user
show snmpversion
show stats port summary
show time
show wlan <id>
show wlan <wlanId>
show wlan summary
```

#### cisco ftd

```
*show arp
*show bridge-group
*show interface
*show inventory
*show mac-address-table
*show memory
*show network
*show route
*show running-config
*show serial-number
*show version
*show version system
show route summary
show startup-config
```

#### cisco aci

```
*show cdp neighbors detail
*show endpoint detail
*show hostname
*show hsrp brief
*show interface
*show interface switchport
*show inventory
*show ip arp vrf all
*show ip interface vrf all
*show ip route vrf <vrf>
*show lldp neighbors detail
*show mac address-table
*show system resources
*show version
*show vpc
show ip route summary vrf all
show port-channel summary
show system internal epm vlan all
show system internal epm vrf all
```

### Dell

#### dell ftos

```
*enable
*show arp
*show interfaces
*show interfaces switchport
*show ip interface
*show ip route
*show lldp neighbors
*show mac address-table
*show mac-address-table
*show memory
*show running-config
*show running-config | grep ^hostname
*show spanning-tree 0
*show spanning-tree mst configuration
*show spanning-tree msti <id>
*show spanning-tree pvst
*show spanning-tree rstp
*show system stack-unit 0
*show version
*show vlan
*terminal length 0
show interfaces port-channel brief
show ntp associations
```

#### dell powerconnect

```
*enable
*show arp
*show interfaces
*show interfaces status
*show ip interface
*show ip interface <type> <id>
*show ip route
*show ip telnet
*show lldp interface all
*show lldp remote-device detail <intName>
*show mac address-table
*show memory cpu
*show running-config
*show spanning-tree
*show spanning-tree detail
*show spanning-tree mst-configuration
*show spanning-tree summary
*show system
*show version
*show vlan
*terminal length 0
show interfaces port-channel
show ntp associations
```

### Hewlett Packard

#### hp comware

```
*_cmdline-mode on
*display arp
*display arp vpn-instance <instanceName>
*display clock
*display current-configuration
*display device manuinfo
*display interface
*display ip interface
*display ip routing-table verbose
*display ip routing-table vpn-instance <name> verbose
*display ip vpn-instance
*display ip vpn-instance instance-name <name>
*display license device-id
*display lldp neighbor-information
*display lldp neighbor-information verbose
*display mac-address
*display memory
*display stp
*display stp region-configuration
*display tcp
*display version
*display vlan all
*display voice vlan state
*display voice-vlan state
*display vrrp verbose
*display wlan ap all verbose
*screen-length disable
*summary
display acl all
display bgp peer
display bgp peer ipv4
display bgp peer ipv4 verbose
display bgp peer ipv4 vpn-instance <instanceName>
display bgp peer ipv4 vpn-instance <instanceName> verbose
display bgp peer verbose
display bgp peer vpn-instance <instanceName>
display bgp peer vpn-instance <instanceName> verbose
display current-configuration configuration isis
display dot1x
display fan
display info-center
display ip netstream export
display ip routing-table statistics
display ip vpn instance <vpnInstance>
display irf
display irf topology
display isis <processId>
display isis brief <processId>
display isis name-table <processId>
display isis peer verose <processId>
display link-aggregation verbose
display mac-authentication
display mirroring-group all
display ntp-service sessions
display object-group
display ospf interface verbose
display ospf peer verbose
display packet-filter all
display packet-filter interface
display poe interfaces
display port-security
display power
display rip
display rip <processId> interfaces
display rip <processId> neighbors
display saved-configuration
display sflow
display transceiver interface
display wlan client stats
display wlan client verbose
```

#### hp aruba

```
*no paging
*show arp
*show datapath bridge
*show hostname
*show interface <int>
*show interface loopback
*show inventory
*show ip interface brief
*show lldp neighbor
*show lldp neighbor interface <int> detail
*show port stats
*show running-config
*show slots
*show telnet
*show version
*show vlan status
*show vrrp
show ap active
show ap association
show ap association client-mac <clientMac>
show ap bss-table
show ap debug lacp ap-name <apName>
show ap debug system-status ap-name <apName>
show ap details ap-name <apName>
show ap image version
show ap lldp neighbors
show ap port status ap-name <apName>
show configuration
show ip-flow-export-profile
show logging server
show ntp server
show running-configuration
show startup-config
show wlan <id>
show wlan summary
```

#### hp arubasw

```
*no page
*show arp
*show cdp neighbors
*show interfaces all
*show interfaces brief
*show ip
*show ip route
*show ip ssh
*show lldp info remote-device detail
*show mac-address
*show modules
*show running-config
*show spanning-tree
*show spanning-tree config
*show spanning-tree debug-counters instance <instance> ports all
*show spanning-tree detail
*show spanning-tree instance <instance>
*show spanning-tree mst-config
*show spanning-tree vlan <vlanId>
*show stacking
*show system
*show tech buffer
*show version
*show vlans
*show vlans ports all detail
*show vrrp vlan <vlan> vrid <vrid> config
show ntp associations
show running-configuration
show syslog config
```

### RiverBed steelhead

```
*enable
*show arp
*show configuration running
*show hosts
*show info
*show interfaces
*show ip in-path route <int>
*show ip route
*show telnet-service
*show version
*terminal length 0
show configuration
show ip flow-export
show ip flow-setting
show logging
show ntp all
show snmp
show snmp usernames
```

### CheckPoint gaia

```
*clish
*fw ctl pstat
*set clienv rows 0
*show arp dynamic all
*show configuration
*show hostname
*show interface <int>
*show interface <name>
*show interfaces all
*show management interface
*show net-access telnet
*show route all
*show uptime
*show version all
*ver
show bgp peers detailed
show config-saved
show configuration snmp
show netflow all
show ntp servers
show ospf interfaces detailed
show ospf neighbors detailed
show route summary
show syslog all
```

### Juniper junos

```
*set cli screen-length 0
*set cli screen-width 0
*show arp no-resolve
*show chassis hardware
*show chassis routing-engine
*show configuration
*show ethernet-switching table
*show interfaces statistics detail
*show interfaces terse
*show lldp neighbors
*show lldp neighbors interface <int>
*show route active-path
*show route instance detail
*show spanning-tree bridge detail
*show spanning-tree interface detail
*show spanning-tree mstp configuration
*show spanning-tree statistics interface
*show system connections
*show system uptime
*show version
*show vlans detail
*show vrrp detail
show analyzer
show bgp neighbor
show bgp neighbor instance <instanceName>
show bgp summary <instanceName>
show chassis cluster interfaces
show chassis cluster status
show chassis environment
show configuration firewall | display omit
show configuration forwarding-options sampling
show configuration groups junos-defaults applications | display set
show configuration interfaces | match sampling | display set
show configuration policy-options | display set
show configuration security address-book | display set
show configuration security applications | display set
show configuration security policies | display set
show configuration | display set
show dot1x interface detail
show ethernet-switching interface
show ethernet-switching interfaces
show forwarding-options analyzer
show interfaces diagnostics optics
show isis adjacency extensive instance <instanceName>
show isis interface extensive instance <instanceName>
show isis overview instance <instanceName>
show lacp interfaces
show ldp interface extensive instance <vrf>
show ldp neighbor extensive instance <vrf>
show ntp associations no-resolve
show ospf interface detail instance <instanceName>
show ospf neighbor detail instance all
show poe interface
show poe interface <intName>
show rip interfaces instance all
show rip statistics instance all
show route summary
show security zones
show sflow
show sflow collector
show sflow interface
show virtual-chassis
show virtual-chassis device-topology
show virtual-chassis vc-port all-member
```

### PaloAlto

```
*set cli pager off
*show arp all
*show config running
*show interface <int>
*show interface <intName>
*show interface all
*show lldp neighbors all
*show mac all
*show route routing
*show system info
*show system resources
*show system services
*show vlan all
show interface <name>
show ntp
show routing protocol bgp peer
show routing protocol bgp summary
show routing protocol ospf interface
show routing protocol ospf neighbor
show system environmentals
```

### Extreme xos

```
*debug vlan show vlans
*disable clipaging
*show configuration
*show edp ports all detail
*show fdb
*show iparp
*show iproute vr <vr>
*show lldp neighbors
*show lldp neighbors detail
*show management
*show memory
*show ports configuration no-refresh port-number
*show ports description
*show ports rxerrors no-refresh port-number
*show ports statistics no-refresh port-number
*show ports txerrors no-refresh port-number
*show ports utilization bytes port-number
*show ports utilization packets port-number
*show stpd
*show stpd <stpDomain> ports counters
*show stpd <stpDomain> ports detail
*show stpd detail
*show switch
*show version
*show virtual router
*show vlan detail
show bgp
show bgp neighbor detail
show ip-fix
show iproute summary
show isis area
show isis neighbors detail
show isis vlan
show log configuration
show ntp associations
show ospf interfaces detail enabled
show ospf neighbor detail
show sflow config
```

### Huawei vrp

```
*display telnet server status
*display arp
*display current-configuration
*display device
*display device manufacture-info
*display esn
*display interface
*display ip interface
*display ip routing-table protocol <name> verbose
*display ip routing-table statistics
*display ip routing-table verbose
*display ip routing-table vpn-instance <name> protocol <name>
  verbose
*display ip routing-table vpn-instance <name> statistics
*display ip routing-table vpn-instance <name> verbose
*display ip vpn-instance
*display ip vpn-instance <name> interface
*display lldp neighbor
*display mac-address
*display memory
*display port vlan
*display port vlan active
*display stp
*display stp region-configuration
*display telnet server
*display version
*display vlan
*display vrrp
*screen-length 0 temporary
display bgp <addressFamiily> <vpnInstance> peer
display bgp <addressFamiily> <vpnInstance> peer verbose
display eth-trunk
display info-center
display ip netstream all
display isis interface verbose [vpn-instance <vpnInstance>]
display isis peer verbose [vpn-instance <vpnInstance>]
display ntp sessions
display observe-port
display ospf interface all
display ospf peer
display port-mirroring
display sflow
display snmp-agent community read
display snmp-agent community write
```

### f5 big-ip

```
*list net self
*list net vlan
*show cm device
*show net arp all
*show net interface all-properties
*show net lldp-neighbors all-properties
*show net route all
*show net self
*show net trunk all-properties
*show running-config
*show sys hardware
*show sys mac-address
*show sys tmm-info raw
*show sys version
*tmsh
*tmsh modify cli preference pager disabled
*tmsh show sys version
imish -r <rd_ID>
list /net route-domain
list /sys sflow receiver all-properties
list net trunk
list sys snmp
list sys syslog
run util bash -c "ntpq -np"
show bgp <addressFamily> summary
show bgp neighbors
show sys sflow data-source
```

### Arista eos

```
*show arp
*show hostname
*show interfaces
*show interfaces switchport
*show interfaces vxlan 1
*show inventory
*show ip interfaces
*show ip route vrf <vrfName>
*show ip route vrf <vrfName> summary
*show lldp neighbors detail
*show mac address-table
*show privilege
*show running-config
*show version
*show vrf
*show vrrp all
*show vxlan address-table
*terminal width 256
show ip bgp neighbors vrf all
show ip interface
show ip interface brief
show ip ospf interface
show ip ospf neighbor detail
show ip route vrf <vrf> summary
show isis interface detail vrf all
show isis summary vrf all
show logging
show ntp associations
show port-channel dense
show port-channel summary
show sflow
show sflow interfaces
show vxlan vtep
```

### FortiNET fortigate

```
*config global
*diagnose hardware deviceinfo nic
*diagnose netlink brctl list
*diagnose netlink brctl name host <bridge>
*diagnose system vd list
*diagnose user device list
*get hardware memory
*get router info routing-table all
*get router info vrrp
*get system arp
*get system interface physical
*get system interface
*get system performance status
*get system status
*get system vdom-link
*show configuration
*show router static
*show system interface
*show system settings
diagnose firewall fqdn list
diagnose netlink aggregate list
diagnose netlink aggregate name <aggInterface>
diagnose sys ntp status
get log disk setting
get log syslogd filter
get log syslogd setting
get log syslogd2 filter
get log syslogd2 setting
get log syslogd3 filter
get log syslogd3 setting
get router info bgp neighbors
get router info bgp summary
get router info ospf interface
get router info ospf neighbor detail
get system interface
get system netflow
get system sflow
get system snmp sysinfo
get system snmp user
show firewall address
show firewall addrgrp
show firewall policy
show firewall service custom
show firewall service group
show full system snmp community
show system ntp
show system zone
```
