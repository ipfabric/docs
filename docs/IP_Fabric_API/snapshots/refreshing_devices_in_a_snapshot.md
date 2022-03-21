# Refreshing devices in a snapshot

Do this in two stages:

1.  Retrieve the snapshot ID and the serial numbers of the devices you want to update using eg **/tables/inventory/devices** with a request body like

    ```js
    {
      "columns":["sn","hostname"],
      "filters":{"siteName",["like","L38"]}
      "snapshot":"$last"
    }
    ```

    to return the actual snapshot ID for $last, and the list of serial numbers and hostnames for devices in site L38.

2.  send a POST to **/snapshots/XXXXXXXXXXX/devices** where XXXXXXXXXX is the snapshot ID that needs to be refreshed with a request body like

    ```jsc
    {
      "snList":["SN_AAAA","SN_BBBB","SN_CCCC"]
    }
    ```

    Where SN_AAAA, SN_BBBB, SN_CCCC are the serial numbers of the devices that need to be updated. This triggers the update.
