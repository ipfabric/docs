---
description: This section is about the Routing technology tables in the IP Fabric GUI.
---

# Routing

## Prefix Lists

The **Prefix lists** section contains definitions of all prefix lists.

There are 2 tabs according to the address family:

- **IPv4**
- **IPv6**

## Routing Policy

The **Routing policy** section contains information about routing policies, their definitions, and where they are applied.

There are 3 tabs:

- **Routing Policies**
- **PBR Interfaces**
- **Policy Based Routing**

### Routing Policies

The **Routing Policies** tab contains definitions of routing policies, their names, sequence numbers, matching conditions, set actions, etc.

In case the match condition uses a reference to an ACL or Prefix list, it is hyperlinked to the appropriate ACL/Prefix list in its section.

![Routing Policies](../../images/technology/IP_Fabric_GUI-technology_tables-routing-routingPolicy_routingPolicies.webp)

### PBR Interfaces

The **PBR Interfaces** tab contains information about interfaces that have some routing policy assigned on them (used for policy-based routing). Optionally, there is also information about the used address family or status of the routing policy.

![PBR Interfaces](../../images/technology/IP_Fabric_GUI-technology_tables-routing-routingPolicy_pbrInterfaces.webp)

### Policy Based Routing

The **Policy Based Routing (PBR)** tab contains matching conditions for traffic and what actions should be applied to packets that match those conditions. All PBR actions are present in the `PBR Actions` column.

In case the match condition uses a reference to an ACL, it is hyperlinked to the appropriate ACL list in its section.

![Policy Based Routing](../../images/technology/IP_Fabric_GUI-technology_tables-routing-routingPolicy_policyBasedRouting.webp)

Clicking `Policy Name` opens a tree view.

![PBR Tree](../../images/diagrams/to-be-checked-IP_Fabric_GUI-technology_tables-routing-routingPolicy_pbrTree.webp)

Policy-based routing rules are now also applied to packets in end-to-end path diagrams.

Selecting PBR's name in a decision table opens a tree view with the highlighted rule that matched the packet and decided that the PBR action should be applied.

!!! Note

    Currently, only IP-based policy-based routing nexthops are supported.

![PBR Decision Table](../../images/diagrams/to-be-checked-IP_Fabric_GUI-technology_tables-routing-routingPolicy_pbrDecisionTable.webp)

![PBR Decision Tree](../../images/diagrams/to-be-checked-IP_Fabric_GUI-technology_tables-routing-routingPolicy_pbrDecisionTree.webp)
