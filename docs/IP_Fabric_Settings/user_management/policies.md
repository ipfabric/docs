# Policies

**Policies** can contain sets of **attributes or endpoints**.

**Attributes Scope** defines devices which are available to end users. Access is defined by a specific attribute such as **siteName**.

**API Endpoints Scope** defines actions which are permitted to end users to perform on allowed devices or in the system. Access is defined only to a **specific API endpoint** within the IP Fabric (e.g. *discovery* policy allows access to discovery API endpoints (actions)).

**Policies page** enables you to create or modify policies.

!!! attention

	Every `custom role` has to have at least 2 policies configured to see diagrams.
		
	  1. **Attributes Scope** policy defining `siteNames`
		
	  2. **API Endpoints Scope** policy defining access to **Graphs** API calls.

	Users with `admin` role have access to all attributes and endpoints by default.

## Add Attributes Scope Policy

1. To add a new policy click on **+ Add policy**.

	![Add policy button](policies_table.png)

2. By default the **Attributes scope** will be selected.

	![Add attribute policy](policies_attributes_add.png)

3. Set a policy name, add attributes (create a filters), select values and **save** your attribute policy.

	![Select attribute](policies_attributes_select.png)

## Add API Endpoint Policy

1. To add new policy click on **+ Add policy**.

	![Add policy button](policies_table.png)

2. Select **Api endpoints scope** 

	![Add endpoint policy](policies_endpoints_select.png)

3. Set a policy name, select API endpoints and **save** your endpoints scope.

## List of Policies

**Policies table** lists all policies including their details and enables you to **modify** or **delete** them _(with exception for built-in policies which cannot be modified or deleted)_.

![Policies Table](policies_table.png)

## Edit Policy

1. To modify policy details, click on **edit icon** in policies table.

	![Policies Table Edit](policies_table_edit.png)

2. Then to modify policy details update data in **Edit Policy** form and click on **Save**.

	![Edit Policy](policies_edit.png)

## Copy Policy

1. To copy policy, click on **copy icon** in policies table.

	![Policies Table Copy](policies_table_copy.png)

2. Then modify policy details in **Copy Policy** form and click on **Save**.

	![Copy Policy](policies_copy.png)

## Delete Policy

1. To delete policy, click on **delete icon** in table.

	![Policies Table Delete](policies_table_delete.png)

2. Then click on **Delete** to confirm action.

	![Policies Table Delete Confirm](policies_table_delete_confirm.png)
