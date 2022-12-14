---
description: This section gives your the list of the Request Parameters for the Host to Gateway Path Lookup with an example.
---

# Host to Gateway Path Lookup

## Request Parameters

- `parameters` *\[mandatory\]* - A nested JSON data structure with keys

  - `type` *\[mandatory\]* - A quoted string with a value of `pathLookup` for an E2E path simulation output

  - `pathLookupType` *\[mandatory\]* - A quoted string containing the word `hostToDefaultGW`

  - `startingPoint` *\[mandatory\]* - A quoted string containing the IP address to search

  - `vrf` *\[optional\]* - A quoted string of the VRF (Not supplying this will default to _auto-detect_)

!!! example Example minimal request body

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
