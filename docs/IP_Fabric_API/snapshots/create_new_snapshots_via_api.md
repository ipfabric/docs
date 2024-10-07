---
description: This page explains how to create a new snapshot using the API.
---

# Create New Snapshots via API

This page explains how to create a new snapshot using the API. You may want to create a new snapshot with the existing settings or with a different set of settings, for example, if you wanted to have a reduced scope.

## API Endpoints

- `/api/{api_version}/snapshots` -- A `POST` method to create a new snapshot.

- `/api/{api_version}/settings` -- A `GET` method to collect all IP Fabric settings.

## Header Authentication

Headers must contain:

- `Content-Type: application/json`
- `X-API-Token:` -- An API token generated in IP Fabric Settings.

## Create a New Snapshot With the Existing Settings

If you want to start a discovery using the existing settings, it is a simple `POST` request to `/api/{api_version}/snapshot`, without a body.

![configure of Creating snapshot](configure_of_Creating_snapshoot.gif)

## Create a New Snapshot With Different Settings Than the Default Ones

What if you wanted a snapshot for a smaller scope of your network? For this, you can use the API to start a new discovery with some specific settings used for that specific discovery.

Here is an example of a body to use to perform a discovery with a new scope (`networks`), new seed devices (`seedList`), and not considering the Vendor APIs (Check Point, Meraki, AWS, etc.) that you may have configured in your settings. (All fields are optional. If not specified, the values from your settings will be used.)

!!! example title="Example Snapshot creation using IP Fabric API"

    Example Snapshot POST JSON Body:
    ```js
    {
        "snapshotName": "Name of the Snapshot",
        "snapshotNote": "Some notes to describe the snapshot",
        "networks":
            {
                "exclude": [],
                "include": [ "10.66.0.0/16" ]
            },
        "seedList": [ "10.66.255.104/31", "10.66.0.1/32" ],
        "vendorApi": []
    }
    ```

    Example cURL command:
    ```bash
    curl -X POST 'https://{ipf_server}/api/{api_version}/snapshots' \
      --header 'Content-Type: application/json' --header 'X-API-Token: {api_token}' \
      -d '{"snapshotName":"Name of the Snapshot","snapshotNote":"Some notes to describe the snapshot","networks":{"exclude":[],"include":["10.66.0.0/16"]},"seedList":["10.66.255.104/31","10.66.0.1/32"],"vendorApi":[]}'
    ```

Let’s see how it looks when using Postman:

![create snapshot](create_snapshot.gif)

## Settings for Creating a New Snapshot

There is a long list of what you can use in the request body to change the settings for this new discovery. The example above is probably enough for some use cases. If you wanted to change different settings, you can collect the settings of your IP Fabric instance via a `GET` on the endpoint `/api/{api_version}/settings`.

The response will look like this _(this is just an extract of the JSON)_:

```json title="Snapshot settings JSON"
{
    "fullBgpLimit": {
        "enabled": true,
        "threshold": 500000
    },
    "networks": {
        "exclude": [],
        "include": [
            "10.66.0.0/16"
        ]
    },
    "resolveNames": {
        "discoveryDevices": true
    },
    "scanner": {
        "enabled": false
    },
    "traceroute": {
        "scope": [
            "10.0.0.0/8",
            "100.64.0.0/10",
            "169.254.0.0/16",
            "172.16.0.0/12",
            "192.168.0.0/16"
        ],
        "protocol": "icmp",
        "port": null
    },
    "limitDiscoveryTasks": {
        "alreadyDiscovered": false,
        "sourceOfTasks": [
            "arp",
            "routes",
            "trace",
            "xdp"
        ]
    },
    "allowTelnet": true,
    "timeouts": {
        "login": 20,
        "session": 20
    },
    "cliSessionsLimit": {
        "enabled": false
    },
    "cliRetryLimit": {
        "default": 3,
        "authFail": 0,
        "tacacs": {
            "retry": 0,
            "delay": 1000
        }
    },
    "seedList": [
        "10.66.255.104/31",
        "10.0.0.1/32"
    ],
    [...]
```

Most fields can be entered in the body of the request to change the settings when performing a new discovery.

This won’t affect the settings for the next scheduled discovery.
