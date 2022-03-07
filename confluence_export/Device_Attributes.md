# Device Attributes

Version 4.3.X has added the ability to add attributes to a device based
on the IP Fabric Unique Serial Number. Currently this supports manually
changing a Device’s Site Name, Routing Domain, or STP Domain. More
functionality will be released in future versions. Once an attribute is
assigned a new snapshot is required for it to be applied.

<img src="attachments/2906128385/2905341963.png" class="image-center" loading="lazy" data-image-src="attachments/2906128385/2905341963.png" data-height="347" data-width="910" data-unresolved-comment-count="0" data-linked-resource-id="2905341963" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-135645.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2906128385" data-linked-resource-container-version="2" data-media-id="8dec2d05-f9b0-49b5-b046-18a0d456b38e" data-media-type="file" />

-   **Serial Number is IP Fabric’s “Unique Serial Number” (API column
    “sn”); this is not the column “Serial Number” which represents the
    Hardware SN (API column “snHw”)**

    -   *Devices discovered via API can also be assigned using Device
        Attributes.*

-   **Hostname** is populated by IP Fabric when a device matching the
    **Serial Number** is found

-   **Attribute** is the Device Attribute to assign. Currently supported
    is Site Name, Routing Domain, or STP Domain

-   **Value** is the attribute’s value to assign.

#### Creating rules in the UI

You are able to create rules in the UI by selecting the **Add
attribute** button. This will provide you a form to fill out.

<img src="attachments/2906128385/2903539788.png" class="image-center" loading="lazy" data-image-src="attachments/2906128385/2903539788.png" data-height="206" data-width="802" data-unresolved-comment-count="0" data-linked-resource-id="2903539788" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-140632.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2906128385" data-linked-resource-container-version="2" data-media-id="f1b6527e-855d-4e20-a376-a11cfbab53b5" data-media-type="file" />

The dropdown is intuitive and will let you search based on SN or
hostname. *Currently there is an issue where IP Fabric will not search
for devices discovered via an API in the UI. Even though it appears no
devices match the SN it will still assign the attribute to the device.*

<img src="attachments/2906128385/2903539794.png" class="image-center" loading="lazy" data-image-src="attachments/2906128385/2903539794.png" data-height="152" data-width="408" data-unresolved-comment-count="0" data-linked-resource-id="2903539794" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220214-184804.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2906128385" data-linked-resource-container-version="2" data-media-id="5f1c52f7-fe91-4c4e-9579-ff1769be7e9e" data-media-type="file" />

#### Creating rules via the API

This is the preferred method of creating rules as it allows for bulk
importing.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="b1440cf5-e6bc-45d3-8f16-fe4def824d35">
<tbody>
<tr class="odd">
<td class="confluenceTd"><p>Method</p></td>
<td class="confluenceTd"><p>PUT</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>URL</p></td>
<td class="confluenceTd"><p>https://&lt;IPF_URL&gt;/api/v1/attributes/global</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Data</p></td>
<td class="confluenceTd"><p>{"attributes": [</p>
<p>{"sn": "&lt;IPF SERIAL NUMBER&gt;", "value": "&lt;SITE NAME&gt;", "name": "siteName"}</p>
<p>]</p></td>
</tr>
</tbody>
</table>

</div>

#### Creating Rules with python-ipfabric package

Please see example at the following GitHub location:

<https://github.com/community-fabric/python-ipfabric/blob/main/examples/settings/attributes.py>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-135645.png](attachments/2906128385/2905341963.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-140632.png](attachments/2906128385/2903539788.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220214-184804.png](attachments/2906128385/2903539794.png)
(image/png)  

</div>
