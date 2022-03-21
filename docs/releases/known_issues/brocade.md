# Brocade

**IP Fabric Version:** 4.3.X and up

**Description**: Brocade purchased Ruckus Wireless and uses the same MAC
OUI. In order to discover Brocade devices we have enabled “Brocade
Communications Systems LLC” and “Ruckus Wireless” in the Settings \> OUI
table.

**Issue for networks that contain Ruckus Wireless Equipment:** Because
we have enabled the OUI IP Fabric will try logging into all the Access
Points which has caused discovery to hang in our lab network.

**Fix for Ruckus Wireless environments that DO NOT have Brocade
devices**: Disable “Ruckus Wireless” in Settings \> OUI table.

**Fix for Ruckus Wireless environments that DO have Brocade devices
(either option should work)**:

-   Disable “Ruckus Wireless” in Settings > OUI table and add Brocade IP
    addresses to Settings > Discovery Seed

-   Add Ruckus Wireless IP addresses (must include /32 at the end of the
    address) in the Settings > Advanced > “IP networks to exclude from
    discovery and analysis”
