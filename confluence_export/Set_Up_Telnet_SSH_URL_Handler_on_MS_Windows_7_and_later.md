# Set Up Telnet/SSH URL Handler on MS Windows 7 and later

## Set Up Telnet/SSH URL Handler on MS Windows 7 and later

If you want to be able to connect directly to a device from the IP
Fabric web interface, you need to register a Telnet/SSH URL handler.

<div>

Backup first

<div>

Before any changes to Windows registry, make a backup first!

</div>

</div>

<div>

<div>

The following instructions are for the *Putty* app.

</div>

</div>

### Backup Windows registry

1.  Click ***Start***, type ***regedit.exe*** in the search box, and
    then press ***Enter***
2.  In Registry Editor, click ***File → Export***
3.  In the Export Registry File box, select the location where you want
    to save the backup copy, name your back up file and click ***Save***

### Download Putty

1.  Go
    to <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>
2.  Download Putty
3.  This tutorial expects Putty in "*C:\\Program Files
    (x86)\\putty.exe*"

### Register Telnet/SSH URL Handler

1.  Go to <https://gist.github.com/sbiffi/11256316>
2.  Download ***putty.reg*** file
3.  Edit path to Putty if differs from "*C:\\Program Files
    (x86)\\putty.exe*"
4.  Download putty.vbs (save it to "C:\\putty.vbs" or change this path
    in putty.reg above)
5.  Edit path to Putty if differs from "*C:\\Program Files
    (x86)\\putty.exe*"
6.  Launch putty.reg to associate ssh:// and telnet:// to this script

  

------------------------------------------------------------------------

  

<div>

<div>

The following instructions are for the *SecureCRT *app.

</div>

</div>

### Backup Windows registry

1.  Click ***Start***, type ***regedit.exe*** in the search box, and
    then press ***Enter***
2.  In Registry Editor, click ***File → Export***
3.  In the Export Registry File box, select the location where you want
    to save the backup copy, name your back up file and click ***Save***

### Download SecureCRT

SecureCRT is not free software. To obtain SecureCRT license please
visit <https://www.vandyke.com/products/securecrt/>

### Register Telnet/SSH URL Handler

1.  Download <https://devops.ipfabric.io/pub/securecrt.reg>
2.  Edit path to SecureCRT if differs from "C:\\Program Files\\VanDyke
    Software\\SecureCRT\\SecureCRT.exe"
3.  Launch securecrt.reg to associate ssh:// and telnet:// to this
    script
