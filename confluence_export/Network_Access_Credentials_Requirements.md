# Network Access Credentials Requirements

# Network Access Credentials Requirements

## Network device access

IP Fabric accesses network-infrastructure devices via CLI (command-line
interface) using SSH or TELNET protocols. All device interaction is
accounted on the platform and only “read-only” or “operator” group
privilege level 1 credentials are required.

The following list contains an example of commands used for Cisco IOS:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

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

</div>

</div>

In the beginning, IP Fabric fingerprints the device using the “show
version” command (or equivalent) to identify a vendor and a system
version. A "terminal length" command is optional but highly recommended,
as it greatly improves the speed of the device interaction, reduces the
load on the network and the device, and improves collection precision.

## Additional device access

Since firewalls do not follow privilege levels, it may be necessary to
explicitly specify the commands allowed for each user. The following
list specifies the exec-mode commands needed for firewall discovery.

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` text
show version
show interface
show route
show arp
show context
terminal pager 0
```

</div>

</div>

Turning off paging greatly improves the speed of the discovery and
allows a terminal pager command, making it highly recommended although
not mandatory. The commands can be allowed through the central TACACS or
RADIUS access control system, or they can be configured locally on a
device. The following example adds the necessary commands to a
privilege-1 user:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` text
privilege show level 1 mode exec command interface
privilege show level 1 mode exec command arp
privilege show level 1 mode exec command route
privilege show level 1 mode exec command context
privilege cmd level 1 mode exec command terminal
```

</div>

</div>

List of all commands used for CLI discovery can be found [on this
page](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/80019486/Used+CLI+commands+for+Discovery)
and in this [feature/vendor
matrix](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/392003585).
