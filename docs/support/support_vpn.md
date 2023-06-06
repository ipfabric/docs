---
description: With IP Fabric a customer is able to establish remote SSL VPN to IP Fabric DC. Support VPN uses OpenVPN.
---

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

1.  Click **Support** in the top right corner of the IP Fabric GUI.
2.  Select **Remote support VPN**:

    ![VPN Menu](vpn/menu.png)

3.  On the newly opened page, click the **Connect** button:

    ![VPN Connect](vpn/connect.png)

4.  VPN status should change to connected and also you should see assigned IP address.

## How To Tear Down Support VPN

1.  Repeat steps 1 and 2 from the **How To Establish Support VPN** section above.
2.  On newly opened page click the **Disconnect** button:

    ![VPN Disconnect](vpn/disconnect.png)

3.  VPN status should change to disconnected.
