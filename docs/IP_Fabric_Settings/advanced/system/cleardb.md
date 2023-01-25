---
description: In rare cases, it may be necessary to delete and recreate the IP Fabric's database.
---

# Clear DB

!!! warning

    Before erasing databases, make sure that you have access to a recent backup!

In rare cases, it may be necessary to delete and recreate the IP
Fabric's database. Go to **Settings → Advanced → System** and click
**Clear DB**.

When running Clear DB, all loaded snapshots are automatically unloaded
and the database recreated.

![ClearDB](2828599305.png)

There is two-way confirmation.

![Confirmation](2829352961.png)

In the second screen, you can choose between "Reset Settings" or "Keep Settings":

![Confirmation Settings](./confirmation-settings.png)

We recommend selecting "Keep Settings". If you choose to "Reset Settings", all system and discovery settings will be lost, including login credentials, site separation rules, saved views, shared URLs, filters and API tokens. The system settings will be reset to defaults **except**:

- Certification authorities
- User settings
- LDAP settings
- Reports settings
- Dashboard settings
