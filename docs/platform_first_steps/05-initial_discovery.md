---
description: This page describes how to start the initial discovery.
---

# Initial Discovery

Now that you've entered the essential details, you can start the discovery!

## Option 1 -- via the Configuration Wizard

In step 4 of the [Configuration Wizard](04-configuration_wizard.md), simply
click **Start Discovery**.

## Option 2 -- via the Discovery Snapshot Section

In the **Discovery Snapshot** section, click **+ New snapshot** and then **Start
discovery**:

![Start discovery](start_discovery.webp)

IP Fabric will attempt to connect to the default gateway of the VM and any
provided seed IP addresses. Once connected to a device, IP Fabric will identify
the vendor, model, and version, and adjust accordingly to run the
[necessary commands](https://matrix.ipfabric.io). You can read more about the
discovery process in
[How Discovery Works](../overview/How_Discovery_Works/CLI_discovery.md).

After the discovery is completed, all state data will be available, and you can
start exploring the [IP Fabric GUI](../IP_Fabric_GUI/discovery_snapshot.md).

**Enjoy using IP Fabric!**

If no devices are discovered, or if something is missing, please check this
[documentation page](../overview/How_Discovery_Works/common_problems/no-devices-discovered.md)
for common problems or contact our Support team.
