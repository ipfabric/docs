---
description: This section explains how to change the osadmin password using IPF CLI Config.
---

# Update `osadmin` Password

!!! warning

    Changing the `osadmin` password will affect:

    - CLI access
    - backup encryption

    Backups created before the password change **will no longer be restorable**:

    - All backups are encrypted using the `osadmin` password that was set at the time of their creation.
    - This means that if you change the `osadmin` password, any backups created prior to the change will no longer be restorable—unless you temporarily revert the password back to the original one used when the backups were made.
    - If you attempt to restore a backup with an incorrect password, the system will not display any available backups, as it won’t be able to decrypt them.
    - Before changing the `osadmin` password, ensure that you’ve either restored all necessary backups or are prepared to create new ones using the new password.

## How To Update `osadmin` Password

1. Connect to your IP Fabric appliance via SSH as the `osadmin` user.

2. Run:

   ```shell
   sudo ipf-cli-config -t
   ```

3. Select `Yes` to proceed:

  ![Do you want to change osadmin user password?](../../images/settings/System_Administration-IPF_CLI_Config_osadmin_password_change2.png){width=500 .center}

4. Enter the new `osadmin` password twice:

   ![Enter osadmin shell user password](../../images/settings/System_Administration-IPF_CLI_Config_osadmin_password_change3.png){width=500 .center}

   ![Repeat osadmin user password](../../images/settings/System_Administration-IPF_CLI_Config_osadmin_password_change4.png){width=500 .center}

   Password setup contains password [complexity check](#password-requirements); simple passwords are
   rejected.

5. Select `Yes` to reboot the system:

  ![Reboot system](../../images/settings/System_Administration-IPF_CLI_Config_reboot.png){width=500 .center}

## Password Requirements

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
