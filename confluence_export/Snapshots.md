# Snapshots

## Snapshots

For [***change management***](Changes), regularly running IP Fabric
discovery is necessary. A periodic discovery run can be scheduled
at ***Settings → Advanced → Snapshots → Timed Snapshots.***

Here is an example for an automatic discovery run at *10 minutes past
every hour* (0:10; 1:10; 2:10; 3:10, etc.).

<img src="attachments/102367300/102564017.png" class="image-left" loading="lazy" data-image-src="attachments/102367300/102564017.png" data-height="182" data-width="487" data-unresolved-comment-count="0" data-linked-resource-id="102564017" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-27 09_37_26-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102367300" data-linked-resource-container-version="11" data-media-id="fead4362-1705-48fb-b01d-0f89898e82a4" data-media-type="file" />

**How scheduling work in IPF:**

Let's assume that snapshot is scheduled for every hour and snapshot
takes 4h:20min to be created, then the next snapshot will be scheduled
once the previous snapshot finishes. The scheduled time will be set at
the next possible period according to the cron setup.

<img src="attachments/102367300/1405059074.jpg?width=272" class="image-center" loading="lazy" data-image-src="attachments/102367300/1405059074.jpg" data-height="264" data-width="1011" data-unresolved-comment-count="0" data-linked-resource-id="1405059074" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="IPF-cron.jpg" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="102367300" data-linked-resource-container-version="11" data-media-id="e223cd7a-d146-40f6-8da3-c853b5747730" data-media-type="file" width="272" />

##  Snapshot Retention Rules (from version 4.1)

We added support for various snapshot retention policies in IP Fabric
version 4.1.

<img src="attachments/102367300/2790883329.png?width=346" class="image-center" loading="lazy" data-image-src="attachments/102367300/2790883329.png" data-height="782" data-width="1910" data-unresolved-comment-count="0" data-linked-resource-id="2790883329" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20211020-112725.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102367300" data-linked-resource-container-version="11" data-media-id="e57bb380-1733-460f-a67b-3291bf1c64ea" data-media-type="file" width="346" />

### How Does the Snapshot Retention Work

It works in two steps:

1.  If any of the “keep” rules are enabled, IP Fabric goes through
    unloaded snapshots and based on enabled “keep” rules it marks
    snapshots that will retain and those that will be deleted.

2.  HDD utilization and a number of unloaded snapshots are checked. If
    any of these rules are exceeded, the oldest unloaded snapshots are
    deleted.

Please note:

1.  HDD utilization and the number of snapshots have precedence over
    “keep” rules. This means that snapshots marked as retained by a
    “keep” rule can be deleted when the HDD utilization or number of
    snapshots are exceeded.

2.  When at least one retention rule is enabled, all snapshots not
    protected by them will be removed regardless of reaching HDD
    utilization or snapshots count limits.

3.  Loaded snapshots are not affected by these rules. It affects only
    unloaded snapshots

4.  IP Fabric only supports delete action at the moment. Additional
    actions will be added in coming releases

<div>

<div>

At the moment, snapshot retention runs everyday at 0:00 UTC time

</div>

</div>

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
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211020-112725.png](attachments/102367300/2790883329.png)
(image/png)  

</div>
