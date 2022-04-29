# Support VPN

Starting IP Fabric version 1.0.3 customer is able to establish remote
SSL VPN to IP Fabric DC. Support VPN uses OpenVPN.

!!! warning "Network requirements"

    Support VPN requires access to
    [remote.ipfabric.io](http://remote.ipfabric.io) remote port 443/TCP. IP
    Fabric image must be also configured with functional DNS server.

    Connection through proxy servers should work, but not guaranteed.

## How To Establish Support VPN

!!! info "Security tip"

    VPN is always established and teared down by customer. VPN connection
    cannot be triggered externally!

1.  Login to IP Fabric web GUI.
2.  At top right corner click **Support**.
3.  Select **Remote support VPN**.

    ![VPN Menu](vpn/menu.png)

4.  On newly opened page click the _Connect_ button.

    ![VPN Connect](vpn/connect.png)

5.  VPN status should change to connected and also you should see assigned IP address.

## How To Tear Down Support VPN

1.  Repeat steps 1 - 3 from **How To Establish Support VPN** part from above
2.  On newly opened page click the **Disconnect** button.

    ![VPN Disconnect](vpn/disconnect.png)

3.  VPN status should change to disconnected.
