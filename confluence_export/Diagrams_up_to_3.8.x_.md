# Diagrams (up to 3.8.x)

## Overview

Diagrams help to visualize the network state information.

## Diagram Types

### Network

The network overview also referred to as “Walk”, shows sites connected
via the routing edge. An overview serves as a general representation of
all sites in the network and individual sites can be double-clicked for
more detail.

### Sites

Site diagrams display all devices discovered on the site. Sites are
automatically calculated based on the administrative domain boundaries,
such as carrier networks and other unmanaged infrastructure. Site
boundary calculation can be [configured in settings](Site_Separation).

The site name can be changed when ***Routing and switching domain***
site separation is used (see [Site separation settings](Site_Separation)
for more information). To rename a site go to ***Diagrams →***
**Sites**, choose the site you would like to rename, click ***Rename
site***, enter a new name and click ***Rename***.

<img src="attachments/78872710/113868804.png" loading="lazy" data-image-src="attachments/78872710/113868804.png" data-unresolved-comment-count="0" data-linked-resource-id="113868804" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-28 13_23_37-Sites - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="78872710" data-linked-resource-container-version="12" data-media-id="7c1e6a7e-89f5-4515-afac-5e70a75464e5" data-media-type="file" />

### Routing

Routing diagrams display contiguously, directly interconnected routers
to form a routing domain.

### Switching

Switching diagrams displays individual spanning-tree instances or a
composite switching domain. Spanning tree instances are identified by a
unique Root ID. The switching Domain is composed of contiguously
connected spanning-tree instances, representing the maximum possible
fault propagation in a Layer 2 failure domain.

### End to End path

End to End path diagram displays a complete path between any two network
endpoints. The reverse-path forwarding check verifies the path's
viability. Only the actual network path is displayed, and missing parts
denote unavailable network information necessary for completing the
routing process.

The End to end path can be found in ***Diagrams → End to end path*** or
on any diagram using three dots (see picture below).

<img src="attachments/78872710/112852993.png" loading="lazy" data-image-src="attachments/78872710/112852993.png" data-unresolved-comment-count="0" data-linked-resource-id="112852993" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-28 08_41_08-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="78872710" data-linked-resource-container-version="12" data-media-id="cbe88996-f1c8-40af-88cc-eafe7fa0eef3" data-media-type="file" />

#### Using the End to End path lookup

Go to ***Diagrams → End to end path*** or open the lookup using three
dots on any diagram (see above). Enter ***Protocol***, optionally ***TCP
Flags***, ***Source*** address and port and ***Destination*** address
and port. Click ***Submit***. An End to End path is generated and shown.
This lookup will take into consideration if an ACL or firewall is in the
way.

<img src="attachments/78872710/112853001.png?height=250" loading="lazy" data-image-src="attachments/78872710/112853001.png" data-unresolved-comment-count="0" data-linked-resource-id="112853001" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-28 08_48_40-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="78872710" data-linked-resource-container-version="12" data-media-id="1217341c-fd56-483b-b9dd-f76b8a927fb0" data-media-type="file" height="250" />

  

### Host to Gateway path

Host to Gateway path diagram displays the Layer 2 path from every
identified endpoint in the network to its active gateway router.

The Host to Gateway path can be found in ***Diagrams → Host to gateway
path*** or on any diagram using three dots (see picture below).

<img src="attachments/78872710/112951300.png" loading="lazy" data-image-src="attachments/78872710/112951300.png" data-unresolved-comment-count="0" data-linked-resource-id="112951300" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-28 08_41_18-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="78872710" data-linked-resource-container-version="12" data-media-id="8eb0f229-8de6-4295-a160-12478cd26fb3" data-media-type="file" />

#### Using Host to Gateway path lookup

Go to ***Diagrams → Host to gateway path ***or open it using three dots
on any diagram (see above). Enter end ***Host*** IP address and click
***Submit***. The end host must exist in the IP Fabric database.

<img src="attachments/78872710/113311745.png" loading="lazy" data-image-src="attachments/78872710/113311745.png" data-unresolved-comment-count="0" data-linked-resource-id="113311745" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-28 09_41_20-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="78872710" data-linked-resource-container-version="12" data-media-id="75115daf-6d8a-4283-b2ce-2b96397fb7a7" data-media-type="file" />

  

## Working with diagrams

### Objects

Diagrams are composed of objects, nodes and the relationships between
them. If no object is added to the ***Objects*** menu then all objects
are displayed which is the default when the ***Diagrams → Network***
page is opened. If all objects are displayed, the objects are grouped
into smaller groups (clouds) for better visibility. You can double click
the object group to explore further.

Top-level view with all objects:

<img src="attachments/89260035/89391108.png?height=250" loading="lazy" data-image-src="attachments/89260035/89391108.png" data-unresolved-comment-count="0" data-linked-resource-id="89391108" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 10_40_55-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="371453fe-dbbb-445c-a460-14919e0d7f9a" data-media-type="file" height="250" />

### Adding objects

To display the required information, select on the right side
***Objects → Add Objects → Object** **type*** and ***Object instance***.

One or more objects can be displayed at a time.

For example, to see a diagram of particular sites called L41 and L33:

1.  Select ***sites*** from ***Object type*** drop-down menu
2.  Select site name *L41* for ***Object instance***
3.  Click ***Add***
4.  Repeat steps 1-3 for site *L33*.

***<img src="attachments/89260035/89260045.png?height=250" loading="lazy" data-image-src="attachments/89260035/89260045.png" data-unresolved-comment-count="0" data-linked-resource-id="89260045" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 11_02_50-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="3d85f31b-8c22-4d5c-a773-777a497d5127" data-media-type="file" height="250" />***

### Removing objects

Objects can be removed from the diagram by:

1.  using the **X** button for a specific object
2.  using the **X** button on the ***Remove Objects*** menu
3.  using the ***Remove All*** button to remove all objects from the
    diagram

<img src="attachments/89260035/89292816.png?height=250" loading="lazy" data-image-src="attachments/89260035/89292816.png" data-unresolved-comment-count="0" data-linked-resource-id="89292816" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 11_09_46-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="f56814db-2399-4d50-81a0-1ea627c7053d" data-media-type="file" height="250" />

### Manipulating objects and nodes

Diagrams are generated automatically, but the following supported
operations can change their layout:

-   Pinch to zoom: touch & desktop (if supported by the trackpad)
-   Mouse wheel to zoom: desktop
-   Two-finger trackpad up or down to zoom: desktop
-   Tap to select: touch & desktop
-   Tap background to deselect: desktop
-   Multiple selections via modifier key (shift, command, control,
    alt) + tap: desktop
-   Box selection: touch (three-finger swipe) & desktop (modifier key +
    mouse down then drag)
-   Grab and drag nodes: touch & desktop

The ***Center*** button can also center the screen view.

<img src="attachments/89260035/89554965.png" loading="lazy" data-image-src="attachments/89260035/89554965.png" data-unresolved-comment-count="0" data-linked-resource-id="89554965" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 12_54_40-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="68b66ac0-7e36-4786-95fe-a9ad5d399c8f" data-media-type="file" />

### Save default layout (view)

After editing the layout, you can save the changes as the default by
using the floppy disk icon at the top left corner of a particular object
(see below).

### Save and load view

Each object can have multiple views that can be saved and loaded again
later.

**Save view**

Click the floppy icon to save the view.

<img src="attachments/89260035/89292824.png" loading="lazy" data-image-src="attachments/89260035/89292824.png" data-unresolved-comment-count="0" data-linked-resource-id="89292824" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 12_43_32-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="51cd436c-c117-4625-847e-c3ca0fc1ef0d" data-media-type="file" />

Enter a name for that view and click save.

<div>

<div>

The view saved in this way is not the default view for that object.
Please check *Save default layout* above.

</div>

</div>

**Load view**

The view can be loaded by clicking the folder icon.

<img src="attachments/89260035/89391124.png" loading="lazy" data-image-src="attachments/89260035/89391124.png" data-unresolved-comment-count="0" data-linked-resource-id="89391124" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 12_43_43-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="90c4802a-1cc2-45c9-acb7-3e3e4b77eab3" data-media-type="file" />

Select the desired view and click to load (the white arrow down in the
green square).

### Export current view to PNG

The view can be exported in the form of a PNG image by clicking on
***...*** and selecting ***Export PNG***:

<img src="attachments/89260035/89325611.png" loading="lazy" data-image-src="attachments/89260035/89325611.png" data-unresolved-comment-count="0" data-linked-resource-id="89325611" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 12_57_04-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="8638cf8b-b4dd-47ec-9ff8-4149b3ea02a9" data-media-type="file" />

### Search

Search looks up any text currently present on the diagram. Typing query
filters the view and clicking on the search button focuses and zooms in
on the item.

### Filtering protocols

The user can filter connection protocols between devices of the second
and third layer of ISO OSI by using filters in the ***Protocols*** menu.

<img src="attachments/89260035/89489437.png?height=250" loading="lazy" data-image-src="attachments/89260035/89489437.png" data-unresolved-comment-count="0" data-linked-resource-id="89489437" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_28_55-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="68022e2f-c56e-411d-a06f-731edea28e4b" data-media-type="file" height="250" />

