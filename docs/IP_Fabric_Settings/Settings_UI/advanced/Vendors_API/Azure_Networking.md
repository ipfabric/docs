# Azure Networking

Starting version 4.3 IP Fabric supports the discovery of the Azure Cloud
infrastructure.

Azure devices are discovered only through API.

To add Azure devices to discovery global settings, go to **Settings →
Advanced → Vendors API** and press **the +Add** button

To discover Azure devices, a subscription ID, tenant ID, client
(application) ID, and client secret are needed.

The IP Fabric covers the IaaS (Infrastructure as a Service) part of the
cloud. Azure Cloud Compute provides an abstract view of the Azure
physical infrastructure.

**Following Azure elements are supported:**

-   Virtual Network
    (<https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview>)

-   NAT Gateway
    (<https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-gateway-resource>)

-   Virtual Network Gateway (both types: VPN
    <https://docs.microsoft.com/en-us/azure/vpn-gateway/> and
    ExpressRoute
    <https://docs.microsoft.com/en-us/azure/expressroute/expressroute-about-virtual-network-gateways>)

and devices related to a Virtual WAN solution
(<https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about>):

-   Virtual HUB

-   VPN Gateway (the same functionality as VNGw type VPN)

-   ExpressRoute Gateway (the same functionality as VNGw type
    ExpressRoute)

The plan is to add support of Load Balancer
(<https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview>
) in one of next releases.
