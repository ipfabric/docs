---
description: On this page, we explain the IP Fabric licensing concept.
---

# Licensing

IP Fabric has a straightforward licensing concept. One license is consumed for every physical or virtual device in the network, excluding wireless access points.

For example:

* A router with multiple VRFs counts as only one device in the license count.
* Each virtual instance on a firewall (VSYS, VDOM, etc.) counts as one license each. If you have one firewall with 80 virtual instances, it will count as 80 devices in the license count.
* A stack of switches (StackWise, etc.) count as one device in the license, regardless of the number of switches in the stack.
* For wireless access points, a single license is consumed by the centralized controller, regardless of the number of APs controlled by it.
* For cloud infrastructure providers, one license is consumed by each networking construct (VPC, gateway, etc.).

!!! info

  	If IP Fabric cannot detect the device type of a discovered device (due to missing information from the CLI or API calls), the device will be counted as unlicensed.

## Changes

### Release 4.4.0

Starting from version `4.4.0`, every device (virtual or physical) will consume one license. This now applies to devices where information is collected via CLI or API. The only exception is wireless access points, which do not consume any licenses.

This change in licensing will affect the following vendors:

* SD-WAN -- Versa, Viptela, Silver Peak
* Wireless access points -- Meraki, Juniper MIST
* Cloud infrastructure -- AWS, Azure

### Releases <= 4.3.x

For versions `4.3.x` or older, every device (virtual or physical) with information collected via CLI will consume one license. Any devices with information collected via API would _not_ consume a license. Examples of API-collected devices are SD-WAN (Versa, Viptela, Silver Peak), cloud wireless (Meraki), and cloud infrastructure (AWS).

## Expired License

When your license expires:

* You will not be able to log in to the IP Fabric main GUI.
* New snapshots will not be created, and automatic snapshots will stop.
* API calls may still work.
* Configuration management will run in the background.
