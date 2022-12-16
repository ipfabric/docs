# How to trigger manual configuration backup for a single device

After adding a new device to the network, and you don't want to wait until the next regular configuration backup collection, you can trigger config backup through IP Fabric's API. Here's how.

## Use Python3 `requests` module

The Python3 [requests module](https://pypi.org/project/requests/) is simple, yet elegant, HTTP library. To trigger a single config backup, we need to set these parameters:

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

## Alternatively use cURL from Linux shell

```shell
curl --location --request POST 'https://FQDN/api/API_VERSION/discovery/trigger-config-backup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Token: YOUR_API_TOKEN' \
--data-raw '{
	  "ip": "IP_OF_DEVICE_TO_BACKUP"
}'
```
