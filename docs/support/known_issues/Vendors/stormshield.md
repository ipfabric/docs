---
description: This page describes known issues with Stormshield.
---

# Stormshield

## Collection of Filter Rules

Implicit rules are not supported.

Filter rules with the following options configured as part of the rule are not
supported:

- Scheduling
- Routing
- Redirection
- Web services and reputations
- Host reputation
- Authentication
- NAT on the destination
- Application inspection

## NAT Rules Collection

Following NAT rules/objects are not currently supported:

- Negated objects
- NAT inside IPsec (beforevpn flag)
- User-based rules
