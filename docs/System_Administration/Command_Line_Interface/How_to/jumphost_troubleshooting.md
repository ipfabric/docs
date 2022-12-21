# Troubleshooting `jumphost`

## Jumphost Troubleshooting Tools

IP Fabric doesn't work with DNS names that have IPv6 address in addition to IPv4 address. It is always better to use IPv4 address record.

It is a good practice to test the SSH from IP Fabric's CLI to any network device that should be discoverable using the jumphost when the jumphost is configured and active.

Other useful commands:

```shell title="Gets the name of the service and latest logs from Jumphost service in real time"
systemctl | grep jumphost

journalctl -f -u jumphost@xxx.service
```

```shell title="Manually Starts a Jumphost"
/usr/bin/python3 /usr/sbin/sshuttle -D -vvv -r jumphost-user@jumphost-ip x.x.x.x/yy
```
!!! example

    replace `x.x.x.x/yy` with a subnet which you want to reach through the jumphost e.g. `10.254.63.0/24`

## Jumphost Status Is Running, But Devices Behind Jumphost Are Not Discovered

### Check Incoming Traffic From the IP Fabric To a Jumphost

1.  On a jumphost machine run tcpdump with parameters: `tcpdump src <IPF_IP> and dst <JUMPHOST_IP>`

2.  On the IP Fabric instance open ssh/telnet session to any host behind jumphost

    ```
    autoboss@ip-fabric:~$ telnet 10.47.102.104
    Trying 10.47.102.104...
    Connected to 10.47.102.104.
    Escape character is '^]'.

    ##########################################################################
    ##        UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED              ##
    ## :::: $$$$$ ::::: ''''' ````` """"" ::::: $$$$$ ::::: ''''' ````` """ ##
    ##########################################################################
    ```
    ```
    root@jumphost:/home/autoboss# tcpdump src 10.0.9.13 and dst 10.0.9.17
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

    12:35:58.065549 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [P.], seq 1498215736:1498215828, ack 173264556, win 687, options [nop,nop,TS val 542423406 ecr 584899103], length 92
    12:35:58.066759 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 661, win 686, options [nop,nop,TS val 542423406 ecr 584912111], length 0
    12:35:58.068806 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 985, win 686, options [nop,nop,TS val 542423407 ecr 584912111], length 0
    ```

    If there is no incoming traffic, check **outgoing traffic from the IP Fabric to a jumphost**

### Check Outgoing Traffic From the IP Fabric To a Jumphost

1. On the IP Fabric instance run tcpdump with parameters: `tcpdump src <IPF_IP> and dst <JUMPHOST_IP>`

2. On the IP Fabric instance open ssh/telnet session to any host behind jumphost.

    ```shell
    root@ip-fabric:/home/autoboss# tcpdump src 10.0.9.13 and dst 10.0.9.17
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

    12:53:25.476825 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [P.], seq 156:248, ack 1657, win 687, options [nop,nop,TS val 542685257 ecr 585170204], length 92
    12:53:25.477998 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 2317, win 686, options [nop,nop,TS val 542685257 ecr 585173962], length 0
    ```

### Check Outgoing Traffic From a Jumphost To a Host

1.  On a jumphost run tcpdump with parameters: `tcpdump src <JUMPHOST_IP> and dst <HOST_IP>`

2.  On the IP Fabric instance open ssh/telnet to any host behind jumphost

    ```shell
    root@jumphost:/home/autoboss# tcpdump src 10.0.9.17 and dst 10.47.102.104
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

    12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
    12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
    ```

### Check Incoming Traffic From a Host To a Jumphost

1.  On a jumphost run tcpdump with parameters: `tcpdump src <HOST_IP> and dst <JUMPHOST_IP>`

2.  On the IP Fabric instance open ssh/telnet to any host behind jumphost

    ```shell
    root@jumphost:/home/autoboss# tcpdump src 10.47.102.104 and dst 10.0.9.17
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

    12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
    12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
    ```

## How To Restore access to IP Fabric's GUI After `jumphost` misconfiguration

If you suddenly cannot open the main GUI or SSH to the IP Fabric machine after saving the jumphost settings, the subnet/IP address of the IP Fabric machine was most likely included in the jumphost configuration.

To fix this issue, you need a **direct access** to the **virtual machine CLI** from your hypervisor, the password for `osadmin` user account, and do following:

1. Login with `osadmin` account to the **virtual machine CLI**

2. Filter `systemctl` output with `jumphost`. Each configured jumphost has its own ID.

    ```shell
    osadmin@ipfabric-server:~$ sudo systemctl | grep jumphost

    [sudo] password for osadmin: 
      jumphost@923216920.service                                   loaded activating auto-restart Jumphost (ID=923216920)
      system-jumphost.slic                                         loaded active     active       system-jumphost.slice
    ```

    ```shell
    osadmin@ipfabric-server:~$ systemctl status jumphost@923216920.service
    Failed to connect to bus: No such file or directory
    osadmin@ipfabric-server:~$ sudo systemctl status jumphost@923216920.service
    ● jumphost@923216920.service - Jumphost (ID=923216920)
         Loaded: loaded (/lib/systemd/system/jumphost@.service; disabled; vendor preset: enabled)
         Active: activating (auto-restart) (Result: exit-code) since Wed 2022-12-14 14:25:52 UTC; 6s ago
        Process: 682331 ExecStart=/opt/nimpee/jumphost/start-one.sh /opt/nimpee/conf.d/jumphost/923216920.conf (code=exited, status=1/FAILURE)
    ```

3. Stop the jumphost service with `sudo systemctl stop jumphost@xxxx.service`

4. Check that the **jumphost process is inactive** with `systemctl status jumphost@xxxx.service` command

    ```shell
    osadmin@ipfabric-server:~$ sudo systemctl status jumphost@923216920.service
    ● jumphost@923216920.service - Jumphost (ID=923216920)
         Loaded: loaded (/lib/systemd/system/jumphost@.service; disabled; vendor preset: enabled)
         Active: inactive (dead)

    Dec 14 14:28:55 ipfabric-server sshuttle[682901]: ssh: connect to host 2.3.2.1 port 22: Network is unreachable
    Dec 14 14:28:55 ipfabric-server sshuttle[682901]: c : fatal: c : failed to establish ssh session (2)
    Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: read eof
    Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: set expect_out(spawn_id) "exp3"
    Dec 14 14:28:55 ipfabric-server start-one.sh[682882]: expect: set expect_out(buffer) ""
    Dec 14 14:28:55 ipfabric-server start-one.sh[682915]: Dec 14 14:28:55 [ERROR] Jumphost was not started
    Dec 14 14:28:55 ipfabric-server systemd[1]: jumphost@923216920.service: Control process exited, code=exited, status=1/FAILURE
    Dec 14 14:28:55 ipfabric-server systemd[1]: jumphost@923216920.service: Failed with result 'exit-code'.
    Dec 14 14:28:55 ipfabric-server systemd[1]: Failed to start Jumphost (ID=923216920).
    Dec 14 14:29:13 ipfabric-server systemd[1]: Stopped Jumphost (ID=923216920).
    osadmin@ipfabric-server:~$ 

    ```

5. IP Fabric GUI should be accessible by now
