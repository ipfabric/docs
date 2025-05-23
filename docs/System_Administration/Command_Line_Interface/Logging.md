---
description: This section describes the various logs that IP Fabric keeps and where you can find them.
---

# Understanding System Logs

System logs are important because they provide a record of all activities that
have occurred on the system. They can be used to track core system or snapshot
activity and help with troubleshooting issues.

## System Logs

System logs are stored in the `/var/log` directory. The `osadmin` user has
access to these sub-directories:

| Files                  | Description                                                                                                        |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------- |
| `/var/log/syslog*`     | All service and system logs, contains additional logs from components called by the `worker` and `tasker` services |
| `/var/log/arangodb3/*` | ArangoDB-related logs                                                                                              |
| `/var/log/nginx/*`     | nginx-related logs                                                                                                 |
| `/var/log/redis/*`     | Redis-related logs                                                                                                 |
| `/var/log/rabbitmq/*`  | RabbitMQ-related logs                                                                                              |

## Service Logs

Service logs for IP Fabric services are stored in the `/var/log/nimpee` and `/var/log/ipf` directories:

| File(s)                                                              | Description                                 |
| :------------------------------------------------------------------- |:------------------------------------------- |
| `/var/log/ipf/ipf-api/api-errors.log`                                | API error logs                              |
| `/var/log/ipf/ipf-api/api.log`                                       | All API logs, including error logs          |
| `/var/log/nimpee/ipf-migrate/migrateBuild*.log`                      | Database migration logs                     |
| `/var/log/ipf/ipf-cli-config/ipf-cli-config.log`                     | IPF CLI Config logs                         |
| `/var/log/ipf/ipf-jumphost/*.log`                                    | Logs related to a specific jumphost service |
| `/var/log/nimpee/sys-lvm-resize.log`                                 | Logs for automatic hard disk resize         |
| `journalctl -u ipf-netshaper`                                        | Discovery bandwidth control logs            |
| `/var/log/nimpee/support-vpn.log`                                    | Support VPN-related logs                    |
| `/var/log/nimpee/sys-backup-duplicity.log`                           | Logs for backup services                    |
| `/var/log/nimpee/duplicity/sys-duplicity-*.log`                      | Detailed logs for each backup session       |
| `/var/log/nimpee/sys-certificate.log`                                | SSL certificate-related logs                |
| `/var/log/ipf/ipf-techsupport-exporter/ipf-techsupport-exporter.log` | Techsupport-related logs                    |
| `/var/log/ipf/system-upgrade-ipf/package-*`                          | IP Fabric new version update logs           |
| `/var/log/ipf/ipf-webhook-worker/webhook-worker-errors.log`          | Webhook error logs                          |
| `/var/log/ipf/ipf-webhook-worker/webhook-worker.log`                 | Webhook worker logs                         |
| `/var/log/nimpee/frontend.log`                                       | Web console errors (received by API)        |
| `/var/log/nimpee/discovery/syslogWorker/*`                           | Configuration management logs               |

## Snapshot Logs

Snapshots are stored in the `/home/autoboss/snapshots` directory. Each
sub-directory represents one snapshot. Snapshot-related logs are in
`/home/autoboss/snapshots/<id>/*`:

| Files                                     | Description                                                        |
| :---------------------------------------- | :----------------------------------------------------------------- |
| `/home/autoboss/snapshots/<id>/*`         | Snapshot-related logs                                              |
| `/home/autoboss/snapshots/<id>/cli/*`     | CLI logs collected during discovery in `JSON Lines` format         |
| `/home/autoboss/snapshots/<id>/devices/*` | Information about devices processed by IP Fabric from the CLI logs |

The CLI logs under `/home/autoboss/snapshots/<id>/cli/*` are differentiated by
the `messageSubType` key as follows:
- `cliUi`: Messages containing the raw text received from the device and some
  error reports. Available for download in the text form from the UI.
- `cliSession`: Messages with a rigid structure describing the commands sent
  and the responses received. Usable for scripting on top of the logs.
- `cliInternal`: Messages with no formal structure used purely for debugging.

The following 4 services -- Networker, Tasker, Updater, and Worker -- all log in
two formats:

| File                                                               | Description                                      |
| :----------------------------------------------------------------- | :----------------------------------------------- |
| `/home/autoboss/snapshots/<id>/services/<service>/all.txt`         | Simple text format, basic information            |
| `/home/autoboss/snapshots/<id>/services/<service>/structured.json` | More detailed information in `JSON Lines` format |

Service directories and their descriptions:

| Directory                                           | Description                                                                              |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| `/home/autoboss/snapshots/<id>/services/networker/` | Networker via `traceroute` looks for other possible next tasks for the `worker` service. |
| `/home/autoboss/snapshots/<id>/services/tasker/`    | Tasker prepares `vTask` records -- connecting into (network) devices.                    |
| `/home/autoboss/snapshots/<id>/services/updater/`   | Updater is transforming device JSONs into the database.                                  |
| `/home/autoboss/snapshots/<id>/services/worker/`    | Worker does the parsing.                                                                 |

## Remote Syslog

In IP Fabric versions greater than `5.0.0`, it is possible to send logs to a
remote collector. Here, we will show a basic example using the default UDP port
`514`. For more advanced examples (such as using a TCP connection), please
consult the
[syslog-ng Administration Guide](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.26/administration-guide)

!!! warning "Changes to `/etc/*.conf` Files"

    It is important not to modify any `*.conf` files in the `/etc/` directory,
    as this can cause issues during upgrades.
    
    The recommended approach is to create a new file under the service's
    `conf.d` directory.

--8<-- "snippets/cli_root_access.md"

### Forwarding Syslog Messages

1. Log in to the IP Fabric CLI as the `osadmin` user.

2. Switch to `root` (you will be asked to enter the `osadmin` password):

   ```shell
   sudo su -
   ```

3. Create a new configuration file in the `/etc/syslog-ng/conf.d/` directory:

    ```shell
    nano /etc/syslog-ng/conf.d/custom-remote-syslog.conf`
    ```

    The file name should be unique and must not conflict with other files in the
    directory:

    ```shell
    ls /etc/syslog-ng/conf.d/ -l
    ```

    ```
    root@ipfabric-server:~# ls /etc/syslog-ng/conf.d/ -l
    total 8
    -rw-r--r-- 1 root root  580 Nov  5 11:10 ipf-api-syslog.conf
    -rw-r--r-- 1 root root 1414 Oct 11 13:31 ipfabric-log.conf
    ```

4. Add the configuration options (replace `<YOUR_IP>` with the IP address of
   your syslog server):

   1. Forwarding all syslog messages (including system messages):

      ```syslog-ng
      destination remote { network("<YOUR_IP>" transport("udp") port(514)); };
      log { source(s_src); destination(remote); };
      ```

   2. Forwarding only IP Fabric syslog messages:

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

6. Restart the `syslog-ng` service:

    ```shell
    systemctl restart syslog-ng
    ```

7. Confirm the `syslog-ng` service status:

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
