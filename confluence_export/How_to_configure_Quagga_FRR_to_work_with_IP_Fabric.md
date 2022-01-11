# How to configure Quagga/FRR to work with IP Fabric

When running discovery, IP Fabric needs to connect directly to the
device console.

Because of that, to discover Quagga/FRR devices, a separate user with a
specific shell needs to be created on a device.

Quagga/FRR shell usually runs in /usr/bin/vtysh.

A new user with a direct access to Quagga/FRR shell needs to be created
as follows in the bash:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
useradd -s /usr/bin/vtysh username
```

</div>

</div>

Afterwards, you will be prompted to set up a password.

Add this username and password to IP Fabric credentials used for
discovery.
