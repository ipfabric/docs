---
description: In this section, we will explain how to set up jumphosts.
---

# Jumphost

## Setting Up Jumphost

**Jumphost** allows setting up a connection to a server that can be used as a
**proxy server for discovery**. IP Fabric uses an SSH tunnel established by
Python on the client and server sides.

The user account used for **jumphost** connection must have access to the
jumphost's shell and must be able to run Python.

We successfully tested IP Fabric against jumphosts with the following Python
versions:

| Jumphost's Python Version  | Status        |
| :------------------------- | : ----------- |
| `2.7`                      | tested        |
| `3.4`                      | tested        |
| `3.5`                      | tested        |
| `3.6`                      | **supported** |
| `3.7`                      | **supported** |
| `3.8`                      | **supported** |
| `3.9`                      | **supported** |
| `3.10`                     | tested        |
| `3.11`                     | tested        |
| `3.12`                     | tested        |
| `3.13`                     | tested        |

!!! note "Tested vs. Supported"

    `tested` -- Python version was successfully tested on a jumphost. However,
    it is not officially supported by the underlying SSH tunnel project.

    `supported` -- Python version was successfully tested on a jumphost and is
    officially supported by the underlying SSH tunnel project. **We strongly
    recommend using a supported Python version in your production environment.**

!!! warning

    Please bear in mind that once the connection is established, it will be
    enabled permanently until disabled or removed! If there are any network
    issues, IP Fabric will try to establish a connection periodically.

!!! important

    In the [Discovery Seeds](../Discovery_Settings/discovery_seeds.md) settings,
    at least one IP address behind the jumphost has to be provided as a starting
    point.

### Adding New Jumphost

1. Navigate to **Settings --> Discovery & Snapshots --> Global Configuration -->
   Jumphost**.

2. On the page, click **+ Add**:

   ![Add button](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_add_button.webp)

