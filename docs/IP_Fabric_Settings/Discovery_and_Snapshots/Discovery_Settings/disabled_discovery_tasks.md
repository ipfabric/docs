---
description: This section explains Disabled Discovery Tasks and describes the default ones.
---

# Disabled Discovery Tasks

The discovery process for network devices is divided into multiple Tasks.
A Task is data collection related to a specific network protocol or
technology (MPLS, Transceivers, ARP Table, Spanning-Tree Protocol,
Multicast, or VXLAN). Each Task consists of 1 or more operational
commands (CLI or API). You can find the list of all Discovery Tasks
in the [Feature Matrix](https://matrix.ipfabric.io).

Some fundamental Tasks are critical for discovery and topology calculations
(Neighbors, ARP, Mac, RIB, etc.).

The **Disabled Discovery Tasks** settings were introduced in version `3.7.0`.
Since then, you can manipulate specific Tasks for the discovery process
to avoid extra data collection (when particular protocols are not
present on the network) or avoid specific operational commands from being
executed on specific hardware platforms. Since version `6.8.0`, you can filter
disabled Tasks by the device's Serial Number.

!!! warning

    Disabling Tasks will reduce the level of information collected by IP Fabric.
    If some fundamental Tasks are disabled, it can affect the topology or path
    lookup results.

## Default Disabled Discovery Tasks

![Default Disabled Discovery Tasks](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings_default_disabled_discovery_tasks.webp)

Since version `6.9`, **Disabled Discovery Tasks** contain the following four
predefined rules:

| Rule Name               | Rule Description                                                                                                                   |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `Disable Pagination`    | By default, it is disabled for F5 devices. The command is modifying the configuration and can break cluster synchronization.       |
| `Transceivers`          | By default, it is disabled for all vendors. Certain Cisco platforms may be affected by a memory leak bug and lead to device crash or hung VTY line. More in [Known Issues -- Cisco](../../../support/known_issues/Vendors/cisco/index.md). |
| `NTP`                   | By default, it is disabled for Cisco Firepower. On some versions, a Firepower bug may freeze the CLI session.                      |
| `BGP Advertised Routes` | Since version `6.9`, it is disabled by default for Cisco devices. The output could be huge, so it may break the discovery process. |

Prior to version `6.3.0`, the `Configuration saved` rule (disabling for all
vendors) was also present by default. New deployments of version `6.3.0` or
newer do not have the rule predefined anymore. Upgrading from version `6.2.2`
or older does not automatically remove the previously predefined rule.

## Example of Adding a New Disabled Discovery Task

In the following example, we are creating a rule for disabling OSPFv3 on Arista
vEOS. The test for the rule reveals 4 matches.

!!! note "Check"

    For a device to be considered a match, all defined regex rules must match 
    (evaluated using AND logic). Additional information about regex syntax can 
    be found in
    [Regular Expression Syntax](../../../IP_Fabric_GUI/technology_tables/index.md#regular-expression-syntax).

![Example](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings_disabled_discovery_tasks_example.webp)
