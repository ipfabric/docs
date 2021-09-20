# IP Fabric

## IP Fabric

-   Diagram displays device, which is not connected to anything. The
    situation appears when site separation prevents displaying the
    device on the other end. To show connection to a device, click “Show
    Edge Cloud”

-   Diagrams drilldown missing. Current diagrams offer vast amount of
    information, which is not available through drilldowns. More
    drilldown capabilities are planned for future releases.

-   Advanced Filter Visibility. When Advanced filter is applied, and
    then collapsed via advanced filter button
    (<img src="attachments/79036476/81657862.png?width=24" loading="lazy" data-image-src="attachments/79036476/81657862.png" data-unresolved-comment-count="0" data-linked-resource-id="81657862" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image29.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="9806dd06-3942-4ecd-a734-ff82543bad28" data-media-type="file" width="24" />),
    it’s not clear that filter is being applied to the table, except for
    the visible clear filter button
    (<img src="attachments/79036476/81657867.png?width=24" loading="lazy" data-image-src="attachments/79036476/81657867.png" data-unresolved-comment-count="0" data-linked-resource-id="81657867" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image30.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79036476" data-linked-resource-container-version="15" data-media-id="b65f86e6-0b63-46a5-89a3-7ff8306b647d" data-media-type="file" width="24" />).

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

### Snapshots (Release Candidate)

-   When Discovery is stopped mid way, and then Refresh is executed, the
    refresh does not consider IPs with status "STOP" for the next
    discovery

-   Resource check for sufficient RAM and HDD use a sliding window.
    Creating a new snapshot immediately after previous one may result in
    a "insufficient resources" failure. In such a case, verify resources
    on the status page and retry in several minutes.

-   Visualization does not work properly in Internet Explorer. Use
    Firefox or Chrome.

-   Switching site separation to RegEx can cause issues.

### Configuration management

**Description**: Format of configurations (show run etc) saved in IP
Fabric is changed, end of line characters were changed from rn to n

**Result**: Configurations saved before 2.1 and from 2.1 can show
differences when configurations are same

### Duplicate IP detection

**Description**: Anycast IP addresses are duplicate IP addressess
deployed at more than one location

**Result**: Anycast IP addresses are reported as duplicate addresses
