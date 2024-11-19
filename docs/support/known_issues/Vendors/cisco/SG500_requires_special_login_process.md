---
description: This page describes a known issue with Special Login process on Cisco SG500 platforms.
---

# Cisco SG500 platform requiring a different login logic

There might be an issue with the Cisco SG500 platform requiring a different login logic compared to standard Cisco platforms.
According to [Workflow 2: Step 3](https://www.cisco.com/c/dam/en/us/td/docs/switches/lan/csbms/sf30x_sg30x/administration_guide/78-19308-01.pdf#page=507&zoom=100,216,420) on the official Cisco webpage, the SG500 platform requires an unusual login process:

- **Username**
- **Password**
- **Username**

Fortunately, this can be easily bypassed by enabling [Automatic Login](https://www.cisco.com/c/dam/en/us/td/docs/switches/lan/csbms/sf30x_sg30x/administration_guide/78-19308-01.pdf#page=508&zoom=100,216,420) on your SG500 device.
