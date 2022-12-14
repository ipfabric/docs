---
description: In this section, we go deeper into the Command Line Interface (CLI) to discover network elements that IP Fabric's discovery is primarily using.
---

# SSH/TELNET

## Fine-Tune SSH/telnet CLI Parameters

The IP Fabric's discovery is primarily using Command Line Interface
(CLI) to discover network elements. The CLI Parameters can be found in **Settings → Advanced → SSH/TELNET**.

![CLI Settings](ssh/2396258368.png)

### Network Device Login Timeout

Timeout before the logging prompt is received. It may take longer for
remote branches over low-speed lines or overloaded devices to respond.

### Network Device Session Timeout

Too many **Command Timeout** errors during the Discovery process may
indicate that **Network device session timeout** is too short and the session is closed before the response arrives. It may be necessary to increase this timeout.

### Maximum Number Of Parallel Sessions

To prevent flooding your network with too many SSH/TELNET sessions set
**Maximum number of parallel sessions**. This setting can be also
helpful if the AAA server (TACACS/Radius) has a limit of parallel AAA
requests for users.

In rare cases, the Cisco ISE or similar systems may rate limit the
command authorization. When there are too many authorization failures
and Cisco ISE is in place, try to limit the number of parallel sessions
down to 10 and steadily increase.

### Basic Failure

How many times to retry a connection for any error, except
authentication failure.

### Authentication Failure

**Authentication failure** can occur even if a user is authorized to
Login. For example, this may happen when an AAA server is overloaded or
an authentication packet is lost.

### Command Authorization Failure Retries

If you see many examples of **Authentication error** during the
Discovery process, please adjust **Authentication failure** and
**Command Authorization Failure retries**.

### Example Of Error Message In Connectivity Report

According to the summary of issues in the very first completed snapshot,
the CLI Settings can be adjusted. Here are some of the most common
errors and adjustments:

| Error                                                                          | Error Type                    | How To Mitigate                                                                                                    |
| ------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| connect ETIMEDOUT XX.XX.XX.XX:22                                               | Connection error              | Received no response from the destination.                                                                         |
| connect ECONNREFUSED XX.XX.XX.XX:22                                            | Connection error              | The connection to the destination is being blocked by an access-list or firewall.                                  |
| All configured authentication methods failed                                   | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed                                                          | Authentication error          | Unable to authenticate to the destination host                                                                     |
| Authentication failed - login prompt appeared again                            | Authentication error          | Unable to authenticate to the destination host                                                                     |
| SSH client not received any data for last 120000 ms! cmd => show vrrp \| e #^$ | Command timeout               | The command 'show vrrp \| e #^$' timed out. Increase **device session timeout.**                                   |
| Can't detect prompt                                                            | Command timeout               | Unable to detect CLI prompt. Increase **network device login timeout.**                                            |
| Command "enable" authorization failed, tried 2x                                | Command authorization failure | The command wasn't authorized. **Increase command authorization failure retries** or increase the timer value (ms) |

## Setting Up Jumphost

**Jumphost** allows to set-up a connection to the server which can be used as a **proxy server for discovery** purposes. IP Fabric uses an SSH tunnel established by python on the client and the server side.

The user used for **Jumphost** connection must have access to jumphosts `shell` and must be able to run `pyhton`.

We successfully tested IP Fabric against jumphosts with the following python versions:

| Jumphost Python Version |               |
|-------------------------|---------------|
| 2.7                     | tested        |
| 3.4                     | tested        |
| 3.5                     | tested        |
| 3.6                     | **supported** |
| 3.7                     | **supported** |
| 3.8                     | **supported** |
| 3.9                     | **supported** |
| 3.10                    | tested        |

!!! Note "Tested vs. Supported"

    `tested` -- Python version was successfully tested on a jumphost however it is not officially supported by the underlying SSH tunnel project.

    `supported` -- Python version was successfully tested on a jumphost and it is officially supported by the underlying SSH tunnel project.
    **We strongly recommend using the supported Python versions in your production environment.**

!!! warning

    Please bear in mind, that once the connection is established, it will be enabled permanently, until disabled or removed! If there are any network issues, IP Fabric software will try to establish a connection periodically.

