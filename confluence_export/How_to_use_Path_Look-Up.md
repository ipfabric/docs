# How to use Path Look-Up

# How to use Path Look-Up

## Unicast Path-Lookup

<img src="attachments/2548858900/2551480336.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2548858900/2551480336.png" data-height="532" data-width="380" data-unresolved-comment-count="0" data-linked-resource-id="2551480336" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-132637.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="754f1f19-dd1c-4a41-ae3d-99ffa7806b6c" data-media-type="file" />

Enter the details:

-   Source IP / CIDR (it can be a network, but the total number of IPs
    has to be less than 255 including source and destination IPs)

-   Port (Source Port)

-   VRF (Virtual Routing and Forwarding Instance)

-   Destination IP / CIDR

-   Port (Destination Port)

-   Protocol: TCP/UDP/ICMP

-   Flags: None/ACK/FIN/SYN/RST/PSH/URG

If you’ve used a network instead of a single IP, you will have the
option between:

– **Network Mode**: simulation stats and ends with whole networks,
individual hosts are not considered

– **Host Mode**: simulation starts and ends with each host. It is
limited to 255 hosts, source and destination combined.

Then click on submit:

<img src="attachments/2548858900/2551087161.png?width=680" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551087161.png" data-height="428" data-width="1557" data-unresolved-comment-count="0" data-linked-resource-id="2551087161" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-135636.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="a9aeb16a-bdf2-4b89-b08b-385cd0fc9fc4" data-media-type="file" width="680" />

## Path Controls

<img src="attachments/2548858900/2613673995.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2613673995.png" data-height="538" data-width="1062" data-unresolved-comment-count="0" data-linked-resource-id="2613673995" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210629-134606.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="2586b41c-aa87-46f5-9af6-f7a3ee9553d1" data-media-type="file" /><img src="attachments/2548858900/2615345159.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2615345159.png" data-height="851" data-width="1233" data-unresolved-comment-count="0" data-linked-resource-id="2615345159" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210629-134859.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="7949f35b-d6f0-449b-aa49-ed43077953ca" data-media-type="file" />

## Understand the path selection

To understand the decision taken by a device, right-click on the device
and “show detail”. You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then in the middle of the table, you will see the
forwarding decision:

<img src="attachments/2548858900/2551054377.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551054377.png" data-height="379" data-width="939" data-unresolved-comment-count="0" data-linked-resource-id="2551054377" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-145508.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="5bd04bbf-67e2-4775-b0eb-2f1d96b45c71" data-media-type="file" />

In this example, we are looking at the device L33R4, which has 2
incoming interfaces and one forwarding for this flow:

<img src="attachments/2548858900/2551054367.gif?width=680" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551054367.gif" data-height="730" data-width="1254" data-unresolved-comment-count="0" data-linked-resource-id="2551054367" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="E2E-doc-02.gif" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/gif" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="b4399477-c1f6-4e09-a3c0-46628af6da46" data-media-type="file" width="680" />

## Multicast Tree Look-Up

You want to understand how a certain multicast flow is used, you can use
the Multicast Tree Look-Up. For that, just select the correct option and
enter the relevant details

<img src="attachments/2548858900/2551611428.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2548858900/2551611428.png" data-height="506" data-width="392" data-unresolved-comment-count="0" data-linked-resource-id="2551611428" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-150903.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="ad9bf05f-aaf9-418c-8ad1-d8800f17b9c9" data-media-type="file" width="340" />

You will then see the Multicast Tree:

<img src="attachments/2548858900/2548826136.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548826136.png" data-height="376" data-width="968" data-unresolved-comment-count="0" data-linked-resource-id="2548826136" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151011.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="1e281835-29ac-4a13-a019-979b7f451338" data-media-type="file" />

And you will have access to a lot of information regarding the Multicast
forwarding decision:

<img src="attachments/2548858900/2548858922.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548858922.png" data-height="430" data-width="1079" data-unresolved-comment-count="0" data-linked-resource-id="2548858922" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151130.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="3f7dc9da-7a18-44f6-ae11-bab2f0b233f0" data-media-type="file" />

## Host To Gateway

To find out more details between a host and its network gateway, you can
use this menu: Host To Gateway. You only need to provide the host, and
you will the details:

<img src="attachments/2548858900/2551644179.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551644179.png" data-height="675" data-width="1242" data-unresolved-comment-count="0" data-linked-resource-id="2551644179" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151356.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="a36dc075-0b08-4fe4-8fc4-a4524e94514a" data-media-type="file" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-132637.png](attachments/2548858900/2551480336.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-135636.png](attachments/2548858900/2551087161.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-135841.png](attachments/2548858900/2551676955.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[E2E-doc-02.gif](attachments/2548858900/2551054367.gif) (image/gif)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-145444.png](attachments/2548858900/2551480347.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-145508.png](attachments/2548858900/2551054377.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-150741.png](attachments/2548858900/2550923289.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-150822.png](attachments/2548858900/2551414811.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-150903.png](attachments/2548858900/2551611428.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-150948.png](attachments/2548858900/2551021598.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-151011.png](attachments/2548858900/2548826136.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-151057.png](attachments/2548858900/2551644173.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-151130.png](attachments/2548858900/2548858922.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-151356.png](attachments/2548858900/2551644179.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210629-134606.png](attachments/2548858900/2613673995.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210629-134859.png](attachments/2548858900/2615345159.png)
(image/png)  

</div>
