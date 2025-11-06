---
description: This page explains how to apply an Attribute filter in the IP Fabric GUI, which will quickly limit the scope of data that will be displayed in tables.
---

# Global Filter

Applying an **Attribute filter** in the IP Fabric GUI will quickly limit the
scope of data that will be displayed in tables. Currently, adding a filter will
not update Intent Rules or the **Dashboard** (in development).

![Attribute filter](global_filter/attribute_filter.webp)

The options for filtering are:

- Site Name
- Routing Domain
- STP Domain
- Any Snapshot Local Attribute[^1]

[^1]:
    See [Device Attributes](../IP_Fabric_Settings/Discovery_and_Snapshots/Global_Configuration/device_attributes.md).
    Please note that after configuring a new **Device Attribute** globally, a
    new snapshot must be run for applying it.

![Select attribute](global_filter/select_attribute.webp)

In this example, we are filtering on `siteName` with the value `35COLO`.

![Select value(s) for siteName](global_filter/select_values_for_sitename.webp)

In **Inventory --> Devices**, we can see that the **Device Inventory** table is
filtered to show only devices from the Site `35COLO`.

![siteName 35COLO selected](global_filter/sitename_selected.webp)

![Attribute filter for siteName 35COLO applied](global_filter/attribute_filter_applied.webp)
