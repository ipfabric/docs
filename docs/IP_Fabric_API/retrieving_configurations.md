---
description: This tech note describes how you can retrieve configuration files from IP Fabric’s configuration management capability, to be consumed outside the platform.
---

# Retrieving configurations

This tech note describes how you can retrieve configuration files from IP Fabric’s configuration management capability, to be consumed outside the platform.

You do this in two stages:

1. send a POST to `/tables/management/configuration` with a request body like

    ```json
    {
      "columns":["id", "hash", "hostname", "lastChangeAt", "lastCheckAt", "reason", "sn", "status"]
    }
    ```

    You can of course filter that list (for example for devices containing `L36`) with a `key:value` pair.

    ```json
    "filters": {
      "hostname": ["like","L36"]
    }
    ```
    Or you can select the range of dates you are interested in:

    ```json
    "filters": {
      "lastCheckAt": ["gte",XXXXXXXXXXXXXX]
    }
    ```
    where XXXXXXXXXXXXXX is the [UNIX epoch time](https://www.epoch101.com/) representing the start of the time range.

    This gives you the list of saved configurations, and most importantly, the "hash" for each.

2. send a `GET` to `/tables/management/configuration/download?hash=XXXXXXXXXXXXX` where `XXXXXXXXXXXXX` is the hash for the required config from the list returned in step 1. This returns the plain text of the configuration in question.
