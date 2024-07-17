---
description: This page describes known issues with Versa and how to fix them.
---

# Versa

## HTTP 500 Error `AsyncRequestTimeoutException`

**Known affected platforms:** all

**Description:** When an API request takes longer than 5 minutes, the API
returns an HTTP 500 error `AsyncRequestTimeoutException`.

This issue is usually encountered on devices with very large routing tables.
