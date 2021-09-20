# Diagrams (from v4.0)

# Overview

Diagrams help to visualize the network state information.

We had to change how the diagrams work to bring more functionalities
soon. One of the key changes in the processing of the diagrams is done
in the backend, which means you will be able to collect diagram
information via the API, where it wasn't possible before.

## Diagram Types

### Network

By default, when you click on Network, all networks are displayed and
the relationships between them. They are grouped into sites represented
by a cloud for better visibility. You can double-click on a cloud to
explore further that specific site.

Check this page
<https://ipfabric.atlassian.net/wiki/pages/resumedraft.action?draftId=2491121666>,
for more details on using the diagrams.

### Sites Diagrams

Site diagrams display all devices discovered per site. Sites are
automatically calculated based on the administrative domain boundaries,
such as carrier networks and unmanaged infrastructure. Site boundary
calculation can be [configured in settings](Site_Separation).

The site name can be changed. To rename a site, go to ***Inventory →***
**Sites**, choose the site you would like to rename, click ***Rename
site***, enter a new name, and click ***Rename***.

<img src="attachments/2548891682/2550988801.png" class="image-left" loading="lazy" data-image-src="attachments/2548891682/2550988801.png" data-height="172" data-width="578" data-unresolved-comment-count="0" data-linked-resource-id="2550988801" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-091856.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548891682" data-linked-resource-container-version="8" data-media-id="3b70c8b4-bd6f-4849-85d4-966784856b1b" data-media-type="file" />

Check this page
<https://ipfabric.atlassian.net/wiki/pages/resumedraft.action?draftId=2491121666>,
for more details on using the diagrams.

### Routing

Routing diagrams display contiguously, directly interconnected routers
to form a routing domain.

### Switching

Switching diagrams displays individual spanning-tree instances or a
composite switching domain. A unique Root ID identifies spanning-tree
instances. The switching Domain is composed of contiguously connected
spanning-tree instances, representing the maximum possible fault
propagation in a Layer 2 failure domain.

### End to End path

End to End path diagram displays a complete path between any two network
endpoints or networks. Only the actual network path is displayed, and
missing parts denote unavailable network information necessary for
completing the routing process.

The End to end path can be found in ***Diagrams → End to end path*** or
on any diagram using the “Path Look-Up” menu on the left (see picture
below)

<img src="attachments/2548891682/2550792202.png" class="image-left" loading="lazy" data-image-src="attachments/2548891682/2550792202.png" data-height="334" data-width="461" data-unresolved-comment-count="0" data-linked-resource-id="2550792202" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-105431.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548891682" data-linked-resource-container-version="8" data-media-id="cbcfce5d-b141-45b4-b36b-ce9ef94ca4f9" data-media-type="file" />

Check this page for more details [How to use Path Look-Up (from
v4.0)](How_to_use_Path_Look-Up)

### Host to Gateway path

The host to Gateway path diagram displays the Layer 2 path from every
identified endpoint in the network to its active gateway router.

The Host to Gateway path can be found in ***Diagrams → Host to gateway
path*** or any diagram using the “Path Look-Up” menu on the left and
selecting “Host To Gateway”(see picture below)

<img src="attachments/2548891682/2550956067.png" class="image-left" loading="lazy" data-image-src="attachments/2548891682/2550956067.png" data-height="304" data-width="463" data-unresolved-comment-count="0" data-linked-resource-id="2550956067" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-105901.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548891682" data-linked-resource-container-version="8" data-media-id="a6275725-2e67-4c16-8eab-2c1a222271b3" data-media-type="file" />

Check this page for more details [How to use Path Look-Up (from
v4.0)](How_to_use_Path_Look-Up)

# Network Viewer

When you go to the page ***Diagrams → Network*****,** all networks are
displayed and the relationships between them. They are grouped into
sites represented by a cloud for better visibility. You can double-click
on a cloud to explore further that specific site.

Top-level view with all network:

<img src="attachments/2491121666/2492825601.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492825601.png" data-height="880" data-width="1424" data-unresolved-comment-count="0" data-linked-resource-id="2492825601" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-9-40.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="a1aaed49-957c-4956-b211-359ddf3e014d" data-media-type="file" width="340" />

### **Adding networks to the view**

