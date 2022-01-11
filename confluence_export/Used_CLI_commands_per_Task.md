# Used CLI commands per Task

The following dataset provides a detailed overview of the command-line
interface (CLI) or API commands that the IP Fabric platform uses to
gather specific information per task. The dataset is built with the
resulting structure.

**LEGEND:**

\[VENDOR_FAMILY\]

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
[TASK_NAME]
  [command1]
  [command2]

[TASK_NAME]
  [command1]
  [command2]
```

</div>

</div>

**TABLE OF CONTENT - VENDOR_FAMILY**

<div class="toc-macro rbtoc1641913371503">

-   [ARISTA_EOS](#UsedCLIcommandsperTask-ARISTA_EOS)
-   [CISCO_IOS](#UsedCLIcommandsperTask-CISCO_IOS)
-   [CISCO_NX-OS](#UsedCLIcommandsperTask-CISCO_NX-OS)
-   [CISCO_ASA](#UsedCLIcommandsperTask-CISCO_ASA)
-   [CISCO_SG](#UsedCLIcommandsperTask-CISCO_SG)
-   [CISCO_IOS-XE](#UsedCLIcommandsperTask-CISCO_IOS-XE)
-   [CISCO_IOS-XR](#UsedCLIcommandsperTask-CISCO_IOS-XR)
-   [CISCO_FTD](#UsedCLIcommandsperTask-CISCO_FTD)
-   [CISCO_WLC-AIR](#UsedCLIcommandsperTask-CISCO_WLC-AIR)
-   [JUNIPER_JUNOS](#UsedCLIcommandsperTask-JUNIPER_JUNOS)
-   [CISCO_ACI](#UsedCLIcommandsperTask-CISCO_ACI)
-   [CISCO_VIPTELA](#UsedCLIcommandsperTask-CISCO_VIPTELA)
-   [DELL_FTOS](#UsedCLIcommandsperTask-DELL_FTOS)
-   [DELL_POWERCONNECT](#UsedCLIcommandsperTask-DELL_POWERCONNECT)
-   [HP_ARUBA](#UsedCLIcommandsperTask-HP_ARUBA)
-   [HP_ARUBASW](#UsedCLIcommandsperTask-HP_ARUBASW)
-   [HP_ARUBACX](#UsedCLIcommandsperTask-HP_ARUBACX)
-   [FORTINET_FORTIGATE](#UsedCLIcommandsperTask-FORTINET_FORTIGATE)
-   [RIVERBED_STEELHEAD](#UsedCLIcommandsperTask-RIVERBED_STEELHEAD)
-   [CHECKPOINT_GAIA](#UsedCLIcommandsperTask-CHECKPOINT_GAIA)
-   [CHECKPOINT_GAIA-EMBEDDED](#UsedCLIcommandsperTask-CHECKPOINT_GAIA-EMBEDDED)
-   [EXTREME_BOSS](#UsedCLIcommandsperTask-EXTREME_BOSS)
-   [EXTREME_ENTERASYS](#UsedCLIcommandsperTask-EXTREME_ENTERASYS)
-   [EXTREME_VOSS](#UsedCLIcommandsperTask-EXTREME_VOSS)
-   [EXTREME_XOS](#UsedCLIcommandsperTask-EXTREME_XOS)
-   [HUAWEI_VRP](#UsedCLIcommandsperTask-HUAWEI_VRP)
-   [F5_BIG-IP](#UsedCLIcommandsperTask-F5_BIG-IP)
-   [MIKROTIK_ROUTEROS](#UsedCLIcommandsperTask-MIKROTIK_ROUTEROS)
-   [VERSA_VOS](#UsedCLIcommandsperTask-VERSA_VOS)
-   [AWS_EC2](#UsedCLIcommandsperTask-AWS_EC2)
-   [CISCO_MERAKI](#UsedCLIcommandsperTask-CISCO_MERAKI)

</div>

**DATASET:**

## ARISTA_EOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show running-config
  show ip access-lists
  show ip access-lists summary

ARP
  show ip arp
  show ip arp vrf <vrfName>

BGP
  show ip bgp neighbors
  show ip bgp neighbors vrf all

FHRP
  show vrrp all
  show ip interface
  show ip virtual-router [vrf all]

IP FLOW
  show sflow
  show sflow interfaces

IS-IS
  show isis interface detail
  show isis interface detail vrf all
  show isis summary
  show isis summary vrf all
  show ip interface brief

L2 INTERFACES
  show interfaces
  show interfaces switchport

L3 INTERFACES
  show ip interfaces
  show vrrp all
  show ip virtual-router [vrf all]
  show interfaces
  show vrf

MAC
  show mac address-table
  show vxlan address-table
  show interfaces vxlan 1
  show interfaces

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail

NTP
  show ntp associations

OSPF
  show ip ospf interface
  show ip ospf neighbor detail

POE
  show poe
  show lldp neighbors detail

PORT-CHANNELS
  show port-channel summary
  show port-channel dense
  show mlag detail
  show mlag interfaces detail
  show ip interfaces

PTP
  show ptp local-clock
  show ptp masters
  show ptp source ip
  show ptp interface

ROUTE SUMMARY
  show vrf
  show ip route summary
  show ip route vrf <vrfName> summary

ROUTING TABLE
  show ip route
  show ip route vrf <vrfName>
  show ip route vrf <vrfName> summary
  show vrf

SN
  show version

SNMP
  show running-config

SYSLOG
  show running-config

TRANSCEIVERS
  show inventory
  show interfaces transceiver properties
  show interfaces transceiver detail

VLAN
  show vlan

VRF
  show vrf

VXLAN
  show vxlan vtep
  show interfaces vxlan 1
  show interfaces
```

</div>

</div>

## CISCO_IOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show ip access-list
  show ip interface
  show object-group

ARP
  show ip arp
  show ip arp vrf <vrf>

BGP
  show bgp all neighbors
  show bgp all summary
  show bgp neighbors
  show ip bgp summary

DMVPN
  show dmvpn

EIGRP
  show ip eigrp vrf * interfaces detail
  show ip eigrp vrf * neighbor

ERROR DISABLED INTERFACES
  show interface status err-disabled

FHRP
  show standby
  show glbp brief
  show vrrp

IP FLOW
  show ip flow export
  show ip flow interface
  show flow exporter
  show flow interface
  show flow monitor

IPSEC
  show crypto isakmp sa detail
  show crypto ikev2 sa detailed
  show crypto ipsec sa
  show interfaces
  show run | inc qos queue-stats-frame-count

IS-IS
  show isis neighbors detail
  show running-config
  show isis hostname
  show ip interface
  show vrf interfaces

L2 INTERFACES
  show interface
  show interface switchport
  show run | inc qos queue-stats-frame-count

L3 INTERFACES
  show ip interface
  show ipv6 interface
  show standby brief
  show glbp brief
  show vrrp brief
  show interface

MAC
  show mac address
  show mac-address

NAT
  show run

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show cdp neighbors detail

NTP
  show ntp associations

OSPF
  show ip ospf neighbor detail
  show ip ospf interface
  show ip vrf interface

OSPFV3
  show ospfv3 vrf * interface
  show ospfv3 vrf * neighbor detail
  show ipv6 ospf interface
  show ipv6 ospf neighbor detail
  show ip vrf interface

POE
  show power inline

PORT-CHANNELS
  show etherchannel summary
  show run | inc qos queue-stats-frame-count

