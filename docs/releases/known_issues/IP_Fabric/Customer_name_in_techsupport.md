# Customer name in techsupport

!!! info

    This issue was fixed in release `6.0.1` of IP Fabric.

Customer name is stored in `/opt/nimpee/conf.d/sys-nimpee.conf`. Its default value is `IPF` after installation and
updated to real customer name upon license upload. When license upload fails, customer name is not updated and generated
techsupport contains `IPF` as a customer name.

Affects only new installations, not upgrades.

User `autoboss` has to be able to create new files in `/opt/nimpee/conf.d/` directory in order to update customer name.
This directory is not writable for user `autoboss` in appliance between versions 5.0.0 and 6.0.1.

Release 6.0.1 implements a fix for this issue, but you still have to re-upload the license.

For older releases between 5.0.0 and 6.0.0 it can be fixed manually:

1. change permissions for `autoboss` user for

  ```shell
  # chown root:autoboss /opt/nimpee/conf.d/
  # chmod 0775 /opt/nimpee/conf.d/
  ```

1. re-upload license
1. validate customer name in `/opt/nimpee/conf.d/sys-nimpee.conf`:

  ```shell
  # grep custname /opt/nimpee/conf.d/sys-nimpee.conf
  custname="IPF"
  #
  ```
