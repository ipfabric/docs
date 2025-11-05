---
description: This section contains information on how to manage IP Fabric users.
---

# Local Users

**Settings --> Administration --> Local Users** allows you to create or modify
local users, as well as to modify LDAP and SSO accounts.

## Add Local User

To add a new user, click **+ Add local user**, fill out the **User Profile**
form, and click **Create user**.

To access IP Fabric, the new user must have one or more **Roles** assigned.

Users with no **Roles** assigned will get an `API_INSUFFICIENT_RIGHTS` error
upon logging in or accessing the API.

To add or modify **Roles**, follow the instructions in the [Roles](roles.md)
section.

![Add local user button and Create User form](../../images/settings/IP_Fabric_Settings-administration-users_users_add_local.png)

## List of Users

The `Users` table lists all local and non-local (LDAP and SSO) users,
including their details, and allows you to modify or delete them. _(Exception:
A currently logged-in user cannot delete their account.)_

![Users table](../../images/settings/IP_Fabric_Settings-administration-users_users_table.png)

## Edit Local User

1. To modify a local user's details or password, find the user in the `Users`
   table and click the **Edit** icon. (Optionally, you may select `Yes` in the
   `Local user` column header to show only local users.)

   ![Users table - edit local user](../../images/settings/IP_Fabric_Settings-administration-users_users_table_edit_local.png)

2. Then, to modify the user's details, update the data in the **User Profile**
   form and click **Update user profile**.

3. Or, to modify the user's password, fill out the **Update Password** form and
   click **Update Password**.

   ![Edit local user](../../images/settings/IP_Fabric_Settings-administration-users_users_edit_local.png)

## Edit LDAP/SSO User

LDAP/SSO users have **Roles** assigned via the LDAP/SSO configuration, hence
it's not possible to modify their **Roles** in the UI (unlike local users).

1. To edit an LDAP/SSO user, find the user in the `Users` table and click the
   **Edit** icon. (Optionally, you may select `No` in the `Local user` column
   header to show only non-local users.)

   ![Users table - edit LDAP/SSO user](../../images/settings/IP_Fabric_Settings-administration-users_users_table_edit_ldap.png)

2. Then, to modify the user's details, update the data in the **User Profile**
   form and click **Update user profile**:

   ![Edit LDAP/SSO user](../../images/settings/IP_Fabric_Settings-administration-users_users_edit_ldap.png)

## Delete User

1. To delete a user, find the user in the `Users` table and click the **Delete**
   icon:

   ![Users table - Delete icon](../../images/settings/IP_Fabric_Settings-administration-users_users_table_delete.png)

2. To confirm the action, click **Delete**:

   ![User will be deleted dialog](../../images/settings/IP_Fabric_Settings-administration-users_users_table_delete_confirm.png)

## Disable Local User's Access

To disable a local user's access to IP Fabric, follow the steps in
[Edit Local User](#edit-local-user) and remove all **Roles** assigned to that
user.
