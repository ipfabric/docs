---
description: A solution to a known issue where the site name can change to an obscure UUID value after update.
---

# Site Name Can Change to an Obscure UUID Value After Update

There have been reported issues that some sites had changed their names to an
obscure UUID value after update to an newer version of IP Fabric.

This might happen only in locations that have manual site separation in place.

To resolve this issue, it is necessary to unload and load back active snapshots
that are affected by this bug.
