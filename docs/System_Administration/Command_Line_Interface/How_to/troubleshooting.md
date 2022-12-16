# How to troubleshoot IP Fabric VM

In the event of a VM network connection problem, DNS issues, network devices connectivity issue, IP Fabric CLI is a useful helper.

CLI can be also used to access system and application logs as well as snapshot files.

## Examining The Network Interface Settings

!!! warning

	When you log in through a VM console or SSH, network settings are displayed. This content is static, generated when VM boots! When DHCP is used, an IP address can change in some cases.

```shell
Linux ipfabric-server 5.10.0-19-amd64 #1 SMP Debian 5.10.149-2 (2022-10-21) x86_64
IP FABRIC 6.0.0+21
NETWORK INFRASTRUCTURE MANAGEMENT PLATFORM
ENGINEERING EDITION
(c) IP FABRIC, INC
UNAUTHORIZED ACCESS PROHIBITED

WEB: https://65.21.240.33/
IP:  65.121.240.33
GW:  172.31.1.1
DNS: 185.12.64.1
DNS: 185.12.64.2

For troubleshooting purpose please login as user "osadmin"
with password configured during initial setup.
Last login: Wed Dec 14 14:21:01 2022 from 192.168.253.6
```

To determine the IP address or addresses of your IP Fabric system:

```shell
ip addr show
```

To show the route entries in the kernel:

```shell
ip route
```

## Examining DNS Settings

DNS can be checked using the `dig` or `nslookup` command.

### Use `dig` to try to resolve a domain

```shell
16:45 #> dig ipfabric.io

; <<>> DiG 9.10.6 <<>> ipfabric.io
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40055
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1480
;; QUESTION SECTION:
;ipfabric.io.			IN	A

;; ANSWER SECTION:
ipfabric.io.		300	IN	A	162.159.137.54
ipfabric.io.		300	IN	A	162.159.136.54

;; Query time: 54 msec
;; SERVER: 10.64.16.1#53(10.64.16.1)
;; WHEN: Wed Dec 14 16:45:46 CET 2022
;; MSG SIZE  rcvd: 72
```

### Use `dig` to get a PTR record

```shell
16:49 #> dig -x 135.181.89.75

; <<>> DiG 9.10.6 <<>> -x 135.181.89.75
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62086
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1480
;; QUESTION SECTION:
;75.89.181.135.in-addr.arpa.	IN	PTR

;; ANSWER SECTION:
75.89.181.135.in-addr.arpa. 600	IN	PTR	static.75.89.181.135.clients.your-server.de.

;; Query time: 225 msec
;; SERVER: 10.64.16.1#53(10.64.16.1)
;; WHEN: Wed Dec 14 16:49:43 CET 2022
;; MSG SIZE  rcvd: 112

```

For PTR record check **ANSWER** which contains requested domain name.

With `nslookup` one can achieve similar results.

```shell
16:49 #> nslookup static.75.89.181.135.clients.your-server.de
Server:		10.64.16.1
Address:	10.64.16.1#53

Non-authoritative answer:
Name:	static.75.89.181.135.clients.your-server.de
Address: 135.181.89.75
```

## Testing Network Connectivity

IP Fabric CLI provides access to standard Unix tools for network testing, such as `ping`, `traceroute`, `telnet`, `ssh`, `netstat` etc.

!!! warning ICMP

    Please bear in mind that ICMP packets used by `ping` and `traceroute` can be blocked by other devices in the network. It does not mean that a device cannot be reached using SSH or Telnet.

To make sure that the network device is available from IP Fabric VM, you
can use the `telnet` and `ssh` client from the command line.

For SSH testing:

```shell
ssh userName@device-IP-or-Hostname
```

For Telnet testing:

```shell
telnet device-IP-or-Hostname
```

Since version 5.0, there is also a tool called `ipf-connection-tester` for testing the network connectivity using SSH library that is used by the Discovery process, which is different than the system SSH library!

To test SSH connectivity, use:

```shell
ipf-connection-tester ssh userName@device-IP-or-Hostname
```

As in example below:

```shell
root@ipfabric-server:~# ipf-connection-tester ssh 192.168.121.119
Username? username1
Password? 
2022-12-14T16:33:30.505Z - debug: Custom crypto binding not available
2022-12-14T16:33:30.507Z - debug: Local ident: 'SSH-2.0-ssh2js1.10.0'
2022-12-14T16:33:30.507Z - debug: Client: Trying 192.168.121.119 on port 22 ...
2022-12-14T16:33:33.576Z - debug: Socket error: connect ETIMEDOUT 192.168.121.119:22
2022-12-14T16:33:33.579Z - info: Awaiting connectionEndedPromise...
2022-12-14T16:33:33.580Z - debug: Socket closed
2022-12-14T16:33:33.582Z - info: SocketClosedPromise finished.
2022-12-14T16:33:33.582Z - info: LogList:  [
  "Trying SSH connect to 192.168.121.119:22",
  "SSH Error: Error: connect ETIMEDOUT 192.168.121.119:22"
]
2022-12-14T16:33:33.583Z - error: connect ETIMEDOUT 192.168.121.119:22 {"name":"ABConnectionError","stack":"Error: connect ETIMEDOUT 192.168.121.119:22\n    at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1157:16)"}
```

If you are getting timeouts, it is possible to increase the default timeout options:

```shell
Options:
  -r, --ready-timeout <timeout>  seconds to wait till connection is ready (default: 30)
  -d, --data-timeout <timeout>   seconds to wait till data is received (default: 10)
```

For example:

```shell
ipf-connection-tester ssh userName@device-IP-or-Hostname -r 60 -d 20
```

For testing telnet, simply change `ssh` to `telnet`:

```shell
ipf-connection-tester telnet userName@device-IP-or-Hostname
```

Timeout options are the same. However, the telnet connection tester is much less verbose than the SSH one, so for both security and verbosity, prefer SSH whenever possible.

If you wish to run `ipf-connection-tester` from your own automation script, here are possible return values:

* `0` -- Connection success
* `1` -- Missing or invalid command line arguments
* `2` -- Connection failed

## Reboot And Shutdown

IP Fabric VM can be also rebooted or shutdown using CLI.

- For VM reboot, use `reboot` command without any parameters.
- For VM shutdown, use `shutdown` command without any parameters.
