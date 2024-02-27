---
description: This page explains how to refresh devices in a snapshot using the API.
---

# Refreshing Devices in a Snapshot

Do this in two stages:

1. Retrieve the snapshot ID and the serial numbers of the devices you want to
   update using, for example, `/tables/inventory/devices` with a request body
   like:

   ```json
   {
     "columns":["sn","hostname"],
     "filters":{"siteName",["like","L38"]}
     "snapshot":"$last"
   }
   ```

   This returns the actual snapshot ID for `$last`, and the list of serial
   numbers and hostnames for devices in the site `L38`.

2. Send a `POST` to `/snapshots/XXXXXXXXXXX/devices`, where `XXXXXXXXXX` is the
   snapshot ID that needs to be refreshed, with a request body like:

   ```json
   {
     "snList":["SN_AAAA","SN_BBBB","SN_CCCC"]
   }
   ```

   Here, `SN_AAAA`, `SN_BBBB`, and `SN_CCCC` are the serial numbers of the
   devices that need to be updated. This triggers the update.
