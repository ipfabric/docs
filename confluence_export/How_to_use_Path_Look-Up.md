# How to use Path Look-Up

# How to use Path Look-Up

## Unicast Path-Lookup

<img src="attachments/2548858900/2551480336.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2548858900/2551480336.png" data-height="532" data-width="380" data-unresolved-comment-count="0" data-linked-resource-id="2551480336" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-132637.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="754f1f19-dd1c-4a41-ae3d-99ffa7806b6c" data-media-type="file" />

Enter the details:

-   Source IP / CIDR (it can be a network, but the total number of IPs
    has to be less than 255 including source and destination IPs.
    Subnets are also supported.)

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

<img src="attachments/2548858900/2551087161.png?width=442" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551087161.png" data-height="428" data-width="1557" data-unresolved-comment-count="0" data-linked-resource-id="2551087161" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-135636.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="a9aeb16a-bdf2-4b89-b08b-385cd0fc9fc4" data-media-type="file" width="442" />

## Path Controls

<img src="attachments/2548858900/2613673995.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2613673995.png" data-height="538" data-width="1062" data-unresolved-comment-count="0" data-linked-resource-id="2613673995" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210629-134606.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="2586b41c-aa87-46f5-9af6-f7a3ee9553d1" data-media-type="file" width="340" /><img src="attachments/2548858900/2764079122.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2764079122.png" data-height="921" data-width="1688" data-unresolved-comment-count="0" data-linked-resource-id="2764079122" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211001-144734.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="d61b3a3c-9a79-4229-9454-08745f6bbe2b" data-media-type="file" width="340" />

## Understand the path selection

To understand the decision taken by a device, right-click on the device
and “show detail”. You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then in the middle of the table, you will see the
forwarding decision:

<img src="attachments/2548858900/2764996611.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2764996611.png" data-height="552" data-width="1181" data-unresolved-comment-count="0" data-linked-resource-id="2764996611" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211001-145019.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="b4b00586-a031-4fc4-9bd9-81ac4a574bc0" data-media-type="file" width="340" />

In this example, we are looking at the device L33R4, which has 2
incoming interfaces and one forwarding for this flow:

<img src="attachments/2548858900/2551054367.gif?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551054367.gif" data-height="730" data-width="1254" data-unresolved-comment-count="0" data-linked-resource-id="2551054367" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="E2E-doc-02.gif" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/gif" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="b4399477-c1f6-4e09-a3c0-46628af6da46" data-media-type="file" width="340" />

## Multicast Tree Look-Up

You want to understand how a certain multicast flow is used, you can use
the Multicast Tree Look-Up. For that, just select the correct option and
enter the relevant details

<img src="attachments/2548858900/2551611428.png?width=108" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551611428.png" data-height="506" data-width="392" data-unresolved-comment-count="0" data-linked-resource-id="2551611428" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-150903.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="ad9bf05f-aaf9-418c-8ad1-d8800f17b9c9" data-media-type="file" width="108" />

You will then see the Multicast Tree:

<img src="attachments/2548858900/2548826136.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548826136.png" data-height="376" data-width="968" data-unresolved-comment-count="0" data-linked-resource-id="2548826136" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151011.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="1e281835-29ac-4a13-a019-979b7f451338" data-media-type="file" width="340" />

And you will have access to a lot of information regarding the Multicast
forwarding decision:

<img src="attachments/2548858900/2548858922.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548858922.png" data-height="430" data-width="1079" data-unresolved-comment-count="0" data-linked-resource-id="2548858922" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151130.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="3f7dc9da-7a18-44f6-ae11-bab2f0b233f0" data-media-type="file" width="340" />

## Host To Gateway

To find out more details between a host and its network gateway, you can
use this menu: Host To Gateway. You only need to provide the host, and
you will the details:

<img src="attachments/2548858900/2765193233.png?width=340" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2765193233.png" data-height="720" data-width="1650" data-unresolved-comment-count="0" data-linked-resource-id="2765193233" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211001-145307.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="e2b34996-824c-43ac-a441-76f637c848cb" data-media-type="file" width="340" />

## Visualization Setup

You can set up what you want to prioritize in the view. Just simply move
the bars up or down.

<img src="attachments/2548858900/2758705153.png?width=102" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2758705153.png" data-height="391" data-width="308" data-unresolved-comment-count="0" data-linked-resource-id="2758705153" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Visualization_Setup.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="15" data-media-id="9ef9b619-adf1-4b0a-aa4f-dd718992f74e" data-media-type="file" width="102" />

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
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Visualization_Setup.png](attachments/2548858900/2758705153.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-144714.png](attachments/2548858900/2762899480.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-144719.png](attachments/2548858900/2764800005.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-144734.png](attachments/2548858900/2764079122.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-145019.png](attachments/2548858900/2764996611.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-145300.png](attachments/2548858900/2765193227.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211001-145307.png](attachments/2548858900/2765193233.png)
(image/png)  

</div>
