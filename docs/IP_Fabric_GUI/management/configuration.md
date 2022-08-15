# Configuration

## Overview

Configuration management can be found at **Management → Configuration** and **backs up the running configuration** of managed network devices based on the defined trigger. Downloaded configuration is then available for viewing in full or sanitized formats, or for comparison. **Only changed configurations** are stored, and these report both the time of the last change and the time of the last configuration check for a change.

Configuration can be retrieved in `full` or `sanitized` forms. Sanitization removes all passwords and network identification information from the configuration to prevent sharing of sensitive information.

## Credential Requirements

Network access credentials allowing the `show run` command (or equivalent)
are necessary for configuration storage and configuration management to work properly. Please review [Authentication Settings](../../IP_Fabric_Settings/authentication.md).

![Config Credentials](config/config_auth.png)

These elevated credentials need **Use for configuration management** box checked.

## Trigger

Trigger archiving can be [configured in settings](../../IP_Fabric_Settings/advanced/configuration_management.md) and can be based on a *syslog message* or a *timed event*.


## Configuration Comparison Table

![Config Table](config/config_table.png)

Stored configurations are displayed in a table that shows information such as the serial number of the device, the device host name, the time when configuration change was detected (`Last Change At` column), and the last time a particular configuration was saved in the `Last Check At` column.

## Configuration Comparison

The table can be used to compare between two different configurations directly from the user interface. This is done by selecting the `Before` and `After` states to compare, and the resulting differences can be displayed side-by-side, inline with all rows, or inline with only rows where the changes have occurred.

### Side by Side Diff

![Side by Side](config/config_side.png)

### Inline

![Inline](config/config_inline.png)

### Inline Diff

![Inline](config/config_inline_diff.png)