---
description: This section contains information on how to set up API discovery for Viptela. Viptela devices are discovered through the API (or the combination of API and CLI).
---

# Cisco Viptela

## Cisco Viptela SD-WAN

Starting with version `4.1.0`, IP Fabric supports the Viptela API. Viptela devices are discovered through the API (or the combination of API and CLI). Both CLI and vManage modes are supported. Some tasks, which retrieve information from templates, are supported only for devices in vManage mode (see our [Feature Matrix](https://matrix.ipfabric.io) for more details).

Since `6.8.0`, IP Fabric supports discovering Cisco Viptela devices in combined (hybrid) mode.

1. To add Viptela to global discovery settings, go to **Settings --> Discovery & Snapshots --> Discovery Settings --> Vendors API** and click **+ Add**:

   ![Add Vendor API](vendor_api_add.png)

2. Afterward, choose `Viptela` from the list and fill in:

   - **Username** and **Password** used to log in to vManage
   - **Base URL** of the vManage server (`https://vmanage-ip-address`)
   - [**Slug**](index.md#slug-and-comment)

3. Optionally, you may enable **Allow API+CLI combined discovery**, which allows the retrieval of data partially using API calls and partially using CLI commands.

   ![Add Connection - Viptela](viptela_api_add.png)

## Cisco Viptela cEdge

Starting with version `4.4.0`, IP Fabric supports Viptela on Cisco IOS XE devices in the controller (SD-WAN) mode (cEdge). Thus, from version `4.4.0`, cEdge devices are discoverable only through the vManage API.

## Known Issues

- [Viptela cEdge shows only one next-hop](../../../../support/known_issues/Vendors/cisco/Viptela_cEdge_shows_only_one_next_hop.md)
- [Viptela Serial Number (SN) Pairing in Cisco Coverage Checker](../../../../support/known_issues/Vendors/cisco/Viptela_vSmart_SN.md)
