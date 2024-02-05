---
description: IP Fabric supports Cisco Firepower Zone Firewall feature which extends (to L7) and improves capabilities of IP Fabric to detect and correctly evaluate traffic.
---

# Dropping Support for ACL on Cisco Firepower

In IP Fabric `4.3`, we are introducing support for Cisco Firepower Zone
Firewall feature which extends (to L7) and improves capabilities of IP
Fabric to detect and correctly evaluate traffic.

Zone Firewall feature substitutes ACL feature for Cisco Firepower.
Therefore, ACL feature is no longer available for Cisco Firepower since
IP Fabric `4.3`.

To discover Cisco Firepower security policies and use Zone Firewall
feature in IP Fabric it is necessary to control Cisco Firepower through
Cisco FMC (Firewall Management Center) and provide IP Fabric with REST
API credentials so that IP Fabric can download all necessary information
from FMC.

When there are no credentials for Cisco FMC proved in IP Fabric, IP
Fabric will still be able to discover Cisco Firepower devices, but there
will be no security policies collected.