PORT MIRRORING
  show monitor detail

PPPOE
  show pppoe session all
  show pppoe summary
  show subscriber session all

ROUTER QOS
  show policy-map interface

RIP
  show ip protocols
  show ip protocols vrf <vrfName>
  show ip interface

ROUTE SUMMARY
  show ip route summary
  show ip route vrf <vrf> summary

ROUTING TABLE
  show ip route [<protocol>]
  show ip route vrf <vrf> [<protocol>]
  show ip cef <vrf> detail
  show mpls interfaces
  show ip cef detail

SECURED ACCESS PORTS
  show interface
  show dot1x all details
  show mab all details
  show run
  show version
  show run | inc qos queue-stats-frame-count
  show authentication sessions
  show authentication sessions interface <int>
  show authentication sessions interface <int> detail
  show authentication sessions
  show authentication sessions interface <int> detail

SN
  show version

SNMP
  show running-config
  show snmp users
  show running-config
  show snmp users

STACKING
  show switch detail
  show version

STORM CONTROL
  show show storm-control broadcast
  show storm-control unicast
  show storm-control multicast
  show interfaces counters storm-control
  show running-config

STP
  show spanning-tree summary
  show spanning-tree detail
  show interface switchport
  show vlan brief
  show vlan-switch brief
  show vlan-switch brief
  show spanning-tree
  show spanning-tree mst
  show spanning-tree mst
  show spanning-tree mst

STP PORT SECURITY
  show spanning-tree detail

SYSLOG
  show running-config

TRANSCEIVERS
  show inventory
  show interfaces transceiver detail
  show interfaces transceiver
  show run | inc qos queue-stats-frame-count

VLAN
  show vlan brief
  show vlan-switch brief

VRF
  show vrf detail

VSS
  show switch virtual redundancy
  show switch virtual link port-channel
  show switch virtual
  show inventory
```

</div>

</div>

## CISCO_NX-OS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show ip access-list
  show access-list summary
  show object-group

ARP
  show ip arp
  show ip arp vrf <vrf>

BGP
  show ip bgp vrf all all neighbors
  show ip bgp vrf all all summary
  show feature

EIGRP
  show ip eigrp interfaces vrf all
  show ip eigrp neighbor vrf all

ERROR DISABLED INTERFACES
  show interface status err-disabled

CHASSIS EXTENDERS
  show fex detail
  show interface fex-fabric

FHRP
  show hsrp
  show glbp brief
  show vrrp detail
  show vrrpv3

IP FLOW
  show flow export
  show flow interface
  show flow monitor

L2 INTERFACES
  show interface
  show interface switchport
  show policy-map system type network-qos

L3 INTERFACES
  show ip interface vrf all
  show ipv6 interface vrf all
  show hsrp brief
  show glbp brief
  show vrrp
  show interface

MAC
  show mac address
  show system internal l2fwder mac
  show interfaces
  show nve vni
  show vpc

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show cdp neighbors detail

NTP
  show ntp peer-status

OSPF
  show feature
  show ip ospf neighbor detail vrf all
  show ip ospf interface vrf all

OSPFV3
  show ospfv3 vrf all interface
  show ospfv3 vrf all neighbors detail
  show ipv6 ospfv3 interface vrf all
  show ipv6 ospfv3 neighbors detail vrf all
  show feature
  show ipv6 interface vrf all
  show ospfv3 vrf all

PORT-CHANNELS
  show port-channel summary
  show vpc
  show feature

PORT MIRRORING
  show monitor session all

PTP
  show ptp clock
  show ptp brief
  show ptp parent
  show ptp clock dataset default
  show ptp clock dataset parent domain <domainId>
  show ptp clock running domain <domainId>

RIP
  show rip interfaces vrf all
  show rip neighbors vrf all
  show rip vrf all

ROUTE SUMMARY
  show routing summary vrf all

ROUTING TABLE
  show ip route detail
  show ip route detail vrf <vrf>
  show ip route vrf <vrf> detail
  show mpls switching
  show mpls interfaces
  show ip interface vrf all

SN
  show version
  show vdc current-vdc
  show inventory

SNMP
  show running-config
  show snmp users
  show running-config
  show snmp users

STORM CONTROL
  show interface counters storm-control
  show running-config

STP
  show spanning-tree summary
  show spanning-tree detail
  show interface switchport
  show vlan brief
  show vlan-switch brief
  show vlan-switch brief
  show spanning-tree
  show spanning-tree mst
  show spanning-tree mst
  show spanning-tree mst

STP PORT SECURITY
  show spanning-tree detail

SYSLOG
  show logging server

TRANSCEIVERS
  show interface transceiver details
  show interface transceiver fex-fabric details
  show interface fex-fabric
  show inventory [all]

VLAN
  show vlan brief

VRF
  show vrf all detail
  show bgp process vrf all

VXLAN
  show nve peers
  show nve interface
  show nve vni
  show interfaces
```

</div>

</div>

## CISCO_ASA

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show run
  show interface
  show interface detail
  show running-config all object
  show dns

ARP
  show arp
  show interface
  show interface detail

BGP
  show bgp neighbors
  show bgp summary

VIRTUAL CONTEXTS
  show context
  changeto system
  show context
  changeto context <contextName>

IP FLOW
  show sflow-export counters

IPSEC
  show crypto isakmp sa detail
  show crypto ipsec sa
  show interfaces detail

L2 INTERFACES
  show interface
  show interface detail

L3 INTERFACES
  show interface
  show interface detail
  show arp
  show ipv6 interface

NAT
  show nat detail

NTP
  show ntp associations
  changeto context system
  changeto context <name>

OSPF
  show ospf interface
  show ospf neighbor detail

OSPFV3
  show ipv6 ospf interfacel
  show ipv6 ospf neighbor detail

ROUTE SUMMARY
  show route summary

ROUTING TABLE
  show route
  show interface
  show interface detail
  show names

SN
  show inventory
  show context
  show version

SNMP
  show running-config
  show interface
  show interface detail

SYSLOG
  show logging

TRANSCEIVERS
  show inventory
  show interface detail
  show interface
```

</div>

</div>

## CISCO_SG

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show interfaces access-lists
  show access-list

ARP
  show arp

ERROR DISABLED INTERFACES
  show errdisable interfaces

IP FLOW
  show sflow configuration

L2 INTERFACES
  show interface status
  show interface counters
  show interface description
  show interface switchport <int>

L3 INTERFACES
  show ip interface

MAC
  show mac address-table

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors
  show lldp neighbors <int>
  show cdp neighbors detail

POE
  show power inline

PORT-CHANNELS
  show interfaces port-channel

PORT MIRRORING
  show ports monitor

ROUTING TABLE
  show ip route

SECURED ACCESS PORTS
  show interface status
  show dot1x
  show dot1x users

SN
  show inventory

SNMP
  show running-config
  show snmp users
  show running-config
  show snmp users

STP
  show spanning-tree detail
  show interface status
  show interface switchport <int>
  show vlan
  show interfaces port-channel

STP PORT SECURITY
  show spanning-tree detail
  show spanning-tree bpdu

SYSLOG
  show running-config

VLAN
  show vlan
```

</div>

</div>

## CISCO_IOS-XE

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show ip access-list
  show ip interface
  show object-group

ARP
  show ip arp
  show ip arp vrf <vrf>

BGP
  show bgp all neighbors
  show bgp all summary
  show bgp neighbors
  show ip bgp summary

