---
description: This page describes known issues with Forcepoint and how to fix them.
---

# Forcepoint

## Forcepoint NGFW CLI Discovery

**IP Fabric version:** all

**Known affected platforms**: Forcepoint NGFW

**Description**: When performing discovery via CLI, ensure that you are using an
account that has the necessary privileges to run the `sg-*` commands. If the
account lacks these privileges, attempting to run the commands will result in a
`command not found` error.

### List of All `sg-*` Commands

![List of commands](../../../images/support/support_known-issues-vendors_forcepoint-sg-command-list.webp)
