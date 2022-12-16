# Custom Transport Layer Security (TLS) Settings

Since IP Fabric version `v5.0`, by default, the only supported TLS version is `v1.3`. TLS 1.3 brings a number of improvements over TLS 1.2, such as stronger encryption, simplified handshake, perfect forward secrecy, fewer round trips, and improved performance. Some older web browsers or proxies may not support the latest version and older TLS version will need to be re-enabled in IP Fabric.

For example, [Splunk](https://docs.splunk.com/Documentation/Splunk/9.0.1/Security/SetyourSSLversion)
does not currently support `TLSv1.3`, meaning any integration between these systems may not be operational without re-enabling an older TLS version.

--8<-- "snippets/cli_root_access.md"

## How to Re-Enable TLSv1.X

To re-enable an older version of TLS, please perform the following:

1. Log into the IP Fabric CLI using the `osadmin` user.
2. Switch to root using the `sudo su root` command.
3. Edit the TLS config file `/etc/nginx/conf.d/ipf-ssl-params.conf` with your preferred editor.
4. Modify the first line of the configuration file by adding other TLS versions separated by spaces:
   1. Original: `ssl_protocols TLSv1.3;`
   2. Updated: `ssl_protocols TLSv1.2 TLSv1.3;`
5. Save the file and restart the `nginx` service using `systemctl restart nginx`.
6. Make sure that nginx is reactivated with `systemctl status nginx`

Confirming the `nginx`status after restart

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


Updated file to support TLSv1.2`/etc/nginx/conf.d/ipf-ssl-params.conf`

```shell
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
    ssl_ecdh_curve secp384r1;
    ssl_session_timeout  10m;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;
    ssl_stapling on;
    ssl_stapling_verify on;
    gzip off;

```

!!! warning "File changes during IP Fabric upgrade"

    The TLS config file will not sustain any changes during the system upgrade. This is because the main configuration file is part of the system image and is overwritten when the upgrade is applied. Therefore, saving any desired changes in a separate configuration file is important before running the upgrade.

!!! note "Other TLS Settings"

    It is possible to adjust other TLS settings, such as ciphers, using the instructions above. However, only re-enabling TLSv1.2 has been tested by the Solution Architect team.

## After IP Fabric System Upgrade

After an IP Fabric system upgrade, it is recommended to check that no new updates to this file have been made. Because the user has customized the file, the update will not override it and instead create a new file with the updated version.

Below you will find an example on how to check if a new version of the
configuration file is added and how to perform a diff. If changes other than
your own have been discovered, please make the necessary updates and
restart the `nginx` service.

```shell
ls /etc/nginx/conf.d/ -l | grep ssl
```

```shell
root@ipfabric-server:~# ls /etc/nginx/conf.d/ -l | grep ssl
-rw-r--r-- 1 root root 300 Nov  2 21:01 ipf-ssl-params.conf
-rw-r--r-- 1 root root 292 Aug 31 13:17 ipf-ssl-params.conf.29865.2022-11-02@21:01:39~
```

There are two SSL config files in the output above. To see which one is being used by Nginx, run:

```shell
nginx -T | grep ssl
```

```shell
root@ipfabric-server:~# nginx -T | grep ssl
nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/ipf-nimpee-update:28
nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/sites-enabled/nimpee-webng:35
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/nginx/ssl/server.crt"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# configuration file /etc/nginx/conf.d/ipf-ssl-params.conf:                                                  gzip off;
```

Based on the output above, the configuration file in use is `/etc/nginx/conf.d/ipf-ssl-params.conf`.
