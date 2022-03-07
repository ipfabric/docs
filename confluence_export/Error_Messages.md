# Error Messages

The following table describes some of the know error messages, that may
be observed during the platform operation.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="10231123-89fe-4952-aee8-91cf8c215643">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Error Message</strong></p></th>
<th class="confluenceTh"><p><strong>Next Step</strong></p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>“a request xxx Failed to fetch HTTP status: 504" followed by "Database seems to be overloaded"</p></td>
<td class="confluenceTd"><p>Immediately after an upgrade or installation, error messages "a request xxx Failed to fetch HTTP status: 504" and "Database seems to be overloaded" might be shown after a successful login. This is because of index database maintenance. Please wait some time and then try to login to IP Fabric again. If it takes longer then an hour, don't hesitate to <a href="https://ipfabric.atlassian.net/servicedesk/customer/portals">contact our service desk</a>.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Error: AQL: internal error - in index</p></td>
<td class="confluenceTd"><p>When any error containing <strong>Error: AQL: internal error - in index</strong> is shown after any main action after upgrade (for example after Unloading snapshot or starting Network discovery).</p>
<p>The database got corrupted (no worries all of your data are safely stored) and is necessary to run maintenance.</p>
<p>This can be done in <em><strong>Settings → Advanced → System</strong></em> in the main GUI. For more information see <a href="Schedule_System_Maintenance">Schedule System Maintenance</a></p>
<p>If this does not help, we recommend restarting ArangoDB process in System Administration (port 8443) <a href="System_Status">System Status</a> and running maintenance - see the previous step</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Error: Resource Conflict</p></td>
<td class="confluenceTd"><p>This error only shows up when a user tries to start a job for the second time (a specific task like discovery, maintenance, unload/upload snapshot) that is already scheduled.</p>
<p>Only one job can be executed at the time, so for example, if discovery is running and you will schedule snapshot unload and then attempt to unload the same snapshot for the second time, you will get this error.</p></td>
</tr>
</tbody>
</table>

</div>
