---
description: 'This page describes a limitation where VRF routes are not collected on Cisco NX-OS devices if the BGP route download limit is not enabled.'
---

# VRF Routes Not Collected on Cisco NX-OS

VRF routes are not collected on Cisco NX-OS devices if the BGP route download limit is not enabled.

Workaround:
Enable Limit download BGP routes and set a sufficiently high threshold (e.g., 100000 or higher) to allow full route collection.
