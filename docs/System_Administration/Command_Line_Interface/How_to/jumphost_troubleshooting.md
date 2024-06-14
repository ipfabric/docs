---
description: This section contains information on how to troubleshoot jumphost-related problems.
---

# How To Troubleshoot Jumphost

## Jumphost Troubleshooting Tools

IP Fabric doesn't work with DNS names that have an IPv6 address in addition to
an IPv4 address. It is always better to use IPv4 address records.

When the jumphost is configured and active, it is good practice to test the SSH
connection from the IP Fabric CLI to any network device that should be
discoverable using the jumphost.

Other useful commands:

```shell title="To Get the Name of the Service and the Latest Logs From the Jumphost Service in Real Time"
systemctl | grep ipf-jumphost

journalctl -f -u ipf-jumphost@<ID>.service
```

```shell title="To Manually Start a Jumphost"
/usr/bin/python3 /usr/sbin/sshuttle -D -vvv -r jumphost-user@jumphost-ip x.x.x.x/yy
```

!!! example

    Replace `x.x.x.x/yy` with a subnet that you want to reach through the
    jumphost (e.g., `10.254.63.0/24`).

## Jumphost Status Is Running, but Devices Behind Jumphost Are Not Discovered

### Check Incoming Traffic From IP Fabric to Jumphost

1. On a jumphost machine, run `tcpdump` with the parameters:

   ```shell
   tcpdump src <IPF_IP> and dst <JUMPHOST_IP>
   ```

2. On the IP Fabric instance, open an SSH/Telnet session to any host behind the
   jumphost:

   ```shell
   autoboss@ip-fabric:~$ telnet 10.47.102.104
   Trying 10.47.102.104...
   Connected to 10.47.102.104.
   Escape character is '^]'.

   ##########################################################################
   ##        UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED              ##
   ## :::: $$$$$ ::::: ''''' ````` """"" ::::: $$$$$ ::::: ''''' ````` """ ##
   ##########################################################################
   ```

   ```shell
   root@jumphost:/home/autoboss# tcpdump src 10.0.9.13 and dst 10.0.9.17
   tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
   listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

   12:35:58.065549 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [P.], seq 1498215736:1498215828, ack 173264556, win 687, options [nop,nop,TS val 542423406 ecr 584899103], length 92
   12:35:58.066759 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 661, win 686, options [nop,nop,TS val 542423406 ecr 584912111], length 0
   12:35:58.068806 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 985, win 686, options [nop,nop,TS val 542423407 ecr 584912111], length 0
   ```

   If there is no incoming traffic, check **outgoing traffic from IP Fabric to
   the jumphost**.

### Check Outgoing Traffic from IP Fabric to Jumphost

1. On the IP Fabric instance, run `tcpdump` with the parameters:

   ```shell
   tcpdump src <IPF_IP> and dst <JUMPHOST_IP>
   ```

2. On the IP Fabric instance, open an SSH/Telnet session to any host behind
   the jumphost:

    ```shell
    root@ip-fabric:/home/autoboss# tcpdump src 10.0.9.13 and dst 10.0.9.17
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

    12:53:25.476825 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [P.], seq 156:248, ack 1657, win 687, options [nop,nop,TS val 542685257 ecr 585170204], length 92
    12:53:25.477998 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 2317, win 686, options [nop,nop,TS val 542685257 ecr 585173962], length 0
    ```

### Check Outgoing Traffic From Jumphost to Host

1. On a jumphost machine, run `tcpdump` with the parameters:

   ```shell
   tcpdump src <JUMPHOST_IP> and dst <HOST_IP>
   ```

2. On the IP Fabric instance, open an SSH/Telnet to any host behind the
   jumphost:

   ```shell
   root@jumphost:/home/autoboss# tcpdump src 10.0.9.17 and dst 10.47.102.104
   tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
   listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

   12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
   12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
   ```

### Check Incoming Traffic From Host to Jumphost

1. On a jumphost machine, run `tcpdump` with parameters:

   ```shell
   tcpdump src <HOST_IP> and dst <JUMPHOST_IP>
   ```

2. On the IP Fabric instance, open an SSH/Telnet to any host behind the
   jumphost:

   ```shell
   root@jumphost:/home/autoboss# tcpdump src 10.47.102.104 and dst 10.0.9.17
   tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
   listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

   12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
   12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
   ```

## Restore Access to IP Fabric GUI After Jumphost Misconfiguration

If you suddenly cannot open the IP Fabric main GUI or connect to the IP Fabric
machine via SSH after saving the jumphost settings, the subnet/IP address of the
IP Fabric machine was most likely included in the jumphost configuration.

To fix this issue, you need **direct access** to **the virtual machine's CLI**
from your hypervisor, the password for the `osadmin` user account, and follow
these steps:

1. Log in to the **virtual machine's CLI** with the `osadmin` account.

2. Filter the `systemctl` output containing `jumphost`. Each configured jumphost
   has its own ID.

   ```shell
   osadmin@ipfabric-server:~$ sudo systemctl | grep ipf-jumphost
   [sudo] password for osadmin: 
     ipf-jumphost@923216920.service                               loaded activating auto-restart ipf-jumphost (ID=923216920)
   ```

   ```shell
   osadmin@ipfabric-server:~$ sudo systemctl status ipf-jumphost@923216920.service
   ● ipf-jumphost@923216920.service - ipf-jumphost (ID=923216920)
        Loaded: loaded (/lib/systemd/system/ipf-jumphost@.service; disabled; vendor preset: enabled)
        Active: activating (auto-restart) (Result: exit-code) since Wed 2022-12-14 14:25:52 UTC; 6s ago
       Process: 682331 ExecStart=/opt/ipf-jumphost/bin/start-one.sh /opt/ipf-jumphost/conf/923216920.conf (code=exited, status=1/FAILURE)
   ```

3. Stop the `jumphost` service:

   ```shell
   sudo systemctl stop ipf-jumphost@<ID>.service
   ```

4. Check that **the `jumphost` process is inactive** with:

   ```shell
   systemctl status ipf-jumphost@<ID>.service
   ```

   ```shell
   osadmin@ipfabric-server:~$ sudo systemctl status ipf-jumphost@923216920.service
   ● ipf-jumphost@923216920.service - ipf-jumphost (ID=923216920)
        Loaded: loaded (/lib/systemd/system/ipf-jumphost@.service; disabled; vendor preset: enabled)
        Active: inactive (dead)

   Dec 14 14:28:55 ipfabric-server sshuttle[682901]: ssh: connect to host 2.3.2.1 port 22: Network is unreachable
   Dec 14 14:28:55 ipfabric-server sshuttle[682901]: c : fatal: c : failed to establish ssh session (2)
   Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: read eof
   Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: set expect_out(spawn_id) "exp3"
   Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: set expect_out(buffer) ""
   Dec 14 14:28:55 ipfabric-server start-one.sh[682915]: Dec 14 14:28:55 [ERROR] Jumphost was not started
   Dec 14 14:28:55 ipfabric-server systemd[1]: ipf-jumphost@923216920.service: Control process exited, code=exited, status=1/FAILURE
   Dec 14 14:28:55 ipfabric-server systemd[1]: ipf-jumphost@923216920.service: Failed with result 'exit-code'.
   Dec 14 14:28:55 ipfabric-server systemd[1]: Failed to start ipf-jumphost (ID=923216920).
   Dec 14 14:29:13 ipfabric-server systemd[1]: Stopped ipf-jumphost (ID=923216920).
   ```

5. The IP Fabric GUI should be accessible by now.
