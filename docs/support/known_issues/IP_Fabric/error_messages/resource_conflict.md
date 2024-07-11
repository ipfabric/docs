---
description: 'This page explains why "Error: Resource Conflict" occurs.'
---

# `Error: Resource Conflict`

This error occurs when you try to start a job for the second time (a specific
task such as discovery, System Maintenance, uploading/unloading a snapshot) that
is already scheduled.

Only one job can be executed at a time. For instance, if discovery is already
running and you schedule the unloading of a snapshot, attempting to unload the
same snapshot a second time will result in this error.
