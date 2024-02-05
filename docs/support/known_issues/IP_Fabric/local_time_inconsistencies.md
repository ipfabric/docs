---
description: An issue that was causing local time inconsistencies was fixed in version 4.2.0.
---

# Local Time Inconsistencies

When setting a time for automatic snapshots and other recurring tasks, UTC time
is used in IP Fabric.

This was resolved in version `4.2.0` where time zone for recurring tasks
(discovery, DB maintenance etc.) was introduced.

After this release, all recurring tasks will run in a time zone defined during
the initial setup, except for API that will always return data in UTC time.
