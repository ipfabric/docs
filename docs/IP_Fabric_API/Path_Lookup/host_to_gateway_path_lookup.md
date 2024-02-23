---
description: This page provides you with the list of the request parameters for the host-to-gateway path lookup, along with an example.
---

# Host-to-Gateway Path Lookup

## Request Parameters

- `parameters` *\[mandatory\]* -- A nested JSON data structure with keys:

  - `type` *\[mandatory\]* -- A quoted string with a value of `pathLookup` for an end-to-end path simulation output.

  - `pathLookupType` *\[mandatory\]* -- A quoted string containing the word `hostToDefaultGW`.

  - `startingPoint` *\[mandatory\]* -- A quoted string containing the IP address to search.

  - `vrf` *\[optional\]* -- A quoted string of the VRF. (Not supplying this will default to _auto-detect_.)

!!! example "Example Minimal Request Body"

    ``` js
    {
        "snapshot": "$last",
        "parameters": {
        	"groupBy": "siteName",
        	"pathLookupType": "hostToDefaultGW",
        	"startingPoint": "10.241.1.203",
        	"type": "pathLookup"
        }
    }
    ```