DMVPN
  show dmvpn

EIGRP
  show ip eigrp vrf * interfaces detail
  show ip eigrp vrf * neighbor

ERROR DISABLED INTERFACES
  show interface status err-disabled

FHRP
  show standby
  show glbp brief
  show vrrp

IP FLOW
  show ip flow export
  show ip flow interface
  show flow exporter
  show flow interface
  show flow monitor

IPSEC
  show crypto isakmp sa detail
  show crypto ikev2 sa detailed
  show crypto ipsec sa
  show interfaces
  show run | inc qos queue-stats-frame-count

IS-IS
  show isis neighbors detail
  show running-config
  show isis hostname
  show ip interface
  show vrf interfaces

L2 INTERFACES
  show interface
  show interface switchport
  show run | inc qos queue-stats-frame-count

L3 INTERFACES
  show ip interface
  show ipv6 interface
  show standby brief
  show glbp brief
  show vrrp brief
  show interface

MAC
  show mac address
  show mac-address
  show interfaces
   show bridge-domain
  show run | inc qos queue-stats-frame-count

NAT
  show run

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show cdp neighbors detail

NTP
  show ntp associations

OSPF
  show ip ospf neighbor detail
  show ip ospf interface
  show ip vrf interface

OSPFV3
  show ospfv3 vrf * interface
  show ospfv3 vrf * neighbor detail
  show ipv6 ospf interface
  show ipv6 ospf neighbor detail
  show ip vrf interface

POE
  show power inline

PORT-CHANNELS
  show etherchannel summary
  show run | inc qos queue-stats-frame-count

PORT MIRRORING
  show monitor detail

PPPOE
  show pppoe session all
  show pppoe summary
  show subscriber session all

PTP
  show ptp clock
  show ptp brief
  show ptp parent
  show ptp clock dataset default
  show ptp clock dataset parent domain <domainId>
  show ptp clock running domain <domainId>

ROUTER QOS
  show policy-map interface

RIP
  show ip protocols
  show ip protocols vrf <vrfName>
  show ip interface

ROUTE SUMMARY
  show ip route summary
  show ip route vrf <vrf> summary

ROUTING TABLE
  show ip route [<protocol>]
  show ip route vrf <vrf> [<protocol>]
  show ip cef <vrf> detail
  show mpls interfaces
  show ip cef detail

SECURED ACCESS PORTS
  show interface
  show dot1x all details
  show mab all details
  show run
  show version
  show run | inc qos queue-stats-frame-count
  show authentication sessions
  show authentication sessions interface <int>
  show authentication sessions interface <int> detail
  show authentication sessions
  show authentication sessions interface <int> detail

SN
  show version

SNMP
  show running-config
  show snmp users
  show running-config
  show snmp users

STACKING
  show switch detail
  show version

STP
  show spanning-tree summary
  show spanning-tree detail
  show interface switchport
  show vlan brief
  show vlan-switch brief
  show vlan-switch brief
  show spanning-tree
  show spanning-tree mst
  show spanning-tree mst
  show spanning-tree mst

STP PORT SECURITY
  show spanning-tree detail

SYSLOG
  show running-config

TRANSCEIVERS
  show inventory
  show interfaces transceiver detail
  show interfaces transceiver
  show run | inc qos queue-stats-frame-count

VLAN
  show vlan brief
  show vlan-switch brief

VRF
  show vrf detail

VSS
  show switch virtual redundancy
  show switch virtual link port-channel
  show switch virtual
  show inventory

VXLAN
  show nve peers
  show nve interface <intName>
  show nve vni
  show interfaces
  show run | inc qos queue-stats-frame-count
```

</div>

</div>

## CISCO_IOS-XR

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config

ACL
  show running-config
  show ipv4 vrf all interface

ARP
  show arp
  show arp vrf <vrfName>

BGP
  show bgp neighbors
  show bgp summary
  show bgp vrf all neighbors
  show bgp vrf all summary

EIGRP
  show ip eigrp vrf all neighbors detail
  show eigrp vrf all interfaces detail
  show eigrp neighbors
  show eigrp interfaces detail
  show vrf all detail
  show ipv4 vrf all interface

FHRP
  show hsrp detail
  show vrrp detail

IS-IS
  show isis neighbors detail
  show isis interface
  show isis hostname
  show vrf all detail
  show ipv4 vrf all interface

L2 INTERFACES
  show interface

L3 INTERFACES
  show ipv4 vrf all interface
  show ipv6 vrf all interface
  show arp
  show hsrp
  show vrrp
  show interface

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show cdp neighbors detail

NTP
  show ntp associations

OSPF
  show ospf vrf all-inclusive neighbor detail
  show ospf vrf all-inclusive interface
  show ospf interface
  show ospf vrf all interface
  show ospf neighbor detail
  show ospf vrf all neighbor detail

OSPFV3
  show ospfv3 vrf all-inclusive interface
  show ospfv3 vrf all-inclusive neighbor detail

PORT-CHANNELS
  show bundle

RIP
  show rip interfaces
  show rip interfaces vrf all
  show rip
  show rip vrf all

ROUTE SUMMARY
  show route summary detail, show route vrf <vrf> summary detail

ROUTING TABLE
  show route
  show route vrf <vrf>
  show mpls interfaces
  show cef vrf <vrf> detail
  show cef detail

SN
  show inventory all

SNMP
  show running-config
  show snmp host

SYSLOG
  show running-config

TRANSCEIVERS
  show inventory all
  show interfaces

VRF
  show vrf all detail
  show bgp process vrf all
```

</div>

</div>

## CISCO_FTD

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show running-config
  show user

ACL
  show run
  show interface
  show interface detail
  show running-config all object
  show dns

ARP
  show arp
  show interface
  show interface detail

L2 INTERFACES
  show interface
  show interface detail
  show network

L3 INTERFACES
  show interface
  show interface detail
  show arp
  show network
  show bridge-group

MAC
  show mac-address-table
  show interface
  show interface detail

NAT
  show nat detail

NTP
  show ntp

ROUTE SUMMARY
  show route summary

ROUTING TABLE
  show route
  show interface
  show interface detail
  show network

SN
  show serial-number

SNMP
  show running-config
  show interface
  show interface detail

SYSLOG
  show logging

TRANSCEIVERS
  show inventory
  show interface detail
  show interface
```

</div>

</div>

## CISCO_WLC-AIR

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show run-config commands

IP FLOW
  show flow monitor summary

L2 INTERFACES
  show port summary
  show port detailed-info
  show stats port summary <portId>
  show lag summary
  show interface summary
  show interface detailed <name>
  show system interfaces
  show redundancy summary

L3 INTERFACES
  show port summary
  show port detailed-info
  show stats port summary <portId>
  show lag summary
  show interface summary
  show interface detailed <name>
  show system interfaces
  show redundancy summary

NEIGHBOR DISCOVERY PROTOCOLS
  show cdp neighbors detail

NTP
  show time

PORT-CHANNELS
  show port summary
  show lag summary
  show interface summary
  show interface detail <int>
  show system interfaces
  show redundancy summary

ROUTING TABLE
  show port summary
  show port detailed-info
  show stats port summary <portId>
  show lag summary
  show interface summary
  show interface detailed <name>
  show system interfaces
  show redundancy summary

SN
  show inventory

SNMP
  show snmpcommunity
  show snmptrap
  show snmpv3user
  show snmpversion
  show sysinfo

SYSLOG
  show run-config commands

TRANSCEIVERS
  show port summary
  show port detailed-info
  show stats port summary
  show interface summary
  show interface detail <int>
  show system interfaces
  show redundancy summary
```

