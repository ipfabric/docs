---
description: The Vendors section provides vendor-specific inventory tables for three cloud providers - AWS, GCP, and Azure.
---

# Vendors

The **Vendors** section provides vendor-specific inventory tables for three cloud providers -- AWS, GCP, and Azure.
Each vendor's inventory table presents slightly different information to reflect the unique characteristics of their resources.

![Technology table showing Vendors](../../../images/technology/cloud/technology-cloud_vendors.webp){: width="200" .center}

## AWS

AWS's inventory table offers the Amazon Resource Name (ARN), resource type, resource ID, owner ID, and region.

![Technology table showing GCP Inventory](../../../images/technology/cloud/technology-cloud_vendors-aws-inventory.webp)

The Scaling Group table shows details of scaling groups including names, ARNs, number of virtual machines, instance types, target group ARNs, launch template and launch template versions.

![Technology table showing AWS Scaling Groups](../../../images/technology/cloud/technology-cloud_vendors-aws-scaling-groups.webp)

The Subnets table shows details of subnets such as their VPC ID, name, IP ranges, route table ID, availability zone, ARN, and whether the subnet is public.

![Technology table showing AWS subnets](../../../images/technology/cloud/technology-cloud_vendors-aws-subnets.webp)

The Private Link VPC Endpoints table provides detailed information, including the Name, IPv4 and IPv6 addresses, a link to the related subnet, the state, the service type, and the service ID.

![Technology table showing VCP Endpoints](../../../images/technology/cloud/technology-cloud_vendors-aws-private-link-endpoints.webp)

## Azure

Azure's Inventory table provides the serial number, subscription ID, subscription name, resource group, location, and SKU.

![Technology table showing Azure Inventory](../../../images/technology/cloud/technology-cloud_vendors-azure-inventory.webp)

The Virtual Machine Scale Sets table provides information about scale sets including the names, IDs, number of virtual machines in the set, instance type and orchestration mode.

![Technology table showing Azure Virtual Machine Scale Sets](../../../images/technology/cloud/technology-cloud_vendors-azure-virtual-machine-scale-sets.webp)

The Subnets table provides information about subnets, including the VNet ID, Name, IPv4 and IPv6 address ranges, a link to the list of related private
service endpoints, the routing table ID, the associated NAT gateway ID, the service to which the subnet is delegated, and whether default outbound access is enabled.

![Technology table showing Azure subnets](../../../images/technology/cloud/technology-cloud_vendors-azure-subnets.webp)

The Service Endpoints table provides information about Azure service endpoints, covering the subnet, service name, state, location, and scope (service endpoint policy).

![Technology table showing Azure Service Endpoints](../../../images/technology/cloud/technology-cloud_vendors-azure-service-endpoints.webp)

The Private Link table provides information about private link endpoints, private link services, and their connections.
It contains three tabs: one for private endpoints, one for private link services, and one for private link service connections.

![Technology table showing Azure Private Link](../../../images/technology/cloud/technology-cloud_vendors-azure-private-link.webp)

The VNet Integration table provides information about resources that are enabled for VNet integration. It contains three tabs: App Services, Container Apps, Flexible Servers and SQL Managed Instances

![Technology table showing Azure VNet Integration](../../../images/technology/cloud/technology-cloud_vendors-azure-vnet-integration.webp)

The DNS table provides information about DNS configuration. It contains five tabs: VNet DNS Configuration, Private Resolvers, Private Resolver Endpoints, Forwarding Rulesets, and Forwarding Rules.

![Technology table showing Azure DNS Configuration](../../../images/technology/cloud/technology-cloud_vendors-azure-dns-vnet.webp)
![Technology table showing Azure DNS Private Resolvers](../../../images/technology/cloud/technology-cloud_vendors-azure-dns-private-resolver.webp)
![Technology table showing Azure DNS Private Resolvers Endpoints](../../../images/technology/cloud/technology-cloud_vendors-azure-dns-resolvers-endpoints.webp)
![Technology table showing Azure DNS Forwarding Rulesets](../../../images/technology/cloud/technology-cloud_vendors-azure-dns-forwarding-rulesets.webp)
![Technology table showing Azure DNS Forwarding Rules](../../../images/technology/cloud/technology-cloud_vendors-azure-dns-forwarding-rulesets-rules.webp)

## GCP (Google Cloud Platform)

Google Cloud Platform's Inventory table contains the full resource name, project, and region.

![Technology table showing GCP Inventory](../../../images/technology/cloud/technology-cloud_vendors-gcp-inventory.webp)

The Instance & Network Endpoint Groups table contains details about managed and unmanaged instance groups and network endpoint groups,
including names, IDs, states, number of virtual machines (where available/applicable), instance types (where available/applicable), types of groups, lists of endpoints in the
groups, zones, regions, minimum and maximum numbers of endpoints in the groups, and auto-scaling information.

![Technology table showing GCP Instance & Network Endpoint Groups](../../../images/technology/cloud/technology-cloud_vendors-gcp-instance-network-endpoint-groups.webp)

The Subnets table provides information about the associated VPC ID, the subnet’s name, the subnet’s range name, the IPv4 and IPv6 address ranges, the region, and whether Private Google Access
for private IPs is enabled.

![Technology table showing GCP Subnets](../../../images/technology/cloud/technology-cloud_vendors-gcp-subnets.webp)

The Private Service Connect tables provide detailed information about Endpoints, Published Services, and Published Service Connections in separate tabs.

![Technology table showing GCP Published Services in Private Service Connect](../../../images/technology/cloud/technology-cloud_vendors-gcp-private-service-connect.webp)

The Serverless Services tables provide information about App Engine, Cloud Functions, and Cloud Run services that use VPC Access Connectors.

![Technology table showing GCP Serverless Services](../../../images/technology/cloud/technology-cloud_vendors-gcp-serverless-services.webp)
