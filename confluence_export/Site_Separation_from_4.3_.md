# Site Separation (from 4.3)

## Regular Expression Site Separation

<div>

<div>

Site distribution cannot be changed manually when regex rules are used.
Sites cannot be renamed.

</div>

</div>

Alternatively, site separation can follow a specific Regular Expression
(RegEx) where separation will be performed based on portion of a device
hostname or SNMP location.

<div>

<div>

If you cannot cover the names of the sites with one regex, you can use
logical ***or***. Use **\|** (pipe) the character between RegEx rules or
use the Device Attributes method shown below.

</div>

</div>

### Hostname Regex

Go to ***Settings → Site separation*** and change ***Routing & Switching
Domain*** to ***RegEx based on hostname*** or create a new rule by **Add
rule** button.

**Transform hostname** is used to normalize site names based on
hostname:

-   Upper case (default) - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" => result is that both devices in one site named
    "PRAGUE"

-   Lower case - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" => result is that both devices in one site named
    "prague"

-   No transformation - first hostname "PRAGUE-RTR1", second hostname
    "prague-rtr2" =>result is that each device has its own site named
    "PRAGUE" and "prague"

<img src="attachments/2887647267/2887417896.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2887417896.png" data-height="272" data-width="792" data-unresolved-comment-count="0" data-linked-resource-id="2887417896" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-132456.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="a11d6eb3-516f-421a-88a2-f05877fb0757" data-media-type="file" />

In this example the regular expression will match items such as PRAGUE-,
LONDON-, etc.

### SNMP Location Regex

Go to ***Settings → Site separation*** and change ***Routing & Switching
Domain*** to ***RegEx based on SNMP location*** or create a new rule by
**Add rule** button.

<img src="attachments/2887647267/2896297985.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2896297985.png" data-height="215" data-width="771" data-unresolved-comment-count="0" data-linked-resource-id="2896297985" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220214-184024.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="d6553a3f-14a4-4b66-b53e-d25382a56b97" data-media-type="file" />

### Testing

The UI now allows you to edit and test your rules directly in the
browser when selecting the **Test rule** option. Here you can see a live
preview of devices that will match the regex you created.

<img src="attachments/2887647267/2888859659.png?width=680" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2888859659.png" data-height="482" data-width="814" data-unresolved-comment-count="0" data-linked-resource-id="2888859659" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-132819.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="22e11f3d-6df9-44a4-958e-ca7f08e72be4" data-media-type="file" width="680" />

You can also test SNMP location rules:

<img src="attachments/2887647267/2896330753.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2896330753.png" data-height="360" data-width="705" data-unresolved-comment-count="0" data-linked-resource-id="2896330753" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220214-184104.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="f5ea5637-4588-4221-ad90-f0620af90ddd" data-media-type="file" />

### RegEx example:

We have several locations whose name is logically designed as one letter
with one to three numbers. From the point of view of a regex, such a
site can generally be expressed as
"**^(\[a-zA-Z\]\\d{1,3})**". Unfortunately, we have two other sites that
do not fit into this schema. These sites can be defined with their own
regex and this can be added to the original one using the logical
operator ***or***:

***^(\[a-zA-Z\]\\d{1,3}\|HWLAB\|static\\d{1})*** - 1st option OR 2nd
option OR 3rd option  

## Device Neighborship

<img src="attachments/2887647267/2896232449.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2896232449.png" data-height="41" data-width="594" data-unresolved-comment-count="0" data-linked-resource-id="2896232449" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220214-184001.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="9781e40d-9fee-4b24-9066-0a3276e0eb2d" data-media-type="file" />

This option will try to define a device based on its neighbor
relationship if a device does not match any previous rule.  Perhaps you
have devices in your environment that do not follow the normal standard
like in a DMZ zone or Day 0 devices that have not been fully
configured.  If that device is connected to a device that did match a
rule, IP Fabric will intelligently group it to the correct site. 

## Manual Site Separation (Device Attributes)

The Manual Site Separation enables the **Device Attributes** feature to
create manual separation if a device does not follow a standard hostname
rule or perhaps the hostname is duplicated in multiple locations.

