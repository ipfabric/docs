---
description: 'This page describes the current limitation in IP Fabric regarding enabled pagination for FortiGate.'
---

# FortiGate CLI Paging Causes Incomplete Parsing

**Known affected platforms:** FortiGate Firewall

**Description:** When CLI paging (`--More--`) is `enabled` on FortiGate devices, command outputs can be truncated during collection. 
This may result in incomplete data in snapshots, such as missing source/destination `IPv4` information in firewall policies.

**Fix:** Disable CLI paging on FortiGate.
