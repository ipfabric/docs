---
description: This section contains information about RBAC policies, how they work and how to set them.
---

# Policies

**Policies** can contain sets of **attributes or endpoints**.

**Attributes scope** defines devices which are available to end users. Access is
defined by a specific attribute such as **siteName**.

**API endpoints scope** defines actions which are permitted for end users to
perform on allowed devices or on the system. Access is defined only to a
**specific API endpoint** within IP Fabric (e.g., _discovery_ policy allows
access to discovery API endpoints (actions)).

The **Policies** page allows you to create or modify policies.

!!! attention

    Every `custom role` has to have at least 2 policies configured to see
    diagrams:

      1. **Attributes scope** policy defining `siteName`s

      2. **API endpoints scope** policy defining access to **Graphs** API calls

    Users with `admin` role have access to all attributes and endpoints by
    default.

## Add Attributes Scope Policy

1. To add a new policy, click **+ Add policy**:

   ![Add policy button](policies/policies_table.png)

2. Click **Attributes scope**:

   ![Add attributes scope policy](policies/policies_attributes_add.png)

3. Set a policy name, add attributes (create filters), select values, and
   **save** your attributes scope policy:

   ![Select attributes scope policy](policies/policies_attributes_select.png)

## Add API Endpoints Scope Policy

1. To add a new policy, click **+ Add policy**:

   ![Add policy button](policies/policies_table.png)

2. **API endpoints scope** should be selected by default:

   ![Add API endpoints scope policy](policies/policies_endpoints_add.png)

3. Set a policy name, select API endpoints and **save** your API endpoints scope
   policy:

   ![Select API endpoints scope policy](policies/policies_endpoints_select.png)

## List of Policies

The **Policies** table lists all policies including their details and allows
you to **modify** or **delete** them _(with the exception of the built-in
policies which cannot be modified or deleted)_.

![Policies table](policies/policies_table.png)

## Edit Policy

1. To modify the details of a policy, click the **Edit** icon next to it in the
   **Policies** table:

   ![Policies table - edit](policies/policies_table_edit.png)

2. Update the data in the **Edit policy** form and click **Save**:

   ![Edit policy form](policies/policies_edit.png)

## Copy Policy

1. To copy a policy, click the **Copy** icon next to it in the **Policies**
   table:

   ![Policies table - copy](policies/policies_table_copy.png)

2. Update the data in the **Copy policy** form and click **Save**:

   ![Copy policy form](policies/policies_copy.png)

## Delete Policy

1. To delete a policy, click the **Delete** icon next to it in the **Policies**
   table:

   ![Policies table - delete](policies/policies_table_delete.png)

2. Click **Delete** to confirm the action:

   ![Confirm deletion](policies/policies_table_delete_confirm.png)