</div>

</div>

## JUNIPER_JUNOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  show configuration | display set | except "^deactivate"

ACL
  show configuration | display set

ARP
  show arp no-resolve

BGP
  show route instance detail
  show bgp neighbor instance <instanceName>
  show bgp summary <instanceName>

CLUSTER
  show chassis cluster status
  show chassis cluster interfaces

ERROR DISABLED INTERFACES
  show ethernet-switching interface
  show ethernet-switching interfaces
  show spanning-tree interface detail
  show interfaces statistics detail

FHRP
  show vrrp detail

IP FLOW
  show configuration firewall | display omit
  show configuration forwarding-options sampling
  show configuration interfaces | match sampling | except filter | display set
  show configuration policy-options | display set
  show interfaces statistics detail
  show sflow collector
  show sflow interface
  show sflow

IPSEC
  show security ike security-associations detail
  show security ipsec security-associations detail
  show configuration | display set | except "^deactivate"

IS-IS
  show isis interface extensive instance <instanceName>
  show isis overview instance <instanceName>
  show isis adjacency extensive instance <instanceName>
  show interfaces statistics detail
  show version
  show chassis cluster status

L2 INTERFACES
  show interfaces statistics detail
  show interfaces terse
  show vlans detail
  show analyzer
  show dot1x interface detail

L3 INTERFACES
  show interfaces statistics detail
  show route instance detail
  show vrrp detail
  show vlans detail

MAC
  show ethernet-switching table
  show vlans detail
  show ethernet-switching vxlan-tunnel-end-point source
  show ethernet-switching vxlan-tunnel-end-point esi

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors
  show lldp neighbors interface <int>

NTP
  show ntp associations no-resolve
  show system connections

OSPF
  show ospf interface detail instance <instanceName>
  show ospf neighbor detail instance all

OSPFV3
  show ospf3 interface detail instance <instanceName>
  show ospf3 neighbor detail instance all
  show ospf3 overview instance <instanceName>
  show route instance detail

POE
  show poe interface
  show poe controller

PORT-CHANNELS
  show interfaces statistics detail
  show lacp interfaces

PORT MIRRORING
  show analyzer
  show forwarding-options analyzer

RIP
  show rip interfaces instance all
  show rip statistics instance all

ROUTE SUMMARY
  show route summary
  show route instance detail
  show bgp neighbor <instanceName>
  show route table <instanceName>.inet.0 protocol isis active-path detail | match level
  show ospf neighbor detail instance all
  show ospf route network detail instance <instanceName>

ROUTING TABLE
  show route active-path

SECURED ACCESS PORTS
  show dot1x interface detail
  show interfaces terse

SN
  show chassis hardware

SNMP
  show configuration | display set | except "^deactivate"
  show interfaces statistics detail

STACKING
  show virtual-chassis
  show virtual-chassis device-topology
  show virtual-chassis vc-port all-member

STP
  show vlans detail
  show spanning-tree bridge detail
  show spanning-tree interface detail
  show spanning-tree mstp configuration
  show spanning-tree statistics interface
  show configuration

STP PORT SECURITY
  show spanning-tree interface detail
  show ethernet-switching interfaces
  show configuration | display set | except "^deactivate"

SYSLOG
  show configuration | display set | except "^deactivate"

TRANSCEIVERS
  show chassis hardware
  show interfaces diagnostics optics
  show interfaces terse

VLAN
  show vlans detail

VRF
  show route instance detail
  show configuration | display set | except "^deactivate"

VXLAN
  show ethernet-switching vxlan-tunnel-end-point source
  show ethernet-switching vxlan-tunnel-end-point remote
  show interfaces statistics detail
  show vlans detail

ZONE FIREWALL
  show configuration | display set
  show configuration groups junos-defaults applications | display set
  show interfaces statistics detail
```

</div>

</div>

HP_COMWARE

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
AAA
  display current-configuration

ACL
  display acl all
  display packet-filter all
  display packet-filter interface
  display object-group

ARP
  display arp
  display ip interface
  display ip vpn-instance
  display arp vpn-instance <instanceName>

BGP
  display bgp peer ipv4
  display bgp peer ipv4 verbose
  display bgp peer ipv4 vpn-instance <instanceName>
  display bgp peer ipv4 vpn-instance <instanceName> verbose
  display bgp peer
  display bgp peer verbose
  display bgp peer vpn-instance <instanceName>
  display bgp peer vpn-instance <instanceName> verbose
  display ip vpn-instance

ERROR DISABLED INTERFACES
  display vrrp verbose

FHRP
  display vrrp verbose

IP FLOW
  display ip netstream export
  display sflow

IS-IS
  display current-configuration configuration isis
  display isis <processId>
  display isis brief <processId>
  display isis peer verose <processId>
  display isis name-table <processId>
  display ip interface
  display ip vpn instance <vpnInstance>

L2 INTERFACES
  display clock
  display interface
  display voice-vlan state
  display voice vlan state

L3 INTERFACES
  display ip vpn-instance instance-name <name>
  display ip interface
  display vrrp verbose

MAC
  display mac-address

NEIGHBOR DISCOVERY PROTOCOLS
  display lldp neighbor-information
  display lldp neighbor-information verbose

NTP
  display ntp-service sessions

OSPF
  display ospf peer verbose
  display ospf interface verbose

POE
  display poe interfaces

PORT-CHANNELS
  display interface
  display link-aggregation verbose

PORT MIRRORING
  display mirroring-group all

RIP
  display rip
  display rip <processId> neighbors
  display rip <processId> interfaces

ROUTE SUMMARY
  display ip routing-table statistics

ROUTING TABLE
  display ip routing-table verbose
  display ip vpn-instance
  display ip routing-table vpn-instance <name> verbose

SECURED ACCESS PORTS
  display port-security
  display dot1x
  display mac-authentication

SN
  display device manuinfo
  display license device-id

SNMP
  display current-configuration

STACKING
  display device manuinfo
  display irf
  display irf topology
  display wlan ap all verbose

STORM CONTROL
  display storm-constrain

STP
  display stp
  display stp region-configuration
  display vlan all
  display interface

SYSLOG
  display info-center

TRANSCEIVERS
  display transceiver interface
  display transceiver diagnosis interface
  display transceiver manuinfo interface

VLAN
  display vlan all

VRF
  display ip vpn-instance
  display ip vpn-instance instance <instanceName>
```

</div>

</div>

## CISCO_ACI

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ACI
  show endpoint detail
  show system internal epm vlan all
  show system internal epm vrf all
  show coop internal info ip-db
  show isis dteps vrf overlay-1

ARP
  show ip arp vrf all

CHASSIS EXTENDERS
  show fex detail
  show interface fex-fabric

FHRP
  show hsrp

L2 INTERFACES
  show interface
  show interface switchport

L3 INTERFACES
  show ip interface vrf all
  show hsrp brief
  show interface

MAC
  show mac address-table
  show vpc

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show cdp neighbors detail

NTP
  show ntp peer-status

OSPF
  show ip ospf neighbor detail vrf all
  show ip ospf interface vrf all

PORT-CHANNELS
  show port-channel summary
  show vpc

ROUTE SUMMARY
  show ip route summary vrf all

