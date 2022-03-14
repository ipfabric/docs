# Configuration

# Configuration Management

## Overview

Configuration management **backs up the running configuration** of managed network devices based on the defined trigger. Downloaded configuration is then available for viewing in full or sanitized formats, or for comparison.
**Only changed configurations** are stored, and these report both the time of the **last change** and the **time of the last** configuration **check** for a change.

Link: `https://\[nimpee_address\]/management/configuration/first`

### Credential Requirements

Network access **credentials allowing** **the “show run” command** (or equivalent) **are necessary** for configuration storage and configuration management to work properly.
These credentials are set-up in ***Setting → Authentication*** menu. These elevated credentials need ***Use for configuration management*** box checked.
See [Authentication](Authentication)

### Trigger

Trigger archiving can be [configured in settings](Configuration_Management) and can be based on a **syslog message** or a **timed event**.

## Configuration

Configuration can be retrieved in **full** or **sanitized forms**. **Sanitization removes all of the passwords and network identification information** from the configuration to prevent sharing of sensitive information.

### Configuration Comparison Table

**Stored configurations are displayed in a table** that shows information such as the serial number of the device, the device host name, the time when configuration change was detected (“Last change” column),
and the last time a particular configuration was saved in the “Last check” column.

The table can be used to compare between two different configurations directly from the user interface. This is done by selecting the “Before” and “After” states to compare,
and the resulting differences can be displayed side-by-side, inline with all rows, or inline with only rows where the changes have occurred.
