---
description: IP Fabric supports Palo Alto Prisma SASE unified API.
---

# Palo Alto Prisma SASE

Starting version **6.1.0** IP Fabric supports Palo Alto Prisma SASE unified API.

For authentization [service account](https://pan.dev/sase/docs/service-accounts/) have to be created with RO role View Only Administrator or higher. Prisma requires the following settings to be applied:

- **Username** -- Service account username
- **Password** -- Service account password
- **TSG ID** -- [Tenant service group ID](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)

## Known Issues

Path lookup isn't fully supported. Currently Prisma SASE unified API doesn't have all needed endpoints.
