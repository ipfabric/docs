---
description: In the configuration management process, there are two ways to detect configuration changes.
---

# Configuration Management

There are two ways to detect configuration changes:

- **Syslog Triggered**
- **Scheduled**

## Syslog Triggered

IP Fabric checks incoming syslog messages for key phrases (for example `Configured from console by admin15 on vty0.`). This option needs the appropriate `syslog` configuration on the device side.

Syslog server listens on the port `514/UDP` and there is no additional configuration on the IP Fabric side needed. You can send syslog directly from network devices ([example for Cisco IOS](https://community.cisco.com/t5/network-architecture-documents/how-to-configure-logging-in-cisco-ios/tac-p/3132436))
or using syslog forwarder ([example for syslog-ng](https://support.symantec.com/en_US/article.TECH92854.html)).

Please note:

- The receiving port `514` cannot be modified.
- The syslog messages are filtered and are stored in RabbitMQ apart from the main DB and cannot be observed in IP Fabric's GUI.

To enable the syslog triggered configuration management, go to **Settings --> Configuration Management --> Configuration Management Setup** and select **Syslog Triggered**.

## Schedule

Configuration change is checked at regular intervals as configured by user.

To enable the scheduled configuration management, go to **Settings --> Configuration Management --> Configuration Management Setup** and select **Schedule**.

!!! example

    Example for scheduling a check every day at 5:00; 5:30; 10:00; 10:30; 15:00; 15:30; 20:00; 20:30.

    ![Configuration Management Setup](configuration_management_setup.png)

Multiple values from the lists can be selected while holding the `Ctrl` or `Shift` keys.

### Single device config collection

A config collection can be triggered for a single device via an API call, the following is a `curl` call which can be executed directly in the IP Fabric machine's shell:

```shell
curl -X POST "https://localhost/api/v<VERSION>/discovery/trigger-config-backup" \
-H "X-API-Token: <TOKEN>" \
-H "Content-Type: application/json" \
-d '{"ip":"<LOGIN_IP>"}' \
-k
```

!!! tip

    You can also execute this command on a remote machine with `curl` installed, just change the `localhost` address to the **FQDN** or **IP address** of your IP Fabric appliance.