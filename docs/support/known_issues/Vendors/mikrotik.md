---
description: IP Fabric describes known affected issues for Mikrotik and how to fix them.
---

# Mikrotik

**Known Affected platforms**: All

**Description**: Mikrotik requires longer session timeout otherwise it will be not discovered

**Fix**: In **Settings --> Discovery & Snapshots --> Discovery Settings -->
Advanced CLI --> CLI Settings**, set **Network device session timeout** to `20`
seconds.
