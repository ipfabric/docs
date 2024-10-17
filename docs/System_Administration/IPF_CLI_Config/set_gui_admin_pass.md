---
description: This section explains how to set initial admin password to IPF GUI using IPF CLI Config.
---

# Set the `admin` Password for the Main IP Fabric GUI

1. Connect to your IP Fabric appliance via SSH as the `osadmin` user.

2. Run:

   ```shell
   sudo ipf-cli-config -u
   ```

3. Select `Yes` to proceed:

   ![Do you want to set admin user password?](gui_admin_password_change.png){: width="500" .center}

4. Enter the new `admin` password twice:

   ![Enter admin user password](gui_admin_password_change2.png){: width="600" .center}

   ![Repeat admin user password](gui_admin_password_change3.png){: width="600" .center}

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

      ![Retry setting an admin password](gui_admin_password_change4.png){: width="500" .center}

5. Select `No` to prevent rebooting the system.

   ![Do not reboot the system](gui_admin_password_change5.png){: width="500" .center}
