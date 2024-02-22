---
description: This section contains information how to trigger a manual configuration backup for a single device using an API call.
---

# Trigger Manual Configuration Backup

[Configuration Backups](../IP_Fabric_GUI/management/configuration.md) is a separate process from that of Discovery. 
This can be configured on a schedule or triggered by syslog in the IP Fabric GUI but can also be triggered using an 
API call.

Some example situations to use the API call:

- A new device was added to the network, but you don't want to wait until the next regular configuration backup collection.
- Syslog messages may not be parsed for all vendors.
- Perform a backup as a part of automation after a configuration change on a device.

## Python `ipfabric` SDK

The [python-ipfabric](../integrations/python) and is the easiest and simplest method to trigger a backup using the API.
This was added to the SDK in version `v6.0.0`.

```python
from ipfabric import IPFClient

ipf = IPFClient(base_url='<FQDN>', auth='<TOKEN>', verify=True)

# Trigger based on IP Address
status_code = ipf.trigger_backup(ip='<IP_OF_DEVICE_TO_BACKUP>')

# Trigger based on IP Fabric Unique Serial Number
status_code = ipf.trigger_backup(sn='<IPF_UNIQUE_SERIAL_NUMBER>')

# Trigger directly on a Device object
dev = ipf.devices.all[0]
status_code = dev.trigger_backup()
```

## Python3 `requests` Module

The Python3 [requests module](https://pypi.org/project/requests/) is a simple, yet elegant, HTTP library. To trigger a
single config backup, you need to set these parameters:

- Request resource `https://{hostname}/api/{api_version}/discovery/trigger-config-backup`
- Request type `POST`
- Request Body:
  - IP address: `{"ip": "<IP_OF_DEVICE_TO_BACKUP>"}`
  - Serial Number: `{"sn": "<IPF_UNIQUE_SERIAL_NUMBER>"}`

```python
from urllib.parse import urljoin

import requests

# Set FQDN and API Token of your IP Fabric installation
FQDN = "https://<FQDN>/"
TOKEN = "<TOKEN>"

# Set an IP Address or IP Fabric Unique Serial Number `sn`
IP = None  # "10.0.0.1"
SN = None  # "a24ff71"

api_version = requests.get(urljoin(FQDN, '/api/version')).json()['apiVersion']
url = urljoin(FQDN, f'/api/{api_version}/discovery/trigger-config-backup')

headers = {"Content-Type": "application/json", "X-API-Token": TOKEN}

if IP:
    response = requests.post(url, headers=headers, json={"ip": IP})
    response.raise_for_status()
    print(response.status_code)
if SN:
    response = requests.post(url, headers=headers, json={"sn": SN})
    response.raise_for_status()
    print(response.status_code)
```

## cURL from Linux Shell

To trigger a backup based on an IP Address:

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/discovery/trigger-config-backup' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{"ip": "<IP_OF_DEVICE_TO_BACKUP>"}'
```

To trigger a backup based on an IP Fabric Unique Serial Number (`sn`):

```shell
curl --location --request POST 'https://<FQDN>/api/<API_VERSION>/discovery/trigger-config-backup' \
--header 'Content-Type: application/json' \
--header 'X-API-Token: <YOUR_API_TOKEN>' \
--data-raw '{"sn": "<IPF_UNIQUE_SERIAL_NUMBER>"}'
```

!!! tip

    You can also execute this cURL command locally on the IP Fabric VM and can replace the FQDN with `localhost`.

!!! note

    If you are using a self-signed certificate use `-k` or `--insecure`.  Required if using `localhost` when running 
    the command locally on the IP Fabric VM.
