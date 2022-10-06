---
description: An issue that was causing Local Time Inconsistencies was fixed with the version 4.2.0.
---

# Local Time Inconsistencies

When setting a time for automatic snapshots and other recurring tasks,
UTC time is used in IP Fabric.

This was resolved in the **4.2.0** where timezone for recurring tasks
(discovery, DB maintenance etc) was introduced.

After this release, all recurring tasks will run in a timezone defined
during the initial setup, except for API that will always return data in
UTC time.
