---
description: This section contains information how to set up API discovery for Cisco FMC.
---

# Cisco FMC (FTD)

Starting version 4.3 IP Fabric collects zone-firewall related data for Cisco
Firepower devices **only via** Cisco FMC API. Cisco Firepower devices are
still discovered via SSH so if Cisco Firepower devices are not managed via FMC
they will still be discovered but **without** security related information.

To discover Cisco Firepower security policies and use the Zone Firewall feature
in IP Fabric it is necessary to control Cisco Firepower through Cisco FMC
(Firewall Management Center) and add Cisco FMC in global vendor API settings.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors
API** and click the **+Add** button.

Afterwards, choose **Cisco FMC** from the list and fill in:

- **Username and password** used to log in to Cisco FMC
- **Base URL** of Cisco FMC server, e.g. `https://cisco-fmc-ip-address`

![Cisco FMC api add](cisco/fmc/ciscoFmcAPIAdd.png)

## Known issues

[FMC REST API Calls Returns HTTP Error Code 500](../../../../support/known_issues/Vendors/cisco/FMC_REST_API.md)
