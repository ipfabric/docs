# Cisco Meraki

## Cisco Meraki

Starting the version 3.5.0, IP Fabric supports API based discovery for
Cisco Meraki.

Meraki requires the following settings to be applied:

-   API key - Generated in [Meraki
    dashboard](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API)

-   Organizations ID - You can specify which organization will be
    included in the discovery process. If you do not specify, all
    available IDs will be used

-   Version - Meraki currently provides only a v0 version of their API.
    This version has a lot of limitations ([Meraki known
    issues](Meraki))

-   Base URL - URL is supported in the following
    format [https://nXYZ.meraki.com/api.](https://nXYZ.meraki.com/api) Be
    aware that the dashboard can redirect communication to a different
    URL
