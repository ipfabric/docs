---
description: Overview of security-related issues in IP Fabric
---

# Security Bulletin

Security notifications affecting the IP Fabric solution published according to our [Security Incident Response](security_incidents.md) policy.

!!! info "Upgrade information"

    Upgrade information can be found in the [System Update](../admin/Administrative_Interface/System_Update.md) section.

## NIM-9199: Privilege escalation via Admin portal

| Severity | Affected Versions | Fix Version |
| -------- | ----------------- | ----------- |
| High     | 5.0.2 or earlier  | 6.0.1       |

A read-only user can create an escalated privilege account by taking advantage of token validation.

Tokens issued in the web app are accepted without proper validation. Using that, users of any privilege level can call an API endpoint for creating a new admin user account using their token. Then it is possible to escalate their privilege by logging in to the new account.

## NIM-9023: API Token privilege escalation

| Severity | Affected Versions     | Fix Version |
| -------- | --------------------- | ----------- |
| High     | 5.0.0, 5.0.1 or 5.0.2 | 6.0.1       |

Users can create an API token with RBAC properties that the token is not authorised for.

An API token can be generated that allows unauthorised collection of network data or modification of IP Fabric system settings.
