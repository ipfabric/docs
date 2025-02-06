---
description: This document provides an overview of Cisco bug CSCwn70589, which causes a switch with MAB configuration to crash when executing the CLI command “show mab all details.”
---

# Switch with MAB configuration crashes on CLI command

As per Cisco bug [CSCwn70589](https://bst.cisco.com/quickview/bug/CSCwn70589), IP Fabric recommendation is to disable the task **Secured access ports** in the section **Disabled Discovery Tasks**.
Please refer to the [documentations](../../../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/disabled_discovery_tasks.md#default-disabled-discovery-tasks) for instructions on how to configure it.

When this Cisco bug is triggered, the following message is logged on the router:

`Reload reason: ‘Critical process sessmgrd fault on rp_0_0 (rc=139)’` 
