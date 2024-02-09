---
description: This page describes how to resolve the issue with no network devices being discovered when discovery is run for the first time or after system changes.
---

# No Devices Discovered

## Problem

No network devices are discovered when you run discovery for the first
time or after system changes.

## Solution

1.  Check the **Connectivity Report** in the **Discovery Snapshot** section to see the
    specific addresses attempted and the reason for the failure.
    
    1.  If the reason reports timeout, IP Fabric has an IP address assigned
        that cannot reach the device. The route may not be present, or
        the traffic may be filtered. Check IP Fabric connectivity
        with [Troubleshooting VM network problems using IP Fabric
        CLI](../../../System_Administration/Command_Line_Interface/How_to/troubleshooting.md).
        
    2.  If the reason reports authentication failure, IP Fabric was not
        able to log in to the device. Check [Device
        Credentials](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/device_credentials.md).
        
    3.  Check the **CLI output** file in the `Action` column of the
        **Connectivity Report** to see the full interaction log to help you
        troubleshoot the issue. Check [Fine-Tune SSH/TELNET
        Parameters](finetune-ssh-telnet.md).

2.  Provide a discovery seed address in **Settings --> Discovery & Snapshots -->
    Discovery Settings --> Discovery Seeds**.

    Seed addresses specify starting points of discovery. If the default
    gateway of the IP Fabric VM is not discoverable, you will need to specify
    an IP address or a network to start the discovery. It is
    recommended to provide the IP address of a router as a starting
    point for discovery. Check [Discovery
    Seeds](../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/discovery_seeds.md).

3.  Test the connection manually using the IP Fabric CLI.

    Connect to IP Fabric using SSH and attempt to connect to the
    device using SSH or Telnet using the credentials entered on the
    authentication page. Check IP Fabric connectivity
    with [Troubleshooting VM Network Problems Using IP Fabric
    CLI](../../../System_Administration/Command_Line_Interface/How_to/troubleshooting.md).

4.  If no devices are discovered after checking the **Connectivity Report**
    and after entering the seed addresses, contact Support for
    troubleshooting assistance. Check [Contacts](../../../support/index.md#contact).
