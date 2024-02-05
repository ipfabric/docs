---
description: This page describes known issues with Brocade and how to fix them.
---

# Brocade

**IP Fabric version:** `4.3.x` and newer

**Description:** Brocade purchased Ruckus Wireless and uses the same MAC OUI.
To discover Brocade devices, we have enabled `Brocade Communications
Systems LLC` and `Ruckus Wireless` in the **OUI** table (in **Settings -->
Discovery & Snapshots --> Global Configuration --> OUI**).

**Issue for networks that contain Ruckus Wireless equipment:** Because we have
enabled the OUI, IP Fabric will try logging in to all the Access Points which
has caused discovery to hang in our lab network.

**Fix for Ruckus Wireless environments that DO NOT have Brocade devices**:
Disable `Ruckus Wireless` in **Settings --> Discovery & Snapshots --> Global
Configuration --> OUI**.

**Fix for Ruckus Wireless environments that DO have Brocade devices (either
option should work)**:

- Disable `Ruckus Wireless` in **Settings --> Discovery & Snapshots --> Global
  Configuration --> OUI** and add Brocade IP addresses to **Settings -->
  Discovery & Snapshots --> Discovery Settings --> Discovery Seeds**.

- Add Ruckus Wireless IP addresses (must include `/32` at the end) in **Settings
  --> Discovery & Snapshots --> Discovery Settings --> Discovery --> IP Scope
  --> IP networks to exclude from discovery and analysis**.
