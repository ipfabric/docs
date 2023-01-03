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

!!! example "Use `dig` to try to resolve a domain"

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

!!! example "Use `dig` to get a PTR record"

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

!!! example

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

!!! example

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

- `0` -- Connection success
- `1` -- Missing or invalid command line arguments
- `2` -- Connection failed

## Check memory and swap usage

```shell
free -m
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ free -m
                   total        used        free      shared  buff/cache   available
    Mem:           15630        4708        8271           3        2649       10662
    Swap:            979           0         979
    ```

## Check which processes use most CPU

```shell
top
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ top
    top - 13:19:40 up 7 min,  1 user,  load average: 0.01, 0.13, 0.10
    Tasks: 186 total,   1 running, 185 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.1 us,  0.2 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :  15630.1 total,   8321.4 free,   4659.0 used,   2649.7 buff/cache
    MiB Swap:    980.0 total,    980.0 free,      0.0 used.  10713.4 avail Mem

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
        683 rabbitmq  20   0 5397952 116476   7984 S   1.3   0.7   0:13.36 beam.smp
        888 arangodb  20   0 8397360   3.3g   1.9g S   1.0  21.7   0:23.53 arangod
        690 redis     20   0   67308  10480   8256 S   0.7   0.1   0:00.85 redis-server
       1423 autoboss  20   0 1056132 272092  38308 S   0.3   1.7   0:04.59 ipfabric-api
       2528 osadmin   20   0   10192   3764   3016 R   0.3   0.0   0:00.02 top
          1 root      20   0  102700  10680   7672 S   0.0   0.1   0:01.46 systemd
          2 root      20   0       0      0      0 S   0.0   0.0   0:00.01 kthreadd
          3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp
          4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp
          6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-events_highpri
    [...]
    ```

## Check which processes use most memory

```shell
top -o %MEM
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ top -o %MEM
    top - 13:20:55 up 9 min,  1 user,  load average: 0.00, 0.10, 0.09
    Tasks: 184 total,   1 running, 183 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.9 us,  0.3 sy,  0.0 ni, 98.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :  15630.1 total,   8321.8 free,   4658.6 used,   2649.8 buff/cache
    MiB Swap:    980.0 total,    980.0 free,      0.0 used.  10716.3 avail Mem

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
        888 arangodb  20   0 8398384   3.3g   1.9g S   0.7  21.7   0:24.11 arangod
        672 autoboss  20   0 4171476   1.7g  40324 S   0.0  10.9   0:35.67 ipfabric-api
       1429 autoboss  20   0 1137824 309384  40568 S   0.0   1.9   0:07.04 ipfabric-api
       1435 autoboss  20   0 1123412 275388  38776 S   0.0   1.7   0:04.67 ipfabric-api
       1417 autoboss  20   0 1122176 273100  38760 S   0.3   1.7   0:06.45 ipfabric-api
       1423 autoboss  20   0 1056132 271580  38308 S   0.0   1.7   0:04.63 ipfabric-api
        701 autoboss  20   0   10.8g 170648  32152 S   0.0   1.1   0:02.52 syslogWorkerBui
        683 rabbitmq  20   0 5398464 116380   7984 S   1.3   0.7   0:14.47 beam.smp
        673 autoboss  20   0  945264 112476  32556 S   0.0   0.7   0:01.76 nimpee-update
        737 autoboss  20   0  811620  53092  30736 S   0.0   0.3   0:00.37 ipfabric-webhoo
    [...]
    ```

## Check status of common services

