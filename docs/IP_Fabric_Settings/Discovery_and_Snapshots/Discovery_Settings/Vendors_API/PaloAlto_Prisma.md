---
description: This section contains information on how to set up API discovery for Prisma.
---

# Palo Alto Prisma SASE

Starting from version `6.1.0`, IP Fabric supports the Palo Alto Prisma SASE unified API.

A [service account](https://pan.dev/sase/docs/service-accounts/) needs to be created with RO role `View Only Administrator` or higher.

In IP Fabric, navigate to **Settings --> Discovery & Snapshots --> Discovery
Settings --> Vendors API**, click **+ Add**, select `Prisma` from the list, and
fill in the following login details:

- **Username** -- Service-account username.
- **Password** -- Service-account password.
- **TSG ID** -- [Tenant service group ID](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)
- [**Slug**](index.md#slug-and-comment)

![Add Connection - Prisma](prisma_api_add.webp)

## Known Issue

Path lookup isn't fully supported. Currently, the Prisma SASE unified API doesn't have all the needed endpoints.
