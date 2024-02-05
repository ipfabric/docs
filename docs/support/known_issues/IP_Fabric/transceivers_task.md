---
description: This page describes known issues with the Transceivers task and how to fix them.
---

# Transceivers Task

## Task Execution Control

Executing some commands to get transceiver related information may cause issues on some devices. In the worst case, a device may crash and reload. To prevent disruptions of your network, IP Fabric uses a transceiver task execution control system. The task is only executed on a device if:

- The Transceivers task is enabled.
- IP Fabric doesn’t classify the device to be affected by any known bugs.

**Note:**

- The Transceivers task is disabled by default. You can enable it in the IP Fabric settings (see the steps below).
- Even if the Transceivers task is enabled, IP Fabric still prevents its execution on any device that is classified to be affected by any known bug. It is not possible to disable this feature now. See the list of known bugs and their corresponding [software and hardware versions.](../Vendors/cisco/Show_Interface_Transceivers.md)

**Disclaimer**

Although we try to prevent task execution on all software and hardware versions that are known to be affected by any bug, we cannot guarantee that all bugs are patched. For example, a device manufacturer may update their list of devices affected by a certain bug in time, but IP Fabric may not fully reflect it.

## How to Find Transceivers in IP Fabric

Navigate to **Technology --> Interfaces --> Transceivers**

![IP Fabric menu](ipf_issues/transceivers_interfaces.png)


## How to Enable/Disable Transceivers Task

This function is **enabled by default** for all vendors and product families. This means that **this command is not executed on any device**.

The function can be **Enabled/Disabled** in **Settings --> Discovery & Snapshots --> Discovery Settings --> Disabled Discovery Tasks**.

![Transceivers settings](ipf_issues/transceivers_settings.png)

To **disable** this task, you need to **delete the default Transceivers task** or **edit** this default task.

When **editing** this rule, you select by regex expression on which devices this command **should not** be executed (so for example, if you don't want to run the `show interface transceivers` command for all Cisco devices, put `cisco` to the **Vendor** field. More specific device selection can be done with the **Family**, **Platform**, **Model**, and **Version** fields). You can simply test your regex rules with the **Test rules** button.

![Edit transceivers rule](ipf_issues/transceivers_edit.png)
