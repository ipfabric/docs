# Discovery Tasks

<div>

<div>

The discovery process for network device divides into multiple Tasks.
The TASK is a data collection related to a specific network protocol or
technology (MPLS, Transceivers, ARP Table, Spanning-Tree Protocol,
Multicast, or VXLAN). Each task consists of 1 or more operational
commands (CLI or API). You can find the list of all Discovery Tasks
in [the Feature matrix](https://docs.ipfabric.io/matrix/).

</div>

</div>

<div>

<div>

Some fundamental TASKS required for discovery and topology calculations
cannot be disabled (Neighbors, ARP, Mac, RIB, etc.)

</div>

</div>

The Discovery Tasks settings are introduced in version 3.7.0. Since
then, the user can manipulate specific tasks for the discovery process
to avoid extra data collection (when particular protocols are not
present on the network) or avoid specific operational commands to be
executed on specific hardware platforms.

**By default, there are three main Discovery Task rules in the
platform:**

<div class="table-wrap">

|                        |                                                                                                                                                                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rule Name**          | **Rule Description**                                                                                                                                                                                                                              |
| **Disable Pagination** | By default disabled for F5 devices - command is modifying the configuration and can break cluster synchronization.                                                                                                                                |
| **Transceivers**       | By default disabled for all vendors - certain Cisco platforms may be affected by a memory leak bug and lead to device crash or hung VTY line. More at [Known Issues \> Cisco](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/79986775/Cisco) |
| **NTP**                | By default disabled for Cisco Firepower - on some versions a Firepower bug may freeze the CLI session                                                                                                                                             |

</div>

In the following example, we are creating a rule to disable OSPFv3 on
Juniper EX. The test for the rule reveals one match, the
HWLAB-JEX2200-SW1 switch:

<img src="attachments/1642102814/1936130053.png" class="image-center" loading="lazy" data-image-src="attachments/1642102814/1936130053.png" data-height="669" data-width="1448" data-unresolved-comment-count="0" data-linked-resource-id="1936130053" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210129-140513.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1642102814" data-linked-resource-container-version="4" data-media-id="bed39fee-1769-481e-af45-800c35a11cf3" data-media-type="file" alt="Discovery Tasks settings in IP Fabric" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210129-140513.png](attachments/1642102814/1936130053.png)
(image/png)  

</div>