To display the required information, select on the left side the site
you want to visualize and click on ***Submit***.

One or more sites can be displayed at a time.

For example, to see a diagram of particular sites called *66 Ostrava DC*
and *47 Brno Warehouse*:

1.  Select ***Site name** *from ***Group Devices by*** drop-down menu

2.  Select the site names

3.  Click ***Submit***

<img src="attachments/2491121666/2492792858.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492792858.png" data-height="867" data-width="1689" data-unresolved-comment-count="0" data-linked-resource-id="2492792858" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-19-22.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="bfa378a4-407e-40b8-8685-de25ef7d7eba" data-media-type="file" width="340" />

### **Removing** **networks**

In a very similar way as to add a site/network to a diagram, to hide it,
just unselect the network and ***Submit.***

### **Manipulating objects and nodes**

Diagrams are generated automatically, and the following supported
operations can change their layout:

-   *Pinch to zoom: touch & desktop (if supported by the trackpad)*

-   Mouse wheel to zoom: desktop

-   Two-finger trackpad up or down to zoom: desktop

-   Tap to select: touch & desktop

-   Tap background to deselect: desktop

-   Multiple selections via modifier key (shift, command, control,
    alt) + tap: desktop

-   Box selection: touch (three-finger swipe) & desktop (modifier key +
    mouse down then drag)

-   Grab and drag nodes: touch & desktop

The ***Center View*** button can also center the screen view.

<img src="attachments/2491121666/2492629041.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492629041.png" data-height="101" data-width="176" data-unresolved-comment-count="0" data-linked-resource-id="2492629041" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-28-24.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="7f888068-f41b-4b1f-ae7e-9c6bb6824b3b" data-media-type="file" />

### **Save User-defined**

After editing the layout, you will see the green box, this allows you to
save the changes as the default view. Click on the green box, this will
open a menu ***Select Diagram Layout Settings*** and the last entry is
the ***User-Defined Layout**. B*y clicking on the floppy disk icon you
will update the default view (see below).

<img src="attachments/2491121666/2492629046.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492629046.png" data-height="90" data-width="384" data-unresolved-comment-count="0" data-linked-resource-id="2492629046" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-31-18.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="f2cab7f5-162f-4d93-8a99-f3c42bc1a3f3" data-media-type="file" /><img src="attachments/2491121666/2492792877.png?width=102" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492792877.png" data-height="378" data-width="346" data-unresolved-comment-count="0" data-linked-resource-id="2492792877" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-35-15.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="abb11ef2-42e0-488d-ac7b-36c679518f97" data-media-type="file" width="102" />

### **Use User-defined layout as the default layout**

Once you have created a user-defined layout, you probably want to use
this as the default layout. For this, click on the icon of the site you
want to update, then select the User-Defined layout and click **Save**

<img src="attachments/2491121666/2495053832.png?width=204" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2495053832.png" data-height="608" data-width="872" data-unresolved-comment-count="0" data-linked-resource-id="2495053832" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210602-135021.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="ef2c42ea-89b6-478d-9807-fe04fda7d031" data-media-type="file" width="204" />

From now on, this will be the default layout for this site:

<img src="attachments/2491121666/2496331777.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2491121666/2496331777.png" data-height="38" data-width="357" data-unresolved-comment-count="0" data-linked-resource-id="2496331777" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210602-135550.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="e336609a-e190-4673-ae09-57230f4fab26" data-media-type="file" />

## **Save, load, and share view**

Each object can have multiple views that can be saved and loaded again
later.

#### **Save view**

Click the floppy icon on the menu on the right end side:

<img src="attachments/2491121666/2492760079.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492760079.png" data-height="98" data-width="172" data-unresolved-comment-count="0" data-linked-resource-id="2492760079" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-37-29.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="fa89df6e-0073-4c61-beb5-2dbdbcf06802" data-media-type="file" />

Enter a name for that view and click save.

<div>

<div>

The view saved in this way is not the default view for that object.

</div>

</div>

#### **Load view**

<img src="attachments/2491121666/2492825633.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2491121666/2492825633.png" data-height="137" data-width="157" data-unresolved-comment-count="0" data-linked-resource-id="2492825633" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-39-38.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="21835bb3-cf28-4272-a3b3-8e7c299b0407" data-media-type="file" />

