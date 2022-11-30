# Custom TLS Settings

Since IP Fabric version `v5.0`, the only supported TLS version is set to `v1.3`
for increased security. Some older browser or proxies may not support
this and will require manual intervention to re-enable the older TLS version.

For example, [Splunk](https://docs.splunk.com/Documentation/Splunk/9.0.1/Security/SetyourSSLversion)
does not currently support `TLSv1.3` which means any integration where Splunk
directly talks to an IP Fabric instance, an older TLS version must be re-enabled.

--8<-- "snippets/cli_root_access.md"

## Re-Enabling TLSv1.X

!!! warning "IP Fabric Updates"

    Once this file has changed, it will not be updated during an IP Fabric
    system upgrade.  A new version of the file named `ipf-ssl-params.dpkg-new`
    will be placed in that directory.  There may be other changes which could
    affect the usability of the product.  Please follow the
    [After Upgrade Instructions](#after-ip-fabric-system-update).

To re-enable an older version of TLS, please perform the following:

1. Log into the IP Fabric CLI using the `osadmin` user.
2. Elevate to root using the `sudo -s` command.
3. Edit `/etc/nginx/conf.d/ipf-ssl-params.conf` with your preferred editor.
4. Change the first line of the configuration by adding other TLS versions separated by spaces:
   1. Original: `ssl_protocols TLSv1.3;`
   2. Updated: `ssl_protocols TLSv1.2 TLSv1.3;`
5. Save the file and restart the `nginx` service using `systemctl restart nginx`.

!!! note "Other TLS Settings"

    It is possible to adjust other TLS settings such as ciphers using the same
    instructions. However, only re-enabling TLSv1.2 has been tested by the
    Solution Architect team.

## After IP Fabric System Update

After an IP Fabric system update, it is recommended to check that no new updates
to this file have been made. Because the file has been customized by the user,
the update will not override it and will instead create a new file with the 
updated version.

Below you will find an example on how to check if a new version of the
configuration file is added and how to perform a diff. If changes other than
your own have been discovered, please make the necessary updates and
restart the `nginx` service.

```commandline
root@ipfabric:/home/osadmin# ls /etc/nginx/conf.d/ipf-ssl-params.dpkg-new
/etc/nginx/conf.d/ipf-ssl-params.dpkg-new

root@ipfabric:/home/osadmin# diff -y /etc/nginx/conf.d/ipf-ssl-params.conf /etc/nginx/conf.d/ipf-ssl-params.dpkg-new
    ssl_protocols TLSv1.2 TLSv1.3;                            |     ssl_protocols TLSv1.3;
    ssl_prefer_server_ciphers on;                                   ssl_prefer_server_ciphers on;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM;                            ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
    ssl_ecdh_curve secp384r1;                                       ssl_ecdh_curve secp384r1;
    ssl_session_timeout  10m;                                       ssl_session_timeout  10m;
    ssl_session_cache shared:SSL:10m;                               ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;                                        ssl_session_tickets off;
    ssl_stapling on;                                                ssl_stapling on;
    ssl_stapling_verify on;                                         ssl_stapling_verify on;
    gzip off;                                                       gzip off;
```
