---
description: IP Fabric supports Ruckus Virtual SmartZone API. Ruckus devices are discovered only through API.
---

# Ruckus Virtual SmartZone

Starting version `4.4.0`, IP Fabric supports Ruckus Virtual SmartZone API.

Ruckus devices are discovered only through API.

To add Ruckus to discovery, go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API** and press the **+ Add** button.

Afterwards, choose **Ruckus Virtual SmartZone** from the list and fill in:

- **Username and password** used to log in to the Virtual SmartZone -- user account needs to have rights to list zone configurations
- **API Version** -- we support only version `9.1` which covers Virtual SmartZone `v5.2.1+` and `v6`
- **Base URL** of Virtual SmartZone (`https://virtual-smart-zone:8443`)
- [**Slug**](index.md#slug-and-comment)