The view can be loaded by clicking the folder icon.

Select the desired view and click to load.

#### **Share view**

<img src="attachments/2491121666/2495119366.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2491121666/2495119366.png" data-height="87" data-width="151" data-unresolved-comment-count="0" data-linked-resource-id="2495119366" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210602-141042.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="e74b2dd6-4dfb-44e8-953b-e12383ace80e" data-media-type="file" />

By clicking here, an URL will be displayed, which you can share with
other users, and they will be able to see this view.

### **Export current view to SVG**

The view can be exported in the form of a SVG image by clicking on
***→SVG ***:

<img src="attachments/2491121666/2492825644.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492825644.png" data-height="75" data-width="168" data-unresolved-comment-count="0" data-linked-resource-id="2492825644" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-43-13.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="d3a3aeb1-f8d6-4474-b7ac-3709e868b636" data-media-type="file" />

### **Search**

Search looks up any text currently present on the diagram. Typing query
filters the view and clicking on the search button focuses and zooms in
on the item.

<img src="attachments/2491121666/2492760087.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492760087.png" data-height="49" data-width="408" data-unresolved-comment-count="0" data-linked-resource-id="2492760087" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-43-42.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="254bba8c-08b6-4f83-8526-b6bffdf77dcc" data-media-type="file" /><img src="attachments/2491121666/2492792893.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492792893.png" data-height="214" data-width="378" data-unresolved-comment-count="0" data-linked-resource-id="2492792893" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-44-40.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="a02229e0-3d46-42b0-ab12-c70e5d14f604" data-media-type="file" />

If you hover your mouse on one entry, you will see the device on the
diagram:

<img src="attachments/2491121666/2492825655.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492825655.png" data-height="160" data-width="592" data-unresolved-comment-count="0" data-linked-resource-id="2492825655" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-45-30.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="a582baf0-dd96-4b9c-8c6c-4e441494f04a" data-media-type="file" />

## **Protocols**

The user can filter connection protocols between devices of the second
and third layer of ISO OSI by using filters in the ***Network Viewer /
Visualization Setup / Protocols ***menu.

<img src="attachments/2491121666/2492760101.png?width=170" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492760101.png" data-height="706" data-width="470" data-unresolved-comment-count="0" data-linked-resource-id="2492760101" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_0-53-4.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="aafbede5-a39e-461b-8d2e-25c24697810e" data-media-type="file" width="170" />

You can decide which layer/protocol you want to display/hide and
group/ungroup

#### **Default Protocols View**

By default, all discovered protocols will be grouped based on the layer
they belong to. This is the “**System**” view. You can edit this, which
means you are able to ungroup certain protocols. For this click on the
Settings icon:

<img src="attachments/2491121666/2551676941.png?width=170" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2551676941.png" data-height="168" data-width="462" data-unresolved-comment-count="0" data-linked-resource-id="2551676941" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-130006.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="fa6f13a4-65ee-469e-9955-9e75ebd352a9" data-media-type="file" width="170" />

Move the protocols you want to ungroup to the “Ungrouped Protocols”,
click on Save as and give a name to the new protocol view.

<img src="attachments/2491121666/2551513097.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2551513097.png" data-height="204" data-width="376" data-unresolved-comment-count="0" data-linked-resource-id="2551513097" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-130352.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="9942deca-51fd-419d-8291-aba87739c15f" data-media-type="file" />

With the example below, you are now able to hide only the DGW protocol,
without affecting the other Layer3 protocols:

<img src="attachments/2491121666/2551513103.png?width=204" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2551513103.png" data-height="631" data-width="811" data-unresolved-comment-count="0" data-linked-resource-id="2551513103" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-131016.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="9bc18101-8e58-40a8-ae59-7f443b98230b" data-media-type="file" width="204" />

#### **Link grouping**

<img src="attachments/2491121666/2492825666.png?width=136" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492825666.png" data-height="233" data-width="413" data-unresolved-comment-count="0" data-linked-resource-id="2492825666" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_1-1-41.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="4696caa5-b339-4ab0-aee9-29bfb2b492b3" data-media-type="file" width="136" />

Link grouping means that protocols of the specific layer are not shown
as separate lines but together as a single line.

#### **Layer grouping**