To configure **Device Attributes** first enable the toggle in the Site
Separation Menu and select Configure or the Device Attributes menu under
settings.

<img src="attachments/2887647267/2888728582.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2888728582.png" data-height="275" data-width="879" data-unresolved-comment-count="0" data-linked-resource-id="2888728582" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-135358.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="9efee28c-a7ea-48d1-8256-9845e99aae40" data-media-type="file" />

### Device Attributes

<img src="attachments/2887647267/2888663043.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2888663043.png" data-height="347" data-width="910" data-unresolved-comment-count="0" data-linked-resource-id="2888663043" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-135645.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="d6922152-a1a9-4569-b25d-66943cc151dd" data-media-type="file" />

-   **Serial Number is IP Fabric’s “Unique Serial Number” (API column
    “sn”); this is not the column “Serial Number” which represents the
    Hardware SN (API column “snHw”)**

    -   *Devices discovered via API can also be assigned using Device
        Attributes.*

-   **Hostname** is populated by IP Fabric when a device matching the
    **Serial Number** is found

-   **Attribute** is the Device Attribute to assign, since we want to
    set the Site based on the serial number set it to **Site name**

-   **Value** is the attribute’s value to assign, in this case we want
    to split site L35 into separate sites named 35COLO, 35PRODUCTION,
    35HEADOFFICE

#### Creating rules in the UI

You are able to create rules in the UI by selecting the **Add
attribute** button. This will provide you a form to fill out.

<img src="attachments/2887647267/2888630298.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2888630298.png" data-height="206" data-width="802" data-unresolved-comment-count="0" data-linked-resource-id="2888630298" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-140632.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="50651e4f-b379-48e3-9efd-87a395f672b6" data-media-type="file" />

The dropdown is intuitive and will let you search based on SN or
hostname. *Currently there is an issue where IP Fabric will not search
for devices discovered via an API in the UI. Even though it appears no
devices match the SN it will still perform the site separation correctly
on the next snapshot.*

<img src="attachments/2887647267/2896265219.png" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2896265219.png" data-height="152" data-width="408" data-unresolved-comment-count="0" data-linked-resource-id="2896265219" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220214-184804.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="e37e8568-9220-4b5f-86de-1ff76b3d3d57" data-media-type="file" />

  

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

## Rule Priority

<img src="attachments/2887647267/2888597511.png?width=557" class="image-center" loading="lazy" data-image-src="attachments/2887647267/2888597511.png" data-height="582" data-width="684" data-unresolved-comment-count="0" data-linked-resource-id="2888597511" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20220208-133503.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887647267" data-linked-resource-container-version="3" data-media-id="d9e339bf-16e3-4c1d-8e9d-9a08ccd2d421" data-media-type="file" width="557" />

Rule precedence are followed in a top down manner.

1.  **Manual site separation** (if enabled) will look at the **Device
    Attributes** and try to first assign a device based on serial number
    if a match is found.

2.  Rules you define. In the example above it will check the following

    1.  If SNMP Location matches “IPFABRIC, (LAB01)” → Site LAB01

    2.  If Hostname matches “^L21” → Site MPLS

    3.  If Hostname matches “^(L\\d{1,2})” → Site L2-99

3.  **Try to assign devices without sites based on device neighborship**
    (if enabled)

    1.  <https://ipfabric.atlassian.net/wiki/spaces/ND/pages/2887647267/Site+Separation+from+4.3#Device-Neighborship>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-57-15.png](attachments/2887647267/2887647276.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-56-3.png](attachments/2887647267/2887647279.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-132404.png](attachments/2887647267/2888695813.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-132456.png](attachments/2887647267/2887417896.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-132819.png](attachments/2887647267/2888859659.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-133412.png](attachments/2887647267/2887712791.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-133503.png](attachments/2887647267/2888597511.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-135358.png](attachments/2887647267/2888728582.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-135645.png](attachments/2887647267/2888663043.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220208-140632.png](attachments/2887647267/2888630298.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220214-184001.png](attachments/2887647267/2896232449.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220214-184024.png](attachments/2887647267/2896297985.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220214-184104.png](attachments/2887647267/2896330753.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220214-184804.png](attachments/2887647267/2896265219.png)
(image/png)  

</div>
