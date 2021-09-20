# API Tech Note - Retrieving configurations

This tech note describes how you can retrieve configuration files from
IP Fabric’s configuration management capability, to be consumed outside
the platform.

You do this in two stages:

1.  send a POST to **/tables/management/configuration** with a request
    body like

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
    {
      "columns":["_id", "hash", "hostname", "lastChange", "lastCheck", "reason", "sn", "status"],
      "snapshot":"$last"
    }
    ```

    </div>

    </div>

      
    You can of course filter that list (for example for devices
    containing "L36") with a

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` jscript
    "filters": {
                  "hostname": ["like","L36"]
                }
    ```

    </div>

    </div>

    key:value pair.  

    This gives you the list of saved configurations, and most
    importantly, the "hash" for each.

2.  send a GET to
    **/tables/management/configuration/download?hash=XXXXXXXXXXXXX**
    where XXXXXXXXXXXXX is the hash for the required config from the
    list returned in step 1.  
      
    This returns the plain text of the configuration in question.
