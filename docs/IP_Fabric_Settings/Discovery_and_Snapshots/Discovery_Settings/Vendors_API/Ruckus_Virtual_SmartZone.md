---
description: This section contains information on how to set up API discovery for Ruckus Virtual SmartZone.
---

# Ruckus Virtual SmartZone

Starting from version `4.4.0`, IP Fabric supports the Ruckus Virtual SmartZone API.

Ruckus devices are discovered only through the API.

To add Ruckus to the global discovery settings, go to **Settings --> Discovery &
Snapshots --> Discovery Settings --> Vendors API**, and click **+ Add**, select
`Ruckus Virtual SmartZone` from the list, and fill in the following details:

- **Username** and **Password** used to log in to the Virtual SmartZone -- The user account needs to have rights to list zone configurations.
- **API Version** -- We only support version `9.1`, covering the Virtual SmartZone `v5.2.1+` and `v6`.
- **Base URL** of the Virtual SmartZone (`https://virtual-smart-zone:8443`)
- [**Slug**](index.md#slug-and-comment)