It is possible to use predefined filters or a filter according to your
own specific requirements. Predefined filters can be selected from the
drop-down menu.

<img src="attachments/89260035/89260074.png?height=250" loading="lazy" data-image-src="attachments/89260035/89260074.png" data-unresolved-comment-count="0" data-linked-resource-id="89260074" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_57_28-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="5bf3d642-022c-4f9b-a656-6174e4ae5591" data-media-type="file" height="250" />

Individual protocols can be ***show*** (show them on the diagram),
***fade*** (show them but without any description in grey) or ***hide***
(do not show them).

<div class="table-wrap">

<div class="content-wrapper">

<img src="attachments/89260035/89423914.png" loading="lazy" data-image-src="attachments/89260035/89423914.png" data-unresolved-comment-count="0" data-linked-resource-id="89423914" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_58_39-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="a8018648-62ce-45c6-9507-8203c4664441" data-media-type="file" />

</div>

</div>

<div class="content-wrapper">

<img src="attachments/89260035/89554988.png" loading="lazy" data-image-src="attachments/89260035/89554988.png" data-unresolved-comment-count="0" data-linked-resource-id="89554988" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_58_51-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="813951f9-9c8e-4665-ad8c-d08def8fe302" data-media-type="file" />

</div>

<div class="content-wrapper">

<img src="attachments/89260035/89587729.png" loading="lazy" data-image-src="attachments/89260035/89587729.png" data-unresolved-comment-count="0" data-linked-resource-id="89587729" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_59_03-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="6d61301a-f05a-414c-afe9-6c4b06b8700f" data-media-type="file" />

</div>

**Link grouping**

**<img src="attachments/89260035/89391132.png" loading="lazy" data-image-src="attachments/89260035/89391132.png" data-unresolved-comment-count="0" data-linked-resource-id="89391132" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_59_21-Edit - Working with diagrams - Confluence.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="070b79e6-15a8-4145-adce-cab3f6bb5ed1" data-media-type="file" />**

Link grouping means that protocols of the specific layer are not shown
as separate lines but together as a single line.

**Layer grouping**

<img src="attachments/89260035/89260079.png" loading="lazy" data-image-src="attachments/89260035/89260079.png" data-unresolved-comment-count="0" data-linked-resource-id="89260079" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 13_59_33-Edit - Working with diagrams - Confluence.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="e3d6f278-16da-41ca-bab7-85d503c1c942" data-media-type="file" />

Layer Grouping collapses groups of devices according to the types of
links that connect these, either in Layer 2 or 3 groups. Devices
connected with different layer protocols can't be grouped together.

**Ignore filters**

All filters can be turned off using **Ignore filters **checkbox.

### Device information deep dive

After clicking on the device, it is possible to obtain additional
information about it and the protocols used on this device.

<img src="attachments/89260035/89555002.png?height=250" loading="lazy" data-image-src="attachments/89260035/89555002.png" data-unresolved-comment-count="0" data-linked-resource-id="89555002" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-07 14_33_52-IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="89260035" data-linked-resource-container-version="10" data-media-id="bd081937-c8ed-4f64-9548-3fa7710055ca" data-media-type="file" height="250" />

### Additional display options

-   Display wired hosts - displays an aggregated view of wired end hosts
    connected to the network. End hosts can be expanded by clicking on
    the edge device hosts are connected to and then ***Expand wired
    hosts*** button.
-   Display access points - displays wireless access points.
    -   Display wireless hosts - adds wireless end hosts to access
        points view.
-   Display unmanaged neighbours - displays devices discovered using
    CDP/LLDP with a management IP address, but IP Fabric cannot login to
    them.
-   Show FEX - displays fabric extenders.
-   Show site edge - displays site edge and connection to the transit
    networks.
-   Hide boundary
-   Hide Interface Labels
-   Hide Protocol Labels
-   Show ACL & ZBF
-   Show QoS
-   Show FHRP
-   Show utilization - device average rate/site average rate. Min=0%,
    max=100%.
-   Nonredundant devices - highlights in red the devices whose failure
    will cause unavailability of part of the network.
-   Nonredundant links - highlights in red the links with no path
    redundancy.
-   MTU Check - checks if MTU is properly set on the end of both links.
-   Hub meshing - creates an aggregate hub for full and partial mesh
    topologies for improved viewing clarity.

------------------------------------------------------------------------

Practical examples:

