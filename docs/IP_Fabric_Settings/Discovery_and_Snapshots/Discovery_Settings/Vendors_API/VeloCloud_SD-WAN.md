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

![Add Connection - VeloCloud - username](velocloud/VeloCloud_username.webp)
![Add Connection - VeloCloud - API token](velocloud/VeloCloud_token.webp)

Please note that VeloCloud discovery utilizes both REST API and WebSocket
connections for network discovery.
