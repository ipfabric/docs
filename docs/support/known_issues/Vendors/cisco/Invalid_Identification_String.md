---
description: IOS SSH server component may report incorrect version 2.99. Enforce SSH version 2 using ip ssh version 2 and validate with show ip ssh. 
---

# Error: Invalid Identification String

**IP Fabric Version:** All

**Affected Platforms:** Cisco IOS `12.4(15)T4` and other versions

**Description:** Under certain circumstances, the IOS SSH server component may report a bogus version
of 2.99 instead of the widely recognized versions 1.5, 1.99, and 2.0. This leads to the failure of
SSH version validation and subsequent discovery issues.

For more details see: [CSCsq51052](https://quickview.cloudapps.cisco.com/quickview/bug/CSCsq51052)

**Fix:** To resolve the issue, enforce SSH version 2 on IOS devices using the command `ip ssh version 2`. Subsequently, validate the current SSH version using the command `show ip ssh`.

**Fix:** Starting with IP Fabric v7.10, our SSH client recognizes SSH protocol version 2.99 and is able to connect to affected Cisco IOS devices.
