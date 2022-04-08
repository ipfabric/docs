# Changes

## Overview

*Snapshots* at different time intervals can be compared to find
dynamic changes in the network when a snapshot of the network
(discovery run) completes successfully.

*To enable a periodic discovery run* check the [Timed
Snapshots](../../IP_Fabric_Settings/advanced/snapshots.md) configuration.

## Comparing changes

To control changes between two discovery runs, go to *Management →
Changes*.

First select the more distant point in time (older snapshot) and then
select the second step point after the first one (newer snapshot).

There are four tables available:

### Devices

This table shows devices that were added, removed, or not changed in a
given time period (between two snapshots).

### Part numbers

This is where you can check for changes in individual device components,
especially useful for modular devices, and the status can be added,
removed, or not changed.

### Managed IP

Changes in addressing can cause problems, especially if they are not
well communicated between teams, and any changes to the IP address can
be seen in this table. Status can be added, removed, or not changed.

### Connectivity Matrix

Loss of connection, redundancy or part of the connection capacity can
also cause problems. Changes in the connections between devices can be
checked here and status can be added, removed, or not changed.
