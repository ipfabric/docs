---
description: This section describes how to re-enable TLS (Transport Layer Security) versions older than 1.3.
---

# Custom TLS Settings

Since IP Fabric `5.0`, the only TLS (Transport Layer Security) version supported
by default is `1.3`. TLSv1.3 brings many improvements over TLSv1.2, such as
stronger encryption, a simplified handshake, perfect forward secrecy, fewer
round trips, and improved performance. Some older web browsers or proxies may
not support the latest version, and older TLS version may need to be re-enabled
in IP Fabric.

For example,
[Splunk](https://docs.splunk.com/Documentation/Splunk/9.0.1/Security/SetyourSSLversion)
does not currently support TLSv1.3, meaning that any integration between these
systems may not be operational without re-enabling an older TLS version.

--8<-- "snippets/cli_root_access.md"

## How To Re-Enable Older TLS Version

To re-enable an older version of TLS, follow these steps:

1. Log in to the IP Fabric CLI as the `osadmin` user.
2. Switch to `root`: `sudo su -`
3. Edit the TLS configuration file `/etc/nginx/conf.d/ipf-ssl-version.conf` with
   your preferred editor.
4. Modify the first line of the configuration file by adding other TLS versions
   separated by spaces:
   1. Original: `ssl_protocols TLSv1.3;`
   2. Updated: `ssl_protocols TLSv1.2 TLSv1.3;`
5. Save the file and restart the `nginx` service: `systemctl restart nginx`.
6. Make sure that `nginx` is reactivated: `systemctl status nginx`

Confirming the `nginx` status after restart:

```shell
systemctl status nginx
```

```shell
root@ipfabric-server:~# systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2022-12-15 07:40:03 UTC; 5s ago
       Docs: man:nginx(8)
    Process: 244197 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 244198 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 244199 (nginx)
      Tasks: 9 (limit: 18709)
     Memory: 6.8M
        CPU: 85ms
     CGroup: /system.slice/nginx.service
             ├─244199 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
```

Updated `/etc/nginx/conf.d/ipf-ssl-version.conf` file to support TLSv1.2:

```shell
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
```

!!! warning "File Changes During IP Fabric Upgrade"

    During a system upgrade, the TLS configuration file will not sustain any
    changes. This is because the main configuration file is part of the system
    image and is overwritten when the upgrade is applied. Therefore, it is
    important to save any desired changes in a separate file before proceeding
    with the upgrade.

!!! note "Other TLS Settings"

    It is possible to adjust other TLS settings, such as ciphers, using the
    instructions above. However, only re-enabling TLSv1.2 has been tested by the
    Solution Architect team.

## After IP Fabric System Upgrade

After an IP Fabric system upgrade, we recommend to check that no new updates to
this file have been made. Because the user has customized the file, the update
will not override it and instead create a new file with the updated version.

Below, you will find an example of how to check if a new version of the
configuration file is added and how to perform a diff. If changes other than
your own have been discovered, please make the necessary updates and restart the
`nginx` service.

```shell
ls /etc/nginx/conf.d/ -l | grep ssl
```

```shell
root@ipfabric-server:~# ls /etc/nginx/conf.d/ -l | grep ssl
-rw-r--r-- 1 root root 208 May  6 08:34 ipf-ssl-params.conf
-rw-r--r-- 1 root root  64 May  6 08:34 ipf-ssl-version.conf
```

In the output above, you can see two TLS-related configuration files.
To confirm which files are actually being used by `nginx`, you can run:


```shell
nginx -T | grep ssl
```

This command displays the fully compiled `nginx` configuration, including all active TLS-related directives.
If both files appear with their paths, it means both are included via conf.d/ and used by `nginx`.

```shell
root@ipfabric-server:~# nginx -T | grep ssl
2025/06/17 12:17:19 [warn] 2494109#2494109: "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# configuration file /etc/nginx/conf.d/ipf-ssl-params.conf:
<omitted>
# configuration file /etc/nginx/conf.d/ipf-ssl-version.conf:
<omitted>
```

In this case, `nginx` is loading configuration directives from both files. They serve different purposes:

- `ipf-ssl-version.conf` defines which TLS protocol versions are allowed and specifies the cipher suites via `ssl_ciphers`.
- `ipf-ssl-params.conf` contains additional SSL/TLS settings like stapling, session timeouts, etc.
