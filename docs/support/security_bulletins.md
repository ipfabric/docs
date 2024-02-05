---
description: Overview of security-related issues in IP Fabric
---

# Security Bulletin

Security notifications affecting the IP Fabric solution published according to our [Security Incident Response](security_incidents.md) policy.

!!! info "Upgrade information"

    Upgrade information can be found in the [System update](../System_Administration/System_Administration_UI/system_update.md) section.

## SA-495: Decoding HTTP/2 Rapid Reset (CVE-2023-44487)

| Severity | Affected Versions | Fix Version |
| -------- | ----------------- | ----------- |
| High     | 6.2.0 or newer    | N/A         |

The HTTP/2 protocol allows a denial of service (server resource consumption) because request cancellation can reset many streams quickly, as exploited in the wild in August through October 2023.

This affects particularly customers who have an internet-facing IP Fabric instance.

### Workaround

The issue lies in the configuration of `http2` on the line `listen 443 ssl http2;` within the nginx configuration files. To resolve this problem, you can remove `http2`, restart nginx, and the issue will be resolved.
Currently, upgrading IP Fabric will overwrite the nginx files, leading to the problem recurring.

- Connect via SSH to IP Fabric VM and check which files contain `http2`:

    ```bash
    sudo grep "http2" /etc/nginx/sites-enabled/*
    ```

    The output should look like this:

    ```bash
    osadmin@ipfabric-632:~$ sudo grep "http2" /etc/nginx/sites-enabled/*
    /etc/nginx/sites-enabled/ipf-frontend:    listen 443 ssl http2;
    /etc/nginx/sites-enabled/ipf-nimpee-update:	listen 8443 ssl http2;
    ```

- Edit each file to remove the `http2` string. You can either do this manually or use the following command:

    ```bash
    sudo sed -i 's/ http2//' /etc/nginx/sites-enabled/*
    ```

    You can verify that the `http2` has been removed by running the `grep` command:

    ```bash
    osadmin@ipfabric-632:~$ sudo grep "443" /etc/nginx/sites-enabled/*
    /etc/nginx/sites-enabled/ipf-frontend:    listen 443 ssl;
    /etc/nginx/sites-enabled/ipf-nimpee-update:	listen 8443 ssl;
    ```

- Restart nginx:

    ```bash
    sudo systemctl restart nginx
    ```

## NIM-9199: Privilege escalation via Admin portal

| Severity | Affected Versions | Fix Version |
| -------- | ----------------- | ----------- |
| High     | 5.0.2 or earlier  | 6.0.1       |

A read-only user can create an escalated privilege account by taking advantage of token validation.

Tokens issued in the web app are accepted without proper validation. Using that, users of any privilege level can call an API endpoint for creating a new admin user account using their token. Then it is possible to escalate their privilege by logging in to the new account.

## NIM-9023: API Token privilege escalation

| Severity | Affected Versions     | Fix Version |
| -------- | --------------------- | ----------- |
| High     | 5.0.0, 5.0.1 or 5.0.2 | 6.0.1       |

Users can create an API token with RBAC properties that the token is not authorized for.

An API token can be generated that allows unauthorized collection of network data or modification of IP Fabric system settings.
