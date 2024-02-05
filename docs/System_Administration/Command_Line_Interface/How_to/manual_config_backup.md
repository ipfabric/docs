---
description: This section contains information how to trigger a manual configuration backup for a single device using an API call.
---

# How to Trigger Manual Configuration Backup for a Single Device

You have added a new device to the network, but you don't want to wait until the next regular configuration backup collection. In that case, you can trigger config backup through IP Fabric's API.

## Use Python3 `requests` Module

The Python3 [requests module](https://pypi.org/project/requests/) is a simple, yet elegant, HTTP library. To trigger a single config backup, you need to set these parameters:

- request resource `https://{hostname}/api/{api_version}/discovery/trigger-config-backup`
- request type `POST`
- define IP address in the request body as `{"ip": "ip_address"}`

```python
import json
import requests

# Set FQDN and version of your IP Fabric installation
url = "https://FQDN/api/API_VERSION/discovery/trigger-config-backup"

payload = json.dumps({ "ip": "IP_OF_DEVICE_TO_BACKUP" })

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Token': 'YOUR_API_TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Alternatively Use cURL from Linux Shell

```shell
curl --location --request POST 'https://FQDN/api/API_VERSION/discovery/trigger-config-backup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Token: YOUR_API_TOKEN' \
--data-raw '{
	  "ip": "IP_OF_DEVICE_TO_BACKUP"
}'
```
