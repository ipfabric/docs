---
description: This page describes a known issue with VRFs not being found on IOS-XR.
---

# VRFs Are Not Found On IOS-XR

To collect full VRF data on the IOS-XR operating system, it is necessary to have
the MPLS package enabled. Without it, the `show vrf all detail` command does not
work and is marked as invalid input.
