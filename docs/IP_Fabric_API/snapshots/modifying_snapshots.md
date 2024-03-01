---
description: This page explains how you can modify snapshots via the SDK and the API.
---

# Snapshot Modifications

For modifying an existing snapshot, the following methods are available:

- refresh device(s)
- delete device(s)
- add device(s)
- rediscover devices with command timeout

## Using Python `ipfabric` SDK

**Added to `ipfabric` SDK version `6.6.3`.**

First, import and initialize `IPFClient` with selecting the loaded snapshot you wish to modify:

```python
from ipfabric import IPFClient

ipf = IPFClient('https://demo3.ipfabric.io/', auth='token', snapshot_id='$last')
```

### Refresh Device(s)

```python
ipf.snapshot.rediscover_devices(
     devices=['a2dff68', ipf.devices.all[0], 'BADSN'],
     wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5,
     skip_invalid_devices=True  # Default, see below
 )
```

- `skip_invalid_devices`:
  - `True`:
   - If a serial number is not found, then remove it from the device modification list.
   - If a Vendor API device and the Vendor were disabled in snapshot settings, then remove the device from the device modification list.
  - `False`: Will return `False` and not modify the snapshot if either of the previous tests found invalid devices.

### Delete Device(s)

```python
ipf.snapshot.delete_devices(
     devices=[ipf.devices.all[-1], 'BADSN'],
     wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5,
     skip_invalid_devices=True  # Default, see above
 )
```

### Refresh Vendor API Device(s)

```python
ipf.snapshot.refresh_vendor_api(wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5)
```

### Add Device(s)

```python
ipf.snapshot.add_ip_devices(
     ip=['1.1.1.1', '10.0.0.0/31'],  # Also accepts ipaddress.IPv4* objects
     wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5
 )
```

### Rediscover Devices With Command Timeout

```python
ipf.snapshot.retry_timed_out_devices(wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5)
```

If no command timeouts are found, it will return `True` stating:
`No Command Timeout Errors found in f4801ab7-c3ea-447d-94f7-31fad649a806, not refreshing snapshot.`

### Multi-Action Add Devices

Using this command, you can perform the following tasks in a single call:

- refresh Vendor API device(s)
- add device(s)
- rediscover devices with command timeout

```python
ipf.snapshot.add_devices(
    ip=['1.1.1.1', '10.0.0.0/31'],  # Also accepts ipaddress.IPv4* objects
    refresh_vendor_api=True,
    retry_timed_out=True,
    wait_for_discovery=True, wait_for_assurance=True, timeout=60, retry=5
)
```

## Using the API

### Refresh Device(s)

Do this in two stages:

1. Retrieve the snapshot ID and the serial numbers of the devices you want to
   update using, for example, `/tables/inventory/devices` with a request body like:

   ```json
   {
     "columns":["sn","hostname"],
     "filters":{"siteName",["like","L38"]}
     "snapshot":"$last"
   }
   ```

   This returns the actual snapshot ID for `$last`, and the list of serial numbers
   and hostnames for devices in the Site `L38`.

2. Send a `POST` to `/snapshots/XXXXXXXXXXX/devices`, where `XXXXXXXXXX` is the
   snapshot ID that needs to be refreshed, with a request body like:

   ```json
   {
     "snList":["SN_AAAA","SN_BBBB","SN_CCCC"]
   }
   ```

   Here, `SN_AAAA`, `SN_BBBB`, and `SN_CCCC` are the serial numbers of the
   devices that need to be updated. This triggers the update.

### Delete Device(s)

Do this in two stages:

1. First, get a list of serial numbers of the devices to remove from the snapshot (see the example above).

2. Send a `DELETE` to `/snapshots/XXXXXXXXXXX/devices`, where `XXXXXXXXXX` is the
   snapshot ID that devices need to be deleted from, with a request body like:

   ```json
   ["SN_AAAA","SN_BBBB","SN_CCCC"]
   ```

   Here, `SN_AAAA`, `SN_BBBB`, and `SN_CCCC` are the serial numbers of the
   devices that need to be deleted.

### Multi-Action Add Devices

Using this command, you can perform the following tasks in a single call:

- add device(s)
- rediscover devices with command timeout
- refresh Vendor API device(s) (not shown)
  - Vendor API JSON settings need to be edited prior to sending the request to IP Fabric.
  - Please use the `ipfabric` SDK client or open a ticket if you require an example using `curl`.

Send a `POST` to `/snapshots/XXXXXXXXXXX/devices`, where `XXXXXXXXXX` is the snapshot ID that needs to be modified, with a request body like:

```json
{
 "ipList":["10.0.0.1","10.0.1.0/24"],
 "retryTimedOut":true
 "vendorApi":[] // Required, see the note above
}
```

- `ipList`: 
  - List of IP addresses or CIDR networks of devices that need to be added.
  - This can be left as an empty list if you would like to only rediscover devices with command timeout.
- `retryTimedOut`:
  - Set to `true` to attempt rediscovering devices with command timeouts.
  - Will only retry devices found in `https://<FQDN>/snapshot-management/errors?showback=1&options={"filters":{"errorType":["eq","ABCommandTimeout"]}}`
