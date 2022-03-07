# 07 - Vendors API

<img src="attachments/2393342021/2393342031.png?width=113" class="image-center" loading="lazy" data-image-src="attachments/2393342021/2393342031.png" data-height="198" data-width="497" data-unresolved-comment-count="0" data-linked-resource-id="2393342031" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210513-232501.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2393342021" data-linked-resource-container-version="3" data-media-id="17359542-f9ec-43b3-8d38-3f1b6fd48cf0" data-media-type="file" width="113" />

## Cisco Meraki

Starting the version 3.5.0, IP Fabric supports API based discovery for
Cisco Meraki.

Meraki requires the following settings to be applied:

-   API key - Generated in [Meraki
    dashboard](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API)

-   Organizations ID - You can specify which organization will be
    included in the discovery process. If you do not specify, all
    available IDs will be used

-   Version - Meraki currently provides only a v0 version of their API.
    This version has a lot of limitations ([Meraki known
    issues](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/968032257/Meraki))

-   Base URL - URL is supported in the following
    format [https://nXYZ.meraki.com/api.](https://nXYZ.meraki.com/api) Be
    aware that the dashboard can redirect communication to a different
    URL

## Check Point

<div>

<div>

We use API only to collect information that cannot be retrieved from CLI
logs.

To discover CheckPoint devices, CLI access also needs to be available.

</div>

</div>

Checkpoint requires the following settings to be applied:

-   API Key - Available in version R80.40 and above (API v1.6). To
    generate the key, use CheckPoint SmartConsole, and select "API Key"
    as user's Authentication method  
    **or**

-   Username - Username to access API data

-   Password - Password to access API data  

-   Base URL - Base URL for API calls
    (ie: [https://management.server.domain.tld).](https://management.server.domain.tld) If
    the API isn't available on the default port 443, add a port part to
    the URL (ie: <https://server:4443/>)

-   Collect following domains - Mandatory only if the "Base URL" points
    to a Multi-Domain Server. Please verify, that all selected domains
    can be accessed by the provided credentials.  

Don't forget to add IPF appliance to the list of allowed clients. In
SmartConsole, go to Manage & Settings \> Blades and click on "Advanced
Settings..." in the “Management API“ section to verify, from where are
API calls allowed. In case that you use setting "All IP addresses that
can be used for GUI clients", don't forget to add IPF appliance address
to Manage & Settings \> Permissions & Administrators \> Trusted Clients.
In case you use Multi-Domain server, all necessary settings are in Multi
Domain menu (ie: Multi Domain \> Blades)

## Versa Networks SD-WAN

Starting version 3.8.0 IP Fabric supports Versa SD-WAN API. API is based
on HTTPS authentication. Versa requires the following settings to be
applied:

-   Username - Username to Versa Director to access API data

-   Password - Password to Versa Director access API data

-   Base URL - Base URL of Versa Director. If the API isn't available on
    the default port 9182, add a port part to the URL (ie:
    <https://server:4443/>)

<div>

<div>

OAuth authentication credentials to Versa Director are not supported at
the moment to access API  

</div>

</div>

# AWS (Amazon Web Services)

Starting version 3.8.0 IP Fabric supports AWS API.

To add AWS to the discovery you will need an access key & secret access
key from your AWS account.

Those keys can be found/generated under your account in the AWS
dashboard.

<img src="attachments/2691563521/2691596295.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596295.png" data-height="345" data-width="1676" data-unresolved-comment-count="0" data-linked-resource-id="2691596295" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (8).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="e1a158d2-3d1b-41b0-9ffe-ccecea18f047" data-media-type="file" width="340" />

Click on “My Security Credentials” and open “Access keys” tab.

<img src="attachments/2691563521/2691596301.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596301.png" data-height="756" data-width="1694" data-unresolved-comment-count="0" data-linked-resource-id="2691596301" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (10).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="d120ae20-ebe5-4241-b2e5-42728b98f30b" data-media-type="file" width="340" />

To generate keys click on “Create New Access Key” and your keys will be
generated. These access keys are available globally for all of yours AWS
regions.

<img src="attachments/2691563521/2691596307.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596307.png" data-height="673" data-width="1679" data-unresolved-comment-count="0" data-linked-resource-id="2691596307" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image (11).png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="28eaf95c-1d5f-4667-aae3-d9ce15b24932" data-media-type="file" width="340" />

Copy those keys to the AWS API settings in your IP Fabric and don't
forget to **fill the region where the devices which you want to discover
are**.

<img src="attachments/2691563521/2691596313.png" class="image-left" loading="lazy" data-image-src="attachments/2691563521/2691596313.png" data-height="290" data-width="401" data-unresolved-comment-count="0" data-linked-resource-id="2691596313" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2021-05-04 165124.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="f6c00564-395f-4a9a-b509-b54f718cf3b5" data-media-type="file" />

<div>

<div>

To ensure that IP Fabric can retrieve all the required data to model the
AWS networks, a series of specific policies are required to be applied
to the user account or role used for the API key. The attached file
contains a JSON description of the required IAM policies:

</div>

</div>

[<img src="attachments/thumbnails/2691563521/2691399704" height="250" />](attachments/2691563521/2691399704.json)

# AWS AssumeRole

From version 4.3, IP Fabric enables you to add AssumeRole to AWS API
configuration. AssumeRole basically sets higher permissions that may be
required for the discovery process in some environments.

AssumeRole is a standard way how to obtain additional rights when
talking to AWS API. It returns a set of temporary security credentials
that you can use to access AWS resources that you might not normally
have access to. These temporary credentials consist of an access key ID,
a secret access key, and a security token. Typically, you use
`AssumeRole` within your account or for cross-account access. For more
information about AssumeRole see
<https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>

<img src="attachments/2691563521/2913828865.png" class="image-center" loading="lazy" data-image-src="attachments/2691563521/2913828865.png" data-height="537" data-width="603" data-unresolved-comment-count="0" data-linked-resource-id="2913828865" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Snímek obrazovky 2022-03-02 v 14.54.49.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2691563521" data-linked-resource-container-version="9" data-media-id="e41e6a4a-875d-49b0-b2a4-5a21b2408167" data-media-type="file" />

## Cisco Viptela SD-WAN

Starting version 4.1.0 IP Fabric supports Viptela API.

Viptela devices are discovered only through API.

To add Viptela to discovery global settings, go to **Settings → Advanced
→ Vendors API** and press **the +Add** button

Afterward, choose Viptela API from the list and fill in

-   **Username and password** used to log in to vManage

-   **Base URL** of vManage server (https://vmanage-ip-address)

  

## VMware NSX-T

Starting version 4.3 IP Fabric supports NSX-T API.

NSX-T devices are discovered only through API.

To add NSX-T to discovery global settings, go to **Settings → Advanced →
Vendors API** and press **the +Add** button

Afterward, choose NSX-T API from the list and fill in

-   **Username and password** used to log in to NSX Manager

-   **Base URL** of NSX Manager server
    ([https://nsx-manager-ip-address](https://vmanage-ip-address))

<img src="attachments/2903408680/2904653834.png?width=170" class="image-left" loading="lazy" data-image-src="attachments/2903408680/2904653834.png" data-height="402" data-width="603" data-unresolved-comment-count="0" data-linked-resource-id="2904653834" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Snímek obrazovky 2022-02-21 v 15.42.08.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2903408680" data-linked-resource-container-version="13" data-media-id="94f31b66-f6ef-4909-8ae4-1dd1d87e6ed5" data-media-type="file" width="170" />

#### General support information

-   IP Fabric is supporting NSX-T from version 3.0 and higher,
    development was done on version 3.1.2, the latest version is 3.2. We
    are not supporting the 2.x version, there are a lot of differences,
    Vmware’s end of general support was in September 2021.
    <https://lifecycle.vmware.com/#/>

-   NSX-T running as on-premise (there are also cloud versions for AWS
    and Azure, where can NSX-T cloud be deployed on top of AWS/Azure
    infrastructure ), but we don’t support it now

-   We don’t collect any data from vCenter, as NSX-T is multiplatform
    and supports KVM and bare metal servers as well, if those are
    connected to the NSX-T cloud, we will collect information about
    those also.

#### We are supporting those types of devices

-   Tier-0 router

-   Tier-1 router

    -   also supporting VRFs

#### Not supported features

-   Load balancing

-   All security features (IPS/IDS, Distributed FW, Gateway FW, Network
    introspection) - planned to add security features in upcoming
    releases

-   Forwarding policies - planned to add in upcoming releases

-   VPN services

-   NAT

-   EVPN Vxlans

#### External connectivity

We are supporting both external connectivity protocols, which are
implemented in NSX-T, and of course static routes. External connectivity
can be done only on Tier-0 routers.

-   OSPF

-   BGP

# Silver Peak SD-WAN

Starting version 4.3 IP Fabric supports the discovery of Silver Peak
(Aruba) EdgeConnect devices in router mode.

EdgeConnect devices are discovered only through API.

To add EdgeConnect to discovery global settings, go to **Settings →
Advanced → Vendors API** and press **the +Add** button

Afterward, choose Silver Peak from the list and fill in

-   **Username and password** to log in to Unity Orchestrator

<div>

<div>

if a user has just RO rights, ARP table will NOT be downloaded - this is
not supported by the orchestrator’s API

</div>

</div>

-   **Base URL** of Unity Orchestrator (https://unity-orchestrator-ip)

<img src="attachments/2910879777/2910552088.png" class="image-center" loading="lazy" data-image-src="attachments/2910879777/2910552088.png" data-height="414" data-width="620" data-unresolved-comment-count="0" data-linked-resource-id="2910552088" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220228-145552.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2910879777" data-linked-resource-container-version="5" data-media-id="16019121-583c-43a2-a76b-f45408bae994" data-media-type="file" />

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

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210513-232501.png](attachments/2393342021/2393342031.png)
(image/png)  

</div>
