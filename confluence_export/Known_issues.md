# Known issues

## Known issues

## IP Fabric

-   Diagram displays device, which is not connected to anything. The
    situation appears when site separation prevents displaying the
    device on the other end. To show connection to a device, click “Show
    Edge Cloud”

-   Diagrams drilldown missing. Current diagrams offer vast amount of
    information, which is not available through drilldowns. More
    drilldown capabilities are planned for future releases.

-   Advanced Filter Visibility. When Advanced filter is applied, and
    then collapsed via advanced filter button
    (<img src="attachments/thumbnails/79036476/81657862" loading="lazy" data-image-src="https://ipfabric.atlassian.net/wiki/download/attachments/79036476/image29.png?version=1&amp;modificationDate=1532345121265&amp;cacheVersion=1&amp;api=v2" data-unresolved-comment-count="0" data-linked-resource-id="81657862" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image29.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="9806dd06-3942-4ecd-a734-ff82543bad28" data-media-type="file" width="24" />),
    it’s not clear that filter is being applied to the table, except for
    the visible clear filter button
    (<img src="attachments/thumbnails/79036476/81657867" loading="lazy" data-image-src="https://ipfabric.atlassian.net/wiki/download/attachments/79036476/image30.png?version=1&amp;modificationDate=1532345122659&amp;cacheVersion=1&amp;api=v2" data-unresolved-comment-count="0" data-linked-resource-id="81657867" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image30.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="b65f86e6-0b63-46a5-89a3-7ff8306b647d" data-media-type="file" width="24" />).

-   Jumphost can be activated only from support console.

-   TACACS may be limited to the specific maximum number of simultaneous
    authentication sessions, preventing discovery of all of the devices
    in the network. If fewer than expected number of devices are
    discovered, decrease bandwidth rate (i.e. to 3Mb/s), increase
    SSH/TELNET session timeout (e.g. to 30 seconds), and decrease the
    maximum number of simultaneous sessions (i.e. 40).

-   Inter-platform spanning-tree topology enumeration requires L2
    discovery protocol to form a connection when
    port_id.port_priority.port_id field separation boundary is in
    inconsistent position between the two platforms.

-   Site separation - Changing “Firewall in site” and new
    discovery/recalculation can change site names.

### Snapshots (Release Candidate)

-   When Discovery is stopped mid way, and then Refresh is executed, the
    refresh does not consider IPs with status "STOP" for the next
    discovery

-   Resource check for sufficient RAM and HDD use a sliding window.
    Creating a new snapshot immediately after previous one may result in
    a "insufficient resources" failure. In such a case, verify resources
    on the status page and retry in several minutes.

-   Visualization does not work properly in Internet Explorer. Use
    Firefox or Chrome.

-   Switching site separation to RegEx can cause issues.

### Configuration management

**Description**: Format of configurations (show run etc) saved in IP
Fabric is changed, end of line characters were changed from rn to n

**Result**: Configurations saved before 2.1 and from 2.1 can show
differences when configurations are same

### Duplicate IP detection

**Description**: Anycast IP addresses are duplicate IP addressess
deployed at more than one location

**Result**: Anycast IP addresses are reported as duplicate addresses

  

## HP

**Affected platforms**: HP 10508 Comware Software, Version 5.20.105,
Release 1208P05

**Description**: Device sometimes randomly doesn’t return chassis
information, SN can’t be detected

**Result**: Device can be saved with some other SN other then correct
one from chassis. This can for example show incorrect change management
results.

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeHeader panelHeader pdl"
style="border-bottom-width: 1px;">

**Output**

</div>

<div class="codeContent panelContent pdl">

``` text
display device manuinfo
Chassis 1:

Chassis self:
Error: Failed to display the manufacture information of the chassis.
```

</div>

</div>

------------------------------------------------------------------------

**Description**: HP Aruba switches may not display their serial number
in “show version” command output. In such cases their base MAC address
from the show version output is set as their serial number. This issue
is known e.g. for HP 2824 version I.10.107.

  

## Cisco

**Affected platforms**: 15.1(4)M4, 15.1(4)M4.7, 15.1(4)M5, 12.2(50)SE3,
6.0(2)N2(3), 15.5(3.0l)M

**Description**: show transceivers command can have on some Cisco
platform fatal issues including device crash. It takes several minutes
to finish the command on some platforms.

**Result**: Affected platforms are removed from collection and
transceivers task is by default disabled in the IP Fabric. Before
enabling it, make sure that your devices are not affected, and if yes,
remove them from in task settings.

**Resources**:

<https://bst.cloudapps.cisco.com/bugsearch/bug/CSCua29548>  
<https://bst.cloudapps.cisco.com/bugsearch/bug/CSCtg41473>  
<https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq13396>  
<https://bst.cloudapps.cisco.com/bugsearch/bug/CSCva00194>

------------------------------------------------------------------------

**Affected platforms**: All IOS family switches

**Description**: show spanning-tree mst command requires enable
password. Currently not supported for IOS family (only SG and ASA).

**Result**: MST is not collected, STP inconsistency check false positive

**Workaround**: Privilege 15 authorization on login or show
spanning-tree mst command authorization

------------------------------------------------------------------------

**Affected platforms**: SG family, sf302-08pp-k9 platform

**Description**:  sh spa d command returns misformatted output
(forgetting newline characters and repeating the output with an offset)

**Result**: STP detail is not collected

------------------------------------------------------------------------

