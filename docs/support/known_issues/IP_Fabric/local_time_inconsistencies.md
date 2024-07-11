---
description: This page describes an issue with local time inconsistencies that was fixed in version 4.2.0.
---

# Local Time Inconsistencies

UTC time is used when setting a time for automatic snapshots and other recurring
tasks in IP Fabric.

This issue was resolved in version `4.2.0`, where a time zone for recurring
tasks (such as discovery and database maintenance) was introduced.

Since this release, all recurring tasks will operate in the time zone defined
during the initial setup, except for the API, which always returns data in UTC
time.
