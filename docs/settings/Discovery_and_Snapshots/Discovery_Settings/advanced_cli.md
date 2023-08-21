---
description: In this section, we go deeper into the Command-Line Interface (CLI) to discover network elements that IP Fabric's discovery is primarily using.
---

# Advanced CLI

## Fine-Tune SSH/Telnet CLI Parameters

IP Fabric's discovery is primarily using the Command-Line Interface
(CLI) to discover network elements. The CLI parameters can be found in
**Settings --> Discovery & Snapshots --> Discovery Settings --> Advanced CLI**.

![CLI Settings](advanced_cli/cli_settings.png)

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

## Custom SSH/Telnet Ports

!!! info

    Custom SSH/Telnet ports settings enable the discovery process to use different ports for connecting. The standard for SSH is port 22 and 23 for Telnet.

In the following example, we configure the discovery process to use port `8080`
for SSH connections to `192.168.168.10`:

![Add custom SSH/Telnet port](advanced_cli/add_custom_ssh_telnet_port.png)

As a result of such a configuration, we would create a new item in the **Custom
SSH/Telnet ports** table, which will be applied to every new snapshot created by
IP Fabric.

![Custom SSH/Telnet ports](advanced_cli/custom_ssh_telnet_ports.png)

## Telnet/SSH URL Handler On MS Windows 7 And Later

If you want to be able to connect directly to a device from the IP Fabric web
interface, you need to register a Telnet/SSH URL handler. You will be touching
Windows Registry, please, be sure that you know what you are doing, have
appropriate backups, and are comfortable in doing so.

### Backup Windows Registry

1. Click `Start`, type `regedit.exe` in the search box, and then press `Enter`
2. In Registry Editor, click **File --> Export**
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

1. Download [securecrt.reg](advanced_cli/securecrt.reg)
2. Edit path to SecureCRT if differs from `C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe`
3. Launch `securecrt.reg` to associate `ssh://` and `telnet://` to this script
