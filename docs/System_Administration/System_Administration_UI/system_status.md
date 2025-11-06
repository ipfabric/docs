---
description: This page explains the System status section of the System Administration UI.
---

# System Status

When you log in to the **System Administration** UI with the `osadmin` user, you
will find yourself in the **System status** section. It displays information
such as the current CPU load, RAM usage, disk space usage, and the running
services.

The most CPU-intensive system processes are also displayed.

![System status](system_status.webp)

Additionally, you can **restart** specific system services or **restart / shut
down** the entire virtual machine.

!!! info

    When no discovery process is running, its services (`Tasker`, `Updater`,
    `Workers`, `Net Worker`, and `Scanner Workers`) are expected to be inactive.