Description: Some Cisco ASA and Firepower Hardware platforms enable
running either Cisco ASA software or Firepower Threat Defense software.
Depending on the software actually in use these devices are detected
either as Cisco ASA or Cisco FTD. E.g. Cisco Firepower 2100 can be
detected as “asa” when running ASA software, or as “ftd” when running
FTD software.

------------------------------------------------------------------------

**Affected platforms**: Cisco Nexus 5000, 6000 and 9000

**Description**: Several Cisco Nexus platforms allow setting MTU on a
per-service basis. Interface MTU shown in IPF GUI is only interface
specific (e.g. inventory/interfaces table). Therefore interface MTU
value for Nexus 5k/6k/9k can only be displayed if the network-qos system
policy defines the same MTU for all services or when no network-qos
system policy is active. Command  “show policy-map system type
network-qos” is used to determine the network-qos system policy. MTU
value displayed in “show interface” command is assumed to be the default
value. Note: class-fcoe is not considered when comparing different
services MTUs. More
details https://bst.cloudapps.cisco.com/bugsearch/bug/CSCsl21529

------------------------------------------------------------------------

**Affected platforms**: ASA and FTD family firewalls

**Description**: Interface security levels are not supported currently.

**Result**: End-to-end path security policy check is only based on ACLs
now.

------------------------------------------------------------------------

**Affected platforms**: ASA and FTD family firewalls

**Description**: VLAN ID detection for interfaces - If “show interface
detail” doesn’t provide VLAN ID, then if the interface name suggests
VLAN presence (e.g. interface names like vlan100, or sub-interfaces like
Gi0/1.100 or Po1.100, etc.) this VLAN will be used.

**Result**: In rare cases, VLAN ID for interface might be not determined
correctly

------------------------------------------------------------------------

**Affected platforms: **FTD family firewalls

**Description**: VLAN ID detection for interfaces - If “show interface
detail” doesn’t provide VLAN ID, then if the interface name suggests
VLAN presence (e.g. interface names like vlan100, or sub-interfaces like
Gi0/1.100 or Po1.100, etc.) this VLAN will be used.

**Result**: When using FTD, if you run the 'show ntp' command a password
prompt will appear in the command line. This will break the discovery of
FTD. NTP tasks for FTD is by default disabled. If your FTD are not
affected by this bug, you can safely enable it.

<https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt01938>

  

-   Route leak defined by reference to another VRF is not supported.
    Route leak with the policy is supported.

  

------------------------------------------------------------------------

**Known Affected platforms**: Juniper SRX300

**Description**: *show ethernet-switching interface detail* can cause
infinite loop output

**Result**: 

Version 3.1.1 and earlier.

-   Endless command execution can cause device control plane
    overutilization issues that might also affect other control plane
    protocol operations (e.g. BFD). Further, it increases the time of
    IPF device/network discovery and can result in not discovering the
    device and gathering information from it.
-   We recommend removing such devices from the scope of IPF discovery
    (putting these devices to discovery exclude list).

Version 3.1.2 and above

-   Command ‘show ethernet-switching interfaces detail’ is no longer
    used and was substituted by other commands including ‘show
    ethernet-switching interfaces’. Further ‘show ethernet-switching
    interfaces’ command is only executed on devices discovered as EX or
    QFX switches.

------------------------------------------------------------------------

**Known Affected platforms**: SRX, MX

**Description**: *show ntp associations no-resolve* command timeouts

**Result**: <https://kb.juniper.net/InfoCenter/index?page=content&id=KB11436>

  

------------------------------------------------------------------------

****Known** Affected platforms**: ALL - valid for version 3.1.1 and
earlier

**Description**: The platform doesn't discover Juniper devices with the
'root' login. The 'root' enters the shell prompt (%) and not the
operational mode directly.

**Result**: 

Version 3.1.1 and earlier - the 'root' login cannot be used for
discovery.

Version 3.1.2 and above - the 'root' login may be used for discovery.

  

------------------------------------------------------------------------

****Known** Affected platforms**: ALL

**Description**: The Link-Layer Discovery Protocol (LLDP) links are not
displayed in diagrams.

**Result**: To display LLDP links in diagrams correctly, the IP address
of the neighbor has to be present in '**shot lldp neighbor interface
xx-x/x/x**' command. The IP address is present only when configured with
the '**set lldp management-address xx.xx.xx.xx**' command in the
configuration mode. More
at: <https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/management-address-edit-protocols-lldp.html>.

  

------------------------------------------------------------------------

****Known** Affected platforms**: ALL

**Description**: Information gathered from running-config doesn't
reflect apply-groups.

**Result**: Some information gathered from running-config can be
missing. It affect all tasks using running config - for example firewall
filters, snmp, syslog.  
More
at: <https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/apply-groups.html>

  

  

## Checkpoint

**Description: "fw ctl pstat" command requires admin rights**

**Known Affected platforms**: All

**Result**: Without this command collected no memory utilization will be
present

**Description: Discovery of Security Policies**

-   CheckPoint VSX is not fully supported yet

-   Wildcard & Dynamic objects and negated services are not supported

-   Settings > Advanced > Vendor API: In case that base URL points to a
    multi-domain server address, domains have to be specified

-   Inline Layers (Sub-policies) and Ordered Layers are not supported
    yet

  

## Mikrotik

**Known Affected platforms**: All

**Description**: Mikrotik requires longer session timeout otherwise it
will be not discovered

**Fix**: Settings => Advanced => SSH/Telnet => **Network device session
timeout** set to 20s