!!! important

    In Discovery Seed, at least one IP address behind the Jumphost has to be provided as a starting point.

### Adding New Jumphost

- Open jumphost settings, using item **Settings → Advanced → SSH/TELNET**
- At the bottom of the page, please select **+ Add** button

  ![Jump host settings](ssh/1384480773.png)

- Fill in all necessary data

  ![Add Jumphost](ssh/1384480780.png)

  - **Label** - the name for configuration (mandatory)
  - **Jump host Address** - IP address of FQDN name (mandatory)
  - **IPv4 subnets** - subnet in CIDR representation, allows adding more than open, separated with spaces (mandatory)

    !!! warning

        If you use `0.0.0.0/0` or another subnet that **includes the IP address of IP Fabric**, please make sure to **add IP Fabric IP address/subnet** to **"Exclude IPv4 subnet"**. Otherwise, the connection to IP Fabric will be lost and you **will not** be able to **access IP Fabric GUI/CLI** and it will require manual intervention to fix.

        Also if you have multiple jumphosts that have IP address that is part of include list of another jumphost, add the IP addresses in all the other jumphosts exclude lists.


  - **Exclude IPv4 subnets** - subnet to exclude in CIDR representation, allows to add more than open, separated with spaces (optional)
  - **Login type**
  - **Use credentials** - required to provide username and password
  - **Use SSH keys** - if you copied the ssh public key to the proxy server, it won’t require providing a password (please jump to the _SSH key configuration_ section)
  - **Username** - Username for authentication (mandatory)
  - **Password** - password for authentication (mandatory if ‘Use credentials’ is used) i.e., refer to the picture below.

    --8<-- "snippets/username_password_regex.md"

- Click **+ Add** button

- If a connection is open, you will see the **_Running_** status in the Jumphost list

  ![Jumphost list](ssh/1384513560.png)

### SSH Key Configuration

!!! info

    To avoid using a password for authentication, you can add the ssh key to the proxy server.

#### Copy SSH Key Manually

1. Download the ssh key from Jumphost settings

   ![Download ssh key](ssh/1384153110.png)

2. Save `jumphost-public-key.pub`

3. Insert content of the `jumphost-public-key.pub` file to the `authorized_keys` file of the user that will authenticate with Jumphost server. Please follow official documentation at <https://www.ssh.com/academy/ssh/authorized-key>.

   You can also use `ssh-copy-id` on your machine to deploy the key (see below).

4. After the key is transferred to the jumphost server, you can use the option _`Use SSH keys`_ instead of _`Use credentials`_

#### Use `ssh-copy-id`

1. Login to IP Fabric CLI using `osadmin` account.

2. Change to user `autoboss` by running `sudo su - autoboss`.

3. Run `ssh-copy-id` with specified identity file replacing `<jumphost-user>` with the
   jumphost user and `<jumphost-ip>` with the IP or FQDN of the jumphost server:

   1. `ssh-copy-id -i ~/.ssh/ipf-jumphost.pub <jumphost-user>@<jumphost-ip>`
   2. When prompted for a password, use the jumphost user's password.

4. To test, ssh to the jumphost server with: `ssh <jumphost-user>@<jumphost-ip>`

5. If the key has been copied you can use the option _`Use SSH keys`_
   instead of _`Use credentials`_

### Disabling Jumphost Connection

1. Edit configuration that needs to be disabled, i.e.\

   ![Jumphost settings](ssh/1384972305.png)

2. Change the setting to **Disabled**,

3. Click the **Update** button

   ![Disable jumphost](ssh/1384906766.png)

### Remove Jumphost Configuration

1. On the Jumphost servers list, select the server you want to remove

2. Click **Delete** button

   ![Delete jumphost](ssh/1384939529.png)

