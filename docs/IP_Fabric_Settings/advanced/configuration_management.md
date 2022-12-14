---
description: In the configuration management process there are two ways to detect configuration changes that are described in this step.
---

# Configuration Management

There are two ways to detect configuration changes:

**Syslog Triggered**

**Scheduled**

## Syslog Triggered

IP Fabric checks incoming syslog messages for key phrases (for example `Configured from console by admin15 on vty0.`). This option needs the appropriate `syslog` configuration on the device side.

Syslog server listens on port `514/UDP` and there is no additional configuration on the IP Fabric side needed. You can send syslog directly from network devices ([example for Cisco IOS](https://community.cisco.com/t5/network-architecture-documents/how-to-configure-logging-in-cisco-ios/tac-p/3132436))
or using syslog forwarder ([example for syslog-ng](https://support.symantec.com/en_US/article.TECH92854.html)).

Please, note

- The receiving port `514` cannot be modified.
- The syslog messages are filtered and are stored in RabbitMQ apart from the main DB and cannot be observed in IP Fabric's GUI

To enable the syslog triggered configuration management go to **Settings → Advanced → Configuration  Management → Configuration Management Setup** and select **Syslogtrigger**.

## Schedule

Configuration change is checked at regular intervals as configured by user.

Schedule can be enabled and configured at **Settings → Advanced → Configuration Management → Configuration Management Setup** and select **Schedule**.

!!! example

    Example for scheduling a check every day at 5:00; 5:30; 10:00; 10:30; 15:00; 15:30; 20:00; 20:30.

    ![configuration managment setup](configuration_managment_setup.png)

Multiple values from the lists can be selected with `CTRL` or `SHIFT` keys.
