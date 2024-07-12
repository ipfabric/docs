---
description: This page provides an overview of security-related issues in IP Fabric.
---

# Security Bulletin

Security notifications affecting the IP Fabric solution published according to
our [Security Incident Response](security_incidents.md) policy.

!!! info "Upgrade Information"

    Upgrade Information can be found in the
    [System Update](../System_Administration/System_Administration_UI/system_update.md)
    section.

## NIM-13396: Opengear -- Prevent `sudo` Password From Being Logged

| Severity | Affected Versions | Fix Version |
| -------- | ----------------- | ----------- |
| High     | `6.3.0` and later | `6.9.4`     |

Enable passwords are used for `sudo`, which is needed for the `Neighbors`
discovery task. Due to incorrect implementation, the password can be seen in
plaintext in the CLI log. This affects all customers who have discovered any
Opengear device with the `Neighbors` task enabled. Anyone with CLI access or
access to device log files and downloaded snapshot files created by affected
versions can obtain stored enable passwords.

### Remediation

1. Upgrade the IP Fabric instance to the latest version.
2. If you are unable to upgrade at this moment, disable the `Neighbors` task for
   the **Vendor** `opengear` in **Settings --> Discovery & Snapshots -->
   Discovery Settings -->
   [Disabled Discovery Tasks](../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/disabled_discovery_tasks.md)**.
3. Change all enable passwords stored in **Settings --> Discovery & Snapshots
   --> Discovery Settings --> Device Credentials -->
   [Passwords for enable mode](../IP_Fabric_Settings/Discovery_and_Snapshots/Discovery_Settings/device_credentials.md#optional-passwords-for-enable-mode)**.

## SA-495: Decoding HTTP/2 Rapid Reset (CVE-2023-44487)

| Severity | Affected Versions | Fix Version |
| -------- | ----------------- | ----------- |
| High     | `6.2.0` or newer  | N/A         |

The HTTP/2 protocol allows a denial of service (server resource consumption),
because request cancellation can reset many streams quickly, as exploited in the
wild in August through October 2023.

This particularly affects customers who have an internet-facing IP Fabric
instance.

### Workaround

The issue lies in the configuration of `http2` on the line `listen 443 ssl
http2;` within the nginx configuration files. To resolve this issue, you can
remove `http2` and restart nginx. Currently, upgrading IP Fabric will overwrite
the nginx files, leading to the issue recurring.

1. Connect to the IP Fabric VM via SSH and check which files contain `http2`:

   ```bash
   sudo grep "http2" /etc/nginx/sites-enabled/*
   ```

   The output should look like this:

   ```bash
   osadmin@ipfabric-632:~$ sudo grep "http2" /etc/nginx/sites-enabled/*
   /etc/nginx/sites-enabled/ipf-frontend:    listen 443 ssl http2;
   /etc/nginx/sites-enabled/ipf-nimpee-update: listen 8443 ssl http2;
   ```

2. Edit each file to remove the `http2` string. You can either do this manually
   or use the following command:

   ```bash
   sudo sed -i 's/ http2//' /etc/nginx/sites-enabled/*
   ```

3. Verify that `http2` has been removed by running the `grep` command:

   ```bash
   osadmin@ipfabric-632:~$ sudo grep "443" /etc/nginx/sites-enabled/*
   /etc/nginx/sites-enabled/ipf-frontend:    listen 443 ssl;
   /etc/nginx/sites-enabled/ipf-nimpee-update: listen 8443 ssl;
   ```

4. Restart nginx:

   ```bash
   sudo systemctl restart nginx
   ```

## NIM-9199: Privilege Escalation via Admin Portal

| Severity | Affected Versions  | Fix Version |
| -------- | ------------------ | ----------- |
| High     | `5.0.2` or earlier | `6.0.1`     |

A read-only user can create an escalated privilege account by exploiting token
validation.

Tokens issued in the web app are accepted without proper validation. Using this,
users of any privilege level can call an API endpoint to create a new admin user
account with their token. They can then their privilege by logging in to the new
account.

## NIM-9023: API Token Privilege Escalation

| Severity | Affected Versions            | Fix Version |
| -------- | ---------------------------- | ----------- |
| High     | `5.0.0`, `5.0.1`, or `5.0.2` | `6.0.1`     |

Users can create an API token with RBAC properties that the token is not
authorized for.

An API token can be generated that allows unauthorized collection of network
data or modification of IP Fabric system settings.
