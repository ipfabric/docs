!!! warning "**Proxy Server Settings**"

    If the proxy server wasn't configured through `ipf-cli-config`, please don't
    forget to add the following line to the `/etc/environment` file:

    `no_proxy="localhost,127.0.0.1,127.0.1.1,::1"`

    This is usually a cause of failed upgrade process as `wget` and `curl` commands are
    used in the backround to check connectivity with IP Fabric API and they attempt to
    reach `localhost` through the proxy server.
