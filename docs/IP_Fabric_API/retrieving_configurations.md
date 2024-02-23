---
description: This page describes how you can retrieve configuration files from IP Fabric's configuration management capability to be consumed outside the platform.
---

# Retrieving Configurations

This page describes how you can retrieve configuration files from IP Fabric's
configuration management capability to be consumed outside the platform.

Do this in two stages:

1. Send a `POST` to `/tables/management/configuration` with a request body like:

   ```json
   {
     "columns":["id", "hash", "hostname", "lastChangeAt", "lastCheckAt", "reason", "sn", "status"]
   }
   ```

   Of course, you can filter that list (for example, for devices containing
   `L36`) with a `key:value` pair:

   ```json
   "filters": {
     "hostname": ["like","L36"]
   }
   ```

   or you can select the range of dates you are interested in:

   ```json
   "filters": {
     "lastCheckAt": ["gte",XXXXXXXXXXXXXX]
   }
   ```

   where `XXXXXXXXXXXXXX` is the [UNIX epoch time](https://www.epoch101.com/)
   representing the start of the time range.

   This gives you the list of saved configurations, and most importantly, the
   "hash" for each of them.

2. Send a `GET` to
   `/tables/management/configuration/download?hash=XXXXXXXXXXXXX`,
   where `XXXXXXXXXXXXX` is the hash for the required configuration from the
   list returned in step 1. This returns the plain text of the configuration in
   question.
