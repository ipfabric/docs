---
description: This page explains the limit for OMP API calls that was added to prevent long discovery time.
---

# Viptela cEdge details of OMP routes might be missing

To properly model path lookup, information about OMP routes needs to be
downloaded with API endpoint
`/dataservice/device/omp/routes/received?deviceId=<id>`.

Cisco SD-WAN has a limitation of 3999 objects per
[API response](https://community.cisco.com/t5/sd-wan-and-cloud-networking/cisco-sd-wan-vmanage-api-omp-route-not-in-omp-received-api/m-p/4919774),
but this can vary depending on the vManage load.

If some routes are missing, IP Fabric will download OMP information for every
missing route using
`/dataservice/device/omp/routes/received?deviceId=<id>&prefix=<prefix>` API
endpoint.

This can generate a large number of API requests. To prevent long discovery
time, there is a default limit of **100 OMP API requests** since version `6.5`
(`ompRoutesReceivedPrefixRequestLimit`). If you need to increase the default
limit, contact the IP Fabric Support or Solution Architect team.

!!! quote "Cisco TAC comment on this issue"

    For omp received or advertised routes API issues, he confirmed that this is limitation up to 4K only.

    From the lab repro, I increased the prefix scale to 1K but the DE advised
    that the router also includes TLOCs and others and my lab is exceeding 4K limit
    so this is why API doesn't return all routes and they get truncated:

    > 4000 is the max limit for routes via NetConf.

    `cEdge1#show sdwan omp summary | inc routes-` this command confirms if the
     router exceeded the limit:

    ```
    routes-received 4144
    routes-installed 40
    routes-sent 4084
    mcast-routes-received 0
    mcast-routes-installed 0
    mcast-routes-sent 0
    ```

    And the 4000 number is not just for prefixes, but incl. children RIB-INs as
    well. routes are counted per rib-ins, not prefixes, prefixes will be lesser,
    but with tlocs it will become 4000

    it’s a limitation via Netconf per the engineering team ; because of system
    cpu/memory limits because of which we have seen ConfD crashes in the field
    previously with too large number of routes, below is the reference defect by
    which DE added this 4K limit:

    > Type of behavior change: vManage real-time omp received and advertised routes limit
    >
    > Release introduced: for 17.6 right now, will keep backporting to old releases.
    >
    > Old behavior: There is no limit to vManage real-time omp received and advertised routes. But when the total number/setup scale is large, ConfD might crash.
    >
    > New behavior( starting from 17.3.5 onwards): Added a limit to vManage real-time omp received and advertised routes. The limit total routes, more specifically, the row number in vManage UI is 4001.
    >
    > Impact on customer: To avoid ConfD crash, only the first 4001 route entries will be shown in vManage UI.

    To solve this, they need to add pagination support from vManage to device.
    There is a Sev6 present for this requirement -- ``CSCvu59961`:

    > Need to add pagination support so that vManage can pull the large amount of API data in batches.”

    So, you need to track this enhancement request `CSCvu59961` with your Cisco
    account team to expedite its progress so the development team can enhance this
    limit.
