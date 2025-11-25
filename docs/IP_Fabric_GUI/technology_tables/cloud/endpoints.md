---
description: Public or private cloud APIs provide information about virtual machines. From version 4.4, IP Fabric displays information about virtual machines discovered through private or public cloud APIs.
---

# Endpoints

Public and private cloud APIs provide information about virtual machines. Previously, IP Fabric was unable to collect information about virtual machines. However, starting from version `4.4`, IP Fabric displays information about virtual machines discovered through these APIs. 

Each vendor provides a different scope of information for VMs, so IP Fabric may not be able to retrieve all the necessary data for end-host calculations (such as ARP or MAC address tables).

The **Virtual Machines** tab provides detailed information about cloud virtual machines, including their hostnames, sites, VM names, status, OS versions, number of interfaces, and endpoint group names (if the information is available).

![Technology table showing Cloud endpoints virtual machines](../../../images/technology/IP_Fabric_GUI-technology_tables-cloud_endpoints_virtual_machines.webp)

The **Virtual Machine Interfaces** tab provides detailed information about the interfaces of each cloud virtual machine, including interface names, interface IDs, MAC addresses, IPv4 addresses, public IPv4 addresses, and inbound and outbound ACLs.

![Technology table showing Cloud endpoints virtual machines interfaces](../../../images/technology/IP_Fabric_GUI-technology_tables-cloud_endpoints_virtual_machines_interfaces.webp)

The **Endpoint Groups** tab provides detailed information about cloud endpoint groups, including group names, IDs, states, number of VMs in the group (if the information is available), and types of VM instances.

![Technology table showing Cloud endpoints endpoint groups](../../../images/technology/IP_Fabric_GUI-technology_tables-cloud_endpoints_endpoint_groups.webp)

