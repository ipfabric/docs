# API Tech Note - 4.3 Unicast Path Lookup

## Request Parameters

-   **"parameters"** *\[mandatory\]*- A nested JSON data structure with
    keys

    -   **"type"** *\[mandatory\]* - A quoted string with a value of
        "pathLookup" for an E2E path simulation output

    -   **"pathLookupType"** *\[mandatory\]* - A quoted string
        containing the word "unicast"

    -   **"protocol"** *\[mandatory\]* - A quoted string with a value of
        "tcp", "udp", "icmp"

    -   **"startingPoint"** *\[mandatory\]*- A quoted string containing
        the source IP address or subnet

    -   **"destinationPoint"** *\[mandatory\]*- A quoted string
        containing the destination IP address or subnet

    -   **"groupBy"** *\[mandatory\]*- A quoted string representing the
        grouping of devices in the output - at this time one of
        "siteName", "routingDomain" or "stpDomain"

    -   **"networkMode"** *\[mandatory\]*- A boolean - the new version
        of IP Fabric allows you to simulate paths between subnets.
        Setting this key to true means that you will create a single
        result representing the subnets; false means that IP Fabric will
        create a separate path for each source or destination in the
        range of addresses up to a maximum of 255.

    -   **"securedPath"** *\[mandatory\]*- A boolean - when you run a
        path simulation, you can tell IP Fabric if you want to stop when
        it hits a security policy which blocks the traffic in question
        (true) or complete the forwarding paht and simply highlight the
        policy enforcement point (false)

    -   **“ttl”** *\[mandatory\]*- integer - Time-to-live value (default
        is 128)

    -   **“fragmentOffset”** *\[mandatory\]*- integer - Fragment offset
        value (default is 0)

    -   **“srcRegions”** *\[mandatory\]*- string - (default “.\*”)

    -   **“dstRegions”** *\[mandatory\]*- string - (default “.\*”)

    -   **“otherOptions”** *\[mandatory\]*- nested JSON data

        -   **“applications”** *\[mandatory\]*- string - (default “.\*”)

        -   **“tracked”** *\[mandatory\]- boolean - (default false)*

    -   **“firstHopAlgorithm”** *\[mandatory\]*- nested JSON data

        -   **“type” ** *\[mandatory\]*- Either “automatic” or
            “userDefined”

        -   **“vrf” ** *\[Optional and if type == automatic\]*

        -   **“entryPoints” ** *\[mandatory and if type ==
            userDefined\]* - nested array of JSON data

            -   **“hostname”** *\[mandatory\]-* Hostname string

            -   **“sn”** *\[mandatory\]-* IP Fabric Unique Serial Number
                string

            -   **“iface”** *\[mandatory\]-* Interface name

    -   **“l4Options”** *\[mandatory\]* - nested JSON data

        -   If **protocol = tcp**

            -   **"srcPorts"** *\[mandatory\]*- A string representing
                ports; ex. “80,443,1025-4096”

            -   **"dstPorts"** *\[mandatory\]*- A string representing
                ports; ex. “80,443,1025-4096”

            -   **“flags”** *\[mandatory\]* - An array of TCP flags to
                be set in the simulated path or empty array

                -   Valid flags:
                    `["ack", "fin", "psh", "rst", "syn", "urg"]`

        -   If **protocol = udp**

            -   **"srcPorts"** *\[mandatory\]*- A string representing
                ports; ex. “80,443,1025-4096”

            -   **"dstPorts"** *\[mandatory\]*- An integer representing
                the destination port

        -   If **protocol = icmp** refer to: [API Tech Note - Path
            Lookup ICMP
            Decoder](API_Tech_Note_-_Path_Lookup_ICMP_Decoder)

            -   **“type”** *\[mandatory\]*- An integer representing the
                ICMP type

            -   **“code”** *\[mandatory\]*- An integer representing the
                ICMP code

## Example minimal request body

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
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

</div>

</div>
