---
description: This page provides an overview of the Administration section of IP Fabric Settings.
---

# Overview

**Settings --> Administration** contains the management of:

- [Local Users](users.md)
- [LDAP](ldap.md)
- [Roles](roles.md)
- [Policies](policies.md)

IP Fabric also supports **Single Sign-On (SSO)** authentication. It uses **Dex** (a federated OpenID Connect provider) and requires the configuration of the Dex service to access third-party OpenID providers. This is not yet included in the UI.

For more information, follow [Single Sign-On (SSO) Authentication](sso.md).

## Role-Based Access Control (RBAC)

IP Fabric uses **Role-Based Access Control** to manage users' access to particular resources as well as allow certain actions on those resources.

The foundation for RBAC is a list of resources (e.g., *Reports*, *Discovery*) and actions on those resources (e.g., *Read*, *Execute*).

Those resources are then assigned to *Policies*, which are sets of resources with their actions (e.g., a *discovery* policy allows access to discovery API endpoints).

*Policies* are, in turn, assignable to *Roles* to enable users assigned to particular roles to perform actions on system resources (e.g., a *user-management* role with an assigned *team* policy enables users to view, add, update, and delete Users, Roles, Policies, LDAP Configuration).
