---
description: Configuration management backs up the running configuration of managed network devices based on the defined trigger.
---

# Configuration

## Overview

Configuration management can be found in **Management --> Configuration** and **backs up the running configuration** of managed network devices based on the defined trigger. The downloaded configuration is then available for viewing in full or sanitized formats or for comparison. **Only changed configurations** are stored, and these report both the time of the last change and the time of the last configuration check for a change.

Configurations can be retrieved in `full` or `sanitized` forms. Sanitization removes all passwords and network identification information from the configuration to prevent the sharing of sensitive information.

## Credential Requirements

Network access credentials allowing the `show run` command (or equivalent)
are necessary for configuration storage and configuration management to work properly. Please review [Device Credentials](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/device_credentials.md).

![Config Credentials](config/config_auth.png)

These credentials need to have the **Use for configuration management** box
checked.

## Trigger

Trigger archiving can be [configured in settings](../../IP_Fabric_Settings/configuration_management.md) and can be based on a _syslog message_ or a _timed event_.

## How To Read Configuration Management Data

There are the following properties in the Management configuration table:

- `Serial Number` -- Serial number of the device.
- `Hostname` -- Device hostname.
- `Last Change At` -- The last time before the very next config change.
- `Last Check At` -- The last config file check before the very next configuration change.
- `Status` -- Config state indicator that tells you whether:
  - `changed` -- The config changed within the last check (initial value).
  - `no change` -- The config did not change within the last check.
- `Hash` -- Unique ID of the configuration file.

Note that every table row, once you filter output for a specific hostname, represents a modified configuration file. When a new configuration is found (either brand new or different from previous) for a given device, it is committed to git, and the new record is entered into the DB, with status set to `changed`. Next time the device's configuration is checked, there are two options:

1. The configuration file remains the same, in which case, the status field of the DB record is set to `no change`, and `Last Check At` is set to the current time.
2. The configuration file is changed again, in which case, the new configuration is committed to git, and a new DB record is inserted into the DB with status `changed` and `Last Change At` and `Last Check At` being set to current time, as described above.

Let's consider the following example:

![Configuration table example](config/config_table_example.png)

Let's go from the bottom of the output:

- `Last Change At` is `2025-03-17, 14:00:14 Z`, and `Last Check At` is `2025-03-17, 14:00:14 Z` with status `changed`
  - It means that configuration file changed in the last check.
- `Last Change At` is `2025-03-17, 14:15:10 Z`, and `Last Check At` is `2025-03-17, 14:30:09 Z` with status `no change`.
  - It means there were no configuration file changes between these two timestamps.
  - Configuration file was checked multiple times, and status transitioned from `changed` to `no change`.

## Comparing Configurations

Stored configurations are displayed in a table that shows information such as the serial number of the device, the device hostname, the time when configuration change was detected (the `Last Change At` column), and the last time a particular configuration was saved in the `Last Check At` column.

The table can be used to compare between two different configurations directly from the user interface. This is done by selecting exactly 2 configuration states to compare followed by clicking the `Compare` button.

![Selecting configs for comparison](config/config_select_compare.png)

There is also a shortcut for comparing configurations directly with their previous state by clicking this button instead:

![alt text](config/config_quick_comparison.png)


!!! Note "Last configuration quick compare behaviour"

    For the last configuration, the quick compare behaviour is the same as for the second to last configuration. That is to say, it compares the last configuration to the second to last configuration instead of a 'previous' one.

The resulting differences can be displayed side-by-side, inline with all rows, or inline with only rows where the changes have occurred.

<figure markdown>
  ![Side by side](config/config_side_by_side.png)
  <figcaption>Side by side</figcaption>
</figure>

<figure markdown>
  ![Inline](config/config_inline.png)
  <figcaption>Inline</figcaption>
</figure>

<figure markdown>
  ![Inline diff](config/config_inline_diff.png)
  <figcaption>Inline diff</figcaption>
</figure>
