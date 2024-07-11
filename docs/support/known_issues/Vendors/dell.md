---
description: This page describes known issues with Dell and how to fix them.
---

# Dell

**IP Fabric Version:** all

**Known affected platforms:** Dell SmartFabric OS10

**Description:** The `show license status` command is only available for users
with the `sysadmin` role. This command is necessary to detect the serial number
and discover the device.

**Fix:** The user must be added to the `sysadmin` role for discovery to occur.
