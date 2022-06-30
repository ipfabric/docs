#Logging

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

##Snapshot Logs

Snapshots are available in `/home/autoboss/snapshots` directory.

Each folder inside represents one snapshot.

Even if snapshots can be copied manually using SCP or SFTP it's strongly recommended to use the export feature in web UI.

Snapshot related logs are visible in `/home/autoboss/snapshots/<id>/*`

```bash
/home/autoboss/snapshots/<id>/*                     - snapshot related logs

/home/autoboss/snapshots/<id>/cli/*                 - CLI logs collected during the disocvery
/home/autoboss/snapshots/<id>/devices/*             - information about devices processed by IP Fabric from the CLI logs  

/home/autoboss/snapshots/<id>/services/networker/all.txt    - networker via traceroute looks for other possible next tasks for worker service
/home/autoboss/snapshots/<id>/services/tasker/all.txt       - tasker prepares `vTask` records - connecting into (network) devices
/home/autoboss/snapshots/<id>/services/updater/all.txt      - updater is transforming device JSON into DB
/home/autoboss/snapshots/<id>/services/worker/*.txt         - worker does parsing
```