<img src="attachments/2491121666/2492792907.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492792907.png" data-height="136" data-width="425" data-unresolved-comment-count="0" data-linked-resource-id="2492792907" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_1-2-21.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="67a79cba-1a9c-46d4-8a6f-4d3ee217f609" data-media-type="file" />

Layer Grouping collapses groups of devices according to the types of
links that connect these, either in Layer 2 or 3 groups. Devices
connected with different layer protocols can't be grouped together.

## **Devices**

You can select/un-select the type o devices you want to see on the
diagram.

<img src="attachments/2491121666/2492760115.png?width=136" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2492760115.png" data-height="317" data-width="387" data-unresolved-comment-count="0" data-linked-resource-id="2492760115" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2021-6-2_1-4-30.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="eda5d6b7-fd9f-46e9-bd1a-c68db44a5299" data-media-type="file" width="136" />

### **Device information deep dive**

After right-clicking on the device, it is possible to display additional
information about it by selecting “show detail”:

<img src="attachments/2491121666/2551152654.png" class="image-left" loading="lazy" data-image-src="attachments/2491121666/2551152654.png" data-height="364" data-width="495" data-unresolved-comment-count="0" data-linked-resource-id="2551152654" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-131552.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2491121666" data-linked-resource-container-version="8" data-media-id="b2a846a7-34b9-40ee-acdc-f177c0d307dd" data-media-type="file" />

# How to use Path Look-Up

## Unicast Path-Lookup

<img src="attachments/2548858900/2551480336.png" class="image-wrap-left" loading="lazy" data-image-src="attachments/2548858900/2551480336.png" data-height="532" data-width="380" data-unresolved-comment-count="0" data-linked-resource-id="2551480336" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-132637.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="754f1f19-dd1c-4a41-ae3d-99ffa7806b6c" data-media-type="file" />

Enter the details:

-   Source IP / CIDR (it can be a network, but the total number of IPs
    has to be less than 255 including source and destination IPs)

-   Port (Source Port)

-   VRF (Virtual Routing and Forwarding Instance)

-   Destination IP / CIDR

-   Port (Destination Port)

-   Protocol: TCP/UDP/ICMP

-   Flags: None/ACK/FIN/SYN/RST/PSH/URG

If you’ve used a network instead of a single IP, you will have the
option between:

– **Network Mode**: simulation stats and ends with whole networks,
individual hosts are not considered

– **Host Mode**: simulation starts and ends with each host. It is
limited to 255 hosts, source and destination combined.

Then click on submit:

<img src="attachments/2548858900/2551087161.png?width=680" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551087161.png" data-height="428" data-width="1557" data-unresolved-comment-count="0" data-linked-resource-id="2551087161" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-135636.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="a9aeb16a-bdf2-4b89-b08b-385cd0fc9fc4" data-media-type="file" width="680" />

## Path Controls

<img src="attachments/2548858900/2613673995.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2613673995.png" data-height="538" data-width="1062" data-unresolved-comment-count="0" data-linked-resource-id="2613673995" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210629-134606.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="2586b41c-aa87-46f5-9af6-f7a3ee9553d1" data-media-type="file" /><img src="attachments/2548858900/2615345159.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2615345159.png" data-height="851" data-width="1233" data-unresolved-comment-count="0" data-linked-resource-id="2615345159" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210629-134859.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="7949f35b-d6f0-449b-aa49-ed43077953ca" data-media-type="file" />

## Understand the path selection

To understand the decision taken by a device, right-click on the device
and “show detail”. You will then be presented with the details. If you
have more than one interface where the flow can come from, you will need
to select the interface you want to look at. Similarly, if you have
several interfaces that can be used to forward the traffic, you will
have to choose one. Then in the middle of the table, you will see the
forwarding decision:

<img src="attachments/2548858900/2551054377.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551054377.png" data-height="379" data-width="939" data-unresolved-comment-count="0" data-linked-resource-id="2551054377" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-145508.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="5bd04bbf-67e2-4775-b0eb-2f1d96b45c71" data-media-type="file" />

In this example, we are looking at the device L33R4, which has 2
incoming interfaces and one forwarding for this flow:

<img src="attachments/2548858900/2551054367.gif?width=680" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551054367.gif" data-height="730" data-width="1254" data-unresolved-comment-count="0" data-linked-resource-id="2551054367" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="E2E-doc-02.gif" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/gif" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="b4399477-c1f6-4e09-a3c0-46628af6da46" data-media-type="file" width="680" />

