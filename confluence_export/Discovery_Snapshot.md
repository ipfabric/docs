# Discovery Snapshot

## What The Snapshot Consists Of

Network snapshot records:

-   The state of the network at the moment of the initialization of the
    snapshot.

-   All service logs - logs used internally by the IP Fabric system as
    well as a log of commands issued on every network device.

-   Connectivity issues that had occurred during the retrieval of the
    snapshot.

A network snapshot is a fully functional software copy of your network,
including all configuration and state data. It enables to retrieve
historical information, to follow network state changes, analyze
connectivity issues, and more.

Information about the network displayed in IP Fabric corresponds to the
network snapshot selected in the Snapshot selector drop-down menu in the
top left corner of the Main User Interface.

<img src="attachments/1878261859/1881636907.png" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1881636907.png" data-height="69" data-width="220" data-unresolved-comment-count="0" data-linked-resource-id="1881636907" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-153059.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="15f55123-99a8-43f4-b7bf-00c3be7acb1d" data-media-type="file" />

## Available Snapshot Operations

### New Snapshot

<img src="attachments/1878261859/1881767958.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1881767958.png" data-height="507" data-width="1522" data-unresolved-comment-count="0" data-linked-resource-id="1881767958" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-154903.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="c2eab364-b853-4d40-8404-f4967bd3c420" data-media-type="file" width="340" />

During the initial configuration of the IP Fabric VM, automatic
snapshots can be scheduled. Initial snapshot of the network may not
include all information about your network. There might be user
privilege level issues, connectivity issues related to firewall rules,
etc. A new snapshot can be taken at any time by clicking the “New
Snapshot” button in the “Discovery Snapshot” menu entry. The system then
automatically starts a new snapshot of the network with globally set
parameters in the “Settings” menu entry. If you need to make some
changes to the discovery process - add a new network seed, change login
credentials, etc. - it needs to be done before a new snapshot is taken.

### Inspection of Network Issues

<img src="attachments/1878261859/1882030127.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1882030127.png" data-height="507" data-width="1522" data-unresolved-comment-count="0" data-linked-resource-id="1882030127" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-154746.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="b04ddc52-3d9c-4332-9f13-21368c2c089a" data-media-type="file" width="340" />

After the snapshot is taken, there might be some devices not showing in
the discovery table. You can then go through [the Summary of
Issues/Connectivity Report tables to see where this device in the
discovery process
failed](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/102268954/Fine-Tune+SSH+TELNET+CLI+parameters).

Each connection attempt - successful or unsuccessful is logged (see the
following picture). Log for each device can be found in the Connectivity
Report. These logs are especially helpful when an error occurs. By
examining them you can find the reason why the device wasn't correctly
or fully discovered or what led to a connection failure.

<img src="attachments/1878261859/1891565569.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1891565569.png" data-height="187" data-width="1701" data-unresolved-comment-count="0" data-linked-resource-id="1891565569" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210118-092925.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="39a9e728-f1e8-4c92-be58-634adb5bcdef" data-media-type="file" width="340" />

### Add a New Device/Changing Snapshot Settings

A new device can be added to an already existing snapshot. This might be
desirable if you performed almost a full snapshot of the network but
only a few devices were not included or had connectivity issues that
were resolved (for example wrong AAA configuration, firewall rules,
forgot to include a network seed, etc). When adding a new device to an
existing snapshot, the discovery setting for that particular snapshot
will be applied. If you need to change some settings (for example new
network seed, login credentials, etc.) in order to add a new device to
an existing snapshot, you need first to change settings for that
particular snapshot and then add a new device.

<img src="attachments/1878261859/1881964560.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1881964560.png" data-height="507" data-width="1522" data-unresolved-comment-count="0" data-linked-resource-id="1881964560" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-155203.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="9f6919af-84af-4d54-8eb4-4b38a1a2a350" data-media-type="file" width="340" />

### Lock Snapshot

Because of database maintenance, only up to 5 snapshots can be loaded
into the memory. By locking a snapshot, IP Fabric won’t unload the
selected snapshot automatically to the hard disk and it will keep it in
the memory.

