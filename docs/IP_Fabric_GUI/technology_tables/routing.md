---
description: This section is about Routing technology tables in IP Fabric GUI.
---

# Routing

## Prefix Lists

The **Prefix lists** section contains definitions of all prefix lists.

There are 2 tabs according to address family:

- **IPv4**
- **IPv6**

## Routing policy

The **Routing policy** section contains information about routing policies, their definitions and where they are applied.

There are 3 tabs:

- **Routing Policies**
- **PBR Interfaces**
- **Policy Based Routing**

### Routing Policies

The **Routing Policies** tab contains definitions of routing policies, their names, sequence numbers, matching conditions, set actions etc.

In case match condition uses reference to ACL or Prefix list, it is a hyperlink to appropriate ACL/Prefix list in its section.

![Routing Policies](routing/routingPolicy/routingPolicies.png)

### PBR Interfaces

The **PBR Interfaces** tab contains information about interfaces which have assigned some routing policy on them (used for policy-based routing). Optionally, there is also information about used address family or status of routing policy.

![PBR Interfaces](routing/routingPolicy/pbrInterfaces.png)

### Policy Based Routing

The **Policy Based Routing (PBR)** tab contains matching conditions for traffic and what actions should be applied on packets that match those conditions. All PBR actions are present in a PBR Actions column.

In case match condition uses reference to ACL, it is a hyperlink to appropriate ACL list in its section.

![Policy Based Routing](routing/routingPolicy/policyBasedRouting.png)

Clicking `Policy Name` opens tree view.

![PBR Tree](routing/routingPolicy/pbrTree.png)

Policy based routing rules are now also applied for packets in end-to-end path diagrams.

Selecting PBR's name in a decision table opens a tree view with the highlighted rule that matched the packet and decided that the PBR action should be applied.

!!! Note

    Currently, only IP-based policy-based routing nexthops are supported.

![PBR Decision Table](routing/routingPolicy/pbrDecisionTable.png)

![PBR Decision Tree](routing/routingPolicy/pbrDecisionTree.png)
