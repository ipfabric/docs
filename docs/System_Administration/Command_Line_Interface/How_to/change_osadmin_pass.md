# How to change `osadmin` password

- First you need to login to your IP Fabric machine via ssh with user `osadmin` and type in command `nimpee-net-config -t` which is going to launch a TUI wizard
    
![Change_osadmin_pass_command](osadmin_password_change1.png) 

![Change_osadmin_pass_TUI_!](osadmin_password_change2.png)

- Click on yes.

!!! attention
    
    Changing the `osadmin` password will affect: terminal access, system update, WEB GUI access and backup encryption!

- Input new osadmin password twice

![Input_new_osadmin_password](osadmin_password_change3.png)

![Confirmed_new_osadmin_password](osadmin_password_change4.png)


- Reboot the device to finish the process properly

![Reboot](osadmin_password_change5.png)
