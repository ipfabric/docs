---
description: This page describes known issues with Opengear and how to fix them.
---

# Opengear

## Opengear IM -- `$` Prompt Detection

**Known affected platforms:** Opengear IM

**Description:** IP Fabric cannot detect the prompt if it contains only the `$`
(dollar) sign.

**Fix:** To discover Opengear with a `$`-only prompt, enable the needed
[feature flag](../../../System_Administration/Command_Line_Interface/Feature_Flags.md#opengear-prompt-detection).

## Opengear OM -- Slow response to NTP command

**Description:** The NTP task may get stuck, causing the discovery of the device to terminate. This issue is due to an overloaded daemon on the device, resulting in a slow response and a timeout on the SSH connection.

**Fix:** Increase SSH timeout or disable NTP task for Opengear vendor, or at least for og-om family.

## Opengear IM -- LLDP task using `sudo` password

**Description:** To collect LLDP information, `sudo lldpcli show chassis` and `sudo lldpcli show neighbors` commands are used. Enable passwords are used for `sudo` access.

**Fix:** To correctly obtain all LLDP-related information, the password for `sudo` access must be configured as the enable password.
