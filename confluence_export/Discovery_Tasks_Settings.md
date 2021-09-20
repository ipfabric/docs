# Discovery Tasks Settings

The Discovery tasks feature was first introduced in **IP Fabric version
3.5.2** as a fast discovery enablement for large scale networks. When
enabled, it will use current ‘Discovery History’ database (in Management
\> Discovery History) only when creating a new snapshot **without
detecting any new network devices** during the discovery process.

If limit is disabled and discovery crawl through whole network is
performed, you can choose which options will be used for new devices
detection (ARP, CDP/LLDP, Routing Table records or a Traceroute).
Default is to use all available options.

<img src="attachments/1157136385/1157300225.png?width=387" class="image-left" loading="lazy" data-image-src="attachments/1157136385/1157300225.png" data-height="134" data-width="610" data-unresolved-comment-count="0" data-linked-resource-id="1157300225" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200519-145530.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1157136385" data-linked-resource-container-version="5" data-media-id="1575dc54-4acc-43d1-8b17-d243b1b1980c" data-media-type="file" width="387" />

The feature is especially helpful for large complex networks with
already defined device scope to avoid multiple repetitive failed
SSH/Telnet attempts that may slow down snapshot creation.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200519-145530.png](attachments/1157136385/1157300225.png)
(image/png)  

</div>
