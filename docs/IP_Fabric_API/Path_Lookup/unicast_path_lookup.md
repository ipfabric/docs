---
description: This section gives your the list of the Request Parameters for the Unicast Path Lookup with an example.
---

# Unicast Path Lookup

## Request Parameters

- `parameters` _\[mandatory\]_ - A nested JSON data structure with keys
  - `type` _\[mandatory\]_ - A string with a value of `pathLookup` for an E2E path simulation output
  - `pathLookupType` _\[mandatory\]_ - A string containing the word `unicast`
  - `protocol` _\[mandatory\]_ - A string with a value of `tcp`, `udp`, `icmp`
  - `startingPoint` _\[mandatory\]_ - A string containing the source IP address or subnet
  - `destinationPoint` _\[mandatory\]_ - A string containing the destination IP address or subnet
  - `groupBy` _\[mandatory\]_ - A quoted string representing the grouping of devices in the output - at this time one of `siteName`, `routingDomain` or `stpDomain`.
  - `networkMode` _\[mandatory\]_ - A boolean - the new version of IP Fabric allows you to simulate paths between subnets. Setting this key to `true` means that you will create a single result representing the subnets; `false` means that IP Fabric will create a separate path for each source or destination in the range of addresses up to a maximum of 255.
  - `securedPath` _\[mandatory\]_ - A boolean - when you run a path simulation, you can tell IP Fabric if you want to stop when it hits a security policy which blocks the traffic in question (`true`) or complete the forwarding path and highlight the policy enforcement point (`false`)
  - `ttl` _\[mandatory\]_ - integer - Time-to-live value (default is `128`)
  - `fragmentOffset` _\[mandatory\]_ - integer - Fragment offset value (default is `0`)
  - `enableRegions` _\[mandatory\]_ - boolean - (default `false`)
  - `srcRegions` _\[mandatory\]_ - string - (default `.*`)
  - `dstRegions` _\[mandatory\]_ - string - (default `.*`)
  - `otherOptions` _\[mandatory\]_ - nested JSON data
    - `applications` _\[mandatory\]_ - string - (default `.*`)
    - `tracked` _\[mandatory\]_ - boolean - (default `false`)
  - `firstHopAlgorithm` _\[mandatory\]_ - nested JSON data
    - `type` _\[mandatory\]_ - Either `automatic` or `userDefined`
    - `vrf` _\[Optional and if type == `automatic`\]_
    - `entryPoints` _\[mandatory and if type == `userDefined`\]_ - nested array of JSON data
      - `hostname` _\[mandatory\]_ - Hostname string
      - `sn` _\[mandatory\]_ - IP Fabric Unique Serial Number string
      - `iface` _\[mandatory\]_ - Interface name
  - `l4Options` _\[mandatory\]_ - nested JSON data
    - If `protocol = tcp`
      - `srcPorts` _\[mandatory\]_ - A string representing ports; ex. `80,443,1025-4096`
      - `dstPorts` _\[mandatory\]_ - A string representing ports; ex. `80,443,1025-4096`
      - `flags` _\[mandatory\]_ - An array of TCP flags to be set in the simulated path or empty array
        - Valid flags: [`ack`, `fin`, `psh`, `rst`, `syn`, `urg`]
    - If `protocol = udp`
      - `srcPorts` _\[mandatory\]_ - A string representing ports; ex. `80,443,1025-4096`
      - `dstPorts` _\[mandatory\]_ - An integer representing the destination port
    - If `protocol = icmp`
      - `type` _\[mandatory\]_ - An integer representing the ICMP type
      - `code` _\[mandatory\]_ - An integer representing the ICMP code

## Example minimal request body

```jscript
{
    "snapshot": "$last",
    parameters": {
    "destinationPoint": "10.35.253.58/32",
    "groupBy": "siteName",
    "networkMode": false,
    "pathLookupType": "unicast",
    "securedPath": false,
    "startingPoint": "10.241.1.203",
    "type": "pathLookup",
    "firstHopAlgorithm": {
      "type": "automatic"
    },
    "protocol": "tcp",
    "enableRegions": false,
    "srcRegions": ".*",
    "dstRegions": ".*",
    "ttl": 128,
    "fragmentOffset": 0,
    "otherOptions": {
      "applications": "(.*)",
      "tracked": false
    },
    "l4Options": {
      "dstPorts": "80,443",
      "srcPorts": "1024",
      "flags": []
    }
}
```
