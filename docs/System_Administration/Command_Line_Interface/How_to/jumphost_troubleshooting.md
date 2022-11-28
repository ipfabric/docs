# Troubleshooting `jumphost`


## Jumphost Troubleshooting Tools

Scripts to start jumphosts are located in `/opt/nimpee/jumphost` folder.

Script logs are gathered in `/var/log/nimpee/net-jumphost-start-one.log` files.

IP Fabric doesn't work with DNS names that have IPv6 address in addition to IPv4 address. It is always better to use IPv4 address record.

It is a good practice to always check, after the jumphost is active and running, to ssh from the IP Fabric console to any network device behind the jumphost.

Other useful commands:

``` title="Gets Status of sshuttle"
sudo nimpee-net-jumphost -s
```

``` title="Manually Starts a Jumphost"
sudo nimpee-net-jumphost -1 192.168.11.197 -u autoboss -p password
```

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

```
root@ip-fabric:/home/autoboss# tcpdump src 10.0.9.13 and dst 10.0.9.17
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes



12:53:25.476825 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [P.], seq 156:248, ack 1657, win 687, options [nop,nop,TS val 542685257 ecr 585170204], length 92
12:53:25.477998 IP dev01.ipf.ipfabric.io.20718 > dev03.ipf.ipfabric.io.ssh: Flags [.], ack 2317, win 686, options [nop,nop,TS val 542685257 ecr 585173962], length 0
```

### Check Outgoing Traffic From a Jumphost To a Host

1.  On a jumphost run tcpdump with parameters: `tcpdump src <JUMPHOST_IP> and dst <HOST_IP>`

2.  On the IP Fabric instance open ssh/telnet to any host behind jumphost

```
root@jumphost:/home/autoboss# tcpdump src 10.0.9.17 and dst 10.47.102.104
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes



12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
```

### Check Incoming Traffic From a Host To a Jumphost

1.  On a jumphost run tcpdump with parameters: `tcpdump src <HOST_IP> and dst <JUMPHOST_IP>`

2.  On the IP Fabric instance open ssh/telnet to any host behind jumphost

```
root@jumphost:/home/autoboss# tcpdump src 10.47.102.104 and dst 10.0.9.17
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes



12:44:05.002545 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [S], seq 270942017, win 29200, options [mss 1460,sackOK,TS val 585033845 ecr 0,nop,wscale 9], length 0
12:44:05.004743 IP dev03.ipf.ipfabric.io.29736 > 10.47.102.104.telnet: Flags [.], ack 1464937247, win 29200, length 0
```

## How To Unstuck IP Fabric GUI After `jumphost` Misconfiguration

If you can't open the main GUI or SSH to the IP Fabric machine after saving the jumphost settings, the subnet/IP address of the IP Fabric machine was most likely included in the jumphost configuration.

To fix this issue, you have to have a **direct access** to the **virtual machine CLI** from a hypervisor, the password for `osadmin` user account, and do the following:

1. Login with `osadmin` account to the **virtual machine CLI**

2. Filter out the **jumphost** services with `systemctl | grep jumphost` command. Each configured jumphost has its own ID.

   ![systemctl_jumphost](../../../IP_Fabric_Settings/advanced/systemctl_jumphost.png)

3. **Stop the jumphost service** with the command `sudo systemctl stop jumphost@xxxx.service`, confirm the `osadmin` password

   ![systemctl_stop_jumphost](../../../IP_Fabric_Settings/advanced/systemctl_stop_jumphost.png)

4. Check that the **jumphost process is inactive** with `systemctl status jumphost@xxxx.service` command

   ![systemctl_status_jumphost](../../../IP_Fabric_Settings/advanced/systemctl_status_jumphost.png)

5. IP Fabric GUI should be accessible by now.

6. Login into the **IP Fabric main GUI** with your regular account and go to **Settings → Advanced → SSH/Telnet**.

7. Make a screenshot or copy the settings of the old jumphost and then delete or edit the jumphost settings.

   ![jumphost_delete_settings](../../../IP_Fabric_Settings/advanced/jumphost_delete_settings.png)

8. Put **IP address/subnet of the IP Fabric** machine to the **exclude IPv4 subnets** or **edit** the **IPv4 subnets** so it does **not contain the IP address of IP Fabric**.

   ![jumphost_exclude](../../../IP_Fabric_Settings/advanced/jumphost_exclude.png)

!!! info

    If **IP Fabric** becomes inaccessible via GUI or SSH again, repeat the previous steps and again edit the jumphost configuration.

