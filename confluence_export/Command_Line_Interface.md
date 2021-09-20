# Command Line Interface

## Command Line Interface

The command-line interface is a secondary service interface in IP Fabric
VM which serves troubleshooting and testing purposes. For example, for
testing authentication credentials from the specific IP address of IP
Fabric VM, in case of address-restricted access. The CLI interface is
the main tool in servicing the system by the support teams.

A first boot wizard can be used to change system settings, such as IP
addressing parameters, domain names, NTP, system proxy settings, or a
user's password. To launch First Boot Wizard again, connect via SSH to
IP Fabric as ***osadmin*** user, launch ipfabric-net-wizard and then
reboot the system.

Command-line also allows the use of the standard networking tools, such
as telnet, ssh, traceroute or ping.

## Troubleshooting VM network problems using IP Fabric CLI

In the event of a VM network connection problem, DNS issues, network
devices connectivity issue, IP Fabric CLI is a useful helper.

CLI can be also used to access system and application logs as well as
snapshot files.

### System and application logs

System and application logs are placed in ***/var/log*** folder.
Specifically IP Fabric application logs can be found in
***/var/log/nimpee***.

### Snapshots

Snapshots are available in ***osadmin*** home directory
***/home/osadmin/snapshots***. Each folder inside represents one
snapshot. Even if snapshots can be copied manually using SCP or SFTP
it's strongly recommended to use the export feature in web UI.

### Checking the network interface settings

When you log in through a VM console or SSH, network settings are
displayed.

<div>

<div>

This content is static, generated when VM boots! When DHCP is used, an
IP address can change in some cases.

</div>

</div>

<img src="attachments/1878327499/1878327505.png" class="image-left" loading="lazy" data-image-src="attachments/1878327499/1878327505.png" data-height="140" data-width="354" data-unresolved-comment-count="0" data-linked-resource-id="1878327505" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-07-23 14_26_45-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327499" data-linked-resource-container-version="3" data-media-id="e6bcd743-9914-485c-9ab1-db47090bf203" data-media-type="file" />

To display actual IP address use command:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
ip addr show
```

</div>

</div>

Default gateway and other routes (if configured) can be check as
follows:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
ip r
```

</div>

</div>

### Checking DNS

DNS can be checked using the ***dig*** or ***nslookup*** command.

For example, let's check A record and PTR (reverse) record of some
device using ***dig***.

For A record check ***ANSWER*** which contains requested IP address.
Also ***SERVER*** section below is important as it tell us what DNS
server answered our DNS query.

<img src="attachments/1878327499/1878327514.png?width=224" class="image-left" loading="lazy" data-image-src="attachments/1878327499/1878327514.png" data-height="344" data-width="603" data-unresolved-comment-count="0" data-linked-resource-id="1878327514" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-14 15_08_44-10.0.32.205 (1) - SecureCRT.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327499" data-linked-resource-container-version="3" data-media-id="d566906f-bbd2-4cd8-8187-97d110c5f697" data-media-type="file" width="224" />

For PTR record check ***ANSWER*** which contains requested domain name.

<img src="attachments/1878327499/1878327511.png?width=224" class="image-left" loading="lazy" data-image-src="attachments/1878327499/1878327511.png" data-height="550" data-width="610" data-unresolved-comment-count="0" data-linked-resource-id="1878327511" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-14 15_09_04-10.0.32.205 (1) - SecureCRT.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327499" data-linked-resource-container-version="3" data-media-id="fb5a2af2-1bee-4430-891e-1f7468221771" data-media-type="file" width="224" />

If you prefer ***nslookup*** you can achieve the same results.

<img src="attachments/1878327499/1878327508.png" class="image-left" loading="lazy" data-image-src="attachments/1878327499/1878327508.png" data-height="204" data-width="533" data-unresolved-comment-count="0" data-linked-resource-id="1878327508" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-14 15_14_39-10.0.32.205 (1) - SecureCRT.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327499" data-linked-resource-container-version="3" data-media-id="6a3162e7-4d20-4f8c-9429-01072b1f70da" data-media-type="file" />

### Testing connectivity to a network device

The very basic test is ***ping*** or ***traceroute***.

<div>

<div>

### ICMP

Please bear in mind that ICMP packets used by ***ping*** and
***traceroute*** can be blocked by ACL or firewall. It does not mean
that a device cannot be reached using SSH or telnet.

</div>

</div>

To make sure that the network device is available from IP Fabric VM, you
can use the ***telnet*** and ***ssh*** client from the command line.

For SSH use:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
ssh userName@device-IP-or-Hostname
```

</div>

</div>

For telnet use:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
telnet device-IP-or-Hostname
```

</div>

</div>

### Reboot and shutdown

IP Fabric VM can be also rebooted or shutdown using CLI.

For VM reboot just use ***reboot*** command without any parameters.

For VM shutdown use ***shutdown*** command without any parameters.

  