## Multicast Tree Look-Up

You want to understand how a certain multicast flow is used, you can use
the Multicast Tree Look-Up. For that, just select the correct option and
enter the relevant details

<img src="attachments/2548858900/2551611428.png?width=340" class="image-left" loading="lazy" data-image-src="attachments/2548858900/2551611428.png" data-height="506" data-width="392" data-unresolved-comment-count="0" data-linked-resource-id="2551611428" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-150903.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="ad9bf05f-aaf9-418c-8ad1-d8800f17b9c9" data-media-type="file" width="340" />

You will then see the Multicast Tree:

<img src="attachments/2548858900/2548826136.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548826136.png" data-height="376" data-width="968" data-unresolved-comment-count="0" data-linked-resource-id="2548826136" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151011.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="1e281835-29ac-4a13-a019-979b7f451338" data-media-type="file" />

And you will have access to a lot of information regarding the Multicast
forwarding decision:

<img src="attachments/2548858900/2548858922.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2548858922.png" data-height="430" data-width="1079" data-unresolved-comment-count="0" data-linked-resource-id="2548858922" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151130.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="3f7dc9da-7a18-44f6-ae11-bab2f0b233f0" data-media-type="file" />

## Host To Gateway

To find out more details between a host and its network gateway, you can
use this menu: Host To Gateway. You only need to provide the host, and
you will the details:

<img src="attachments/2548858900/2551644179.png" class="image-center" loading="lazy" data-image-src="attachments/2548858900/2551644179.png" data-height="675" data-width="1242" data-unresolved-comment-count="0" data-linked-resource-id="2551644179" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-151356.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548858900" data-linked-resource-container-version="9" data-media-id="a36dc075-0b08-4fe4-8fc4-a4524e94514a" data-media-type="file" />

## **Intent Checks**

You can overlay the Intent Verification Rules on top of any diagrams.

<img src="attachments/2551152645/2551349268.png?width=353" class="image-left" loading="lazy" data-image-src="attachments/2551152645/2551349268.png" data-height="671" data-width="1089" data-unresolved-comment-count="0" data-linked-resource-id="2551349268" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-132230.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2551152645" data-linked-resource-container-version="6" data-media-id="2e160329-beaf-4401-80d6-dac4e23ae571" data-media-type="file" width="353" />

**Intent Check** includes the Built-In checks (Single Points of Failure,
Non-Redundant Links) and the Custom Checks. The Custom Checks are all
the Verification Rules in IP Fabric: the default checks and the ones you
have created.

# Compare Snapshot

It can be very useful to have a quick look at the topology and observe
what has changed from one snapshot to another. To compare, you just need
to click on “Compare Snapshots” and select the snapshot you want to
compare your active snapshot with, and you will see the result.

<img src="attachments/2548826144/2548924460.png?width=442" class="image-left" loading="lazy" data-image-src="attachments/2548826144/2548924460.png" data-height="583" data-width="1410" data-unresolved-comment-count="0" data-linked-resource-id="2548924460" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210615-235902.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2548826144" data-linked-resource-container-version="3" data-media-id="843fd879-e3f6-45e4-83b3-2f5ed15f3ce9" data-media-type="file" width="442" />

In the example above, we notice that 3 devices have been removed in the
Demo day 4 Snapshot, and they were there in the Demo day 3 Snapshot.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 13_23_37-Sites - IP Fabric network infrastructure controller
- IPFabric.png](attachments/2548891682/2548891696.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 09_41_20-IP Fabric network infrastructure controller -
IPFabric.png](attachments/2548891682/2548891699.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_48_40-IP Fabric network infrastructure controller -
IPFabric.png](attachments/2548891682/2548891702.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_41_18-IP Fabric network infrastructure controller -
IPFabric.png](attachments/2548891682/2548891705.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-28 08_41_08-IP Fabric network infrastructure controller -
IPFabric.png](attachments/2548891682/2548891708.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-091856.png](attachments/2548891682/2550988801.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-105431.png](attachments/2548891682/2550792202.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210615-105901.png](attachments/2548891682/2550956067.png)
(image/png)  

</div>
