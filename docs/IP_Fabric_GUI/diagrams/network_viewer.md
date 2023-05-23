---
description: In the network viewer, all networks are displayed and the relationships between them. They are grouped into sites represented by a cloud for better...
---

# Network Viewer

When you go to the page **Diagrams --> Network**, all networks are
displayed and the relationships between them. They are grouped into
sites represented by a cloud for better visibility. You can double-click
on a cloud to explore further that specific site.

Top-level view with all network:

![Network Viewer -> All network](network_viewer/all_network.png)

## Adding Networks To The View

To display the required information, select on the left side the site
you want to visualize and click on **_Submit_**.

One or more sites can be displayed at a time.

For example, to see a diagram of particular sites called `66 Ostrava DC`
and `47 Brno Warehouse`:

1.  Select **_Site name_** from **_Group Devices by_** drop-down menu

2.  Select the site names

3.  Click **_Submit_**

![Networks selected to show](network_viewer/networks_selected_to_show.png)

## Removing Networks

In a very similar way as to add a site/network to a diagram, to hide it,
just unselect the network and click **_Submit_**.

## Manipulating Objects And Nodes

Diagrams are generated automatically, and the following supported
operations can change their layout:

- _Pinch to zoom: touch & desktop (if supported by the trackpad)_

- Mouse wheel to zoom: desktop

- Two-finger trackpad up or down to zoom: desktop

- Tap to select: touch & desktop

- Tap background to deselect: desktop

- Multiple selections via modifier key (shift, command, control,
  alt) + tap: desktop

- Box selection: touch (three-finger swipe) & desktop (modifier key +
  mouse down then drag)

- Grab and drag nodes: touch & desktop

The **_Center View_** button can also center the screen view.

![Center view button](network_viewer/button_center_view.png)

## Hide/Collapse Items In The View

After selecting a set of devices, or cloud, if you do a right-click, you
have the option to collapse the selected items into a new cloud, or hide
them:

![Collapse selected nodes](network_viewer/collapse_selected_nodes.png)

![Hide selected nodes](network_viewer/hide_selected_nodes.png)

##Layouts

### Save User-defined Layout

After editing the layout, you will see the green box, this allows you to
save the changes as the default view. Click on the green box, this will
open a menu **_Select Diagram Layout Settings_** and the last entry is
the **User-Defined Layout**. By clicking on the floppy disk icon you
will update the default view (see below). Please, be aware that only
position of the visible nodes will be saved.

![Save user-defined or choose another layout](network_viewer/button_save_user_defined_1.png)

![Save user-defined layout](network_viewer/button_save_user_defined_2.png)

### Use User-defined Layout As The Default Layout

Once you have created a user-defined layout, you probably want to use
this as the default layout. For this, click on the icon of the site you
want to update, then select the User-Defined layout and click **Save**

![set default user layout](network_viewer/set_user_defined_layout_as_default.png)

From now on, this will be the default layout for this site:

![default user defined layout](network_viewer/network_default_user_defined_layout.png)

### Choose a Specific Layout For a Selection Of Devices

You can now specify which layout you want to use for a set of devices:

![Use specific layout for selected devices](network_viewer/specific_layout_for_selected_devices.gif)

### Choose a Layout To Apply For The Whole Site

Similarly, you can select a layout for the whole site, using the layout
selection.

- Circular Layout can be used only for 500 nodes or less.

![Change diagram layout for site](network_viewer/change_diagram_layout_for_site.png)

## Save, Load, And Share View

Each object can have multiple views that can be saved and loaded again
later.

### Save View

Click the floppy icon on the menu on the right end side:

![Save View](network_viewer/button_save_view.png)

Enter a name for that view and click save.

!!! info

    The view saved in this way is not the default view for that object.

### Load View

![Select View](network_viewer/button_select_view.png)

The view can be loaded by clicking the folder icon.

Select the desired view and click to load.

### Share View

![Share View](network_viewer/button_share_view.png)

By clicking here, an URL will be displayed, which you can share with
other users, and they will be able to see this view.

### Export Current View To SVG/PNG

The view can be exported in the form of a SVG or PNG image by clicking
on **_Export_** and selecting the format you want

![Export View to SVG/PNG](network_viewer/button_export_view.gif)

!!! info

    The SVG file can be imported into a Visio diagram, or on other drawing
    application

### Search

Search looks up any text currently present on the diagram. Typing query
filters the view and clicking on the search button focuses and zooms in
on the item.

![Search diagram](network_viewer/button_search_diagram.png)

![Search diagram results](network_viewer/search_diagram_results.png)

If you hover your mouse on one entry, you will see the device on the
diagram:

![Hover over search diagram results](network_viewer/search_diagram_results_hover.png)

## Protocols

The user can filter connection protocols between devices of the second
and third layer of ISO OSI by using filters in the **_Network Viewer /
Visualization Setup / Protocols_** menu.

![Protocols - Visualization setup](network_viewer/protocols_visualization_setup.png)

You can decide which layer/protocol you want to display/hide and
group/ungroup

### Default Protocols View

By default, all discovered protocols will be grouped based on the layer
they belong to. This is the **System** view. You can edit this, which
means you are able to ungroup certain protocols. For this click on the
Settings icon:

![Configure visualization setup](network_viewer/visualization_setup_settings.png)

Drag and drop protocols you want to put to a custom group to the **Other
Protocols**, click on Save as and give a name to the new protocol view.

![Drag & drop protocol](network_viewer/protocols_drag_drop.png)

With the example below, you are now able to hide only the DGW protocol,
without affecting the other Layer3 protocols:

![Hide protocol](network_viewer/protocols_hide_dgw.png)

**Link grouping**

![Link grouping](network_viewer/protocols_link_grouping.png)

Link grouping means that protocols of the specific layer are not shown
as separate lines but together as a single line.

### Layer Grouping

![Layer grouping](network_viewer/protocols_layer_grouping.png)

Layer Grouping collapses groups of devices according to the types of
links that connect these, either in Layer 2 or 3 groups. Devices
connected with different layer protocols can't be grouped together.

## Devices

You can select/un-select the type o devices you want to see on the
diagram.

![Select type of devices to see](network_viewer/select_device_type.png)

### Device Information Deep Dive

After right-clicking on the device, it is possible to display additional
information about it by selecting **Show detail**:

![Device - Show detail](network_viewer/device_show_detail.png)