<img src="attachments/1878261859/1882226714.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1882226714.png" data-height="221" data-width="1111" data-unresolved-comment-count="0" data-linked-resource-id="1882226714" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-155628.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="f3d71bbf-c72a-4133-be86-0e182ea22ead" data-media-type="file" width="340" />

### Unload/load Snapshot

Because of database maintenance, only up to 5 snapshots can be loaded
into the memory. If the maximum number of loaded snapshot is 5 and 6th
snapshot is created, the IP Fabric will automatically unload the oldest
snapshot from the memory and save it to the hard drive. This can be done
also manually on a selected snapshot by the “Unload snapshot” button.

When a snapshot is unloaded, it's safely stored on your hard drive, but
the data from a snapshot cannot be accessed directly through the IP
Fabric user interface. To browse an unloaded snapshot, it needs to be
loaded again to the memory by “Load snapshot”

<img src="attachments/1878261859/1891631117.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/1878261859/1891631117.png" data-height="30" data-width="42" data-unresolved-comment-count="0" data-linked-resource-id="1891631117" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210118-142045.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="94d7697c-8c9f-48ca-be7f-fba9d9a7e159" data-media-type="file" />

button accessible on an unloaded snapshot.

<img src="attachments/1878261859/1882226720.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1882226720.png" data-height="221" data-width="1111" data-unresolved-comment-count="0" data-linked-resource-id="1882226720" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-155742.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="1590fd19-b429-41c6-a68a-5cc67a1268e6" data-media-type="file" width="340" />

### Download Snapshot

If needed, a selected snapshot can be downloaded directly from IP Fabric
to your hard drive by the “Download snapshot” button.

<img src="attachments/1878261859/1881964566.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1881964566.png" data-height="221" data-width="1111" data-unresolved-comment-count="0" data-linked-resource-id="1881964566" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-155846.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="89b9df59-387a-440c-b334-b8a9065096ff" data-media-type="file" width="340" />

This snapshot can be loaded back to the IP Fabric platform by a “Load
From File” button.

<img src="attachments/1878261859/1892188171.png" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1892188171.png" data-height="59" data-width="343" data-unresolved-comment-count="0" data-linked-resource-id="1892188171" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210118-141214.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="dfd7eda7-c1d3-4a03-9df8-9fd19a1169d5" data-media-type="file" />

### Clone Snapshot

Loaded as well as unloaded snapshots can be cloned by the “Clone
snapshot“ button. This is handy in case you want to make some changes to
the snapshot (adding a device etc.) but you want to keep the original
file as a backup.

<img src="attachments/1878261859/1882193962.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1882193962.png" data-height="221" data-width="1111" data-unresolved-comment-count="0" data-linked-resource-id="1882193962" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-155940.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="c72022ee-f998-4fc5-ba71-333855931efe" data-media-type="file" width="340" />

### Delete Snapshot

Snapshots can be deleted by the “Delete snapshot“ button.

<img src="attachments/1878261859/1881538594.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/1878261859/1881538594.png" data-height="221" data-width="1111" data-unresolved-comment-count="0" data-linked-resource-id="1881538594" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210115-160024.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878261859" data-linked-resource-container-version="13" data-media-id="53a1e3c1-9fce-4fa2-9481-4035321c2399" data-media-type="file" width="340" />

### Related Articles

If you want to learn more about how network discovery works from a
technical point of view, [read this article](How_Discovery_Works).

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-2-7_15-56-53.png](attachments/1878261859/1882325021.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-153059.png](attachments/1878261859/1881636907.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-154746.png](attachments/1878261859/1882030127.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-154903.png](attachments/1878261859/1881767958.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155203.png](attachments/1878261859/1881964560.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155348.png](attachments/1878261859/1882226708.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155628.png](attachments/1878261859/1882226714.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155742.png](attachments/1878261859/1882226720.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155846.png](attachments/1878261859/1881964566.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-155940.png](attachments/1878261859/1882193962.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-160024.png](attachments/1878261859/1881538594.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210115-161359.png](attachments/1878261859/1878491256.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210118-092925.png](attachments/1878261859/1891565569.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210118-141142.png](attachments/1878261859/1891696667.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210118-141214.png](attachments/1878261859/1892188171.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210118-142045.png](attachments/1878261859/1891631117.png)
(image/png)  

</div>
