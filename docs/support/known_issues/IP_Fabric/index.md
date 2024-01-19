---
description: IP Fabric describes general known affected issues that may occur in the IP Fabric's platform and shows how to fix them.
---

# General

- Diagram displays device, which is not connected to anything. The
  situation appears when site separation prevents displaying the
  device on the other end. To show connection to a device, click **Show
  Edge Cloud**

- Diagrams drill-down missing. Current diagrams offer vast amount of
  information, which is not available through drill-downs. More
  drill-down capabilities are planned for future releases.

- TACACS may be limited to the specific maximum number of simultaneous
  authentication sessions, preventing discovery of all of the devices in the
  network. If fewer than expected number of devices are discovered, decrease
  bandwidth rate (like to 3Mb/s), increase SSH/TELNET session timeout (for
  example to 30 seconds), and decrease the maximum number of simultaneous
  sessions (like 40).

- Inter-platform spanning-tree topology enumeration requires L2
  discovery protocol to form a connection when
  `port_id.port_priority.port_id` field separation boundary is in
  inconsistent position between the two platforms.

- Site separation - Changing "Firewall in site" and new
  discovery/recalculation can change site names.

## Snapshots

- When Discovery is stopped mid way, and then Refresh is executed, the
  refresh does not consider IPs with status "STOP" for the next
  discovery

- Resource check for sufficient RAM and HDD use a sliding window.
  Creating a new snapshot immediately after previous one may result in
  a "insufficient resources" failure. In such a case, verify resources
  on the status page and retry in several minutes.

- Switching site separation to RegEx can cause issues.

## Duplicate IP detection

- Anycast IP addresses are reported as duplicate addresses.
