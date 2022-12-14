---
description: IP Fabric supports NSX-T API. NSX-T devices are discovered only through API.
---

# VMware NSX-T

Starting version **4.3** IP Fabric supports NSX-T API. NSX-T devices are discovered only through API.

To add NSX-T to discovery global settings, go to **Settings → Advanced → Vendors API** and press the **+Add** button. Afterward, choose NSX-T API from the list and fill in

- **Username and password** used to log in to NSX Manager
- **Base URL** of NSX Manager server (`https://nsx-manager-ip-address`)

## General Support Information

- IP Fabric is supporting NSX-T from version 3.0 and higher,
  development was done on version 3.1.2, the latest version is 3.2. We
  are not supporting the 2.x version, there are a lot of differences,
  VMware’s end of general support was in September 2021. [Product Lifecycle Matrix](https://lifecycle.vmware.com/#/)

- NSX-T running as on-premise (there are also cloud versions for AWS
  and Azure, where can NSX-T cloud be deployed on top of AWS/Azure
  infrastructure ), but we don’t support it now

- We don’t collect any data from vCenter, as NSX-T is multiplatform
  and supports KVM and bare metal servers as well, if those are
  connected to the NSX-T cloud, we will collect information about
  those also.

## We Are Supporting These Types Of Devices

- Tier-0 router
- Tier-1 router
  - also supporting VRFs

## Not Supported Features

- Load balancing
- All security features (IPS/IDS, Distributed FW, Gateway FW, Network
  introspection) - planned to add security features in upcoming
  releases
- Forwarding policies - planned to add in upcoming releases
- VPN services
- NAT
- EVPN Vxlans

## External Connectivity

We are supporting both external connectivity protocols, which are
implemented in NSX-T, and of course static routes. External connectivity
can be done only on Tier-0 routers.

- OSPF
- BGP
