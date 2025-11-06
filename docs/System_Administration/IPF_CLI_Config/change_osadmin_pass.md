---
description: This section explains how to change the osadmin password using IPF CLI Config.
---

# Update `osadmin` Password

1. Connect to your IP Fabric appliance via SSH as the `osadmin` user.

2. Run:

   ```shell
   sudo ipf-cli-config -t
   ```

3. Select `Yes` to proceed:

  ![Do you want to change osadmin user password?](osadmin_password_change2.webp)

  !!! warning

      Changing the `osadmin` password will affect:

      - CLI access
      - System Administration UI access
      - backup encryption

      Backups created before the password change **will no longer be restorable**:

      - All backups are encrypted using the `osadmin` password that was set at the time of their creation.
      - This means that if you change the `osadmin` password, any backups created prior to the change will no longer be restorable—unless you temporarily revert the password back to the original one used when the backups were made.
      - If you attempt to restore a backup with an incorrect password, the system will not display any available backups, as it won’t be able to decrypt them.
      - Before changing the `osadmin` password, ensure that you’ve either restored all necessary backups or are prepared to create new ones using the new password.

4. Enter the new `osadmin` password twice:

   ![Enter osadmin shell user password](osadmin_password_change3.webp)

   ![Repeat osadmin user password](osadmin_password_change4.webp)

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

5. Select `Yes` to reboot the system:

  ![Reboot system](reboot.webp)