3. Fill in all necessary data:

   ![Add Jumphost form](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_add_jumphost_form.webp)

   - **Label** -- _(mandatory)_ Name of the configuration.

   - **Jumphost Address** -- _(mandatory)_ IP address or FQDN name.

   - **Port** -- _(optional)_  Port number to connect. Defaults to the standard 22 if not specified.

   - **IPv4 subnets** -- _(mandatory)_ Subnet in CIDR representation. Allows
     adding more than one, separated with spaces. The subnet `0.0.0.0/0` cannot
     be added here.

    !!! warning

        If you use any subnet that **includes IP Fabric's IP address or the IP
        address of its default gateway**, please **add both of these IP
        addresses or the IP Fabric subnet** to **Exclude IPv4 subnet**.
        Otherwise, the connection to IP Fabric will be lost, and you **will
        not** be able to **access the IP Fabric GUI/CLI**, requiring manual
        intervention to fix.

        Also, if you have multiple jumphosts with IP addresses that are part of
        the include list of another jumphost, add these IP addresses to all the
        other jumphosts' exclude lists.

   - **Exclude IPv4 subnets** -- _(optional)_ Subnet to exclude in CIDR
     representation. Allows adding more than one, separated with spaces.

   - **Login type**

     - `Use credentials` -- Required to provide username and password.

     - `Use SSH keys` -- If you copied the SSH public key to the proxy server,
     it won't require providing a password (please jump to the
     [SSH Key Configuration](#ssh-key-configuration) section).

   - **Username** -- _(mandatory)_ Username for authentication.

   - **Password** -- _(mandatory if `Use credentials` is selected)_ Password for
     authentication.

    --8<-- "snippets/username_password_regex.md"

4. Click the green **Add** button to save the configuration.

5. If the connection is open, you will see `Yes` in the `Status` column in the
   `Jumphost settings` table:

   ![Jumphost settings table - Yes status for jumphost](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_jumphost_settings_table.webp)

### SSH Key Configuration

!!! info

    To avoid using a password for authentication, you can add the SSH key to the
    proxy server.

#### Copy SSH Key Manually

1. Download the SSH key from Jumphost settings:

   ![Download public key button](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_download_public_key_button.webp)

2. Save `jumphost-public-key.pub`.

3. Insert the content of the `jumphost-public-key.pub` file into the
   `authorized_keys` file of the user that will authenticate with the jumphost
   server. Please follow the official documentation at
   <https://www.ssh.com/academy/ssh/authorized-key>.

   You can also use `ssh-copy-id` on your machine to deploy the key (see below).

4. After the key is transferred to the jumphost server, you can use the `Use SSH
   keys` option instead of `Use credentials`.

#### Use `ssh-copy-id`

1. Log in to the IP Fabric CLI using the `osadmin` account.

2. Change to the `autoboss` user by running `sudo su - autoboss`.

3. Run `ssh-copy-id` with the specified identity file, replacing
   `<jumphost-user>` with the jumphost user and `<jumphost-ip>` with the IP or
   FQDN of the jumphost server:

   1. `ssh-copy-id -i ~/.ssh/ipf-jumphost.pub <jumphost-user>@<jumphost-ip>`
   
   2. When prompted for a password, use the jumphost user's password.

4. To test, connect to the jumphost server via SSH with: `ssh
   <jumphost-user>@<jumphost-ip>`

5. If the key has been copied, you can use the `Use SSH keys` option instead of
   `Use credentials`.

### Disabling Jumphost Connection

1. Edit the configuration that needs to be disabled, i.e.:

   ![Edit icon](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_edit_icon.webp)

2. Change the setting to `Disabled`.

3. Click **Update**.

   ![Disable jumphost](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_disable_jumphost.webp)

### Remove Jumphost Configuration

1. In the `Jumphost settings` table, select the server you want to remove.

2. Click **Delete**.

   ![Delete jumphost](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_delete_jumphost.webp)

3. (If SSH key authentication was enabled) Delete the inserted IP Fabric public
   key from the `authorized_keys` file on the jumphost server added in the
   [SSH Key Configuration](#ssh-key-configuration).

## Jumphost Known Issues

### `Invalid Input` Error When Saving Jumphost Configuration

This might be caused by one of the following requirements not being met:

- The jumphost's **IPv4 subnets** must not contain the subnet `0.0.0.0/0`.

- If a subnet in the jumphost's **IPv4 subnets** contains either IP Fabric's IP
  address or the IP address of its default gateway, then these IP addresses must
  be added to **Exclude IPv4 subnets**.

- The `127.0.0.0/8` network must not be included in **IPv4 subnets**. If it is
  currently part of **IPv4 subnets**, it must be explicitly added to **Exclude
  IPv4 subnets**.

- The **Username** or **Password** configured for the jumphost must not contain
  any restricted characters.

### Non-TCP Discovery

Only TCP connections work through the jumphost.

Traceroute with ICMP is not supported, so the discovery process might not be
able to traverse the unreachable parts of the network (for example, sites
separated by the provider's network).

Due to this, you will have to add at least one IP address of a network device
from each site to the
[Discovery Seeds](../Discovery_Settings/discovery_seeds.md) settings.

### IP Fabric Is Not Accessible After Saving Jumphost Configuration

If you can't open the main GUI or connect to the IP Fabric machine via SSH, the
subnet/IP address of the IP Fabric machine was most likely included in the
jumphost configuration.

To fix this issue, you must have **direct access** to the **virtual machine's
CLI** from the hypervisor, the password for the `osadmin` user account, and
follow these steps:

1. Log in to the **virtual machine's CLI** with the `osadmin` account.

2. Filter out the **jumphost** services with the `systemctl | grep ipf-jumphost`
   command. Each configured jumphost has its own `ID`.

   ```shell
   osadmin@Appliance-5:~$ systemctl | grep ipf-jumphost
     ipf-jumphost@10001843.service                               loaded activating auto-restart ipf-jumphost (ID=10001843)
   ```

3. **Stop the jumphost service** with the `sudo systemctl stop
   ipf-jumphost@<ID>.service` command and enter the `osadmin` password:

   ```shell
   osadmin@Appliance-5:~$ sudo systemctl stop ipf-jumphost@10001843.service
   [sudo] password for osadmin: 
   osadminaAppliance-5:~$ 
   ```

4. Check that the **jumphost process is inactive** with the `systemctl status
   ipf-jumphost@<ID>.service` command:

   ```shell
   osadmin@Appliance-5:~$ sudo systemctl status ipf-jumphost@10001843.service
   ● ipf-jumphost@10001843.service - ipf-jumphost (ID=10001843)
        Loaded: loaded (/lib/systemd/system/ipf-jumphost@.service; disabled; vendor preset: enabled)
        Active: inactive (dead)

   Jul 12 13:53:25 Appliance-5 sshuttle[671008]: ssh: connect to host 192.168.5.5 port 22: Network is unreachable
   Jul 12 13:53:25 Appliance-5 sshuttle[671008]: c : fatal: c : failed to establish ssh session (2)
   Jul 12 13:53:25 Appliance-5 start-one.sh[670989]: expect: read eof
   Jul 12 13:53:25 Appliance-5 start-one.sh[670989]: expect: set expect_out(spawn_id) "exp3"
   Jul 12 13:53:25 Appliance-5 start-one.sh[670989]: expect: set expect_out(buffer) ""
   Jul 12 13:53:26 Appliance-5 start-one.sh[671021]: Jul 12 13:53:25 [ERROR] Jumphost was not started
   Jul 12 13:53:26 Appliance-5 systemd[1]: ipf-jumphost@10001843.service: Control process exited, code=exited, status=1/FAILURE
   Jul 12 13:53:26 Appliance-5 systemd[1]: ipf-jumphost@10001843.service: Failed with result 'exit-code'.
   Jul 12 13:53:26 Appliance-5 systemd[1]: Failed to start ipf-jumphost (ID=10001843).
   Jul 12 13:53:36 Appliance-5 systemd[1]: Stopped ipf-jumphost (ID=10001843).
   ```

5. The IP Fabric GUI should now be accessible.

6. Log in to the **IP Fabric main GUI** with your regular account and go to
   **Settings --> Discovery & Snapshots --> Global Configuration --> Jumphost**.

7. Make a screenshot or copy the settings of the old jumphost. Then, delete or
   edit the jumphost settings.

   ![Jumphost settings - edit or delete](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_jumphost_delete_settings.webp)

8. Put the **IP address/subnet of the IP Fabric machine** to **Exclude IPv4
   subnets** or **edit** the **IPv4 subnets** so it does **not contain the IP
   address of IP Fabric**:

   ![Add IP Fabric VM's IP address to jumphost's exclude list](../../../images/settings/IP_Fabric_Settings-Discovery_and_Snapshots-Global_Configuration-jumphost_jumphost_exclude.webp)

!!! info

    If IP Fabric becomes inaccessible via GUI or SSH again, repeat the previous
    steps and again edit the jumphost configuration.
