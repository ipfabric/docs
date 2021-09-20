# SNMP

## SNMP

IP Fabric appliance can be monitored using SNMP protocol. CPU, memory,
hard drives and network interfaces can be monitored. Appliance uses
standard Linux OS OIDs.

To enable SNMP on IP Fabric appliance do following steps:

1.  Login to IP Fabric web interface
2.  Go to ***Settings → Advanced → SNMP***
3.  Click ***disabled*** button to enable it
4.  Select ***Version*** (2c or 3 is supported)

<img src="attachments/640548865/640614407.png?height=250" loading="lazy" data-image-src="attachments/640548865/640614407.png" data-unresolved-comment-count="0" data-linked-resource-id="640614407" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-16 12_45_43-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="640548865" data-linked-resource-container-version="1" data-media-id="788057b4-6bcb-4004-acfe-6fe315357e67" data-media-type="file" height="250" />

  

<div>

Security note

<div>

Only IP address specified in the ***Host IP*** field is enabled to have
access to SNMP 161/udp.

</div>

</div>

If you selected **version 2c** please configure:

1.  ***Host IP*** - IP address of remote monitoring server
2.  ***Locality*** - location of IP Fabric appliance
3.  ***System Contact*** - contact to responsible person or department
4.  ***Community string*** - must match community string configured on
    monitoring server
5.  Click ***Save***

<img src="attachments/640548865/640286725.png?height=250" loading="lazy" data-image-src="attachments/640548865/640286725.png" data-unresolved-comment-count="0" data-linked-resource-id="640286725" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-16 12_50_00-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="640548865" data-linked-resource-container-version="1" data-media-id="61f73335-a7cd-4989-b7f2-bbdab076e9b9" data-media-type="file" height="250" />

If you selected **version 3** please configure:

<div>

SNMP v3

<div>

For user authentication only SHA is supported. For data privacy AES is
used.

</div>

</div>

1.  ***Host IP*** - IP address of remote monitoring server
2.  ***Locality*** - location of IP Fabric appliance
3.  ***System Contact*** - contact to responsible person or department
4.  ***Username*** - SNMP v3 user
5.  ***Passphrase*** - authentication and privacy passphrase
6.  Click ***Save***

<img src="attachments/640548865/640516117.png?height=250" loading="lazy" data-image-src="attachments/640548865/640516117.png" data-unresolved-comment-count="0" data-linked-resource-id="640516117" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2019-05-16 12_53_35-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="640548865" data-linked-resource-container-version="1" data-media-id="797b00fd-e355-4519-9035-e196088c1931" data-media-type="file" height="250" />

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-16 12_45_43-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/640548865/640614407.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-16 12_50_00-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/640548865/640286725.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2019-05-16 12_53_35-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/640548865/640516117.png)
(image/png)  

</div>
