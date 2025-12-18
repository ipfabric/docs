---
description: The Load Balancing section provides information about load balancing configurations on the network.
---

# Load Balancing

The Load Balancing section provides information about load balancing configurations on the network.

## Virtual Servers

The **Virtual Servers** table displays load balancer configuration details, including virtual server names, virtual IP addresses (VIPs), availability states, and associated pools. 
Each entry shows port and protocol details, pool membership counts, and advanced settings like source NAT and VRF assignments.

![Virtual Servers](LOAD_BALANCING/IP_Fabric_GUI-technology_tables-load-balancing_virtual_servers.webp)

## Virtual Servers - Pools

The **Virtual Servers - Pools** table provides detailed information about backend pools associated with each load balancer. 
It displays pool names, member counts, and individual pool members by hostname or IP address.

![Virtual Servers Pools](LOAD_BALANCING/IP_Fabric_GUI-technology_tables-load-balancing_virtual_servers_pools.webp)

## Virtual Servers - Pool Members

The **Virtual Servers - Pool Members** table shows individual pool member details, including backend endpoints such as VMs or FQDNs.
It displays member names, IP addresses (both IPv4 and IPv6), port numbers, and operational status, including availability (up/down) and state (enabled/disabled).

![Virtual Servers Pool Members](LOAD_BALANCING/IP_Fabric_GUI-technology_tables-load-balancing_virtual_servers_pool_members.webp)

## Virtual Servers - Partitions

The **Virtual Servers - Partitions** table displays partition names and descriptions.