ROUTING TABLE
  show ip route vrf <vrf>
  show ip interface vrf all
  show interfaces
  show system internal epm vrf all

SN
  show version
  show inventory

TRANSCEIVERS
  show interface transceiver details
  show interface transceiver fex-fabric details
  show interface fex-fabric
  show inventory [all]

VLAN
  show vlan extended

VRF
  show vrf detail
```

</div>

</div>

## CISCO_VIPTELA

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  GET /dataservice/device/arp?deviceId=<deviceId>

BGP
  GET /dataservice/device/bgp/neighbors?deviceId=<deviceId>
  GET /dataservice/device/bgp/summary?deviceId=<deviceId>

FHRP
  GET /dataservice/device/vrrp?deviceId=<deviceId>

IPSEC
  GET /dataservice/device/ipsec/ike/sessions?deviceId=<deviceId>
  GET /dataservice/device/ipsec/ike/outbound?deviceId=<deviceId>
  GET /dataservice/device/interface?deviceId=<deviceId>

L2 INTERFACES
  GET /dataservice/device/interface?deviceId=<deviceId>

L3 INTERFACES
  GET /dataservice/device/interface?deviceId=<deviceId>
  GET /dataservice/device/bfd/sessions?deviceId=<deviceId>

NTP
  GET /dataservice/device/ntp/peer?deviceId=<deviceId>

OSPF
  GET /dataservice/device/ospf/neighbor?deviceId=<deviceId>
  GET /dataservice/device/ospf/interface?deviceId=<deviceId>

ROUTING TABLE
  GET /dataservice/device/ip/routetable?deviceId=<deviceId>
  GET /dataservice/device/interface?deviceId=<deviceId>
  GET /dataservice/device/bfd/sessions?deviceId=<deviceId>

SN
  GET /dataservice/device

SNMP
  GET /dataservice/device/config?deviceId=<deviceId>

SYSLOG
  GET /dataservice/device/config?deviceId=<deviceId>
  GET /dataservice/device/interface?deviceId=<deviceId>
```

</div>

</div>

## DELL_FTOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp

L2 INTERFACES
  show interfaces
  show interfaces switchport

L3 INTERFACES
  show ip interface

MAC
  show mac-address-table
  show mac address-table

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors

NTP
  show ntp associations

PORT-CHANNELS
  show interfaces port-channel brief

ROUTING TABLE
  show ip route

SN
  show system stack-unit 0

STP
  show spanning-tree mst configuration
  show spanning-tree msti <id>
  show spanning-tree pvst
  show spanning-tree rstp
  show spanning-tree 0
  show vlan
  show interfaces switchport
  show interfaces

VLAN
  show vlan

VRF
  show ip vrf
```

</div>

</div>

## DELL_POWERCONNECT

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp

L2 INTERFACES
  show interfaces
  show interfaces status
  show ip interface
  show ip interface <type> <id>

L3 INTERFACES
  show ip interface
  show ip interface <type> <id>

MAC
  show mac address-table

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp interface all
  show lldp remote-device detail <intName>

NTP
  show ntp associations

PORT-CHANNELS
  show interfaces status
  show interfaces port-channel

ROUTING TABLE
  show ip route

SN
  show version

STP
  show spanning-tree summary
  show spanning-tree
  show spanning-tree detail
  show spanning-tree mst-configuration
  show interfaces status
  show vlan

VLAN
  show vlan
```

</div>

</div>

## HP_ARUBA

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp

FHRP
  show ip interface brief
  show vrrp
  show ip interface brief

IP FLOW
  show ip-flow-export-profile

L2 INTERFACES
  show port stats
  show vlan status
  show interface <int>
  show interface loopback
  show datapath bridge

L3 INTERFACES
  show ip interface brief
  show vrrp

MAC
  show datapath bridge

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbor
  show lldp neighbor interface <int> detail

NTP
  show ntp server

PORT-CHANNELS
  show port stats
  show vlan status
  show interface <int>

SN
  show inventory

SNMP
  show running-configuration

SYSLOG
  show logging server

VLAN
  show vlan
```

</div>

</div>

## HP_ARUBASW

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp

FHRP
  show vrrp vlan <vlan> vrid <vrid> config
  show run
  show ip

L2 INTERFACES
  show interfaces all
  show interfaces brief
  show vlans ports all detail
  show vlans
  show vlans <id>
  show run
  show ip

L3 INTERFACES
  show run
  show ip
  show vlans
  show vrrp vlan <vlan> vrid <vrid> config

MAC
  show mac-address
  show mac-address vlan <vlanId>
  show vlans

NEIGHBOR DISCOVERY PROTOCOLS
  show cdp neighbors
  show lldp info remote-device detail
  show lldp info remote-device
  show lldp info remote-device <intName>

NTP
  show ntp associations

PORT-CHANNELS
  show trunks
  show interface brief

ROUTING TABLE
  show ip route
  show vlans

SN
  show system

SNMP
  show running-configuration

STACKING
  show stacking

STP
  show spanning-tree
  show spanning-tree config
  show spanning-tree vlan <vlanId>
  show spanning-tree mst-config
  show spanning-tree detail
  show spanning-tree instance <instance>
  show spanning-tree debug-counters instance <instance> ports all
  show vlans
  show vlans ports all detail

STP PORT SECURITY
  show spanning-tree detail

SYSLOG
  show syslog config

TRANSCEIVERS
  show interfaces transceiver
  show interfaces transceiver detail

VLAN
  show vlans
```

</div>

</div>

## HP_ARUBACX

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp all-vrfs
  show arp

BGP
  show bgp all-vrf all neighbors
  show bpg all neighbors

FHRP
  show vrrp
  show interface

L2 INTERFACES
  show interface
  show interface mgmt

L3 INTERFACES
  show ip interface brief
  show ip interface brief all-vrfs
  show interface mgmt
  show vrrp

MAC
  show mac-address-table

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbor info
  show lldp neighbor info <int>
  show cdp neighbor info
  show cdp neighbor info <int>

NTP
  show ntp associations

OSPF
  show ip ospf interface
  show ip ospf interface all-vrfs
  show ip ospf neighbors detail
  show ip ospf neighbors detail all-vrfs

PORT-CHANNELS
  show interface lag
  show interface
  show vsx brief
  show vsx status
  show lacp interfaces multi-chassis

ROUTE SUMMARY
  show ip route summary all-vrfs
  show ip route summary

ROUTING TABLE
  show ip route
  show ip route all-vrfs
  show ip route summary all-vrfs
  show ip route summary
  show ip route <protocolName> all-vrfs
  show ip route <protocolName>
  show interface mgmt

SN
  show system

STACKING
  show vsf detail
  show vsf link

STP
  show spanning-tree detail
  show spanning-tree mst detail
  show spanning-tree summary root
  show vlan

TRANSCEIVERS
  show interface transceiver detail

VLAN
  show vlan

VRF
  show vrf
