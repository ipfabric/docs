---
description: This page describes known issues with Mikrotik and how to fix them.
---

# Mikrotik

**Known affected platforms:** all

**Description:** Mikrotik requires a longer session timeout; otherwise, it will
be not discovered.

**Fix:** In **Settings --> Discovery & Snapshots --> Discovery Settings -->
Advanced CLI --> CLI Settings**, set **Network device session timeout** to `20`
seconds.
