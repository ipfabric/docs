# Cisco APIC

Starting version 5.0 IP Fabric collects information from APIC controller and provides information about Tenants (including Contexts/VRFs, Applications, Endpoint groups and Contracts) and APIC cluster members.

Information about controller is collected via SSH.

Tenants, applications, contracts etc. data are collected via API.

To successfully collect data from Cisco APIC it is necessary to configure Cisco APIC in global Vendor API settings and to add Cisco APIC IP address to the discovery seeds.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Discovery
Seeds** and add Cisco APIC IP address.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors
API** and press the **+Add** button.

Afterwards, choose **Cisco APIC** from the list and fill in:

- **Username and password** used to log in to Cisco APIC

- **Base URL** of Cisco APIC, e.g. `https://cisco-apic-ip-address`

![Cisco APIC api add](cisco/apic/ciscoApicAPIAdd.png)

## Know issues

[APIC Tables are all empty except Controllers](../../../../support/known_issues/Vendors/cisco/apic_tables_empty.md)
