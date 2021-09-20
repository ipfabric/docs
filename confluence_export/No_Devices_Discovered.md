# No Devices Discovered

## Problem

No network devices are discovered when you run Discovery for the first
time or after system changes

## Solution

1.  Check the "Connectivity report" on the Discovery page to see the
    specific addresses attempted and the reason for the failure (link:
    /discovery/tasks)
    1.  If the reason reports timeout, IP Fabric has IP address assigned
        that cannot reach the device. The route may not be present or
        the traffic may be filtered. Check IP Fabric connectivity
        with [Troubleshooting VM network problems using IP Fabric
        CLI](Troubleshooting_VM_Network_Problems_Using_IP_Fabric_CLI).
    2.  If the reason reports authentication failure, IP Fabric was not
        able to login to the device. Check [Authentication -
        Settings](Authentication).
    3.  Check the "CLI output" file in the Action column of the
        Connectivity Report to see the full interaction log to help you
        troubleshoot the issue. Check [Fine-Tune SSH/TELNET
        parameters](Fine-Tuning_SSH_TELNET_parameters).
2.  Provide discovery seed address on Discovery Seed page of the
    Settings section (link: /settings/discovery-seed)
    1.  Seed addresses specify starting points of discovery. If default
        gateway of IP Fabric VM is not discoverable, you need to specify
        an IP address or a network to start the discovery. It is
        recommended to provide IP address of a router as a starting
        point for discovery. Check [Discovery Seed -
        Settings](Discovery_Seed).
3.  Test the connection manually using IP Fabric CLI
    1.  Connect to IP Fabric using SSH and attempt to connect to the
        device using SSH or TELNET using the credentials entered on the
        authentication page. Check IP Fabric connectivity
        with [Troubleshooting VM Network Problems Using IP Fabric
        CLI](Troubleshooting_VM_Network_Problems_Using_IP_Fabric_CLI).
4.  If no devices are discovered after checking the Connectivity Report
    and after entering the Seed addresses, contact support for
    troubleshooting assistance. Check [Contacts](Contacts).
