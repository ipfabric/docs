---
description: IP Fabric describes known affected issues for HP and how to fix them.
---

# HP

**Affected platforms**: HP 10508 Comware Software, Version 5.20.105,
Release 1208P05

**Description**: Device sometimes randomly doesn’t return chassis
information, SN can’t be detected

**Result**: Device can be saved with some other SN other than correct
one from chassis. This can for example show incorrect change management
results.

**Output**

``` text
display device manuinfo
Chassis 1:

Chassis self:
Error: Failed to display the manufacture information of the chassis.
```
------------------------------------------------------------------------

**Description**: HP Aruba switches may not display their serial number
in "show version" command output. In such cases their base MAC address
from the show version output is set as their serial number. This issue
is known e.g. for HP 2824 version I.10.107.
