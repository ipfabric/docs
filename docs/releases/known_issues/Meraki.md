# Meraki

## Meraki

**Known Affected platforms**: All

**Description**: Meraki API has limited functionality and doesn’t
provide all necessary data for our model. Following issues are known:

-   Multiple Meraki devices can have the same public IP

<!-- -->

-   CDP/LLDP might be not linked between devices correctly as reported
    port ID doesn’t allow it

-   CDP/LLDP timespan is 2h, so it might not show actual state

-   ARP is missing, MAC table is reconstructed from endpoints

-   DHCP/STATIC doesn’t provide IP mask

-   STP is missing

-   Routing table static routes only for Firewalls

-   Pathlookup is not working because tables for forwarding are not all
    provided

-   Can't add Meraki device into snapshot (refresh works)

-   Limited snapshot - Meraki tasks will be always downloaded

-   MX firewall uplink ports - not possible to determine if traffic load
    balancing is enabled and/or which port is primary and backup

-   Multiple Meraki devices can have the same public IP

Following issues will be resolved in future IP Fabric releases

-   Can't add Meraki device into snapshot (refresh works)

-   Mini snapshot - Meraki will be always downloaded

-   All discovered devices from Meraki are licensed (no matter if it's
    Meraki AP)
