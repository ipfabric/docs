# Snapshots

## Snapshots

For ***[change management](Changes)***, regularly running IP Fabric
discovery is necessary. A periodic discovery run can be scheduled
at ***Settings → Advanced → Snapshots → Timed Snapshots.***

Here is an example for an automatic discovery run at 10 minutes past
every hour (0:10; 1:10; 2:10; 3:10, etc.).

<img src="attachments/102367300/102564017.png" loading="lazy" data-image-src="attachments/102367300/102564017.png" data-unresolved-comment-count="0" data-linked-resource-id="102564017" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-27 09_37_26-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102367300" data-linked-resource-container-version="8" data-media-id="fead4362-1705-48fb-b01d-0f89898e82a4" data-media-type="file" />

**How scheduling work in IPF:**

Let's assume that snapshot is scheduled for every hour and snapshot
takes 4h:20min to be created, then the next snapshot will be scheduled
once the previous snapshot finishes. The scheduled time will be set at
the next possible period according to the cron setup.

<img src="attachments/102367300/1405059074.jpg?height=250" loading="lazy" data-image-src="attachments/102367300/1405059074.jpg" data-unresolved-comment-count="0" data-linked-resource-id="1405059074" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="IPF-cron.jpg" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="102367300" data-linked-resource-container-version="8" data-media-id="e223cd7a-d146-40f6-8da3-c853b5747730" data-media-type="file" height="250" />

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-27 09_37_26-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/102367300/102564017.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[IPF-cron.jpg](attachments/102367300/1405059074.jpg) (image/jpeg)  

</div>
