---
description: This section explains how to set initial admin password to IPF GUI using IPF CLI Config.
---

# Set the `admin` Password for the Main IP Fabric GUI

## Set `admin` Password via IPF CLI Config Tool

1. Connect to your IP Fabric appliance via SSH as the `osadmin` user.

2. Run:

   ```shell
   sudo ipf-cli-config -u
   ```

3. Select `Yes` to proceed:

   ![Do you want to set admin user password?](gui_admin_password_change.webp){: width="500" .center}

4. Enter the new `admin` password twice:

   ![Enter admin user password](gui_admin_password_change2.webp){: width="600" .center}

   ![Repeat admin user password](gui_admin_password_change3.webp){: width="600" .center}

   Password setup contains password complexity check; simple passwords are
   rejected.

   Password requirements are as follows:

   - The maximum password length is 256.
   - Single-character class passwords are not supported.
   - Two-character class must be at least 24 characters long.
   - The minimal length of the passphrase is 24 characters.
   - Three-character class must be at least 16 characters long.
   - Four-character class must be at least 12 characters long.
   - The passphrase must have at least five words.

   The character classes are:

   - digits
   - lower-case letters
   - upper-case letters
   - other characters

   There is also a special class for non-ASCII characters, which could not be 
   classified but are assumed to be non-digits.

  !!! Info

      If the password is already set or the database has not started yet, you can retry.

      ![Retry setting an admin password](gui_admin_password_change4.webp){: width="500" .center}

5. Select `No` to prevent rebooting the system.

   ![Do not reboot the system](gui_admin_password_change5.webp){: width="500" .center}

## Create a User with Administrative Privileges via CLI

The `IPF CLI Config` tool can only create the `admin` user for the main GUI. If you need to create an additional user with administrative privileges or if you have forgotten the password for the `admin` user and you need to log in to the GUI as a different user, follow these steps:

1. Connect to your IP Fabric appliance via SSH as the `osadmin` user.

2. Switch to the `root` user using the following command:
   
   ```
   sudo su
   ```

3. Navigate to the `/opt/ipf-backend-cli-tools` directory:

   ```
   cd /opt/ipf-backend-cli-tools
   ```

4. Run the following command:

   ```
   bin/ipf-backend-cli-tools create-admin-user --username <name_of_admin_user> --password <password_of_admin_user>
   ```

