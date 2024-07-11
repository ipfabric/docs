---
description: This page describes that the Transceivers task is disabled by default due to a known issue, and how you can enable it.
---

# Transceivers Task

## Task Execution Control

Executing certain commands to retrieve transceiver-related information may cause issues on some devices. In the worst case, a device may crash and reload. To prevent network disruptions, IP Fabric employs a transceiver task execution control system. The task is only executed on a device if:

- The `Transceivers` task is enabled.
- IP Fabric doesn’t classify the device as affected by any known bugs.

### Note

- By default, the `Transceivers` task is disabled. You can enable it in the IP Fabric settings (follow the steps below).
- Even if the `Transceivers` task is enabled, IP Fabric still prevents its execution on any devices classified as affected by any known bugs. This feature cannot be disabled at this time. Refer to the list of known bugs and their corresponding [software and hardware versions](../Vendors/cisco/Show_Interface_Transceivers.md).

### Disclaimer

While we strive to prevent task execution on all software and hardware versions known to be affected by bugs, we cannot guarantee that all bugs are patched. For example, a device manufacturer may update their list of devices affected by a specific bug over time, but IP Fabric may not fully reflect these updates.

## How To Find Transceivers in IP Fabric

Navigate to **Technology --> Interfaces --> Transceivers**:

![IP Fabric menu](ipf_issues/transceivers_interfaces.png)

## How To Enable/Disable Transceivers Task

This task is **enabled by default** for all vendors and product families, meaning that **this command is not executed on any device**.

You can **enable/disable** this task in **Settings --> Discovery & Snapshots --> Discovery Settings --> Disabled Discovery Tasks**.

![Transceivers settings](ipf_issues/transceivers_settings.png)

To **disable** this task, you need to **delete the default `Transceivers` task** or **edit** it.

When **editing** this task, you select devices by using a regex expression where this command **should not** be executed. For example, if you don't want to run the `show interface transceivers` command on all Cisco devices, enter `cisco` to the **Vendor** field. More specific device selection can be done using the **Family**, **Platform**, **Model**, and **Version** fields. You can test your regex rules with the **Test rules** button.

![Edit transceivers rule](ipf_issues/transceivers_edit.png)
