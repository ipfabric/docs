---
description: This section contains information on how to troubleshoot common problems with the IP Fabric VM's setup.
---

# How To Troubleshoot IP Fabric VM

In the event of a VM network connection problem, DNS issues, or network devices
connectivity issue, the IP Fabric CLI is a useful helper.

The CLI can also be used to access system and application logs and snapshot
files.

## Examine Network Interface Settings

!!! warning

    When you log in through the VM console or SSH, the network interface
    settings are displayed. This content is static, generated when VM boots!
    When DHCP is used, the IP address(es) can change in some cases.

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

To determine the IP address(es) of your IP Fabric system:

```shell
ip addr show
```

To show the route entries in the kernel:

```shell
ip route
```

## Examine DNS Settings

DNS can be checked using the `dig` or `nslookup` command.

!!! example "Use `dig` To Try To Resolve Domain"

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

!!! example "Use `dig` To Get PTR Record"

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

For PTR record, check the `ANSWER SECTION` which contains the requested domain
name.

With `nslookup`, you can achieve similar results.

!!! example

    ```shell
    16:49 #> nslookup static.75.89.181.135.clients.your-server.de
    Server:		10.64.16.1
    Address:	10.64.16.1#53

    Non-authoritative answer:
    Name:	static.75.89.181.135.clients.your-server.de
    Address: 135.181.89.75
    ```

## Test Network Connectivity

The IP Fabric CLI provides access to standard Unix tools for network testing,
such as `ping`, `traceroute`, `telnet`, `ssh`, `netstat`, etc.

!!! warning "ICMP"

    Please remember that ICMP packets used by `ping` and `traceroute` might be
    blocked by other devices in the network. It does not mean that a device
    cannot be reached using SSH or Telnet.

To make sure that an network device is available from the IP Fabric VM, you can
use the `telnet` and `ssh` client from the command line.

For SSH testing:

```shell
ssh userName@device-IP-or-Hostname
```

For Telnet testing:

```shell
telnet device-IP-or-Hostname
```

### `ipf-connection-tester`

Since version `5.0`, there is also a tool called `ipf-connection-tester` for
testing the network connectivity using the same SSH library that is used by the
discovery process, which is different than the system SSH library!

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

If you are getting timeouts, you may increase the default timeout options:

```shell
Options:
  -r, --ready-timeout <timeout>  seconds to wait till connection is ready (default: 30)
  -d, --data-timeout <timeout>   seconds to wait till data is received (default: 10)
```

For example:

```shell
ipf-connection-tester ssh userName@device-IP-or-Hostname -r 60 -d 20
```

To test Telnet, simply change `ssh` to `telnet`:

```shell
ipf-connection-tester telnet userName@device-IP-or-Hostname
```

Timeout options are the same. However, the Telnet connection tester is much less
verbose than the SSH one, so for both security and verbosity, prefer SSH
whenever possible.

If you wish to run `ipf-connection-tester` from your automation script, here are
the possible return values:

- `0` -- Connection succeeded
- `1` -- Missing or invalid command-line arguments
- `2` -- Connection failed

## Check Memory and Swap Usage

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

## Check Which Processes Use Most CPU

```shell
top
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ top
    top - 08:24:59 up 13 min,  2 users,  load average: 0.22, 0.14, 0.10
    Tasks: 289 total,   5 running, 284 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  5.9 us,  2.0 sy,  0.0 ni, 89.1 id,  2.6 wa,  0.0 hi,  0.5 si,  0.0 st
    MiB Mem :  31337.8 total,  24126.5 free,   6125.0 used,   1684.1 buff/cache
    MiB Swap:   8192.0 total,   8192.0 free,      0.0 used.  25212.8 avail Mem

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
       2044 autoboss  20   0   31.4g 679504  46556 S  56.7   2.1   0:21.73 ipfabric-api
       2069 postgres  20   0 4519376  87744  67064 S  30.0   0.3   0:01.41 postgres
       1003 rabbitmq  20   0 4333988 212260  68512 S   5.7   0.7   0:09.29 beam.smp
          1 root      20   0  169180  13708   9160 S   3.0   0.0   0:05.43 systemd
        438 root      20   0       0      0      0 S   1.7   0.0   0:00.18 jbd2/dm-1-8
       5347 autoboss  20   0  302240  33612  24552 D   1.3   0.1   0:00.04 updaterBuild
        217 root       0 -20       0      0      0 I   1.0   0.0   0:00.06 kworker/7:1H-kblockd
        919 message+  20   0    8060   4496   3784 S   1.0   0.0   0:01.70 dbus-daemon
       5349 autoboss  20   0  302548  33348  24276 R   1.0   0.1   0:00.03 updaterBuild
       1047 root      20   0 1573940  51148  27876 S   0.7   0.2   0:03.48 containerd
       1373 vector    20   0  807644 421408  41868 S   0.7   1.3   0:05.23 vector
       2962 root      20   0       0      0      0 I   0.7   0.0   0:00.07 kworker/u32:0-events_unbound
       5348 autoboss  20   0  302240  34932  25812 R   0.7   0.1   0:00.02 updaterBuild
       5350 autoboss  20   0  302240  36876  25704 R   0.7   0.1   0:00.02 updaterBuild
       5356 autoboss  20   0  165180  25904  19928 D   0.7   0.1   0:00.02 workerBuild
       5357 autoboss  20   0  165180  23992  20056 R   0.7   0.1   0:00.02 workerBuild
    [...]
    ```

