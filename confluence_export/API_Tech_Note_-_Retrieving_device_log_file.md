# API Tech Note - Retrieving device log file

This tech note describes how you can retrieve log files for a device
from IP Fabric’s discovery, to be consumed outside the platform.

You do this in two stages:

1.  send a POST to **/tables/inventory/devices** with a request body
    like

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
    {
      "columns":["hostname", "taskKey"],
      "snapshot":"$last"
    }
    ```

    </div>

    </div>

      
    You can (and probably would) filter that list (for example for a
    specific device with the hostname “SWITCH01”) by including a

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
      "filters": {
                    "hostname": ["eq","SWITCH01"]
                }
    ```

    </div>

    </div>

    key:value pair.  

    This gives you the task ID for the discovery for the device in
    question.

2.  send a GET to **/os/logs/task/XXXXXXXXXXXXX** where XXXXXXXXXXXXX is
    the taskKey value returned in step 1 for the required network
    device.  
      
    This returns the plain text of the log file for that device
    discovery.
