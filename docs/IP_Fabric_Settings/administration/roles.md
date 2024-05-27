---
description: This section contains information about RBAC roles to which you can assign policies, and then assign those roles to IP Fabric users.
---

# Roles

**Roles** allow users to perform actions on system resources (e.g., a
_user-management_ role with the _team_ policy assigned allows users to view,
add, update, or delete `users`, `roles`, `policies`, and `LDAP configuration`).

The **Roles** section (in **Settings --> Administration --> Roles**) allows you
to create or modify roles.

!!! note "`ipf-checker` Role"

    You may ignore the `ipf-checker` role, which is used by our internal
    diagnostics tool.

## Add Role

1. To add a new role, click **+ Add role**:

   ![Add role button](roles/roles_table.png)

2. Set a role name, description, select policies, and click **Save**:

   ![Add role form](roles/roles_add.png)

## List of Roles

The `Roles` table lists all roles, including their details, and allows you to
**modify** or **delete** them _(except for the built-in **admin** and
**ipf-checker** roles, which cannot be modified nor deleted)_.

![Roles table](roles/roles_table.png)

## Edit Role

1. To modify the details of a role, click the **Edit** icon next to it in the
   `Roles` table:

   ![Roles table - Edit icon](roles/roles_table_edit.png)

2. Update the data in the **Edit role** form and click **Save**:

   ![Edit role form](roles/roles_edit.png)

## Copy Role

1. To copy a role, click the **Copy** icon next to it in the `Roles` table:

   ![Roles table - Copy icon](roles/roles_table_copy.png)

2. Update the data in the **Copy role** form and click **Save**:

   ![Copy role form](roles/roles_copy.png)

## Delete Role

1. To delete a role, click the **Delete** icon next to it in the `Roles` table:

   ![Roles table - Delete icon](roles/roles_table_delete.png)

2. To confirm the action, click **Delete**:

   ![Role will be removed dialog](roles/roles_table_delete_confirm.png)
