# Set Up Telnet/SSH URL Handler on MS Windows 7 and later

## Set Up Telnet/SSH URL Handler on MS Windows 7 and later

If you want to be able to connect directly to a device from the IP
Fabric web interface, you need to register a Telnet/SSH URL handler.

!!! warning **Backup first**

    Before any changes to Windows registry, make a backup first!

!!! note

    The following instructions are for the *Putty* app.

### Backup Windows registry

1.  Click ***Start***, type ***regedit.exe*** in the search box, and
    then press ***Enter***
1.  In Registry Editor, click ***File → Export***
1.  In the Export Registry File box, select the location where you want
    to save the backup copy, name your back up file and click ***Save***

### Download Putty

1.  Go to <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>
1.  Download Putty
1.  This tutorial expects Putty in "*C:\\Program Files (x86)\\putty.exe*"

### Register Telnet/SSH URL Handler

1.  Go to <https://gist.github.com/sbiffi/11256316>
1.  Download ***putty.reg*** file
1.  Edit path to Putty if differs from "*C:\\Program Files (x86)\\putty.exe*"
1.  Download ***putty.vbs*** (save it to "C:\\putty.vbs" or change this path
    in ***putty.reg*** above)
1.  Edit path to Putty if differs from "*C:\\Program Files (x86)\\putty.exe*"
1.  Launch ***putty.reg*** to associate ssh:// and telnet:// to this script

---

!!! info  

    The following instructions are for the *SecureCRT *app.

### Backup Windows registry

1.  Click ***Start***, type ***regedit.exe*** in the search box, and
    then press ***Enter***
1.  In Registry Editor, click ***File → Export***
1.  In the Export Registry File box, select the location where you want
    to save the backup copy, name your back up file and click ***Save***

### Download SecureCRT

SecureCRT is not free software. To obtain SecureCRT license please
visit <https://www.vandyke.com/products/securecrt/>

### Register Telnet/SSH URL Handler

1.  Download <https://devops.ipfabric.io/pub/securecrt.reg>
1.  Edit path to SecureCRT if differs from "C:\\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.exe"
1.  Launch securecrt.reg to associate ssh:// and telnet:// to this script
