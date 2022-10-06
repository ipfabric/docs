# Logging

## System Logs

System logs are placed in `/var/log` folder. `osadmin` has access to these folders.

```bash
/var/log/syslog*                               - all service and system logs
/var/log/arangodb3/*                           - ArangoDB related logs
/var/log/nginx/*                               - NGINX related logs
/var/log/redis/*                               - REDIS related logs
/var/log/rabbitmq/*                            - RabbitMQ related logs
```

## IP Fabric Service Logs

Service logs for IP Fabric services are stored in the `/var/log/nimpee` folder:

```bash
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

Snapshots are available in `/home/autoboss/snapshots` directory. Each folder inside represents one snapshot. Even if snapshots can be copied manually using SCP or SFTP it's strongly recommended to use the export feature in web UI.

Snapshot related logs are located at `/home/autoboss/snapshots/<id>/*`

```bash
/home/autoboss/snapshots/<id>/*                     - snapshot related logs

/home/autoboss/snapshots/<id>/cli/*                 - CLI logs collected during the disocvery
/home/autoboss/snapshots/<id>/devices/*             - information about devices processed by IP Fabric from the CLI logs

# Following 4 services - Networker, Tasker, Updater, Worker all log in two formats:
# /home/autoboss/snapshots/<id>/services/<service>/all.txt          - simple text format, basic information
# /home/autoboss/snapshots/<id>/services/<service>/structured.json  - more detailed information in JSON Lines format

# Service folders and their descriptions:
/home/autoboss/snapshots/<id>/services/networker/    - networker via traceroute looks for other possible next tasks for worker service
/home/autoboss/snapshots/<id>/services/tasker/       - tasker prepares `vTask` records - connecting into (network) devices
/home/autoboss/snapshots/<id>/services/updater/      - updater is transforming device JSON into DB
/home/autoboss/snapshots/<id>/services/worker/       - worker does parsing
```

## Remote Syslog

In IP Fabric version >= `5.0.0` it is now possible to send logs to a remote collector. This will use a basic example
using default UDP port of 514. More advanced examples such as TCP connections please consult the [syslog-ng documentation](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.26/administration-guide)

!!! warning "Changes to `/etc/*.conf` files"

    It is important not to touch any `*.conf` files in the `/etc/` as this can cause issues during upgrades.
    The recommended approach is to create a new file under the service's `conf.d` directory.

### Forwarding Syslog Messages

1. Log into IP Fabric CLI using `osadmin` user.
2. Elevate to root access using `sudo -s` and the `osadmin` password
3. Create a new file (filename should be understandable by your team and should not conflict with other files).
   1. `nano /etc/syslog-ng/conf.d/custom-remote-syslog.conf`
4. Add the following lines (replacing `<YOUR_IP>` with the IP of your syslog server):

   1. Forwarding All Syslog Messages (including system messages)

      ```syslog-ng
      destination remote { network("<YOUR_IP>" transport("udp") port(514)); };
      log { source(s_src); destination(remote); };
      ```

   2. Forwarding Only IP Fabric Syslog Messages

      ```syslog-ng
      destination remote { network("<YOUR_IP>" transport("udp") port(514)); };

      log {
        source(s_src);
        filter(f_ipf_api);
        parser(p_json);
        destination(remote);
      };
      ```

5. Save the file and exit
6. Restart syslog-ng: `systemctl restart syslog-ng`
