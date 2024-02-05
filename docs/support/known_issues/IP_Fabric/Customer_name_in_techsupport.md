---
description: On some old IP Fabric versions, the generic customer name 'IPF' was not updated upon license upload. This page explains how to fix that.
---

# Customer name in techsupport

!!! info

    This issue was fixed in IP Fabric version `6.0.1`.

The customer name is stored in `/opt/nimpee/conf.d/sys-nimpee.conf`. Its default
value is `IPF` after the initial deployment and it is updated to the real
customer name upon license upload. When license upload fails, the customer name
is not updated and generated techsupports would contain `IPF` as the customer
name.

Affects only new deployments of versions between `5.0.0` and `6.0.0`, not
upgrades.

The `autoboss` user must be able to create new files in the
`/opt/nimpee/conf.d/` directory to update the customer name. Between versions
`5.0.0` and `6.0.0`, this directory was not writable for the `autoboss` user.

Version `6.0.1` fixes this issue, but you still have to re-upload your license.

On older versions between `5.0.0` and `6.0.0`, the issue can be fixed manually
(`#` denotes a root prompt):

1. Log in to the IP Fabric CLI as the `osadmin` user.

1. Change to the `root` user with the `sudo su` command.

1. Change the ownership and permissions of the `/opt/nimpee/conf.d/` directory:

   ```shell
   # chown root:autoboss /opt/nimpee/conf.d/
   # chmod 0775 /opt/nimpee/conf.d/
   ```

1. Re-upload your license.

1. Validate that the customer name was updated in
   `/opt/nimpee/conf.d/sys-nimpee.conf`:

   ```shell
   # grep custname /opt/nimpee/conf.d/sys-nimpee.conf
   custname="<your_company_name>"
   ```
