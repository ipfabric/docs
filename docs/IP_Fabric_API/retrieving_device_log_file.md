---
description: This tech note describes how you can retrieve log files for a device from IP Fabric’s discovery, to be consumed outside the platform.
---

# Retrieving device log file

This tech note describes how you can retrieve log files for a device from IP Fabric’s discovery, to be consumed outside the platform.

You do this in two stages:

1. send a POST to `/tables/inventory/devices` with a request body like

    ```json
    {
      "columns": ["hostname", "taskKey"],
      "snapshot": "$last"
    }
    ```

    You can (and probably would) filter that list (for example for a specific device with the hostname `SWITCH01`) by including a `key:value` pair.

    ```json
    "filters": {
      "hostname": ["eq","SWITCH01"]
    }
    ```

    This gives you the task ID for the discovery for the device in question.

2. send a `GET` to `/os/logs/task/XXXXXXXXXXXXX` where `XXXXXXXXXXXXX` is the `taskKey` value returned in step 1 for the required network device. This returns the plain text of the log file for that device discovery.
