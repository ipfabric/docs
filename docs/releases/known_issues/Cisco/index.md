# Cisco

## Cisco
!!! bug **Affected platforms**: 15.1(4)M4, 15.1(4)M4.7, 15.1(4)M5, 12.2(50)SE3, 6.0(2)N2(3), 15.5(3.0l)M

    **Description**: show transceivers command can have on some Cisco platform fatal issues including device crash. It takes several minutes to finish the command on some platforms.
 
    **Result**: Affected platforms are removed from collection and transceivers task is by default disabled in the IP Fabric. Before enabling it, make sure that your devices are not affected, and if yes, remove them from in task settings.

    **Resources**:

    - [CSCua29548](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCua29548)
    - [CSCtg41473](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCtg41473)
    - [CSCuq13396](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq13396)
    - [CSCva00194](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCva00194)

------------------------------------------------------------------------

!!! bug **Affected platforms**: All IOS family switches
    **Description**: show spanning-tree mst command requires enable password. Currently not supported for IOS family (only SG and ASA).

    **Result**: MST is not collected, STP inconsistency check false positive

    **Workaround**: Privilege 15 authorization on login or show spanning-tree mst command authorization

------------------------------------------------------------------------

!!! bug **Affected platforms**: SG family, sf302-08pp-k9 platform

    **Description**:  sh spa d command returns misformatted output (forgetting newline characters and repeating the output with an offset)

    **Result**: STP detail is not collected

------------------------------------------------------------------------

!!! info Cisco ASA
    **Description**: Some Cisco ASA and Firepower Hardware platforms enable running either Cisco ASA software or Firepower Threat Defense software. Depending on the software actually in use these devices are detected either as Cisco ASA or Cisco FTD. E.g. Cisco Firepower 2100 can be detected as “asa” when running ASA software, or as “ftd” when running FTD software.

------------------------------------------------------------------------

!!! bug **Affected platforms**: Cisco Nexus 5000, 6000 and 9000

    **Description**: Several Cisco Nexus platforms allow setting MTU on a per-service basis. Interface MTU shown in IPF GUI is only interface specific (e.g. inventory/interfaces table). Therefore interface MTU value for Nexus 5k/6k/9k can only be displayed if the network-qos system policy defines the same MTU for all services or when no network-qos system policy is active. Command “show policy-map system type network-qos” is used to determine the network-qos system policy.
    MTU value displayed in “show interface” command is assumed to be the default value. Note: class-fcoe is not considered when comparing different services MTUs.
    
    - [CSCsl21529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCsl21529)

------------------------------------------------------------------------

!!! bug **Affected platforms**: ASA and FTD family firewalls

    **Description**: Interface security levels are not supported currently.

    **Result**: End-to-end path security policy check is only based on ACLs now.

------------------------------------------------------------------------

!!! bug **Affected platforms**: ASA and FTD family firewalls

    **Description**: VLAN ID detection for interfaces - If “show interface detail” doesn’t provide VLAN ID, then if the interface name suggests VLAN presence (e.g. interface names like vlan100, or sub-interfaces like Gi0/1.100 or Po1.100, etc.) this VLAN will be used.

    **Result**: In rare cases, VLAN ID for interface might be not determined correctly

------------------------------------------------------------------------

!!! bug **Affected platforms**: FTD family firewalls

    **Description**: VLAN ID detection for interfaces - If “show interface detail” doesn’t provide VLAN ID, then if the interface name suggests VLAN presence (e.g. interface names like vlan100, or sub-interfaces like Gi0/1.100 or Po1.100, etc.) this VLAN will be used.

    **Result**: When using FTD, if you run the 'show ntp' command a password prompt will appear in the command line. This will break the discovery of FTD. NTP tasks for FTD is by default disabled. If your FTD are not affected by this bug, you can safely enable it.

    - [CSCvt01938](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt01938)