```

</div>

</div>

## FORTINET_FORTIGATE

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  get system arp

BGP
  get router info bgp neighbors
  get router info bgp summary

VIRTUAL CONTEXTS
  config global
  diagnose system vd list

FHRP
  get router info vrrp

IP FLOW
  get system interface
  get system netflow
  get system sflow

IPSEC
  get system status
  diagnose vpn ike gateway list
  diagnose vpn tunnel list
  show vpn ipsec phase1
  show vpn ipsec phase1-interface

L2 INTERFACES
  get system interface physical
  diagnose hardware deviceinfo nic
  show system interface
  get system status
  diagnose netlink aggregate list
  diagnose netlink aggregate name <aggInterface>
  diagnose vpn ike gateway list
  diagnose sys ha mac

L3 INTERFACES
  show system interface
  get router info vrrp
  show system settings
  get system status
  get system interface
  show system ha

MAC
  get system status
  show system interface
  diagnose netlink brctl list
  diagnose netlink brctl name host <bridge>

NEIGHBOR DISCOVERY PROTOCOLS
  diagnose user device list
  show system interface
  get system vdom-link
  get system status

NTP
  diagnose sys ntp status
  show system ntp

OSPF
  get router info ospf interface
  get router info ospf neighbor detail

PORT-CHANNELS
  diagnose netlink aggregate list
  diagnose netlink aggregate name <aggInterface>

ROUTING TABLE
  get router info routing-table all
  show router static

SN
  get system status

SNMP
  show full system snmp community
  get system snmp sysinfo
  get system snmp user

SYSLOG
  get log syslogd setting
  get log syslogd2 setting
  get log syslogd3 setting
  get log syslogd filter
  get log syslogd2 filter
  get log syslogd3 filter
  get log disk setting

TRANSCEIVERS
  get system interface transceiver
  get system interface transceiver <intName>

ZONE FIREWALL
  diagnose firewall auth list
  diagnose firewall fqdn list
  diagnose internet-service id [ID]
  get system status
  show firewall address
  show firewall addrgrp
  show firewall policy
  show firewall service custom
  show firewall service group
  show firewall vip
  show firewall vipgrp
  show full-configuration application list
  show system interface
  show system zone
```

</div>

</div>

PALOALTO

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp all
  show arp management

BGP
  show routing protocol bgp peer
  show routing protocol bgp summary

VIRTUAL CONTEXTS
  show system state filter sw.mprelay.s1.dp0.vsys.stats.session

IPSEC
  show vpn flow tunnel-id <id>
  show vpn gateway
  show vpn ike-sa
  show vpn ipsec-sa
  show vpn tunnel
  show interface <name>
  show inteface all

L2 INTERFACES
  show interface all
  show interface <int>
  show interface management
  show system state filter-pretty sw.dev.runtime.ifmon.port-states

L3 INTERFACES
  show interface all
  show interface <int>
  show interface management

MAC
  show mac all
  show vlan all

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors all

NTP
  show ntp

OSPF
  show routing protocol ospf interface
  show routing protocol ospf neighbor
  show interface all
  show interface <name>

PORT-CHANNELS
  show interface all
  show lacp aggregate-ethernet all

ROUTING TABLE
  show routing route
  show routing route virtual-router <vr>
  show interface <intName>
  show interface all
  show interface management

SN
  show mac all

SYSLOG
  show config merged

TRANSCEIVERS
  show system state filter-pretty sys.s*.p*.phy
  show system state filter-pretty sw.dev.runtime.ifmon.port-states
  show interface <INT>
  show interface all

VLAN
  show vlan all

VRF
  show interface <int>
  show interface all

ZONE FIREWALL
  show config pushed-shared-policy vsys <vsysName>
  show interface <intName>
  show interface all
  show config merged
  request system fqdn show
  show dns-proxy fqdn all
  show object dynamic-address-group all
```

</div>

</div>

## RIVERBED_STEELHEAD

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp
  show interfaces

IP FLOW
  show ip flow-export
  show ip flow-setting

L2 INTERFACES
  show interfaces

L3 INTERFACES
  show interfaces

NTP
  show ntp all

ROUTING TABLE
  show ip route
  show ip in-path route <int>

SN
  show info

SNMP
  show snmp
  show snmp usernames

SYSLOG
  show logging
```

</div>

</div>

## CHECKPOINT_GAIA

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp dynamic all
  show route all

BGP
  show bgp peers detailed
  show router-id

VIRTUAL CONTEXTS
  show vsx
  show virtual-system all

FHRP
  show vrrp interfaces

IP FLOW
  show netflow all

L2 INTERFACES
  show interfaces all
  show virtual-system all

L3 INTERFACES
  show interfaces all
  show cluster state
  show cluster members interfaces all
  show route all
  show virtual-system all
  show vrrp interfaces

MAC
  show interfaces all
  show bridging groups
  /web_api/show-gateways-and-servers

NEIGHBOR DISCOVERY PROTOCOLS
  show interfaces all
  show virtual-system all
  show hostname
  show bridging groups
  /web_api/show-gatways-and-servers

NTP
  show ntp servers

OSPF
  show interfaces all
  show ospf interfaces detailed
  show ospf neighbors detailed
  show virtual-system all

PORT-CHANNELS
  show bonding groups
  show interfaces all

ROUTE SUMMARY
  show route summary

ROUTING TABLE
  show route all

SN
  show management interface
  show interfaces all

SNMP
  show configuration snmp

SYSLOG
  show syslog all

ZONE FIREWALL
  /web_api/showAccessLayers
  /web_api/showAccessRulebase
  /web_api/showGatewaysAndServers
  /web_api/showObject
  /web_api/showObjects
  /web_api/showPackages
```

</div>

</div>

## CHECKPOINT_GAIA-EMBEDDED

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  arp

L2 INTERFACES
  show interfaces all
  show interface <int>

L3 INTERFACES
  show interfaces all
  show interface <int>

NTP
  show ntp

ROUTE SUMMARY
  show route summary

ROUTING TABLE
  show route all

SN
  show diag

ZONE FIREWALL
  /web_api/showAccessLayers
  /web_api/showAccessRulebase
  /web_api/showGatewaysAndServers
  /web_api/showObject
  /web_api/showObjects
  /web_api/showPackages
```

</div>

</div>

## EXTREME_BOSS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp-table

L2 INTERFACES
  show interfaces verbose
  show port statistics
  show vlan interface info
  show vlan interface vids
  show mlt
  show jumbo-frames
  show lldp local-sys-data

L3 INTERFACES
  show vlan ip
  show jumbo-frames
  show ip
  show vlan

MAC
  show mac-address-table
  show mac-address-table vid <vid>
  show vlan

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbor
  show lldp neighbor-mgmt-addr

ROUTING TABLE
  show ip route
  show vlan ip
  show ip
  show vlan

SN
  show sys-info

STP
  show mlt
  show sys-info
  show vlan interface vids
  show running-config
  show spanning-tree mode
  show spanning-tree op-mode
  show spanning-tree mstp config
  show spanning-tree mstp msti config <id>
  show spanning-tree mstp msti port config <id>
  show spanning-tree mstp msti port role <id>
  show spanning-tree mstp msti port statistics <id>
  show spanning-tree mstp port config
  show spanning-tree mstp port role
  show spanning-tree mstp port statistics
  show spanning-tree mstp status
  show spanning-tree mstp statistics
  show spanning-tree rstp config
  show spanning-tree rstp port config
  show spanning-tree rstp port role
  show spanning-tree rstp port statistics
  show spanning-tree rstp statistics
  show spanning-tree rstp status
  show spanning-tree stp <id> config
  show spanning-tree stp <id> port vlans

VLAN
  show vlan
