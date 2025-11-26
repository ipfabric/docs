---
description: This page explains how the discovery via Vendor APIs works.
---

# How API Discovery Works

Starting with version `3.8`, the IP Fabric platform can combine CLI
(Command-Line Interface) discovery with API (Application Programming Interface)
discovery.

Please consider connectivity requirements for the platform when planning to add
cloud or SD-WAN vendors for API discovery.

API discovery is not automated and requires manually adding all necessary
HTTP endpoints to initiate connection to in **Settings --> Discovery & Snapshots
--> Discovery Settings --> Vendors API**.

The settings common for all Vendor APIs are described in the [Vendors API Overview](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/index.md).

List of supported Vendor APIs (the links lead to the settings specific for each
vendor):

- [AWS](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/AWS_Amazon_Web_Services.md)
- [Azure](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Azure.md)
- [Check Point Management](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Check_Point.md)
- [Cisco APIC](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Cisco_APIC.md)
- [Cisco FMC](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Cisco_FMC.md)
- [Forcepoint](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/forcepoint.md)
- [Google Cloud Platform](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/GCP_Google_Cloud_Platform.md)
- [Juniper Mist](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/juniper_mist.md)
- [Meraki REST](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Cisco_Meraki.md)
- [Prisma](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/PaloAlto_Prisma.md)
- [Ruckus Virtual SmartZone](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Ruckus_Virtual_SmartZone.md)
- [Silver Peak](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Silver_Peak_SD-WAN.md)
- [Versa](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Versa_Networks_SD-WAN.md)
- [Viptela](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/Cisco_Viptela_SD-WAN.md)
- [VMware NSX-T](../../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/Vendors_API/VMware_NSX-T.md)

All Vendor API clients share the same behaviors described below.

## Rate Limiting

When a Vendor API client needs to apply rate limiting, it instantiates its own
rate limiter. Then, any request is sent only when the rate limiter has free
capacity. The rate limiting is determined by:

- capacity
- refill rate
- refill rate interval

The rate limiting algorithm is based around the standard
[token bucket](https://en.wikipedia.org/wiki/Token_bucket) rate limiting
algorithm. The bucket fills up with permissions to send a request at a constant
rate (the refill rate each refill rate interval). When a client wants to make a
request, it consumes one token from the bucket. If the bucket is empty, the
request gets queued until a token becomes available. The bucket has a capacity
that limits the burstiness of the requests.

The rate limiter also ensures an even distribution of accepted requests over
time and doesn't allow short-term request spikes. It attempts to distribute all
requests equally through time (the refill rate interval) with some random
fluctuation.

## Automatic Session Renewal

If the Vendor API requires the client to log in or to create a session with a
specified expiration, the Vendor API client actively tries to renew it. The
first attempt is sent at 80% of the session lifetime. If the renewal request
doesn't succeed, it is repeated while data requests can be sent until the
session expires.

## Expired Session Detection and Handling

If the Vendor API requires the client to log in or to create a session, the
Vendor API client creates it and takes care of its timely renewal. Note that
there are cases when the session can become invalid before its expiration. The
Vendor API client is aware of this and can detect it. When such a situation is
detected, the session is immediately renewed, and the discovery continues.

## Overloaded Server Detection and Handling

Although the discovery process respects the configured rate limiting parameters,
the discovery traffic is not the only traffic the Vendor API server has to
serve, so the server can become overloaded. The Vendor API clients are aware of
this and can detect it. When the overloaded server situation is detected, the
Vendor API client waits for some time and sends all unanswered requests again.
Vendor API clients apply exponential backoff for the wait time. If the
overloaded server situation is not mitigated for some time, the Vendor API
discovery is terminated.

## Recoverable Network Errors

Vendor API clients are aware of some recoverable network errors (e.g.,
`ECONNRESET`, `ECONNABORTED`, `ECONNREFUSED`). When a recoverable network error
is detected, the request is not immediately rejected but is resent with
exponential backoff. If the network error is not mitigated for some time, then
the request is rejected -- but the Vendor API discovery can continue with
additional requests.

## Vendor-Specific Cases

Some Vendor APIs have specific situations that are detected and handled to
increase the probability of successful discovery.

### Unreachable Viptela Devices

Sometimes, some Viptela devices are unreachable for a short time. The Viptela
client is aware of this -- it detects it and repeats the request again to
increase the probability of successful discovery. The request for an unreachable
device is terminated only when it fails more than the configured number of
times. Whenever that happens, the discovery of other devices can continue.
