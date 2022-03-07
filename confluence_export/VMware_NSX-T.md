# VMware NSX-T

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

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211118-105748.png?version=1&modificationDate=1637233072856&cacheVersion=1&api=v2&width=204&height=135](attachments/2903408680/2904490009)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Snímek
obrazovky 2022-02-21
v 15.42.08.png](attachments/2903408680/2904195089.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Snímek
obrazovky 2022-02-21
v 15.42.08.png](attachments/2903408680/2904653834.png) (image/png)  

</div>
