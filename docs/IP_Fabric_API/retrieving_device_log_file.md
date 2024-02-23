---
description: This page describes how you can retrieve log files for a device from IP Fabric's discovery to be consumed outside the platform.
---

# Retrieving Device Log File

This page describes how you can retrieve log files for a device from IP Fabric's
discovery to be consumed outside the platform.

Do this in two stages:

1. Send a `POST` to `/tables/inventory/devices` with a request body like:

   ```json
   {
     "columns": ["hostname", "taskKey"],
     "snapshot": "$last"
   }
   ```

   You can (and probably would) filter that list (for example, for a specific
   device with the hostname `SWITCH01`) by including a `key:value` pair:

    ```json
    "filters": {
      "hostname": ["eq","SWITCH01"]
    }
    ```

    This provides you with the task ID for the discovery of the device in
    question.

2. Send a `GET` to `/os/logs/task/XXXXXXXXXXXXX`, where `XXXXXXXXXXXXX` is the
   `taskKey` value returned in step 1 for the required network device. This
   returns the plain text of the log file for that device discovery.