```shell
systemctl status nimpee-api.service
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl status nimpee-api.service
    ● nimpee-api.service - IPFabric API
         Loaded: loaded (/lib/systemd/system/nimpee-api.service; enabled; vendor preset: enabled)
         Active: active (running) since Fri 2022-11-18 13:11:48 UTC; 18min ago
       Main PID: 672 (ipfabric-api)
          Tasks: 58 (limit: 18711)
         Memory: 2.7G
            CPU: 1min 3.168s
         CGroup: /system.slice/nimpee-api.service
                 ├─ 672 /opt/ipf-api/ipfabric-api
                 ├─1417 /opt/ipf-api/ipfabric-api /snapshot/api/build/bundle.js --worker --port=20000 --slave
                 ├─1423 /opt/ipf-api/ipfabric-api /snapshot/api/build/bundle.js --worker --port=20001
                 ├─1429 /opt/ipf-api/ipfabric-api /snapshot/api/build/bundle.js --worker --port=20002
                 ├─1435 /opt/ipf-api/ipfabric-api /snapshot/api/build/bundle.js --worker --port=20003
                 └─1503 bwm-ng -o csv -I eth0 -t 1000 -u bytes -t rate

    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3599]: pam_unix(sudo:session): session closed for user root
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3606]: autoboss : PWD=/opt/ipf-api ; USER=root ; COMMAND=/usr/sbin/service rabbitmq-server status
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3606]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1001)
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3606]: pam_unix(sudo:session): session closed for user root
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3614]: autoboss : PWD=/opt/ipf-api ; USER=root ; COMMAND=/usr/sbin/service syslogWorker@1 status
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3614]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1001)
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3614]: pam_unix(sudo:session): session closed for user root
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3630]: autoboss : PWD=/opt/ipf-api ; USER=root ; COMMAND=/usr/sbin/service webhookWorker status
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3630]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1001)
    Nov 18 13:30:00 ipfabric-howto1118135353 sudo[3630]: pam_unix(sudo:session): session closed for user root
    ```

```shell
systemctl status nginx.service
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl status nginx.service
    ● nginx.service - A high performance web server and a reverse proxy server
         Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
         Active: active (running) since Fri 2022-11-18 13:11:56 UTC; 19min ago
           Docs: man:nginx(8)
        Process: 1445 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
        Process: 1446 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
       Main PID: 1447 (nginx)
          Tasks: 9 (limit: 18711)
         Memory: 26.7M
            CPU: 573ms
         CGroup: /system.slice/nginx.service
                 ├─1447 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
                 ├─1448 nginx: worker process
                 ├─1449 nginx: worker process
                 ├─1450 nginx: worker process
                 ├─1451 nginx: worker process
                 ├─1452 nginx: worker process
                 ├─1453 nginx: worker process
                 ├─1454 nginx: worker process
                 └─1455 nginx: worker process

    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1445]: nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/ipf-nimpee-update:28
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1445]: nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/nimpee-webng:35
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1445]: nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1445]: nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1446]: nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/ipf-nimpee-update:28
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1446]: nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/nimpee-webng:35
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1446]: nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
    Nov 18 13:11:56 ipfabric-howto1118135353 nginx[1446]: nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
    Nov 18 13:11:56 ipfabric-howto1118135353 systemd[1]: nginx.service: Failed to parse PID from file /run/nginx.pid: Invalid argument
    Nov 18 13:11:56 ipfabric-howto1118135353 systemd[1]: Started A high performance web server and a reverse proxy server.
    ```

