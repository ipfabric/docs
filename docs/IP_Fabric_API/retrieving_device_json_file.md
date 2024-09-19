---
description: This page describes how you can retrieve device JSON files from IP Fabric's discovery to be consumed outside the platform.
---

# Retrieving Device JSON File

This page describes how you can retrieve JSON files for a device from IP Fabric
to be consumed outside the platform.

## Overview

The JSON file contains all the information about a device after IP Fabric has parsed the 
command outputs found in the [log file](retrieving_device_log_file.md) and normalized the data. This data can be 
easily consumed by external automation for further processing.

```json title='Example device file'
{
    "attemptCount": 1,
    "errorReasonsList": [],
    "ip": "10.35.254.1",
    "isLoggedIn": true,
    "timestamp": 1724882430,
    "tryDeviceAgain": false,
    "vCollectId": "vCollect/a9c6ca82-0e7d-4cc8-9cbd-b8b43a1b3051",
    "versionDetail": {
        "vendor": "cisco",
        "family": "ios",
        "platform": "i86bi_linux",
        "model": "",
        "featureSet": "adventerprisek9",
        "major": "15",
        "minor": "5",
        "maintenance": "2",
        "train": "t",
        "alpha": "",
        "rebuild": "",
        "devTypeList": [],
        "version": "15.5(2)T"
    },
    "vTaskId": "vTask/0b597d69-1d38-4967-b711-3665da27258d",
    "status": "ok",
    "logFile": "/home/autoboss/snapshots/a9c6ca82-0e7d-4cc8-9cbd-b8b43a1b3051/cli/10.35.254.1/2024-08-28T22:00:30.389Z_discovery_telnet.gz",
    "credentialsId": "cb99c0e9-8d5f-4d94-a5a6-d72059f136d2",
    "sn": {
        "sn": "a15ff97",
        "snHw": "a15ff97"
    },
    "arp": [{
            "ip": "10.21.151.151",
            "mac": "0021.81ca.79cf",
            "intL3Name": "Et0/1",
            "ipLong": 169187223,
            "ouiEnabled": false
        },
        ...
```

## Using API and Bash

Do this in three stages:

1. Send a `POST` to `/tables/inventory/devices` with a request body like:

   ```json
   {
     "columns": ["hostname", "sn"],
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

   This provides you with the IP Fabric Unique Serial Number `sn` for the discovery of the device in
   question. Please note the `_meta['snapshot']` value in the response as you are required to use the UUID
   and not a snapshot reference (`$last`).

2. Convert the `sn` value to a URL safe base64 encoded value:

   ```shell
   > echo "SERIAL_NUMBER" | base64 | tr '/+' '_-' | tr -d '='
   U0VSSUFMX05VTUJFUgo
   ```

3. Send a `GET` to `/api/v#.#/snapshots/<SNAPSHOT_ID>/devices/XXXXXXXXXXXXX/json`, where `XXXXXXXXXXXXX` is the
   base64 encoded value (`U0VSSUFMX05VTUJFUgo`) returned in step 2 for the required network device. The
   `SNAPSHOT_ID` must be the actual snapshot UUID (located in the `_meta` of the returned data in step 1) and not a 
   snapshot reference ID. This returns the JSON device data for that device discovery.

## Using the Python SDK

Using the [python-ipfabric](https://pypi.org/project/ipfabric/) Python SDK this has been simplified to the following (requires `ipfabric>=v6.9.5`).

```python
from ipfabric import IPFClient

ipf = IPFClient()
device = ipf.devices.by_sn['DEVICE_SERIAL_NUMBER']
json_log = device.get_json()
```
