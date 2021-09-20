# System Architecture

## Solution Overview

The IP Fabric network infrastructure management platform provides
on-demand network discovery, advanced analytics, and detailed
engineering visibility. The lightweight discovery capabilities (through
SSH or telnet) quickly detect the current network state, including
detailed data for each address and port. A network model of gathered
data reconstructs the topologies for each switching and routing protocol
to enable a cross-technology analysis of upstream and downstream
relationships. Dependencies and dependents are calculated for each
network element, allowing analysis to represent each aspect of the
network in the context of productivity impact on the downstream hosts
and on network devices, while the immediate productivity impact of
performance and capacity is calculated for each user and every element.

## Solution Architecture

A distributed system of micro-service components resides within IP
Fabric VM, all based around a multi-model database with a mathematical
network model at its core. Operating system-level controls provide high
availability, security and log collection. The kernel-level
bidirectional traffic shaper and application-level worker flow control
mechanisms provide comprehensive traffic management and automatically
respond to any sign of network congestion to ensure that only freely
available bandwidth is utilized. The user interface is available on port
443 of the VM's IP address through any modern web browser and on any
screen. Table output can be exported into CSV format for further
processing, and selected reports are exportable into Word format.

<img src="attachments/1831174153/1830944786?width=340" class="image-left" loading="lazy" data-image-src="attachments/1831174153/1830944786" data-height="698" data-width="1205" data-unresolved-comment-count="0" data-linked-resource-id="1830944786" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="architecture.png?version=1&amp;modificationDate=1572581015982&amp;cacheVersion=1&amp;api=v2&amp;width=619" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1831174153" data-linked-resource-container-version="5" data-media-id="e39a8e58-c972-4df1-91b0-4e07b31f8561" data-media-type="file" width="340" />

* Figure* *1: Solution architecture overview*

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[architecture.png?version=1&modificationDate=1572581015982&cacheVersion=1&api=v2&width=619](attachments/1831174153/1830944786)
(image/png)  

</div>
