---
description: This page describes known issues with Huawei and how to fix them.
---

# Huawei

**Known affected platforms:** Huawei platforms with bridge domains

**Description:** IP Fabric currently does not have a separate bridge domain
model. The bridge domain is mapped into the VLAN model, which has limitations:

- The bridge domain number can have a maximum value of 4095 and must be the same
  as the VLAN tag.

- VLAN and bridge domain with the same number is not supported.

**Fix:** Currently, there is no solution available. Improvement may be made in
future releases.
