---
description: On this page, we explain the IP Fabric licensing concept.
---

# Licensing

IP Fabric has a straightforward licensing concept. One license is consumed for
every physical or virtual device in the network, excluding wireless access
points.

For example:

- A router with multiple VRFs counts as only one device in the license count.
- Each virtual instance on a firewall (VSYS, VDOM, etc.) counts as one license
  each. If you have one firewall with 80 virtual instances, it will count as 80
  devices in the license count.
- A stack of switches (StackWise, etc.) count as one device in the license,
  regardless of the number of switches in the stack.
- For wireless access points, a single license is consumed by the centralized
  controller, regardless of the number of APs controlled by it.
- For public cloud providers, licensing uses Cloud Connectivity Units
  (CCUs), not a license per device. See
  [Cloud Licensing](#cloud-licensing) below, and
  [What Counts Against a License, by Provider](#what-counts-against-a-license-by-provider)
  for construct level details.
- Each VMware NSX-T Tier-0 and Tier-1 router consumes one license. See
  [NSX-T](#nsx-t) below.

!!! info

  	If IP Fabric cannot detect the device type of a discovered device (due
  	to missing information from the CLI or API calls), the device will be
  	counted as unlicensed.

## Cloud Licensing

Cloud licensing covers the public cloud providers IP Fabric discovers -- AWS,
Azure, and GCP. IP Fabric licenses VMware NSX-T as on-premises infrastructure.
It is not part of this model; see [NSX-T](#nsx-t) below.

### How Cloud Licensing Works

IP Fabric discovers a large number of cloud objects, but **not every object
consumes a license**. Cloud licensing uses **Cloud Connectivity Units
(CCUs)**. IP Fabric assigns each supported construct a CCU value based on the role it
plays in the network:

| Tier       | CCU per Object | What It Represents                                                                                      |
| ---------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| **Tier A** | **1 CCU**      | Primary routing and security control points                                                             |
| **Tier B** | **0.5 CCU**    | Traffic-steering objects that are smaller, simpler, or far more numerous than an on-premises equivalent |
| **Tier C** | **0 CCU**      | Objects that are discovered and displayed, but do not bill on their own                                 |

Two principles govern this page:

- **Everything we license is listed here.** If a construct is not shown in the
  tables below, it is **not yet discovered or supported** -- it is _not_ a
  silent "free" object. The moment we begin discovering a new construct, we
  decide its tier and add it here.
- **Non-billable (0 CCU) constructs are listed explicitly.** We do not leave
  the non-billable constructs implicit.

!!! info "Why CCUs instead of one license per object?"

    Cloud environments fragment functions that an on-premises network would
    concentrate in a single device. A single on-premises load balancer may
    correspond to hundreds of individual cloud load-balancer constructs
    deployed per application. Flat per-object licensing would penalize exactly
    the customers who adopt cloud-native, elastic, infrastructure-as-code
    patterns. The tiered CCU model keeps licensing proportional to network
    _function_, not object count.

### Tier Definitions

These definitions are authoritative. When a new construct appears, IP Fabric places it
in a tier using these definitions.

#### Tier A -- 1 CCU

A construct qualifies as Tier A when it does **all** of the following:

- **Makes routing decisions or enforces a traffic policy**, and
- **Requires real configuration effort** (it has a non-trivial configuration
  surface), and
- Is **functionally similar to an on-premises device** (it behaves like a
  router, firewall, or equivalent appliance you would otherwise deploy in
  hardware).

In short, it is a primary control point you would recognize as a "device"
on-premises.

#### Tier B -- 0.5 CCU

A construct is Tier B when it behaves like a Tier A construct but **fails one**
of the Tier A conditions. Typical cases:

- It influences routing or enforces policy, but is **far smaller and more
  granular than its on-premises equivalent** (for example, one complex
  on-premises load balancer versus hundreds of fine-grained cloud load
  balancers), or
- It influences routing or enforces policy, but has **effectively no
  configuration** -- an on/off, "flip-the-switch" object, or
- It **does not make routing or policing decisions itself**, but is more than a
  passive connector.

#### Tier C -- 0 CCU (Discovered, Not Billed)

A construct is Tier C when it does not deliver a network function on its own.
Three groups exist:

- **Contributing objects with no standalone function** -- routing tables, rule
  sets, tags.
- **Connectors and link representations** -- provided the parent construct they
  attach to is already Tier A or Tier B. This avoids double-charging the same
  connectivity. For example, Transit Gateway attachments and VPC peerings.
- **Objects with no influence on traffic** -- hosts and compute such as virtual
  machines and EC2 instances.

### What Counts Against a License, by Provider

CCU values below are the current agreed values. Object codes are the internal
identifiers IP Fabric uses. Rows in the 0 CCU tables are discovered but never
billed.

#### AWS

Billed:

| AWS Networking Object  | Object Code | Tier | CCU |
| ---------------------- | ----------- | ---- | --- |
| VPC                    | `vpc`       | A    | 1   |
| Transit gateway        | `tgw`       | A    | 1   |
| Direct Connect gateway | `dxgw`      | A    | 1   |
| VPN gateway            | `vgw`       | A    | 1   |
| Core Network Edge      | `cne`       | A    | 1   |
| Internet gateway       | `igw`       | B    | 0.5 |
| Elastic Load Balancer  | `elb`       | B    | 0.5 |
| NAT gateway            | `nat`       | B    | 0.5 |

Not billed (Tier C, 0 CCU):

| AWS Object                                |
| ----------------------------------------- |
| Transit gateway attachment                |
| VPC peering and connections               |
| VPC endpoint                              |
| EC2 instances, ENIs, Elastic IPs          |
| Route tables and individual route entries |
| Security group rule counts                |
| Tags and metadata                         |

VPC endpoints are discovered as devices, under the object code `vpce`, and are
priced explicitly at 0 CCU.

#### Azure

Billed:

| Azure Networking Object             | Object Code    | Tier | CCU |
| ----------------------------------- | -------------- | ---- | --- |
| Virtual Network                     | `vnet`         | A    | 1   |
| Azure Firewall                      | `azfw`         | A    | 1   |
| Route Server                        | `ars`          | A    | 1   |
| Virtual HUB                         | `vhub`         | A    | 1   |
| Virtual Network gateway             | `vngw`         | A    | 1   |
| VPN gateway                         | `vpngw`        | A    | 1   |
| Express Route Circuit               | `erc`          | A    | 1   |
| Load Balancer / Application Gateway | `lb` / `appgw` | B    | 0.5 |
| NAT gateway                         | `nat`          | B    | 0.5 |

Not billed (Tier C, 0 CCU):

| Azure Object              |
| ------------------------- |
| Express Route gateway     |
| VNet peering              |
| Route tables and UDRs     |
| Virtual machines and NICs |
| Public IP objects         |
| NSG rules                 |
| Resource groups           |

Express Route gateways are discovered as devices, under the object code `erg`,
but are not assigned a CCU cost.

#### GCP

Billed:

| GCP Networking Object | Object Code | Tier | CCU |
| --------------------- | ----------- | ---- | --- |
| VPC                   | `vpc`       | A    | 1   |
| (Cloud) Router        | `router`    | A    | 1   |
| VPN gateway           | `vpngw`     | A    | 1   |
| Load Balancer         | `lb`        | B    | 0.5 |

Not billed (Tier C, 0 CCU):

| GCP Object                |
| ------------------------- |
| Cloud NAT                 |
| Virtual machines and NICs |
| Route tables and entries  |
| Firewall rule counts      |
| Labels and metadata       |

Cloud NAT is discovered as a device, under the object code `nats`, but is not
assigned a CCU cost.

### Consistency Across Providers

When the same function appears in multiple providers, we aim to license it
consistently. For example, an Azure ExpressRoute gateway and an AWS Transit
Gateway play comparable roles, and their tiering should be reasoned about
consistently. If applying the tier definition to one provider yields a
different result than another, that is a signal to revisit the definition, not
to special-case a single cloud.

### Empty VPC, VNet, or VPC Network

!!! warning "Planned, not yet in effect"

    This behavior is not active in release `8.1`. In `8.1`, an empty VPC or
    VNet is still discovered and still consumes its CCU. The rules below
    describe the intended future behavior once implemented.

The intent is that a VPC, VNet, or VPC Network with **no active participation
in the topology** will be classified as **empty** and billed at **0 CCU**, even
though a populated VPC or VNet is Tier A. It will remain discovered and
visible; it just will not bill.

IP Fabric treats a construct as **non-empty** (and bills it at its normal CCU) if
any of these signals are present:

| Signal                                          | AWS                                         | Azure                                                  | GCP                                                                |
| ----------------------------------------------- | ------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------ |
| Active route table beyond default/system routes | Route table with custom routes              | UDR with custom routes                                 | Custom routes in a routing table                                   |
| Attached gateway                                | IGW, NAT GW, VGW, TGW attachment, CNE, DXGW | ExpressRoute GW, VPN GW, Azure Firewall                | Cloud Router with peer, Cloud NAT, VPN GW, Interconnect attachment |
| Active peering with route propagation           | VPC peering                                 | VNet peering                                           | VPC peering                                                        |
| Compute resources deployed                      | Instance                                    | Virtual machine                                        | Instance                                                           |
| Service connectivity                            | Private Link service or endpoint            | Subnet with service delegation / private endpoint, DNS | Private Service Connect endpoint or service                        |

If none of these is detected, the construct is empty and excluded from billing.

## NSX-T

VMware NSX-T is licensed as on-premises infrastructure. Its constructs are not
assigned CCUs and do not fall under [Cloud Licensing](#cloud-licensing) above.

One license is consumed by each NSX-T networking object, counted against your
device limit. Currently, these are at least:

| NSX-T Networking Object | Object Code |
| ----------------------- | ----------- |
| Tier 0 router           | `tier0`     |
| Tier 1 router           | `tier1`     |

!!! info

    NSX-T Tier-0 and Tier-1 routers are unrelated to the CCU tiers described
    under [Tier Definitions](#tier-definitions). They are VMware's own names
    for the two router types in an NSX-T topology.

## Changes

### Release `8.1.0`

Starting from version `8.1.0`, licenses can use the new CCU cloud licensing
strategy instead of counting cloud constructs against the on-premises device
limit. See [Cloud Licensing](#cloud-licensing) above.
Licenses without a CCU limit continue to use the devices strategy.

### Release `7.3.16`

Starting from version `7.3.16`, when Aruba Instant Access Points (IAPs) are already managed by Aruba Central, discovering their Virtual Controller (VC) will no longer consume a license.

### Release `4.4.0`

Starting from version `4.4.0`, every device (virtual or physical) will consume
one license. This now applies to devices where information is collected via CLI
or API. The only exception is wireless access points, which do not consume any
licenses.

This change in licensing will affect the following vendors:

- SD-WAN -- Versa, Viptela, Silver Peak
- Wireless access points -- Meraki, Juniper MIST
- Cloud infrastructure -- AWS, Azure

### Releases <= `4.3.x`

For versions `4.3.x` or older, every device (virtual or physical) with
information collected via CLI will consume one license. Any devices with
information collected via API would _not_ consume a license. Examples of
API-collected devices are SD-WAN (Versa, Viptela, Silver Peak), cloud wireless
(Meraki), and cloud infrastructure (AWS).

## Expired License

When your license expires:

- You will not be able to log in to the IP Fabric main GUI.
- New snapshots will not be created, and automatic snapshots will stop.
- API calls may still work.
- Configuration management will run in the background.
