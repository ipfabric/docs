# How Snapshots Work

Network snapshots record the state of the network in time, enabling to
retrieve historical information, follow network state changes, analyze
connectivity, and more. A network snapshot is a fully functional
software copy of the network, including all configuration and state
data. Active network view displays information from a network snapshot
which can be selected using Snapshot selector drop-down menu in the top
left corner of the Main User Interface.

<img src="attachments/474677271/474775561.png" title="Snapshot selector menu" loading="lazy" data-image-src="attachments/474677271/474775561.png" data-unresolved-comment-count="0" data-linked-resource-id="474775561" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2019-2-7_15-56-53.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="474677271" data-linked-resource-container-version="3" data-media-id="767739d3-87bf-4c6c-83c4-d4ac598cb2e2" data-media-type="file" alt="Snapshot selector menu" />

# Snapshot Management

<img src="attachments/474677271/475037701.png?height=250" title="Snapshot Management Overview" loading="lazy" data-image-src="attachments/474677271/475037701.png" data-unresolved-comment-count="0" data-linked-resource-id="475037701" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2019-2-7_15-59-44.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="474677271" data-linked-resource-container-version="3" data-media-id="c2d57ac6-40ad-4d2f-9aaa-63263cbb3509" data-media-type="file" height="250" alt="Snapshot Management Overview" />

Up to five (5) snapshots can be loaded simultaneously into active
memory. When the snapshot is active it is considered "loaded". Other
snapshots can be stored on HDD, with only free HDD space being the
limiting factor.

Locking active snapshot will always keep snapshot in memory.

Unloading snapshot will move network state information from RAM to HDD.
It usually takes several minutes to load and unload the snapshot,
depending on the network size.

Snapshots can be downloaded for external storage, which can be later
uploaded back to the system.

Snapshots can be cloned to accommodate change management practices, for
example when change comparison is desired but only a small part of the
network is affected by the change. A snapshot can be restricted to a
specific portion of the network through IP Scope in Advanced Settings
menu. This will enable visual comparison of a portion of the network,
and provide historical data for the collected portion of the network.
However when comparing partial snapshot with full network snapshot, a
number of false positives will appear, because large portion of the
network will be missing.

Snapshots can be also permanently deleted from the system.

# Snapshot Manipulation

New network state snapshots can be created from the Discovery page using
the start button.

To add devices to existing snapshot, use
the <img src="attachments/474677271/474710044.png?width=140" title="Add Device" loading="lazy" data-image-src="attachments/474677271/474710044.png" data-unresolved-comment-count="0" data-linked-resource-id="474710044" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2019-2-7_16-41-21.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="474677271" data-linked-resource-container-version="3" data-media-id="499a4228-83fa-4d3b-af6b-f4db5eee6fec" data-media-type="file" width="140" alt="Add Device" /> button.
When adding devices, no data is overwritten.

To refresh network state data for specific devices in existing snapshot,
use <img src="attachments/474677271/475136030.png?width=140" title="Refresh Device Data" loading="lazy" data-image-src="attachments/474677271/475136030.png" data-unresolved-comment-count="0" data-linked-resource-id="475136030" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2019-2-7_16-42-22.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="474677271" data-linked-resource-container-version="3" data-media-id="805fcccf-e5d6-4354-aac4-b3b26500f46d" data-media-type="file" width="140" alt="Refresh Device Data" /> button.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-2-7_15-56-53.png](attachments/474677271/474775561.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-2-7_15-59-44.png](attachments/474677271/475037701.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-2-7_16-41-21.png](attachments/474677271/474710044.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-2-7_16-42-22.png](attachments/474677271/475136030.png)
(image/png)  

</div>
