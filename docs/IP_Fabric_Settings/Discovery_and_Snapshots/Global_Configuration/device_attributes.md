---
description: IP Fabric allows adding attributes to a device based on the IP Fabric Unique Serial Number.
---

# Device Attributes

Version `4.3` introduced the ability to add attributes to a device based on the IP
Fabric Unique Serial Number. In versions before `6.0.0`, this only supported
manually changing a device's `siteName`, `routingDomain`, or `stpDomain`. IP Fabric
now supports adding custom attributes. Attribute names may not contain any
spaces or special characters.

## Attribute Requirements

![Attribute field warning](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-device_attributes_device_attributes_warning.webp)

Attribute names must match the following regex:
`/^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]+$/`. The underscore `_` is valid and will
later be used to denote hierarchical attributes (i.e., `REGION_COUNTRY`).

## Global Attributes

Attributes can be assigned globally or locally to an individual snapshot. To
assign global attributes, navigate to **Settings --> Discovery & Snapshots -->
Global Configuration --> Device Attributes**. Once an attribute is assigned, a
new snapshot is required for it to be applied.

![Device Attributes table](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-device_attributes_device_attributes.webp)

- `Serial number` is IP Fabric's "Unique Serial Number" (API column
  `sn`). Note that this is not the `Serial Number` column, which represents the
  Hardware SN (API column `snHw`). Devices discovered via API can also be
  assigned using Device Attributes.

- `Hostname` is populated by IP Fabric when a device matching the `Serial
  number` is found.

- `Attribute` is the Device Attribute to assign.

- `Value` is the attribute's value to assign.

### Creating Rules in the UI

To create a rule in the UI, click **+ Add attribute** and fill out the form:

![Device Attributes - create rule](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-device_attributes_device_attributes_rules.webp)

The dropdown is intuitive and will let you search based on SN or hostname.

![Device Attributes - dropdown](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-device_attributes_device_attributes_dropdown.webp)

### Creating Rules via the API

This is the preferred method of creating rules as it allows for bulk importing.

| Method | Put                                                                                                         |
| :----- | :---------------------------------------------------------------------------------------------------------- |
| URL    | `https://<IPF_URL>/api/v6.0/attributes/global`                                                              |
| Data   | `{"attributes": [{"sn": "<IPF SERIAL NUMBER>", "value": "<ATTRIBUTE NAME>", "name": "<ATTRIBUTE VALUE>"}]}` |

### Creating Global Attributes in Python

Please see the examples at
[`examples/settings/attributes_mgmt_ip.py`](https://gitlab.com/ip-fabric/integrations/python-ipfabric/-/blob/develop/examples/settings/attributes_mgmt_ip.py)
and
[`examples/settings/attributes_sitename.py`](https://gitlab.com/ip-fabric/integrations/python-ipfabric/-/blob/develop/examples/settings/attributes_sitename.py).

## Local Attributes

Local or "Snapshot-Specific" Attributes are applied during discovery and stored
in the snapshot file separate from the global settings. Currently, you are able
to:

1. Update from the global settings:
  1. Update global device attributes in **Settings --> Discovery & Snapshots --> Global Configuration --> Device Attributes**.
  2. Go to **Discovery Snapshot**.
  3. Select a snapshot and navigate to its **Settings --> Device Attributes**.
  4. Click **Override with global settings**.
2. Use the API (or Python SDK) to view, add, or edit a snapshot's Local Attributes.

Editing a snapshot's Local Attributes will require recalculations if a device's `siteName`,
`routingDomain`, or `stpDomain` have been changed.

### Creating Local Attributes in Python

Please see the example at
[`examples/settings/local_attributes.py`](https://gitlab.com/ip-fabric/integrations/python-ipfabric/-/blob/develop/examples/settings/local_attributes.py).

## Device Attributes Import/Export

The device attributes import/export feature allows you to manage custom device attributes using CSV files, making it easy to bulk-add or update device information.

![Device Attributes Import/Export](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-device_attributes_device_attributes_import_export.webp)

### Export Functionality

#### Export Current Data
- Click the **Export** button to download all existing device attributes as a CSV file.
- The file will be named `Device_Attributes.csv`.
- The CSV file contains the following columns: Serial Number, Hostname, Attribute, Value.

### Import Functionality

#### File Requirements
- **Format:** CSV file only
- **Maximum size:** 10 MB
- **Required columns:** Serial Number, Attribute, Value
- **Optional column:** Hostname (for reference only)

#### Import Options

##### Import Data
- Adds new attributes from the CSV file.
- **Duplicate handling:** Prevents adding attributes that already exist for a device; duplicate rows are ignored and the import continues.
- Existing data remains unchanged.

##### Import & Replace
- This option **overrides** all existing attributes and **imports** new ones.
!!! warning  "Warning"
    
	Use with caution — this operation completely replaces your attribute data.