```

</div>

</div>

## EXTREME_ENTERASYS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show arp

L2 INTERFACES
  show port status
  show port alias
  show port counters
  show vlan portinfo

L3 INTERFACES
  show ip address
  show ip interface
  show host vlan
  router

MAC
  show mac

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp port remote-info

PORT-CHANNELS
  show lacp
  show port status

ROUTING TABLE
  show ip route
  router

SN
  show system hardware

STP
  show vlan
  show vlan portinfo
  show spantree version
  show spantree mstmap
  show spantree stats active
  show spantree stats active sid <id>

VLAN
  show vlan
```

</div>

</div>

## EXTREME_VOSS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show ip arp

L2 INTERFACES
  show interfaces gigabitEthernet interface
  show interfaces gigabitEthernet statistics
  show interfaces gigabitEthernet statistics verbose
  show interfaces gigabitEthernet l1-config
  show interfaces mgmtEthernet
  show port vlans

L3 INTERFACES
  show ip vrf
  show ip interface

MAC
  show vlan mac-address-entry

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbor

OSPF
  show ip vrf
  show ip interface
  showip interface vrf <VRF>
  show ip ospf interface
  show ip ospf interface vrf <VRF>
  show ip ospf neighbor
  show ip ospf neighbor vrf <VRF>

PORT-CHANNELS
  show mlt
  show interfaces gigabitEthernet state

ROUTE SUMMARY
  show ip route count-summary

ROUTING TABLE
  show ip vrf
  show ip route
  show ip route vrf <VRF>

SN
  show sys-info

STP
  show mlt
  show port vlans
  show spanning-tree config
  show spanning-tree mstp msti config
  show spanning-tree mstp msti port config
  show spanning-tree mstp msti port role
  show spanning-tree mstp msti port statistics
  show spanning-tree mstp port config
  show spanning-tree mstp port role
  show spanning-tree mstp port statistics
  show spanning-tree mstp status
  show spanning-tree rstp port config
  show spanning-tree rstp port role
  show spanning-tree status

SYSLOG
  show syslog
  show syslog host <id>

VLAN
  show vlan name
  show port vlans

VRF
  show ip vrf
```

</div>

</div>

## EXTREME_XOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show iparp vr <vrName>
  show virtual router

BGP
  show bgp neighbor detail
  show bgp

IP FLOW
  show ip-fix
  show sflow config

IS-IS
  show isis area
  show isis neighbors detail
  show isis vlan
  show vlan detail

L2 INTERFACES
  show ports configuration no-refresh port-number
  show switch
  show ports statistics no-refresh port-number
  show ports utilization bytes port-number
  show ports utilization packets port-number
  show ports rxerrors no-refresh port-number
  show ports txerrors no-refresh port-number
  show ports description
  show configuration

L3 INTERFACES
  show vlan detail
  debug vlan show vlans

MAC
  show fdb

NEIGHBOR DISCOVERY PROTOCOLS
  show lldp neighbors detail
  show edp ports all detail

NTP
  show ntp associations

OSPF
  show ospf interfaces detail enabled
  show ospf neighbor detail
  show vlan detail

PORT-CHANNELS
  show sharing
  show mlag peer
  show mlag ports

ROUTE SUMMARY
  show iproute summary

ROUTING TABLE
  show iproute vr <vr>
  show virtual router
  show vlan detail
  debug vlan show vlans

SN
  show version

SNMP
  show configuration
  show management

STP
  show stpd
  show stpd detail
  show stpd <stpDomain> ports detail
  show stpd <stpDomain> ports counters
  show vlan detail

SYSLOG
  show log configuration

TRANSCEIVERS
  show ports information detail
  show ports transceiver information detail

VLAN
  show vlan detail

VRF
  show virtual-router
```

</div>

</div>

## HUAWEI_VRP

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  display arp
  display arp all

BGP
  display bgp <addressFamiily> <vpnInstance> peer
  display bgp <addressFamiily> <vpnInstance> peer verbose

FHRP
  display vrrp
  display vrrp verbose
  display vrrp protocol-information

IP FLOW
  display ip netstream all
  display sflow
  display sflow configuration

IS-IS
  display ip vpn-instance
  display isis interface verbose [vpn-instance <vpnInstance>]
  display isis peer verbose [vpn-instance <vpnInstance>]

L2 INTERFACES
  display interface
  display port vlan active
  display port vlan
  display vlan

L3 INTERFACES
  display ip interface
  display ip vpn-instance
  display ip vpn-instance <name> interface
  display vrrp

MAC
  display mac-address
  display interface
  display vxlan vni

NEIGHBOR DISCOVERY PROTOCOLS
  display lldp neighbor

NTP
  display ntp sessions

OSPF
  display ospf interface all
  display ospf peer

PORT-CHANNELS
  display eth-trunk
  display interface

PORT MIRRORING
  display port-mirroring
  display port-mirroring configuration
  display observe-port

ROUTE SUMMARY
  display ip routing-table statistics
  display ip routing-table vpn-instance <instanceName> statistics

ROUTING TABLE
  display ip routing-table statistics
  display ip routing-table verbose
  display ip routing-table protocol <name> verbose
  display ip vpn-instance
  display ip routing-table vpn-instance <name> statistics
  display ip routing-table vpn-instance <name> verbose
  display ip routing-table vpn-instance <name> protocol <name> verbose
  display mpls lsp verbose
  display ip interface
  display ip vpn-instance
  display ip vpn-instance <name> interface
  display vrrp

SN
  display esn
  display device manufacture-info

SNMP
  display current-configuration
  display snmp-agent community read
  display snmp-agent community write

STP
  display interface
  display port vlan active
  display port vlan
  display vlan
  display stp
  display stp vlan <vlanId>
  display stp region-configuration
  display stp vlan information
  display stp vlan bpdu statistics
  display vbst bpdu-statistics

SYSLOG
  display info-center

TRANSCEIVERS
  display transceiver verbose
  display interface transceiver verbose
  display interface
  display optical-module extend information interface <intName>

VLAN
  display vlan
  display current-configuration

VRF
  display ip vpn-instance verbose

VXLAN
  display vxlan vni
  display vxlan tunnel
  display interfaces
```

</div>

</div>

## F5_BIG-IP

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  show net arp all

BGP
  list /net route-domain
  imish -r <rd_ID>
  show bgp neighbors
  show bgp <addressFamily> summary

IP FLOW
  list /sys sflow receiver all-properties
  show sys sflow data-source

L2 INTERFACES
  show net interface all-properties
  show net trunk all-properties
  list net vlan
  show net self
  show sys cluster all-properties

L3 INTERFACES
  list net self
  show net self
  list net vlan
  list /sys management-ip
  show sys cluster all-properties

MAC
  show sys mac-address
  list net vlan

NTP
  run util bash -c "ntpq -np"

PORT-CHANNELS
  list net trunk
  show net trunk all-properties
  show net interface all-properties

ROUTING TABLE
  show net route all
  list net self

SN
  show sys hardware

SNMP
  list sys snmp

SYSLOG
  list sys syslog

VLAN
  list net vlan

VRF
  list /net route-domain
```

</div>

</div>

## MIKROTIK_ROUTEROS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  /ip arp print detail without-paging

BGP
  /routing bgp instance print detail without-paging
  /routing bgp peer print status without-paging

FHRP
  /interface vrrp print detail without-paging
  /ip address print detail without-paging

IPSEC
  /ip ipsec peer print detail
  /ip ipsec active-peer print detail
  /ip ipsec policy print detail
  /ip ipsec identity print detail
  /ip ipsec installed-sa print detail
  /ip ipsec profile print detail
  /ip ipsec proposal print detail
  /ip address print detail

