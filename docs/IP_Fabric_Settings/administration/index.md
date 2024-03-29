---
description: The local user in IP Fabric has administrative privileges to create or manage other users and to perform network management tasks.
---

# Overview

**Settings --> Administration** contains the management of:

- [Local Users](users.md)
- [LDAP](ldap.md)
- [Roles](roles.md)
- [Policies](policies.md)

IP Fabric also supports **Single Sign-On (SSO)** authentication. It uses **Dex** (A Federated OpenID Connect Provider) and requires configuration of Dex service to access 3rd party OpenID providers. This is not yet included in the UI.

For more information, follow [Single Sign-On (SSO) Authentication](sso.md).

## Role Based Access Control (RBAC)

IP Fabric uses **Role Based Access Control** to manage users access to particular resources as well as allow certain actions on the top of those resources.

The foundation for RBAC is a list of resources (e.g. *Reports*, *Discovery*) and actions on those resources (e.g. *Read*, *Execute*).

Those resources are then assigned to *Policies* which are sets of resources with their actions (e.g. *discovery* policy allows access to discovery api endpoints).

*Policies* are then assignable to *Roles* to enable users assigned to particular roles perform actions on system resources (e.g. *user-management* role with assigned *team* policy enables users view, add, update and delete Users, Roles, Policies, LDAP Configuration).
