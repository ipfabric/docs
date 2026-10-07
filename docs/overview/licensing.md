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
- **Non-billable (0 CCU) constructs are listed explicitly.** Standalone objects
  are listed per provider, grouped. The parts, links, and labels that belong to
  other objects are covered by one general rule -- see
  [Never Billed Separately](#never-billed-separately-all-providers).

!!! info "Why CCUs instead of one license per object?"

    Cloud environments fragment functions that an on-premises network would
    concentrate in a single device. A single on-premises load balancer may
    correspond to hundreds of individual cloud load-balancer constructs
    deployed per application. Flat per-object licensing would penalize exactly
    the customers who adopt cloud-native, elastic, infrastructure-as-code
    patterns. The tiered CCU model keeps licensing proportional to network
    _function_, not object count.

### How Your License Counts Cloud Objects

Your license type determines how these tiers apply:

| License                    | Tier A Object    | Tier B Object    | Tier C Object |
| -------------------------- | ---------------- | ---------------- | ------------- |
| **Cloud (CCU) license**    | 1 CCU            | 0.5 CCU          | 0 CCU         |
| **Device-based license**   | 1 device license | 1 device license | None          |

- **Cloud (CCU) license:** cloud objects never consume device licenses. The
  device limit applies to on-premises devices only.
- **Device-based license** (all licenses issued before version `8.1.0`, and
  licenses without cloud licensing): every Tier A or Tier B cloud object
  consumes one full device license, including Tier B objects. Tier C objects
  consume nothing.
- A snapshot is counted under the license that was active when it was
  discovered. Changing your license applies to snapshots discovered after the
  change; existing snapshots keep the licensing they were discovered with.

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
  connectivity. For example, VPC peerings, or an ExpressRoute gateway
  connecting a VNet to its (billed) ExpressRoute circuit.
- **Objects with no influence on traffic** -- hosts and compute such as virtual
  machines and EC2 instances.

#### Never Billed Separately (All Providers)

These are discovered and shown, but they are not constructs in their own right,
so they never consume a license:

- **Parts of another object** -- routes and route entries, address ranges and
  CIDR blocks, NAT rules, peering prefixes, the entries of an address list, the
  rules inside a security group, and the connections of a private-link service.
  They are covered by their parent object.
- **Links between objects** -- attachments and associations, for example
  subnet to route table, NAT gateway to subnet, network interface to security
  group, Transit Gateway and other gateway attachments, and tag assignments.
- **Labels and organizational context** -- tags and labels, accounts,
  subscriptions, projects, resource groups, and regions.

An object that IP Fabric shows in several places (inventory, topology, path
lookup) is counted once.

### What Counts Against a License, by Provider

CCU values below are the current agreed values. Object codes are the internal
identifiers IP Fabric uses. Rows in the 0 CCU tables are discovered but never
billed.

#### AWS

Billed:

| AWS Networking Object                                      | Object Code | Tier | CCU |
| ---------------------------------------------------------- | ----------- | ---- | --- |
| VPC (see [Empty VPC](#empty-vpc-vnet-or-vpc-network))      | `vpc`       | A    | 1   |
| Transit gateway                                            | `tgw`       | A    | 1   |
| VPN gateway                                                | `vgw`       | A    | 1   |
| Core Network Edge                                          | `cne`       | A    | 1   |
| Direct Connect gateway                                     | `dxgw`      | B    | 0.5 |
| Internet gateway                                           | `igw`       | B    | 0.5 |
| Elastic Load Balancer                                      | `elb`       | B    | 0.5 |
| NAT gateway                                                | `nat`       | B    | 0.5 |

Not billed (Tier C, 0 CCU):

| Group                   | AWS Objects                                                                                     | Object Code           |
| ----------------------- | ----------------------------------------------------------------------------------------------- | --------------------- |
| Networks and addressing | Subnets, Elastic IPs (public IP addresses), managed prefix lists                                | --                    |
| Connectivity            | VPC peering connections; VPC endpoints (gateway type, and interface or Gateway Load Balancer type) | `vpce` (gateway type) |
| Routing and security    | Route tables, security groups                                                                   | --                    |
| Compute                 | EC2 instances, Elastic Network Interfaces (ENIs), Auto Scaling groups                           | --                    |

#### Azure

Billed:

| Azure Networking Object                                         | Object Code    | Tier | CCU |
| --------------------------------------------------------------- | -------------- | ---- | --- |
| Virtual Network (see [Empty VNet](#empty-vpc-vnet-or-vpc-network)) | `vnet`      | A    | 1   |
| Azure Firewall                                                  | `azfw`         | A    | 1   |
| Virtual HUB                                                     | `vhub`         | A    | 1   |
| Virtual Network gateway, VPN or Local Gateway type              | `vngw`         | A    | 1   |
| VPN gateway                                                     | `vpngw`        | A    | 1   |
| ExpressRoute circuit                                            | `erc`          | A    | 1   |
| Route Server                                                    | `ars`          | B    | 0.5 |
| Load Balancer / Application Gateway                             | `lb` / `appgw` | B    | 0.5 |
| NAT gateway                                                     | `nat`          | B    | 0.5 |

Not billed (Tier C, 0 CCU):

| Group                                     | Azure Objects                                                                                                | Object Code     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| Gateways to a billed ExpressRoute circuit | ExpressRoute gateway (vWAN construct); Virtual Network gateway of ExpressRoute type (VNet construct)          | `erg`, `vngw`   |
| Networks and addressing                   | Subnets, public IP addresses and prefixes, application security groups, service tags                         | --              |
| Connectivity                              | VNet peerings, private endpoints, Private Link services                                                      | --              |
| Routing and security                      | Route tables (User-Defined Routes, UDRs), Network Security Groups (NSG)                                      | --              |
| Compute                                   | Virtual machines, network interfaces, Virtual Machine Scale Sets                                             | --              |

#### GCP

Billed:

| GCP Networking Object                                        | Object Code | Tier | CCU |
| ------------------------------------------------------------ | ----------- | ---- | --- |
| VPC (see [Empty VPC Network](#empty-vpc-vnet-or-vpc-network)) | `vpc`      | A    | 1   |
| Cloud Router                                                 | `router`    | A    | 1   |
| VPN gateway (HA and Classic)                                 | `vpngw`     | A    | 1   |
| Load Balancer                                                | `lb`        | B    | 0.5 |

Cloud NAT is configured on a Cloud Router and is currently covered by that
router; it is not billed separately.

Not billed (Tier C, 0 CCU):

| Group                   | GCP Objects                                                                                   | Object Code |
| ----------------------- | --------------------------------------------------------------------------------------------- | ----------- |
| Networks and addressing | Subnets, external (public) IP addresses, address groups                                       | --          |
| Connectivity            | VPC peerings, Private Service Connect endpoints and services                                  | --          |
| Routing and security    | Routes, firewall rules and firewall policies                                                  | --          |
| Compute                 | VM instances, network interfaces, instance groups and network endpoint groups                 | --          |

### Consistency Across Providers

When the same function appears in multiple providers, we aim to license it
consistently. For example, an Azure ExpressRoute gateway and an AWS Transit
Gateway play comparable roles, and their tiering should be reasoned about
consistently. If applying the tier definition to one provider yields a
different result than another, that is a signal to revisit the definition, not
to special-case a single cloud.

### Empty VPC, VNet, or VPC Network

!!! info "In effect from version `8.2.0`"

    In version `8.1`, an empty VPC or VNet is still discovered and still
    consumes its CCU.

A VPC, VNet, or VPC Network with **no active participation in the topology** is
classified as **empty** and billed at **0 CCU** (Tier C). It remains discovered
and visible; it just does not bill. Under a device-based license, it does not
consume a device license either.

IP Fabric treats a construct as **non-empty** (and bills it at its normal CCU) if
any of these signals are present:

| Signal                             | AWS                                                                                                                                  | Azure                                                                                       | GCP                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Route beyond default/system routes | Route table with custom routes (anything other than the local route or the plain default route to the VPC's internet gateway)       | A route table associated with a subnet                                                      | Custom routes (excluding the default route, peering-learned routes, and subnet routes)   |
| Attached gateway                   | NAT gateway, VPN gateway, Transit Gateway attachment, Core Network Edge, Direct Connect gateway; internet gateway (except the one AWS attaches to the default VPC) | ExpressRoute gateway, VPN gateway, Azure Firewall, Route Server, NAT gateway on a subnet   | Cloud Router with Cloud NAT, an Interconnect attachment, or a BGP peer; VPN gateway (HA or Classic) |
| Active peering                     | VPC peering                                                                                                                          | Connected VNet peering                                                                      | Active VPC peering                                                                       |
| Compute or load balancing deployed | Instance; any managed network interface (load balancer, NAT gateway, Lambda, endpoint, Transit Gateway attachment). An unattached plain network interface does not count | Virtual machine, load balancer, Application Gateway                                         | Instance, load-balancer forwarding rule                                                  |
| Service connectivity               | Private Link service or endpoint                                                                                                     | Subnet with service delegation, private endpoint, or Private Link service; DNS linkage      | Private Service Connect endpoint or service; Serverless VPC Access connector             |

!!! info

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

## License Consumption Overview

The [License Consumption Overview](../IP_Fabric_Settings/administration/license_consumption_overview.md) displays a breakdown of license consumption.

## Add-on Licenses

Some capabilities are licensed separately from the device count. They are enabled
through an **additional feature** entry in the product license file, and each such
entry carries its own validity period. Until a license containing the entry is
uploaded, the capability is not available -- there is no setting or switch in the
product that turns it on.

### Application Infrastructure Mapping (AIM)

Application Infrastructure Mapping requires the **AIM feature** to be enabled in
the uploaded product license.

- The AIM feature has **its own validity period**, which sits within the
  license's overall validity. It **cannot extend beyond the product license's
  expiration date**, but it can be shorter -- which is how an AIM trial period is
  issued.
- Because that period can be shorter, AIM can expire -- or not have started yet
  -- while the rest of the license remains perfectly valid.
- AIM is available only when the product license is valid **and** the current
  date falls within the AIM feature's validity period. Both conditions have to
  hold, so the feature never outlives the product license.
- **All AIM functionality in the product is gated by this feature license.**
  Without it:
    - the **Application mapping** section is hidden from the Discovery Settings;
    - **Inventory --> Applications** shows an overview of the capability instead
      of the inventory tables;
    - the AIM API endpoints return `403`;
    - the path-lookup address fields stop suggesting application and workload
      names, and match IP addresses and DNS names only.

### Getting AIM

AIM is a **premium add-on**. For what it covers, see
[go.ipfabric.io/aim](https://go.ipfabric.io/aim), or the
[Application Infrastructure Mapping (AIM)](application_infrastructure_mapping.md)
overview in this documentation.

To add or renew it, contact your **Customer Success Manager** or email
[support@ipfabric.io](mailto:support@ipfabric.io), then upload the reissued
license file.

The product shows the same guidance in place of the feature: without the AIM
license, **Inventory --> Applications** displays a **Premium add-on** page
carrying the link and contact details above. See
[Without an AIM License](../IP_Fabric_GUI/inventory/applications.md#without-an-aim-license).

## Changes

### Release `8.2.0`

- An empty VPC, VNet, or VPC Network is billed at 0 CCU (Tier C). See
  [Empty VPC, VNet, or VPC Network](#empty-vpc-vnet-or-vpc-network) above.
- Direct Connect gateways and internet gateways (AWS), and Route Servers
  (Azure), are Tier B (0.5 CCU). ExpressRoute gateways and ExpressRoute-type Virtual Network
  gateways (Azure) are Tier C (0 CCU).

### Release `8.1.0`

Starting from version `8.1.0`, licenses can use the new CCU cloud licensing
strategy instead of counting cloud constructs against the on-premises device
limit. See [Cloud Licensing](#cloud-licensing) above.
Device-based licenses -- including all licenses issued before `8.1.0` --
continue to count cloud constructs against the device limit.

### Release `7.3.16`

Starting from version `7.3.16`, when Aruba Instant Access Points (IAPs) are already managed by Aruba Central, discovering their Virtual Controller (VC) will no longer consume a license.

## Expired License

When your license expires:

- You will not be able to log in to the IP Fabric main GUI.
- New snapshots will not be created, and automatic snapshots will stop.
- API calls may still work.
- Configuration management will run in the background.

An expired **feature** license behaves differently: only that capability becomes
unavailable, and the rest of the platform is unaffected. If the AIM feature's
validity period ends while the product license is still valid, AIM simply stops
being accessible -- see [Add-on Licenses](#add-on-licenses).
