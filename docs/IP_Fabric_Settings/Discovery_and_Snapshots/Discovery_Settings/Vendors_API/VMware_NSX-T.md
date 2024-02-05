---
description: IP Fabric supports NSX-T API. NSX-T devices are discovered only through API.
---

# VMware NSX-T

Starting version `4.3`, IP Fabric supports NSX-T API. NSX-T devices are discovered only through API.

To add NSX-T to discovery global settings, go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API** and click **+ Add**. Afterwards, choose `VMware NSX-T` from the list and fill in:

- **Username and password** used to log in to NSX Manager
- **Base URL** of NSX Manager server (`https://nsx-manager-ip-address`)
- [**Slug**](index.md#slug-and-comment)

## General Support Information

- IP Fabric supports NSX-T from version `3.0` and higher,
  development was done on version `3.1.2`, the latest version is `3.2`. We
  are not supporting the `2.x` versions, there are a lot of differences,
  VMware’s end of general support was in September 2021. [Product Lifecycle Matrix](https://lifecycle.vmware.com/#/)

- NSX-T running as on-premises (there are also cloud versions for AWS
  and Azure, where can NSX-T cloud be deployed on top of AWS/Azure
  infrastructure), but we don’t support it now.

- We don’t collect any data from vCenter, as NSX-T is multiplatform
  and supports KVM and bare metal servers as well, if those are
  connected to the NSX-T cloud, we will collect information about
  those also.

## We Are Supporting These Types of Devices

- Tier-0 router
- Tier-1 router
  - also supporting VRFs

## Security

- Distributed Firewall
- Gateway / Edge Firewall
- Context profiles

!!! note

    Source and destination objects for DFW / Gateway Firewall can be defined by:

     - IP address or range
     - Group
     - Virtual Machine
     - Segment

## Not Supported Features

- Load balancing
- Some security features (IPv6, IPS/IDS, Network introspection, Endpoint protection rules,
  AD identity groups) -- planned for upcoming releases
- Forwarding policies -- planned for upcoming releases
- VPN services
- NAT
- EVPN VxLANs

## External Connectivity

We are supporting both external connectivity protocols, which are
implemented in NSX-T, and of course static routes. External connectivity
can be done only on Tier-0 routers.

- OSPF
- BGP

## API Rate Limiting

According to the
[NSX-T Data Center API Guide](https://vdc-download.vmware.com/vmwb-repository/dcr-public/d6de7a5e-636f-4677-8dbd-6f4ba91fa5e0/36b4881c-41cd-4c46-81d1-b2ca3a6c693b/api.html#mainFrame):

> The NSX-T API service has three settings that control the rate of incoming API
> requests:
>
> 1) A per-client rate limit, in requests per second. If a client makes more
> requests than this limit in one second, the API server will refuse to service
> the API request and will return an HTTP 429 Too Many Requests Error. By
> default, this limit is 100 requests per second.
>
> 2) A per-client concurrency limit. This is the maximum number of outstanding
> requests that a client can have. For example, a client can open multiple
> connections to NSX-T and submit operations on each connection. When this limit
> is exceeded, the server returns a 429 Too Many Requests error to the client.
> By default, this limit is 40 concurrent requests.
>
> 3) An overall maximum number of concurrent requests. This is the maximum
> number of API requests that can be in process on the server. If the server is
> at this limit, additional requests will be refused and the HTTP error 503
> Service Unavailable will be returned to the client. By default, this limit is
> 199 concurrent requests.

The default settings for API rate limiting in IP Fabric are based on 0.75 times
the VMware values, which means 75 requests per second and 30 concurrent
requests. If you need to modify these settings, please reach out to IP Fabric
Support or Solution Architect team.

We recommend using a dedicated NSX-T user for discovery in IP Fabric and running
discovery at a time when no other automation is accessing the NSX-T controller.
