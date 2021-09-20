# Network Connectivity Requirements

# Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth
limit which never exceeds an aggregate of set bandwidths in any
direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity
to managed devices. [Jumphost
server](https://ipfabric.atlassian.net/wiki/spaces/ND/pages/1384841217/Jumphost+settings)
can also be set-up and used. (Jumphost server requires an installation
of SSH Python (versions 2.4 to 3.7).)

<div class="table-wrap">

<table class="confluenceTable" data-layout="default">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Source port (remote)</p></th>
<th class="confluenceTh"><p>Destination port (local)</p></th>
<th class="confluenceTh"><p>Protocol</p></th>
<th class="confluenceTh"><p>Description</p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>User Interface</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>8443</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Administrative Interface</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - API</p>
<p>Support, Updates (Optional)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>22</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - SSH</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>23</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - Telnet</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p> n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a </p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>ICMP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - Traceroute</p></td>
</tr>
</tbody>
</table>

</div>

*Table* *3: Inbound flow list*

<div class="table-wrap">

<table class="confluenceTable" data-layout="default">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Source port (local)</p></th>
<th class="confluenceTh"><p>Destination port (remote)</p></th>
<th class="confluenceTh"><p>Protocol</p></th>
<th class="confluenceTh"><p>Description</p></th>
</tr>

<tr class="odd">
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>User Interface</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>8443</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Administrative Interface</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>443</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - API</p>
<p>Technical Support, Updates (Optional)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>&gt;1024</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>22</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>TCP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - SSH</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>&gt;1024</p></td>
<td class="confluenceTd"><p>23</p></td>
<td class="confluenceTd"><p>TCP</p></td>
<td class="confluenceTd"><p>Network Infrastructure Interaction - Telnet</p></td>
</tr>
<tr class="even">
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>ICMP</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>Network Infrastructure Interaction - Traceroute</p></td>
</tr>
</tbody>
</table>

</div>

*Table* *4: Outbound flow list*

Internet connectivity is used to check product updates, upgrades, setup
support VPN, send error reports, and submit support tickets.
