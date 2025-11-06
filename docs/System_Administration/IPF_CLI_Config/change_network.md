---
description: This page explains how to change the IP Fabric VM's network configuration using IPF CLI Config.
---

# Update Network Configuration

To change the IP address, subnet, gateway, DNS, or proxy configuration of your
IP Fabric appliance from the CLI, follow these steps:

1. Connect to the IP Fabric appliance via SSH as the `osadmin` user.

2. Run:

   ```shell
   sudo ipf-cli-config -n
   ```

  !!! note

      To keep the current configuration for any item, select `OK` and press
      `Enter`.
   
  !!! note

      If you will choose to not configure IPv6 network, current IPv6
      configuration will be removed.


3. The first two options are to modify the hostname and the DNS domain name.
   See [Update Hostname or DNS Domain Name](change_hostname.md).

4. Next, select DHCP or static IP address assignment. Use the `up`/`down` and
   `Space` keys to change `()` to `(*)`.

   ![Use DHCP or Static IP Address](change_ip_assignment.webp)

5. If you selected static IP address assignment, then enter:

   - IP address and prefixlen in format `address/prefixlen`
   - gateway

   ![Configure a static IP](change_static_ip.webp)

6. Next, answer if you want to configure IPv6 network

   ![IPv6 configuration question](question_ipv6.webp)

7. If you chose to configure IPv6 network, select IPv6 configuration type.
   Use the `up`/`down` and `Space` keys to change `()` to `(*)`.

   ![IPv6 configuration type](change_ipv6_configuration_type.webp)

8. If you selected `static` IPv6 configuration, then enter

   - IPv6 address and prefixlen in form `address/prefixlen`
   - IPv6 gateway

   ![Configure a static IPv6](change_static_ipv6.webp)

9. If you selected `auto` IPv6 configuration, then answer if you want to run
   Recursive DNS server daemon which reads DNS resolvers addresses from router
   advertisements and adds them to DNS configuration.

   ![Run RDNSSD question](question_rdnssd.webp)

10. Next, insert IP addresses of DNS resolvers. If you chose to use IPv6,
   then you can use both IPv4 and IPv6 addresses, otherwise IPv4 only.
   If you selected static configuration, then at least one resolver address
   is required.

   ![Configure DNS resorvers](change_dns_resolvers.webp)

11. Confirm or change FQDN which will be resolved during DNS tests.

   ![Configure FQDN for DNS tests](change_dns_test_fqdn.webp)

12. Select `Yes` to reboot the system:

   ![Reboot system](reboot.webp)
