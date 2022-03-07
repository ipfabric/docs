# Support VPN

Starting IP Fabric version 1.0.3 customer is able to establish remote
SSL VPN to IP Fabric DC. Support VPN uses OpenVPN software.

<div>

Network requirements

<div>

Support VPN requires access to
*[remote.ipfabric.io](http://remote.ipfabric.io)* (194.228.111.174)
remote port 443/TCP. IP Fabric image must be also configured with
functional DNS server.

Connection through proxy servers is also supported but not guaranteed.

</div>

</div>

## How to establish support VPN​

<div>

Security tip

<div>

VPN is always established and teared down by customer. VPN connection
cannot be triggered externally! 

</div>

</div>

1.  Login to IP Fabric web ui.

2.  At top right corner click *Support.*

3.  Select *Remote support VPN.*  
    <img src="attachments/1878327298/1877737482.png" loading="lazy" data-image-src="attachments/1878327298/1877737482.png" data-unresolved-comment-count="0" data-linked-resource-id="1877737482" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="supp-vpn1.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327298" data-linked-resource-container-version="2" data-media-id="55b81055-ea41-42e5-ba98-8e88f79c8a20" data-media-type="file" />  
      

4.  On newly opened page click the *Connect* button.  
    <img src="attachments/1878327298/1877737486.png" loading="lazy" data-image-src="attachments/1878327298/1877737486.png" data-unresolved-comment-count="0" data-linked-resource-id="1877737486" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="supp-vpn2.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327298" data-linked-resource-container-version="2" data-media-id="161e22ad-990f-4c27-96e5-aedd102f672e" data-media-type="file" />  
      

5.  VPN status should change to connected and also you should see
    assigned IP address.

## How to tear down support VPN​

1.  Repeat steps 1 - 3 from *How to establish support VPN*​ part (see
    above)
2.  On newly opened page click the Disc*onnect* button.
3.  VPN status should change to disconnected.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[supp-vpn1.png](attachments/1878327298/1877737482.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[supp-vpn2.png](attachments/1878327298/1877737486.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[supp-vpn3.png](attachments/1878327298/1877737490.png) (image/png)  

</div>