L2 INTERFACES
  /interface print detail without-paging
  /interface print stats-detail without-paging
  /interface vlan print detail without-paging
  /interface ethernet print detail without-paging

L3 INTERFACES
  /ip address print detail without-paging
  /interfaces print detail without-paging
  /ip route vrf print detail without-paging
  /ipv6 address print detail without-paging

MAC
  /interface bridge host print detail without-paging where !local

NEIGHBOR DISCOVERY PROTOCOLS
  /ip neighbor print detail without-paging
  /interface print detail without-paging
  /interface vlan print detail without-paging

NTP
  /system ntp client print without-paging

OSPF
  /ip address print detail without-paging
  /routing ospf area print detail without-paging
  /routing ospf instance print detail without-paging
  /routing ospf interface print detail without-paging
  /routing ospf neighbor print detail without-paging

PORT-CHANNELS
  /interface print detail without-paging
  /interface bonding print detail without-paging

ROUTING TABLE
  /ip route print detail without-paging

SN
  /system license print

SNMP
  /snmp print without-paging
  /snmp community print detail without-paging

SYSLOG
  /system logging print detail without-paging
  /system logging action print detail without-paging

VRF
  /ip route vrf print detail
```

</div>

</div>

## VERSA_VOS

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
ARP
  GET vnms/dashboard/appliance/<appliance>/live?command=arp/all

BGP
  GET vnms/dashboard/appliance/<appliance>/live?command=bgp/neighbors/detail?deep
  GET vnms/dashboard/appliance/<appliance>/live?command=bgp/neighbors/brief?deep

FHRP
  GET /vnms/dashboard/appliance/<appliance>/live?command=vrrp?deep

IPSEC
  GET /vnms/dashboard/appliance/<appliance>/live?command=orgs/org-services/<organization>/ipsec/vpn-profile?deep
  GET /vnms/dashboard/appliance/<appliance>/live?command=interfaces?deep

L2 INTERFACES
  GET vnms/dashboard/appliance/{site_name}/live?command=interfaces?deep

L3 INTERFACES
  GET vnms/dashboard/appliance/<appliance>/live?command=interfaces?deep
  GET vnms/dashboard/appliance/<appliance>/live?command=vrrp?deep

OSPF
  GET /vnms/dashboard/appliance/<appliance>/live?command=ospf/neighbor/nbr-extensive
  GET /vnms/dashboard/appliance/<appliance>/live?command=ospf/interface/int-extensive
  GET /vnms/dashboard/appliance/<appliance>/live?command=interfaces?deep

ROUTING TABLE
  GET /vnms/dashboard/appliance/<appliance>/live?command=rib?deep
  GET /vnms/dashboard/appliance/<appliance>/live?command=interfaces?deep

SN
  GET /vnms/appliance/appliance?offset=0&limit=2500

VRF
  GET api/config/devices/device/{site-name}/config/routing-instances/routing-instance
```

</div>

</div>

FRR

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
BGP
  show ip bgp neighbors json
  show interface vrf all

L2 INTERFACES
  show interface vrf all

L3 INTERFACES
  show interface vrf all

OSPF
  show ip ospf vrf all interface json
  show ip ospf vrf all neighbor detail json
  show interface vrf all

ROUTE SUMMARY
  show vrf
  show ip route vrf <VRF> summary [table <TABLE>]

ROUTING TABLE
  show vrf
  show ip route vrf <VRF>
  show interface vrf all

SN
  show interface vrf all

VRF
  show vrf
```

</div>

</div>

QUAGGA

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
BGP
  show daemons
  show bgp neighbors
  show bgp summary
  show interface

L2 INTERFACES
  show interface

L3 INTERFACES
  show interface

OSPF
  show daemons
  show interface
  show ip ospf interface
  show ip ospf neighbor

ROUTE SUMMARY
  show ip route summary

ROUTING TABLE
  show ip route
  show interface

SN
  show interface

VRF
  show interface
```

</div>

</div>

## AWS_EC2

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
IPSEC
  DescribeCustomerGatewaysCommand
  DescribeVpnConnectionsCommand

L2 INTERFACES
  DescribeSubnetsCommand
  DescribeTransitGatewayVpcAttachmentsCommand
  DescribeVpcPeeringConnectionsCommand
  DescribeVpnConnectionsCommand
  DescribeVpnGatewaysCommand

L3 INTERFACES
  DescribeNatGatewaysCommand
  DescribeNetworkInterfacesCommand
  DescribeRouteTablesCommand
  DescribeSubnetsCommand
  DescribeTransitGatewayAttachmentsCommand
  DescribeTransitGatewayVpcAttachmentsCommand
  DescribeVpcPeeringConnectionsCommand
  DescribeVpnConnectionsCommand
  DescribeVpnGatewaysCommand

NEIGHBOR DISCOVERY PROTOCOLS
  DescribeNatGatewaysCommand
  DescribeNetworkInterfacesCommand
  DescribeSubnetsCommand
  DescribeTransitGatewayVpcAttachmentsCommand
  DescribeVpcPeeringConnectionsCommand
  DescribeVpnGatewaysCommand

ROUTING TABLE
  DescribeNatGatewaysCommand
  DescribeNetworkInterfacesCommand
  DescribeRouteTablesCommand
  DescribeSubnetsCommand
  DescribeTransitGatewayAttachmentsCommand
  DescribeTransitGatewayRouteTablePropagationsCommand
  DescribeTransitGatewayVpcAttachmentsCommand
  DescribeVpcPeeringConnectionsCommand
  DescribeVpnGatewaysCommand
  DescribeVpnConnectionsCommand

SN
  DescribeNatGatewaysCommand
  DescribeTransitGatewaysCommand
  DescribeVpcsCommand
  DescribeVpnGatewaysCommand

VRF
  DescribeRouteTablesCommand
  DescribeTransitGatewayRouteTablesCommand
```

</div>

</div>

## CISCO_MERAKI

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
L2 INTERFACES
  GET /networks/{networkId}/devices/{sn}/uplink
  GET /networks/{networkId}/devices/{sn}/lldp_cdp
  GET /devices/{sn}/switchPorts
  GET /devices/{sn}/switchPortStatuses
  GET /devices/{sn}/switchPortStatusesPackets
  GET /networks/{networkId}/switch/settings
  GET /networks/{networkId}/switch/settings/mtu
  GET /devices/{sn}/clients
  GET /networks/{networkId}/appliancePorts
  GET /networks/{networkId}/vlans

L3 INTERFACES
  GET /networks/{networkId}/devices/{sn}/uplink
  GET /networks/{networkId}/vlans
  GET /networks/{networkId}/switch/settings

MAC
  GET /devices/{deviceSn}/clients

NEIGHBOR DISCOVERY PROTOCOLS
  GET /organizations/{organizationId}/devices
  GET /organizations/{organizationId}/deviceStatuses
  GET /networks/{networkId}/devices/{sn}/lldp_cdp
  GET /devices/{sn}/switchPortStatuses

ROUTING TABLE
  GET /networks/{networkId}/devices/{sn}/uplink
  GET /networks/{networkId}/vlans
  GET /networks/{networkId}/switch/settings
  GET /networks/{networkId}/staticRoutes

SN
  GET /organizations/{organizationId}/devices
  GET /organizations/{organizationId}/deviceStatuses
```

</div>

</div>
