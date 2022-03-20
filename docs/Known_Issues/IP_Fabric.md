# IP Fabric

-   Diagram displays device, which is not connected to anything. The
    situation appears when site separation prevents displaying the
    device on the other end. To show connection to a device, click “Show
    Edge Cloud”
-   Diagrams drilldown missing. Current diagrams offer vast amount of
    information, which is not available through drilldowns. More
    drilldown capabilities are planned for future releases.
-   Jumphost can be activated only from support console.
-   TACACS may be limited to the specific maximum number of simultaneous
    authentication sessions, preventing discovery of all of the devices
    in the network. If fewer than expected number of devices are
    discovered, decrease bandwidth rate (i.e. to 3Mb/s), increase
    SSH/TELNET session timeout (e.g. to 30 seconds), and decrease the
    maximum number of simultaneous sessions (i.e. 40).
-   Inter-platform spanning-tree topology enumeration requires L2
    discovery protocol to form a connection when
    port_id.port_priority.port_id field separation boundary is in
    inconsistent position between the two platforms.
-   Site separation - Changing “Firewall in site” and new
    discovery/recalculation can change site names.
-   Visualization does not work properly in Internet Explorer. Use
    Firefox or Chrome.
-   Switching site separation to RegEx can cause issues.

## Configuration management

***Description***: Format of configurations (show run etc) saved in IP
Fabric is changed, end of line characters were changed from rn to n

***Result***: Configurations saved before 2.1 and from 2.1 can show
differences when configurations are same

## Duplicate IP detection

***Description***: Anycast IP addresses are duplicate IP addressess
deployed at more than one location

***Result***: Anycast IP addresses are reported as duplicate addresses