---
description: In this section we talk about snapshots, scheduling, retention rules and how they work.
---

# Snapshot Retention

## Create Snapshots Periodically

For [change management](../../IP_Fabric_GUI/management/changes.md), regularly running IP Fabric
discovery is necessary. A periodic discovery run can be scheduled
in **Settings --> Discovery & Snapshots --> Snapshot Retention --> Create Snapshots Periodically**.

Here is an example for an automatic discovery run at **10 minutes past
every hour** (0:10; 1:10; 2:10; 3:10, etc.).

![Create Snapshots Periodically](snapshot_retention/create_snapshots_periodically.png)

### How Scheduling Works in IP Fabric

Let's assume that a snapshot is scheduled for every hour, and it
takes 4h:20min to be created, then the next snapshot will be scheduled
once the previous snapshot finishes. The scheduled time will be set at
the next possible period according to the cron setup.

![Cron Setup](snapshot_retention/cron_setup.jpg)

## Maximum Number of Loaded/Locked Snapshots

In **Settings --> Discovery & Snapshots --> Snapshot Retention**, you can change these parameters:

- **Maximum number of loaded snapshots**
  - maximum number of snapshots that can be loaded in **Discovery Snapshot**
  - default value: 3
  - possible values: 1-5
- **Maximum number of locked snapshots**
  - maximum number of loaded snapshots that can be locked in **Discovery Snapshot** to prevent them from being unloaded
  - default value: 1
  - possible values: 0-4

![Maximum number of loaded/locked snapshots](snapshot_retention/maximum_number_of_loaded_or_locked_snapshots.png)

## Snapshot Retention Rules

In version `4.1`, we added support for various snapshot retention policies.

![Snapshot Retention Rules](snapshot_retention/snapshot_retention_rules.png)

### How Snapshot Retention Works

It works in two steps:

1.  If any of the **keep** rules are enabled, IP Fabric goes through
    unloaded snapshots and based on enabled **keep** rules it marks
    snapshots to be retained or deleted.

2.  HDD utilization and a number of unloaded snapshots are checked. If
    any of these rules are exceeded, the oldest unloaded snapshots are
    deleted.

Please note:

1.  HDD utilization and the number of snapshots have precedence over
    **keep** rules. This means that snapshots marked as retained by a
    **keep** rule can be deleted when the HDD utilization or number of
    snapshots are exceeded.

2.  When at least one retention rule is enabled, all snapshots not
    protected by them will be removed regardless of reaching HDD
    utilization or snapshots count limits.

3.  Loaded snapshots are not affected by these rules. It affects only
    unloaded unlocked snapshots.

4.  Currently, IP Fabric only supports the delete action. Additional
    actions will be added in upcoming releases.

!!! info

    At the moment, snapshot retention runs every day at 0:00 UTC.
