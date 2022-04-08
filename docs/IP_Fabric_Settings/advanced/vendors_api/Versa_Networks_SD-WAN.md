# Versa Networks SD-WAN

Starting version 3.8.0 IP Fabric supports Versa SD-WAN API. API is based
on HTTPS authentication. Versa requires the following settings to be
applied:

-   Username - Username to Versa Director to access API data
-   Password - Password to Versa Director access API data
-   Base URL - Base URL of Versa Director. If the API isn't available on
    the default port `9182`, add a port part to the URL (ie: `https://server:4443/`)

!!! note

    OAuth based authentication for Versa Director is not supported.

