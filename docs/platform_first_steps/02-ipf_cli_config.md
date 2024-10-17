---
description: This page explains what parameters can be configured in IPF CLI Config when the IP Fabric appliance is started for the first time.
---

# IPF CLI Config

**IPF CLI Config** starts when the IP Fabric appliance is run for the first time
and configures basic system parameters:

1. Assign hostname.
2. Assign domain name.
3. Choose IP address acquisition method.
4. If the static method is used, configure IP address, netmask, default GW, and
   DNS servers.
5. Configure internet proxy if used.
6. Set the password of the `osadmin` user.
   - This password is used for encrypting system backups and accessing the CLI
     and the System Administration UI.
     - But it is not used for accessing the main GUI, which is accessible with a
       local administrator account configured in the System Administration UI --
       see [Access User Interface and Install License](03-access_ui.md).
7. Set the `admin` password for the main IP Fabric GUI
8. Optionally, define organization parameters for the local SSL certificate.
9. After rebooting, the console login screen will display the assigned IP
   address of the system and provide a link to access the user interface.

IPF CLI Config can also be re-run later from the CLI.

Its documentation can be found in
[IPF CLI Config](../System_Administration/IPF_CLI_Config/index.md).

!!! warning

    Remember the password from step 8! IP Fabric support engineers are able to
    reset `osadmin` user passwords, but **encrypted backups will be lost**!

!!! info

    The self-signed SSL certificate can be replaced by a trusted certificate in
    the IP Fabric web UI. Please see
    [IPF Certificates](../IP_Fabric_Settings/system/ipf_cert.md).
