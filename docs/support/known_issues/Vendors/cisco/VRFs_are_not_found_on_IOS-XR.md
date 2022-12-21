---
description: IP Fabric describes a known affected issue where VRFs Are Not Found On IOS-XR.
---

# VRFs Are Not Found On IOS-XR

To collect full VRF data on IOS-XR operating system, it is necessary to have
enabled the MPLS package. Without it, the command `show vrf all detail` does
not work and it is marked as invalid input.
