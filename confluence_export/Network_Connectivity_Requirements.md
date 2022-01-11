# Network Connectivity Requirements

# Network Connectivity Requirements

During the snapshot operations, the user can control network bandwidth
limit which never exceeds an aggregate of set bandwidths in any
direction to provide an additional safety measure.

IP Fabric should be connected to a network that has direct connectivity
to managed devices. [Jumphost server](Jumphost_settings) can also be set
up and used.

## Inbound Flow List

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="c4bd1fd9-7fce-440f-8fcf-96adfe6ba2b2">
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

## Outbound Flow List

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="9480f0b6-5fc7-4d3a-8320-13d3f6cf0374">
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

Internet connectivity is used to check product updates, upgrades, setup
support VPN, send error reports, and submit support tickets.

## Jumphost server requirements

<div class="table-wrap">

|                    |             |
|--------------------|-------------|
| **Python version** |             |
| 2.7                | supported   |
| 3.5                | supported   |
| 3.6                | supported   |
| 3.7                | supported   |
| 3.8                | unsupported |
| 3.9                | unsupported |

</div>