## Check Which Processes Use Most Memory

```shell
top -o %MEM
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ top -o %MEM
    Tasks: 294 total,   2 running, 292 sleeping,   0 stopped,   0 zombie
    %Cpu(s): 33.3 us,  0.0 sy,  0.0 ni, 66.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :  31337.8 total,  22013.0 free,   7099.0 used,   3048.6 buff/cache
    MiB Swap:   8192.0 total,   8192.0 free,      0.0 used.  24238.8 avail Mem
    
        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
       2027 autoboss  20   0  154.0g   2.4g  48576 S   0.0   7.9   0:43.63 ipfabric-api
       2044 autoboss  20   0   31.4g 680884  46620 S   0.0   2.1   0:35.72 ipfabric-api
       2050 autoboss  20   0   31.3g 592972  47180 S   0.0   1.8   0:15.22 ipfabric-api
       6362 autoboss  20   0   21.3g 569300  39076 S   0.0   1.8   0:05.71 taskerBuild
       1373 vector    20   0  807644 473256  42056 S   0.0   1.5   0:06.45 vector
        924 autoboss  20   0   21.1g 323556  38444 S   0.0   1.0   0:07.55 syslogWorkerBui
        991 ipf-vic+  20   0 1515444 253420  14216 S   0.0   0.8   0:04.31 victoria-metric
       6520 postgres  20   0 4661336 233624 191276 S   0.0   0.7   0:02.21 postgres
       6578 postgres  20   0 4646108 222564 196132 S   6.7   0.7   0:01.40 postgres
       5710 postgres  20   0 4674564 221224 167688 S   0.0   0.7   0:03.38 postgres
        966 autoboss  20   0   20.7g 218404  38220 S   0.0   0.7   0:02.91 ipf-backend-ext
       1003 rabbitmq  20   0 4335184 217416  68512 S   0.0   0.7   0:12.62 beam.smp
       6499 postgres  20   0 4508660 202916 191528 S  26.7   0.6   0:05.06 postgres
       6521 postgres  20   0 4513440 198104 178964 S   0.0   0.6   0:00.74 postgres
       6575 postgres  20   0 4525416 195656 164960 S  40.0   0.6   0:02.08 postgres
    [...]
    ```

## Check Status of Common Services

```shell
systemctl status ipf-api.service
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl status ipf-api.service
    ● ipf-api.service - IPFabric API
         Loaded: loaded (/lib/systemd/system/ipf-api.service; enabled; vendor preset: enabled)
         Active: active (running) since Fri 2022-11-18 13:11:48 UTC; 18min ago
       Main PID: 672 (ipfabric-api)
          Tasks: 58 (limit: 18711)
         Memory: 2.7G
            CPU: 1min 3.168s
         CGroup: /system.slice/ipf-api.service
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
systemctl status postgresql@15-main.service
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl status postgresql@15-main.service
    ● postgresql@15-main.service - PostgreSQL Cluster 15-main
    Loaded: loaded (/lib/systemd/system/postgresql@.service; enabled-runtime; preset: enabled)
    Active: active (running) since Fri 2025-07-11 10:34:44 UTC; 3h 57min ago
    Process: 1097 ExecStart=/usr/bin/pg_ctlcluster --skip-systemctl-redirect 15-main start (code=exited, status=0/SUCCESS)
    Main PID: 1299 (postgres)
    Tasks: 8 (limit: 18685)
    Memory: 1.2G
    CPU: 1min 42.461s
    CGroup: /system.slice/system-postgresql.slice/postgresql@15-main.service
    ├─ 1299 /usr/lib/postgresql/15/bin/postgres -D /var/lib/postgresql/15/main -c config_file=/etc/postgresql/15/main/postgresql.conf
    ├─ 1373 "postgres: 15/main: checkpointer "
    ├─ 1374 "postgres: 15/main: background writer "
    ├─ 1379 "postgres: 15/main: walwriter "
    ├─ 1380 "postgres: 15/main: autovacuum launcher "
    ├─ 1381 "postgres: 15/main: logical replication launcher "
    ├─ 1899 "postgres: 15/main: ipf_api_user ipf_appliance_db ::1(3782) idle"
    └─21716 "postgres: 15/main: postgres ipf_appliance_db [local] idle"
    
    Jul 11 10:34:41 ipfabric-howto1118135353 systemd[1]: Starting postgresql@15-main.service - PostgreSQL Cluster 15-main...
    Jul 11 10:34:44 ipfabric-howto1118135353 systemd[1]: Started postgresql@15-main.service - PostgreSQL Cluster 15-main.
    ```

## Check if There Are Any Failed Services

```shell
systemctl --failed
```

!!! example

    ```shell
    osadmin@ipfabric-howto1118135353:~$ systemctl --failed
      UNIT LOAD ACTIVE SUB DESCRIPTION
    0 loaded units listed.
    ```

## Check Disk Space Usage

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

## Check Inode Usage on Filesystems

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

## Reboot and Shutdown

The IP Fabric VM can also be rebooted or shut down using the CLI:

- To reboot the VM, use the `reboot` command.
- To shut down the VM, use the `poweroff` command.
