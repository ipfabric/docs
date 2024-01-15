---
description: This section helps you define passwords for different services that IP Fabric uses.
---

# Service Passwords

Passwords to the following services must match this regular expression:
`/^[A-Za-z0-9.,\/_@%^:=+ -]*$/` (they can contain only these characters: `A-Z`
`a-z` `0-9` `.,/_@%^:=+ -`).

- Backup
- Jumphosts
- SNMP
- Certificates

This was done because of issues with some special characters and to increase
security.
