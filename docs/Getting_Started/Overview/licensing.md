# Licensing

IP Fabric has a straightforward licensing concept. For every physical or virtual device in the network, with the exception of wireless access points, one license is used.

For example:

* A router with multiple VRFs counts as only one device in the license count
* Each virtual instance on a firewall (VSYS, VDOM, etc.) counts as one license each. If you have one firewall with 80 virtual instances, it will count as 80 devices in the license count
* A stack of switches (StackWise, etc.) count as one device in the license, regardless of the number of switches in the stack
* For wireless access points, a single license is consumed by the centralized controller, regardless of the number of APs controlled by it
* For cloud infrastructure providers, every construct (VPC, gateway, etc.) counts as one license

## Changes

### Release 4.4.0

From **4.4.0** every device (virtual or physical) will consume one license. This now applies to devices where information is collected via CLI or API. The only exception is wireless access points, which don't consume any licenses.

This change in licensing will affect the following vendors:

* SD-WAN -- Versa, Viptela, Silver Peak
* Wireless access points -- Meraki, Juniper MIST
* Cloud Infrastructure -- AWS, Azure

### Releases <= 4.3.X

For any release **4.3.X** or older, every device (virtual or physical) with information collected via CLI will consume one license. Any devices with information collected via API would _not_ consume a license. Examples of API-collected devices are SD-WAN (Versa, Viptela, Silver Peak), cloud wireless (Meraki) and cloud infrastructure (AWS).
