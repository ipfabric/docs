---
description: This page describes the password restrictions for various services used by IP Fabric.
---

# Service Passwords

Passwords to the following services:

- Backup
- Jumphosts
- SNMP

must match this regular expression:

```
/^[A-Za-z0-9\.,\/_@%^:=+ -]*$/
```

(They can only contain these characters: `A-Z` `a-z` `0-9` `.,/_@%^:=+ -`)

Additionally, the same restriction applies to the fields **Organization name**,
**Department**, **City**, and **State / Province** in **Settings --> System -->
IPF Certificates**.

This restriction was implemented due to issues with certain special characters
and to enhance security.
