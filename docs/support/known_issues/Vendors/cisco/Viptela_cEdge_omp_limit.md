---
description: This page explains the limit for OMP API calls that was added to prevent long discovery time.
---

# Viptela cEdge details of OMP routes might be missing

To properly model path lookup, information about OMP routes needs to be
downloaded with API endpoint
`/dataservice/device/omp/routes/received?deviceId=\<id\>`.

Cisco SD-WAN has a limitation of 3999 objects per
[API response](https://community.cisco.com/t5/sd-wan-and-cloud-networking/cisco-sd-wan-vmanage-api-omp-route-not-in-omp-received-api/m-p/4919774),
but this can vary depending on the vManage load.

If some routes are missing, IP Fabric will download OMP information for every
missing route using
`/dataservice/device/omp/routes/received?deviceId=\<id\>&prefix=\<prefix\>` API
endpoint.

This can generate a large number of API requests. To prevent long discovery
time, there is a default limit of **100 OMP API requests** since version `6.5`.

If you need to increase the default limit, contact the IP Fabric Support or
Solution Architect team.
