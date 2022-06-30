# Troubleshooting VM Using IP Fabric CLI

In the event of a VM network connection problem, DNS issues, network devices connectivity issue, IP Fabric CLI is a useful helper.

CLI can be also used to access system and application logs as well as snapshot files.

## Checking The Network Interface Settings

!!! warning
	When you log in through a VM console or SSH, network settings are displayed. This content is static, generated when VM boots! When DHCP is used, an IP address can change in some cases.

![VM IP](vm_ip.png)

To display actual IP address use command:

```shell
ip addr show
```

Default gateway and other routes (if configured) can be check as follows:

```shell
ip r
```

## Checking DNS

DNS can be checked using the `dig` or `nslookup` command.

For example, let's check A record and PTR (reverse) record of some device using `dig`.

For A record check **ANSWER** which contains requested IP address. Also **SERVER** section below is important as it tell us what DNS server answered our DNS query.

![DNS A record](dns_a_rec.png)

For PTR record check **ANSWER** which contains requested domain name.

![DNS PTR record](dns_ptr_rec.png)

If you prefer `nslookup` you can achieve the same results.

![nslookup](nslookup.png)

## Testing Connectivity To a Network Device

The very basic test is `ping` or `traceroute`.

!!! warning ICMP
	Please bear in mind that ICMP packets used by `ping` and `traceroute` can be blocked by ACL or firewall. It does not mean that a device cannot be reached using SSH or telnet.

To make sure that the network device is available from IP Fabric VM, you
can use the `telnet` and `ssh` client from the command line.

For SSH use:

```bash
ssh userName@device-IP-or-Hostname
```

For telnet use:

```shell
telnet device-IP-or-Hostname
```

## Reboot And Shutdown

IP Fabric VM can be also rebooted or shutdown using CLI.

For VM reboot just use `reboot` command without any parameters.

For VM shutdown use `shutdown` command without any parameters.
