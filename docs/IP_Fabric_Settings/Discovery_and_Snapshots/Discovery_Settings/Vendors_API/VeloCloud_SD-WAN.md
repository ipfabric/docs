---
description: This section contains information on how to set up API discovery for VeloCloud.
---

# VeloCloud SD-WAN

Starting from version `6.9.0`, IP Fabric supports the VeloCloud Orchestrator
API.  This feature can be activated using [a feature
flag](../../../../System_Administration/Command_Line_Interface/Feature_Flags.md#velocloud-discovery).

!!! warning "Experimental Feature"

    VeloCloud discovery is still new and experimental feature. Although IP
    Fabric strives for the best result, IP Fabric still can't guarantee 100%
    success on experimental features.

In IP Fabric, navigate to **Settings --> Discovery & Snapshots --> Discovery
Settings --> Vendors API**, click **+ Add**, choose `VeloCloud` type from the
list, select type of authentication, and fill in the following details:

- **Username** and **Password** configured in the Global Settings of the
  VeloCloud Orchestrator, or
- **API Token** configured in the Global Settings of the VeloCloud Orchestrator
- **Base URL** of VeloCloud Orchestrator (e.g., `https://velocloud-ip-address`)
- [**Slug**](index.md#slug-and-comment)

![Add Connection - VeloCloud - username](../../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings-Vendors_API-velocloud_VeloCloud_username.png)
![Add Connection - VeloCloud - API token](../../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Discovery_Settings-Vendors_API-velocloud_VeloCloud_token.png)

Please note that since version `7.0` VeloCloud discovery utilizes both REST API and WebSocket
connections for network discovery.

For successful discovery, Edge devices **must be** running software versioned `5.0.0` or newer, see
[WebSocket API documentation](https://developer.broadcom.com/xapis/vmware-sd-wan-remote-diagnostics-websocket-api/latest/).

!!! Warning "Edge devices **not** running on version `5.0.0` or newer"

    If your Edge devices are **not** running on version `5.0.0` or newer, there are workarounds available
    to ensure continued functionality. Specifically, you need to add the tasks **ARP**, **Routing Table**
    and **L2 Interfaces** to the **Disabled Discovery Tasks** list. For detailed documentation on how to
    perform this, see [Adding a New Disabled Discovery Task](../disabled_discovery_tasks.md#example-of-adding-a-new-disabled-discovery-task).
    Ensure that you fill in `velocloud` as a family while disabling tasks.