```shell
systemctl status arangodb3.service
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl status arangodb3.service
    ● arangodb3.service - ArangoDB database server
         Loaded: loaded (/lib/systemd/system/arangodb3.service; enabled; vendor preset: enabled)
        Drop-In: /etc/systemd/system/arangodb3.service.d
                 └─ipf-nofile-override.conf
         Active: active (running) since Fri 2022-11-18 13:11:48 UTC; 20min ago
        Process: 662 ExecStartPre=/usr/bin/install -g arangodb -o arangodb -d /var/tmp/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 744 ExecStartPre=/usr/bin/install -g arangodb -o arangodb -d /var/run/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 799 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/log/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 800 ExecStartPre=/usr/bin/env chmod 700 /var/log/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 801 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/lib/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 880 ExecStartPre=/usr/bin/env chmod 700 /var/lib/arangodb3 (code=exited, status=0/SUCCESS)
        Process: 885 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/lib/arangodb3-apps (code=exited, status=0/SUCCESS)
        Process: 887 ExecStartPre=/usr/bin/env chmod 700 /var/lib/arangodb3-apps (code=exited, status=0/SUCCESS)
       Main PID: 888 (arangod)
          Tasks: 49 (limit: 131072)
         Memory: 3.4G
            CPU: 29.865s
         CGroup: /system.slice/arangodb3.service
                 └─888 /usr/sbin/arangod --uid arangodb --gid arangodb --pid-file /var/run/arangodb3/arangod.pid --temp.path /var/tmp/arangodb3 --log.foreground-tty true

    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [e52b0] ArangoDB 3.5.7 [linux] 64bit, using jemalloc, build tags/v3.5.7-0-ga94761e8c6, VPack 0.1.33, RocksDB 6.2.0, ICU 58.1, V8 7.1.302.28, OpenSSL 1.1.1h  22 Sep 2020
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [75ddc] detected operating system: Linux version 5.10.0-19-amd64 (debian-kernel@lists.debian.org) (gcc-10 (Debian 10.2.1-6) 10.2.1 20210110, GNU ld (GNU Binutils for Debian) 2.35.2) #1 SMP Debia>
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [43396] {authentication} Jwt secret not specified, generating...
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [144fe] using storage engine mmfiles
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [3bb7d] {cluster} Starting up with role SINGLE
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [a1c60] {syscall} file-descriptors (nofiles) hard limit is 1048576, soft limit is 1048576
    Nov 18 13:11:48 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:48Z [888] INFO [3844e] {authentication} Authentication is turned on (system only), authentication for unix sockets is turned on
    Nov 18 13:11:49 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:49Z [888] INFO [8767f] {engines} DB recovery finished successfully
    Nov 18 13:11:50 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:50Z [888] INFO [6ea38] using endpoint 'http+tcp://0.0.0.0:8529' for non-encrypted requests
    Nov 18 13:11:50 ipfabric-howto1118135353 arangod[888]: 2022-11-18T13:11:50Z [888] INFO [cf3f4] ArangoDB (version 3.5.7 [linux]) is ready for business. Have fun!
    ```

## Check if there are any failed services

```shell
systemctl --failed
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl --failed
      UNIT LOAD ACTIVE SUB DESCRIPTION
    0 loaded units listed.
    ```

## Check disk space usage

```shell
df -h
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ df -h
    Filesystem                     Size  Used Avail Use% Mounted on
    udev                           7.7G     0  7.7G   0% /dev
    tmpfs                          1.6G  688K  1.6G   1% /run
    /dev/mapper/ipfabric--vg-root  224G   12G  203G   6% /
    tmpfs                          7.7G  8.0K  7.7G   1% /dev/shm
    tmpfs                          5.0M     0  5.0M   0% /run/lock
    /dev/sda1                      470M   88M  358M  20% /boot
    tmpfs                          1.6G     0  1.6G   0% /run/user/0
    ```

## Check inode usage on filesystems

```shell
df -i
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ df -i
    Filesystem                      Inodes IUsed    IFree IUse% Mounted on
    udev                           1995938   379  1995559    1% /dev
    tmpfs                          2000655   600  2000055    1% /run
    /dev/mapper/ipfabric--vg-root 14822080 65161 14756919    1% /
    tmpfs                          2000655     2  2000653    1% /dev/shm
    tmpfs                          2000655     3  2000652    1% /run/lock
    /dev/sda1                       124928   356   124572    1% /boot
    tmpfs                           400131    17   400114    1% /run/user/0
    ```

## Reboot And Shutdown

IP Fabric VM can be also rebooted or shutdown using CLI.

- For VM reboot, use `reboot` command without any parameters.
- For VM shutdown, use `shutdown` command without any parameters.
