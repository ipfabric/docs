---
description: This section contains information on how to set up API discovery for F5OS.
---

# F5OS

## Supported F5OS Variants

- **F5OS-A** (R-series)
- **F5OS-C** (VELOS)

## How to Add F5OS to API discovery

- Navigate to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API**.
- Click **+ Add**
- From the list, choose: 
  - `F5OS-A (R)` or
  - `F5OS-C (VELOS)`
- Fill in:
  - **Username** and **Password** used to log in to all F5OS base URLs
  - **Base URLs** line separated list of base URLs sharing the same username and password (e.g., `https://f5os-ip-address/api`)
  - [**Slug**](index.md#slug-and-comment)
  - [**Comment**](index.md#slug-and-comment)

## How VELOS discovery works
- You should provide the actual controller URL.
- IP Fabric will discover the controller, download partition information from it, then attempt to connect to the partitions and discover them as devices using the same credentials as the controller.

  !!! Summary
      You must ensure that the same credentials are configured on both the controller and its partitions to enable IPF to fully discover the F5 VELOS system.
  !!! Note 
      Tenants on both systems (F5OSA, F5OSC) are discovered using CLI.

![Add Connection - F5OS](f5os/F5OS_add_connection.webp)

