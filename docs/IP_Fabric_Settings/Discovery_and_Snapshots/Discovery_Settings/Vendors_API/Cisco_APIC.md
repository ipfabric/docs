---
description: This section contains information how to set up API discovery for Cisco APIC.
---

# Cisco APIC

Starting version `5.0`, IP Fabric collects information from APIC controllers and provides information about Tenants (including Contexts/VRFs, Applications, Endpoint groups and Contracts) and APIC cluster members.

Information about controllers is collected via SSH.

Tenants, applications, contracts etc. data are collected via API.

To successfully collect data from Cisco APIC, it is necessary to configure Cisco APIC in the global Vendor API settings and to add the Cisco APIC IP address to the discovery seeds.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Discovery
Seeds** and add Cisco APIC IP address.

Go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors
API** and click **+ Add**.

Afterwards, choose `Cisco APIC` from the list and fill in:

- **Username and password** used to log in to Cisco APIC

  ??? info "Username if Local Domain is set on the APIC"

      If local domain is set on your APIC controller the format of the `username` for IP Fabric settings is

      ```text
      apic:LOCAL-DOMAIN-NAME\\username
      ```

      ![APIC login screen](apic_local_domain.png)
      ![IPF Settings screen](local_domain_apic_ipf_settings.png)

- **Base URL** of Cisco APIC, e.g. `https://cisco-apic-ip-address`

- [**Slug**](index.md#slug-and-comment)

![Cisco APIC api add](cisco/apic/ciscoApicAPIAdd.png)