3. (If SSH key authentication was enabled) Delete inserted IP Fabric public key from the `authorized_keys` file on the jumphost server added in the [SSH Key Configuration](#ssh-key-configuration).

## Jumphost Known Issues

### Non-TCP Discovery

Only TCP connections work through the jumphost.

Traceroute with ICMP is not supported so the discovery process might not be able to get over the unreachable parts of the network (for example sites separated by the provider’s network).

Because of this, you will have to add at least one IP address of a network device from each site to the [Discovery seeds](../discovery_seed.md) settings.

### IP Fabric Is Not Accessible After Saving Jumphost Configuration

If you can't open the main GUI or SSH to the IP Fabric machine, the subnet/IP address of the IP Fabric machine was most likely included in the jumphost configuration.

To fix this issue, you have to have a **direct access** to the **virtual machine CLI** from a hypervisor, the password for `osadmin` user account, and do the following:

1. Login with `osadmin` account to the **virtual machine CLI**

2. Filter out the **jumphost** services with `systemctl | grep jumphost` command. Each configured jumphost has its own ID.

   ![systemctl_jumphost](systemctl_jumphost.png)

3. **Stop the jumphost service** with the command `sudo systemctl stop jumphost@xxxx.service`, confirm the `osadmin` password

   ![systemctl_stop_jumphost](systemctl_stop_jumphost.png)

4. Check that the **jumphost process is inactive** with `systemctl status jumphost@xxxx.service` command

   ![systemctl_status_jumphost](systemctl_status_jumphost.png)

5. IP Fabric GUI should be accessible by now.

6. Login into the **IP Fabric main GUI** with your regular account and go to **Settings → Advanced → SSH/Telnet**.

7. Make a screenshot or copy the settings of the old jumphost and then delete or edit the jumphost settings.

   ![jumphost_delete_settings](jumphost_delete_settings.png)

8. Put **IP address/subnet of the IP Fabric** machine to the **exclude IPv4 subnets** or **edit** the **IPv4 subnets** so it does **not contain the IP address of IP Fabric**.

   ![jumphost_exclude](jumphost_exclude.png)

!!! info

    If **IP Fabric** becomes inaccessible via GUI or SSH again, repeat the previous steps and again edit the jumphost configuration.

## Custom SSH/Telnet Ports

!!! info

    Custom SSH/Telnet ports settings enable the discovery process to use different ports for connecting. The standard for SSH is port 22 and 23 for Telnet.

In the following example we configure the discovery process to use port `8080`
for SSH connections to `192.168.168.10`:

![edit custom ssh telnet port](ssh/edit_custom_ssh_telnet_port.png)

As a result of such configuration, we would create a new item under the
**Custom SSH/Telnet ports** configuration, which will be applied to every
new snapshot created by IP Fabric.

![custom ssh telnet ports](ssh/custom_ssh_telnet_ports.png)

## Telnet/SSH URL Handler On MS Windows 7 And Later

If you want to be able to connect directly to a device from the IP Fabric web
interface, you need to register a Telnet/SSH URL handler. You will be touching
Windows Registry, please, be sure that you know what you are doing, have
appropriate backups, and are comfortable in doing so.

### Backup Windows Registry

1. Click `Start`, type `regedit.exe` in the search box, and then press `Enter`
2. In Registry Editor, click **File → Export**
3. In the Export Registry File box, select the location where you want to save the backup copy, name your backup file, and click _Save_

### Putty

#### Download Putty

1. Go to <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>
2. Download `Putty`
3. This tutorial expects Putty in `C:\Program Files (x86)\putty.exe`

#### Register Telnet/SSH URL Handler

1. Go to <https://gist.github.com/sbiffi/11256316>
2. Download `putty.reg` file
3. Edit path to Putty if differs from `C:\Program Files (x86)\putty.exe`
4. Download `putty.vbs` (save it to `C:\putty.vbs` or change this path in `putty.reg` above)
5. Edit path to Putty if differs from `C:\Program Files (x86)\putty.exe`
6. Launch `putty.reg` to associate `ssh://` and `telnet://` to this script

### SecureCRT

#### Download SecureCRT

SecureCRT is not free software. To obtain SecureCRT license please visit <https://www.vandyke.com/products/securecrt/>

#### Register Telnet/SSH URL Handler

1. Download [securecrt.reg](ssh/securecrt.reg)
2. Edit path to SecureCRT if differs from `C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe`
3. Launch `securecrt.reg` to associate `ssh://` and `telnet://` to this script
