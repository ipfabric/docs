---
description: In this section, IP Fabric publishes previous version releases of NIMPEE v1.x.x
---

# NIMPEE v1.x.x

### Version 1.0.6

**System BugFixes**

-   Added firewall rule for Syslog 514/UDP​
-   Debugging tool fixes
-   Added DB parameter tuning (THP disabled)

### Version 1.0.5

**Platforms**

-   Cisco SG300

**Features**

-   ACL table - intelligent port filter
-   Site report - inventory description column added

**Fixes**

-   IOS route leaking parsing
-   VPC info was not collected
-   Risk graph EoX and reload now based on traffic impact
-   NX-OS ACL matches statement fix
-   /32 routes to discovery
-   NX-OS error-disabled parsing
-   Bridge-groups stp parsing
-   C890 WLAN interface parsing

### Version 1.0.4

**System Features**

-   added update script
-   Added automatic HTTPS redirect

**System BugFixes**

-   Debugging tools fixes

### Version 1.0.3

**Features**

-   Added calculation of affected users on L3 paths
-   Dashboard capacity and performance tables improvement
-   Routing graph mesh to cloud

**Fixes**

-   Affected users calculation in partially discovered network fix

**System Features**

-   Improved MOTD for "nimpee" troubleshooting user
-   HTTPS access.
-   HTTPS certificate wizard is now part of the initial configuration
-   Image hardening
-   network configuration wizard automatically pre-fill current values
    (for example current hostname or domain name)
-   Remote support SSL VPN

**System BugFixes**

-   Simplified bandwidth management
-   Added ability to rerun initial boot wizard
-   User configured BW limit is still in place after the reboot
-   DNS is now properly configured in case of static IP address
-   NTP configuration was not properly applied

### Version 1.0.2

**Fixes**

-   Continuous analysis log overflow fix
-   Improved systemd process control

### Version 1.0.1

**Features**

-   Periodic run of Analysis
-   L3 affected users on L2 path
-   L3 Uplink calculation

**Protocol support**

-   Mac address collection now supports static entries

**UI improvements**

-   Mac table now includes edge port flag, VLAN and source
    (dynamic/static) columns

**Fixes**

-   Risk radar chart calculation for routing stability fix
-   Cache for analyzing API routes
-   L2 affected users network mac addresses removed

### Version 1.0.0

**UI improvements**

-   IP-aware lookups
-   Lookup IP via VLSM prefix
-   Lookup Route via single IP
-   Faster tables, table filtering
-   Case insensitive search
-   Regex filtering support
-   Rearranged menu as L1/L2/L3 items

**Diagrams**

-   Routing domain diagrams
-   End to End Path lookup diagram
    -   added vrf support
    -   added RPF
    -   added neighboring domains

**Analytics**

-   Site uplink calculation
-   Table sorting by severity (color)
-   Added human readability
-   Transfer rates: added Mcast/bcast/packets and overall loss impact to
    transfer rates

**Protocols and technology support**

-   Routing
    -   Routing domain overview
-   ACL
    -   Added ACL support
    -   Added IP ACL interface table
    -   Added Reflexive ACL support
-   FEX support
    -   Users connected to FEX are displayed on the diagrams
-   vPC support
-   ARP
    -   Added ARP state table
    -   Added ARP VRF Support
    -   Added Proxy ARP Support
-   MAC
    -   Added MAC state table
-   Added CDP/LLDP neighborship tables

**Management and technical visibility**

-   Added connectivity matrix
-   Added syslog target
    -   Lookup and filter by message, mnemonic, system time, sequence
        number
-   Added Configuration management
    -   Sanitization of configurations
    -   Configuration comparison
-   Improved Low-Level Design document export
    -   Added connectivity matrix, OS versions, CDP/LLDP neighbors

**Enterprise features**

-   Added integrated support
-   Configurable site boundary detection
-   Configurable operational scope
-   Added first boot wizard
-   Added Automated error reporting
-   Added Licensing
