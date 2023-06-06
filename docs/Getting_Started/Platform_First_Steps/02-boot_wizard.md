---
description: Information of what settings you can change in our Boot Wizard.
---

# First Boot Wizard

The *First Boot Wizard* starts when IP Fabric is run for the first time and
configures system options. The wizard can also be re-run later from the cli
to modify basic system parameters. Documentation can be found at
[System 'Boot Wizard'](../../System_Administration/boot_wizard/index.md).

1. Assign hostname.
2. Assign domain name.
3. Choose IP address acquisition method.
4. If a static method is used, configure IP address, netmask, default GW, and
   DNS servers.
5. Configure NTP servers or just click OK to continue if not using NTP.
6. Select time zone.
7. Configure Internet Proxy if used.
8. Set shell user password of `osadmin` user. The password is used to access the
   IP Fabric administrative interface and system shell (not for the GUI access,
   the GUI is accessible with the `admin` username by default, for more
   information, please,
   read: [Access User Interface and Install License](03-access_ui.md) and also
   for encrypting system backups.
9. Optionally define organization parameters for the local SSL certificate.
10. After rebooting, the console login screen will display the assigned IP
    address of the system and provide a link to access the user interface.

!!! warning

    Remember password from step 8! IP Fabric support engineers are able to reset
    `osadmin`user passwords but **encrypted backups will be lost**!

!!! info

    A trusted certificate can replace a self-signed SSL certificate using IP 
    Fabric web UI. Please see 
    [IPF Certificates](../../IP_Fabric_Settings/system/ipf_cert.md)
