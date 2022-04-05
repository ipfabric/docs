# Custom SSH/Telnet ports

Custom SSH/Telnet ports settings enable the discovery process to use different than standard ports for connecting. The standard for SSH is port `22` and `23` for Telnet.

In the following example we will configure the discovery process to use port `8080` for SSH connections towards firewall sitting behind `192.168.168.10`:

![edit custom ssh telnet port](edit_custom_ssh_telnet_port.png)

As a result of such configuration, we would create a new item under the "Custom SSH/Telnet ports" configuration, which will be applied to every new snapshot created by IP Fabric.

![custom ssh telnet ports](custom_ssh_telnet_ports.png)
