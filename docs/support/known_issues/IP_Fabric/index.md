---
description: This page describes general known issues affecting the IP Fabric platform and how to fix them.
---

# General

- The diagram displays a device that is not connected to anything. This
  situation occurs when Site Separation prevents displaying the
  device on the other end. To show the connection to a device, click **Show
  Edge Cloud**.

- Diagrams drill-down is missing. Current diagrams offer a vast amount of
  information, which is not available through drill-downs. More
  drill-down capabilities are planned for future releases.

- TACACS may be limited to a specific maximum number of simultaneous
  authentication sessions, preventing the discovery of all of the devices in the
  network. If fewer than the expected number of devices are discovered, decrease
  the bandwidth rate (e.g., to 3Mb/s), increase SSH/Telnet session timeout (e.g.,
  to 30 seconds), and decrease the maximum number of simultaneous
  sessions (e.g., to 40).

- Inter-platform spanning-tree topology enumeration requires an L2
  discovery protocol to form a connection when
  the `port_id.port_priority.port_id` field separation boundary is in
  an inconsistent position between the two platforms.

- Site Separation -- Changing "Firewall in site" and new
  discovery/recalculation can change Site names.

- When entering IP addresses in the Settings UI, changes will only be saved if you click the **Add to list** button next to the input field or press the **Enter** key. Although a red validation message appears below the field, it does not prevent the UI from saving the settings—however, any IP addresses not added to the list will be omitted. This issue affects all input fields that accept IP addresses.

## Snapshots

- When discovery is stopped mid-way, and then Refresh is executed, the
  refresh does not consider IP addresses with status "STOP" for the next
  discovery

- Resource checks for sufficient RAM and HDD use a sliding window.
  Creating a new snapshot immediately after the previous one may result in
  an "insufficient resources" failure. In such a case, verify resources
  on the status page and retry in several minutes.

## Duplicate IP detection

- Anycast IP addresses are reported as duplicate addresses.
