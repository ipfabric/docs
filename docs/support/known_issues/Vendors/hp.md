---
description: This page describes known issues with HP and how to fix them.
---

# HP

**Affected platforms:** HP 10508 Comware Software, version `5.20.105`, release
`1208P05`

**Description:** Sometimes the device randomly fails to return chassis
information, and the serial number cannot be detected.

**Result:** The device may be saved with a serial number different from the
correct one from the chassis. This can, for example, lead to incorrect change
management results.

**Output:**

```commandline
display device manuinfo
Chassis 1:

Chassis self:
Error: Failed to display the manufacture information of the chassis.
```

---

**Affected platforms:** HP Aruba 2530 and 2930 series switches.

**Description:** These devices may not be discovered immediately and might
require multiple attempts due to sporadic errors such as `Bad Packet Length`
or `Telnet terminated due to inactivity` when receiving the output for
either of these two commands.

`show interfaces all`

`show spanning-tree debug-counters instance 0 ports all`

**Fix:** In **Settings --> Discovery & Snapshots --> Discovery Settings -->
Disabled Discovery Tasks**, click **Add rule**, select Task `Disable Pagination`, and
add these three Regex rules:

- Vendor: `hp`
- Family: `arubasw`
- Platform: `2530|2930`

This fix might extend the network discovery process by a few minutes, depending
on the number of affected devices.

---

**Description**: HP Aruba switches may not display their serial number in the
`show version` command output. In such cases, their base MAC address from the
`show version` output is set as their serial number. This issue is known, e.g.,
for HP 2824 version `I.10.107`.