[How to use IP Fabric - working with diagrams and technology
tables](https://ipfabric.atlassian.net/wiki/spaces/NK/pages/88014871/How+to+use+IP+Fabric+-+working+with+diagrams+and+technology+tables)

------------------------------------------------------------------------

# Site Separation

The site represents a separate collection of devices. A site can be a
branch, a factory, a production floor, a campus, or anything that might
represent a logical group for a user.

By default, the Site distribution is generated automatically after the
discovery process ends and is based on the rules described below. It can
also be triggered manually without the need for the whole discovery
process by going to ***Settings → Advanced → Discovery → Site
separation*** **<u>(</u>In global or Snapshot settings<u>)</u>**. 

## Routing and switching domain

<div>

<div>

With this setting, you can manually edit the distribution of sites
later. Sites can be also renamed.

</div>

</div>

By default, the site is comprised of the topology of all contiguously
interconnected protocols, and the boundary of a site is formed by the
network protocol relation that is not under management using the
provided authentication credentials. The default separation is useful
for MPLS networks where directly connected routing infrastructure at the
site’s edge is not accessible. For situations where an inaccessible
routed firewall is used at the site (i.e. device under different
management team), an option “***Firewall at site***” can be turned on so
the infrastructure before and behind the firewall is not separated into
two different sites.

For networks that have direct routing connectivity between sites, such
as DMVPN or Leased Lines (usually over Serial or MFR interfaces), an
option to separate the site using ***tunnel*** and/or
***serial** the *interface should be selected.

For configuration go to ***Settings → Advanced → Discovery → Site
separation***.

<img src="attachments/102203393/802750477.png?width=285" class="image-left" loading="lazy" data-image-src="attachments/102203393/802750477.png" data-height="242" data-width="891" data-unresolved-comment-count="0" data-linked-resource-id="802750477" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-56-3.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="12" data-media-id="0c5c7a43-bae9-4bc5-aa8e-ff64e834f2b7" data-media-type="file" width="285" />

## RegEx based on hostname

<div>

<div>

Site distribution cannot be changed manually when regex rules are used.
Sites cannot be renamed.

</div>

</div>

Alternatively, site separation can follow a specific Regular Expression
(RegEx) where separation will be performed based on portion of a device
hostname.

Go to ***Settings → Advanced → Discovery → Site separation*** and change
***Site boundary calculation*** to ***RegEx based on hostname***.

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

In the last step, introduce the ***Regular Expression***. Use [this
tool](https://regex101.com/) for validation and parentheses to extract
the site from the hostname correctly.

<div>

<div>

If you cannot cover the names of the sites with one regex, you can use
logical ***or***. Use **\|** (pipe) the character between RegEx rules.

</div>

</div>

The change in the regex is displayed as a live preview.

Once the regex is ready, click '***Site overview with this RegEx'*** and
observer results. ***Save*** (in the upper right corner).

<img src="attachments/102203393/802652173.png?width=394" class="image-left" loading="lazy" data-image-src="attachments/102203393/802652173.png" data-height="445" data-width="1350" data-unresolved-comment-count="0" data-linked-resource-id="802652173" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-57-15.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203393" data-linked-resource-container-version="12" data-media-id="627d2d24-beb4-4fa7-87dd-f187bb50ef7b" data-media-type="file" width="394" />

**RegEx example**:

We have several locations whose name is logically designed as one letter
with one to three numbers. From the point of view of a regex, such a
site can generally be expressed as
"**^(\[a-zA-Z\]\\d{1,3})**". Unfortunately, we have two other sites that
do not fit into this schema. These sites can be defined with their own
regex and this can be added to the original one using the logical
operator ***or***:

***^(\[a-zA-Z\]\\d{1,3}\|HWLAB\|static\\d{1})*** - 1st option OR 2nd
option OR 3rd option  

<div>

<div>

For devices that do not match the RegEx, IP Fabric automatically adds
those to the site based on protocol relation (CDP, LLDP, STP, L3) under
the condition that there's only a single relation to one particular
site. This feature is especially useful for Access Points and similar
devices, that do not follow the standard naming conventions and are
linked to one specific location.

</div>

</div>

## Manual Site Separation

<div>

<div>

With this setting, you can manually edit the distribution of sites.

</div>

</div>

The Manual Site Separation option is complementary to two previous
options and provides the users with full flexibility. It can be enabled
in **Inventory \> Sites \> Manual Separation** where any device's site
can be adjusted based on more attributes.

  

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_41_08-IP Fabric network infrastructure controller -
IPFabric.png](attachments/78872710/112852993.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_41_18-IP Fabric network infrastructure controller -
IPFabric.png](attachments/78872710/112951300.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_48_40-IP Fabric network infrastructure controller -
IPFabric.png](attachments/78872710/112853001.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 09_41_20-IP Fabric network infrastructure controller -
IPFabric.png](attachments/78872710/113311745.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 13_23_37-Sites - IP Fabric network infrastructure controller
- IPFabric.png](attachments/78872710/113868804.png) (image/png)  

</div>
