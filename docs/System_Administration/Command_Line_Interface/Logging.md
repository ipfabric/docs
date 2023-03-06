# Understanding System Logs

System logs are important because they provide a record of all activities that have occurred on a system. They can be used to track core system or snapshot activity and help with troubleshooting issues. 

## System Logs

System logs are stored in the `/var/log` directory. The `osadmin` user has access to these sub-directories:

```shell
/var/log/syslog*                               - all service and system logs
/var/log/arangodb3/*                           - ArangoDB related logs
/var/log/nginx/*                               - NGINX related logs
/var/log/redis/*                               - REDIS related logs
/var/log/rabbitmq/*                            - RabbitMQ related logs
```

## Service Logs

Service logs for IP Fabric services are stored in the `/var/log/nimpee` directory:

```shell
/var/log/nimpee/api-errors.log                      - API error logs
/var/log/nimpee/api.log                             - all API logs including error logs
/var/log/nimpee/migrate/                            - DB migrate logs
/var/log/nimpee/net-config.log                      - Boot wizard related logs
/var/log/nimpee/net-jumphost-*.log                  - Logs related to a specific jumphost service
/var/log/nimpee/sys-lvm-resize.log                  - Logs for automatic HDD resize
/var/log/nimpee/net-shaping-newshape.log            - Discovery bandwidth control logs
/var/log/nimpee/support-vpn.log                     - Support VPN related logs
/var/log/nimpee/sys-arangodb-dump.log               - ArangoDB dump logs
/var/log/nimpee/sys-backup-duplicity.log            - Logs for backup services
/var/log/nimpee/sys-certificate.log                 - SSL certificates related logs
/var/log/nimpee/sys-install.log                     - Logs related to IP Fabric installation
/var/log/nimpee/sys-service-autorestart.log         - Logs related to service auto restart
/var/log/nimpee/sys-techsupport.log                 - Techsupport related logs
/var/log/nimpee/sys-update.log                      - IP Fabric new version update logs
/var/log/nimpee/webhook-worker-errors.log           - webhook errors logs
/var/log/nimpee/webhook-worker.log                  - webhook worker logs
/var/log/nimpee/webng.log                           - web console errors (received by API)
```

## Snapshot Logs

Snapshots are available in the `/home/autoboss/snapshots` directory. Each sub-directory represents one snapshot. Snapshot-related logs are located in `/home/autoboss/snapshots/<id>/*`:

```bash
/home/autoboss/snapshots/<id>/*                     - snapshot related logs
/home/autoboss/snapshots/<id>/cli/*                 - CLI logs collected during the disocvery
/home/autoboss/snapshots/<id>/devices/*             - information about devices processed by IP Fabric from the CLI logs
```

Following 4 services - Networker, Tasker, Updater, Worker all log in two formats:

```shell
/home/autoboss/snapshots/<id>/services/<service>/all.txt          - simple text format, basic information
/home/autoboss/snapshots/<id>/services/<service>/structured.json  - more detailed information in JSON Lines format
```

Service folders and their descriptions:

```shell
/home/autoboss/snapshots/<id>/services/networker/    - networker via traceroute looks for other possible next tasks for worker service
/home/autoboss/snapshots/<id>/services/tasker/       - tasker prepares `vTask` records - connecting into (network) devices
/home/autoboss/snapshots/<id>/services/updater/      - updater is transforming device JSON into DB
/home/autoboss/snapshots/<id>/services/worker/       - worker does parsing
```

## Remote Syslog

In IP Fabric version greater than `5.0.0`, it is possible to send logs to a remote collector. Here we will show a basic example using the default UDP port `514`. For more advanced examples (such as using TCP connection), please consult the [syslog-ng documentation](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.26/administration-guide)

!!! warning "Changes to `/etc/*.conf` files"

    It is important not to modify any `*.conf` files in the `/etc/` directory as this can cause issues during upgrades.
    The recommended approach is to create a new file under the service's `conf.d` directory.

--8<-- "snippets/cli_root_access.md"

### Forwarding Syslog Messages

1. Log into the IP Fabric CLI with the `osadmin` user.
2. Switch to root account using `sudo su` and enter the `osadmin` password.
3. Create a new configuration file in the `/etc/syslog-ng/conf.d/` folder

    ```shell
    nano /etc/syslog-ng/conf.d/custom-remote-syslog.conf`
    ```

    The file name should be unique and must not conflict with other files in folder.

    ```shell
    ls /etc/syslog-ng/conf.d/ -l
    ```

    ```
    root@ipfabric-server:~# ls /etc/syslog-ng/conf.d/ -l
    total 8
    -rw-r--r-- 1 root root  580 Nov  5 11:10 ipf-api-syslog.conf
    -rw-r--r-- 1 root root 1414 Oct 11 13:31 ipfabric-log.conf
    ```

4. Add the configuration options (replacing `<YOUR_IP>` with the IP of your syslog server)

   1. Forwarding All Syslog Messages (including system messages):

      ```syslog-ng
      destination remote { network("<YOUR_IP>" transport("udp") port(514)); };
      log { source(s_src); destination(remote); };
      ```

   2. Forwarding Only IP Fabric Syslog Messages:

      ```syslog-ng
      destination remote { network("<YOUR_IP>" transport("udp") port(514)); };

      log {
        source(s_src);
        filter(f_ipf_api);
        parser(p_json);
        destination(remote);
      };
      ```

5. Save the file and exit.

6. Restart syslog-ng.

    ```shell
    systemctl restart syslog-ng
    ```

7. Confirm the `syslog-ng` service status.

    ```shell
    systemctl status syslog-ng
    ```

    ```
    root@ipfabric-server:~# systemctl status syslog-ng
    ● syslog-ng.service - System Logger Daemon
         Loaded: loaded (/lib/systemd/system/syslog-ng.service; enabled; vendor preset: enabled)
         Active: active (running) since Fri 2022-12-09 20:16:51 UTC; 5 days ago
           Docs: man:syslog-ng(8)
        Process: 741235 ExecReload=/bin/kill -HUP $MAINPID (code=exited, status=0/SUCCESS)
       Main PID: 786 (syslog-ng)
          Tasks: 4 (limit: 18710)
         Memory: 79.0M
            CPU: 1min 5.538s
         CGroup: /system.slice/syslog-ng.service
                 └─786 /usr/sbin/syslog-ng -F
    ```
