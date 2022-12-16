# How to change the hostname

To change the hostname of your IP Fabric machine from the CLI, please do the following:

1. `ssh` to the IP Fabric appliance as the `osadmin` user

2. Execute command `nimpee-net-config -n` to launch network configuration wizard.

3. Modify the `hostname` -- the very first option.

  ![change_hostname2](change_hostname2.png)

  !!! info

      Valid characters for hostnames are ASCII letters from **a** to **z**, the digits from **0** to **9**, and the hyphen (**−**). A hostname may not start with a hyphen.

4. The IP Fabric wizard can modify other configuration items like DNS name, Network Interface configuration, NTP etc. To change only the `hostname` leave everything as is until you reach the `"Do you want to reboot now?"` prompt screen. Select `Yes` to reboot the system.

  ![change_hostname4](change_hostname4.png)
