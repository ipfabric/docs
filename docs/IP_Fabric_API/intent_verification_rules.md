---
description: This page describes the association between the intent verification rules and the technology tables and explains how to read those associations through the API.
---

# Intent Verification Rules

This page describes the association between the intent verification rules and the technology tables and explains how to read those associations through the API.

The results of the intent verification checks are identified as "reports" in the API and essentially consist of a series of rules by which columns in the technology tables are colored.

## Instructions

To handle the intent verification checks and be able to act on them, there is a series of steps.

The first step is to fetch a list of the reports from the snapshot you're interested in. This involves a simple GET request to `/api/{api_version}/reports?snapshot=<id>`, where `<id>` is either the `$last` or a valid snapshot ID. The returned JSON dictionary is a list of reports created in the snapshot, providing information about:

- the table they relate to
- the columns colored by the test
- the conditions for each color
- the values used to mark the columns

!!! example

    Example of DMVPN status report:

    ```json
        {
            "groups": [
                {
                    "id": "318508186",
                    "custom": false,
                    "name": "Stability"
                }
            ],
            "apiEndpoint": "/v1/tables/security/dmvpn",
            "checks": {
                "0": {
                    "and": [
                        {
                            "state": [
                                "eq",
                                "UP"
                            ]
                        }
                    ]
                }
            },
            "column": "state",
            "custom": false,
            "defaultColor": 20,
            "descriptions": {
                "checks": {
                    "0": "DMVPN tunnels that are in the 'UP' state.",
                    "10": "",
                    "20": "DMVPN tunnels that are in other than the 'UP' state.",
                    "30": ""
                },
                "general": "Verifies the operational state of Dynamic Multipoint VPN (DMVPN) tunnels.\n"
            },
            "name": "DMVPN Tunnel State",
            "webEndpoint": "/technology/security/dmvpn",
            "id": "322178616",
            "status": -1,
            "result": {}
        }
    ```

Breaking this down, we can see that the report:

- is called "DMVPN Tunnel State"
- is presented in the "Stability" group on the dashboard
- relates to the technology table accessed through the API endpoint `/api/{api_version}/tables/security/dmvpn` or the web UI endpoint `/technology/security/dmvpn`
- sets the color of the "state" column in that table
- sets the color to a value of 0 (which maps to green) if the tunnels are in the `UP` state, signified by the content of the "state" column having the value `UP`; otherwise, it resorts to the default of 20 (which maps to amber) if the tunnels are in any other state

We can compare that with the web UI dialog for the same check:

![Intent verification rule](../images/miscellaneous/IP_Fabric_API_intent_verification_rule.webp)

So, once we have found the report we are looking for, we retrieve the technology table from the `apiEndpoint` field in the report dictionary, filtered for the color that matches the condition we're interested in from the validation check. From our above example, to retrieve the DMVPN tunnels that are in an `UP` state, we make a POST request to `/api/{api_version}/tables/security/dmvpn` with the following request payload:

```json
{
  "columns": [
    "id",
    "sn",
    "hostname",
    "siteName",
    "peerNbma",
    "peerTunnel",
    "state",
    "time",
    "attrb"
  ],
  "filters": { "state": ["color", "eq", "0"] },
  "snapshot": "$last",
  "reports": "/technology/security/dmvpn"
}
```

This will retrieve a dictionary with the data from the columns listed in the technology table from the last snapshot, filtered on the value of the `state` column equaling `0` -- which equates to the color green from the validation check.

Note that snapshot management is referred to in a separate article -- the `$last` snapshot may not be the best to query in all cases.
