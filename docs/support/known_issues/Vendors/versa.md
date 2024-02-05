---
description: This page describes known issues with Versa and how to fix them.
---

# Versa

## HTTP 500 error `AsyncRequestTimeoutException`

**Known Affected platforms**: All

**Description**: When API request takes longer than 5 minutes, API returns HTTP
500 error `AsyncRequestTimeoutException`.

This issue can be usually encountered on devices with very large routing tables.
