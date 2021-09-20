# IP Fabric's API

The following API endpoints are available in IP Fabric. Descriptions and
allowed methods are coming soon. For more information about IP Fabric
API, please, read: <https://docs.ipfabric.io/api/>

# Technology Table Endpoints

The technology tables use **POST requests only** for reading information
and the payload is used to specify or filter requested data from listed
tables. The **POST & DELETE request** can be used for Intent
verification rules at each endpoint. At every technology table, search
for the question mark button that will expose the endpoints (can be used
with filters as well).

<img src="attachments/1105690625/1163198480.png" class="image-center" loading="lazy" data-image-src="attachments/1105690625/1163198480.png" data-height="828" data-width="1555" data-unresolved-comment-count="0" data-linked-resource-id="1163198480" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200521-121659.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1105690625" data-linked-resource-container-version="9" data-media-id="94f0448e-6b95-4d11-a645-30c37e43814e" data-media-type="file" />

## Payload definition

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
{
  columns:[],
  filters:{},
  pagination:{},
  snapshot:"snapshotID",
  reports:""
}
```

</div>

</div>

-   **columns** - specifies columns that we request for the endpoint

-   **filters** - filtering options, for any column or intent
    verification
    `{"vendor":["like","cisco"],"family":["eq","lap"],"reload":["color","eq","0"]}`(optional)

-   **pagination** - specifies tha pagination and response limits
    `{"limit":26,"start":0}` (optional)

-   **snapshot** - defines snapshot ID or we can use: $last, $prev,
    $lastlocked

-   **reports** - Intent rules definition (optional)

For more information, please, see:
<https://docs.ipfabric.io/api/#header-request-payload>

## Endpoint definition

<https://server/api/v1/tables/> + endpoint

aci/endpoints  
aci/vlan  
aci/vrf  
addressing/arp  
addressing/duplicateIp  
addressing/hosts  
addressing/mac  
addressing/managedDevs  
addressing/nat  
fhrp/balancing  
fhrp/glbpForwarders  
fhrp/groupMembers  
fhrp/groupState  
fhrp/stprootAlignment  
interfaces/aql  
interfaces/connectivityMatrix  
interfaces/drops  
interfaces/duplex  
interfaces/errors  
interfaces/inconsistencies  
interfaces/load  
interfaces/mtu  
interfaces/portChannel  
interfaces/switchports  
interfaces/transceivers  
interfaces/transferRates  
inventory/devices  
inventory/discoveryHistory  
inventory/fans  
inventory/interfaces  
inventory/modules  
inventory/phones  
inventory/pn  
inventory/powerSuppliesFans  
inventory/powerSupplies  
inventory/sites  
management/changes  
management/configuration  
management/connectivityErrors  
management/discoveryRuns  
management/flow  
management/logging  
management/ntp  
management/osverConsistency  
management/portMirroring  
management/snmp  
mpls/forwarding  
mpls/l2Vpn  
mpls/l3Vpn  
mpls/ldp  
multicast/igmp  
multicast/pim  
multicast/routes  
neighbors/all  
neighbors/unidirectional  
neighbors/unmanaged  
networks/domain  
networks/networks  
networks/pathLookupChecks  
networks/routeStability  
networks/routes  
networks/summary  
platforms/cluster  
platforms/fex  
platforms/poe  
platforms/stack  
platforms/vdc  
platforms/vpc  
qos/marking  
qos/policing  
qos/policyMaps  
qos/priorityQueuing  
qos/queuing  
qos/randomDrops  
qos/shaping  
reports/capacity  
reports/discoveryErrors  
reports/discoveryTasks  
reports/eof  
reports/performance  
reports/settingsOui  
routing/protocols  
security/aaa  
security/acl  
security/dhcp  
security/dmvpn  
security/enabledTelnet  
security/ipsec  
security/securePorts  
security/zoneFirewall  
spanningTree/bridges  
spanningTree/guards  
spanningTree/inconsistencies  
spanningTree/instances  
spanningTree/neighbors  
spanningTree/ports  
spanningTree/radius  
spanningTree/topology  
spanningTree/vlans  
vlan/deviceSummary  
vlan/device  
vlan/networkSummary  
vlan/siteSummary  
vrf/detail  
vrf/interfaces  
vrf/summary  
vxlan/interfaces  
vxlan/peers  
vxlan/vni  
vxlan/vtep  
wireless/accessPoints  
wireless/clients  
wireless/controllers  
wireless/radio  
wireless/ssidSummary

# Settings & Snapshots

Multiple request types are available (GET, POST, PATCH, DELETE or PUT),
depends on the endpoint type.

[https://server/api/v1/](https://server/api/v1/tables/) + endpoint

auth  
discovery  
filter  
graph  
license  
os  
report  
settings  
site  
snapshot  
support  
user

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200521-121659.png](attachments/1105690625/1163198480.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200521-121659.png](attachments/1105690625/1162739746.png)
(image/png)  

</div>
