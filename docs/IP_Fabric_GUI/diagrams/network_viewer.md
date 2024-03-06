---
description: In the Network Viewer, all networks are displayed along with the relationships between them.
---

# Network Viewer

When you go to **Diagrams --> Network**, all networks are
displayed along with the relationships between them. They are grouped into
sites (which are represented by clouds) for better visibility. You can double-click
a cloud to explore further that specific site.

Top-level view with all networks:

![Network Viewer - All network](network_viewer/all_network.png)

## Adding Networks to the View

To display the required information, select on the left side the site
you want to visualize and click **Submit**.

One or more sites can be displayed at the same time.

For example, to see a diagram of the particular sites `35HEADOFFICE` and
`35COLO`:

1.  Select `Site name` from the **Group Devices by Attribute** drop-down menu.

2.  Select the site names.

3.  Click **Submit**.

![Networks selected to show](network_viewer/networks_selected_to_show.png)

## Removing Networks

In a very similar way as to add a site/network to a diagram, to hide it,
just unselect the network and click **Submit**.

## Manipulating Objects and Nodes

Diagrams are generated automatically, and the following supported
operations can change their layout:

- _Pinch to zoom: touch & desktop (if supported by the trackpad)_

- Mouse wheel to zoom: desktop

- Two-finger trackpad up or down to zoom: desktop

- Tap to select: touch & desktop

- Tap background to deselect: desktop

- Multiple selections via modifier key (`Shift`, `Command`, or `Control`) + tap: desktop

- Box selection: touch (three-finger swipe) & desktop (modifier key +
  mouse down then drag)

- Grab and drag nodes: touch & desktop

The **Center View** button can also center the screen view.

![Center View button](network_viewer/button_center_view.png)

## Hide/Collapse Items in the View

If you right-click after selecting a set of devices or cloud, you will have the
option to either:

1. collapse the selected items into a new cloud:

   ![Collapse selected nodes](network_viewer/collapse_selected_nodes.png)

   ![Selected nodes collapsed](network_viewer/collapse_selected_nodes_done.png)


2. or hide them:

   ![Hide selected nodes](network_viewer/hide_selected_nodes.png)

   ![Selected nodes hidden](network_viewer/hide_selected_nodes_done.png)

## Layouts

### Save User-Defined Layout

After editing the layout, you will see the green box. This allows you to
save the changes as the default view. Click the green box; this will
open a menu **Select Diagram Layout Settings**, and the last entry is
the **User-Defined Layout**. By clicking the **Floppy disk** icon, you
will update the default view (see below). Please be aware that only
the position of the visible nodes will be saved.

![Save user-defined or choose another layout](network_viewer/button_save_user_defined_1.png)

![Save user-defined layout](network_viewer/button_save_user_defined_2.png)

### Use User-Defined Layout as the Default Layout

Once you have created a user-defined layout, you probably want to use
this as the default layout. For this, click the icon of the site you
want to update, then select the User-Defined layout and click **Save**.

![Set default user layout](network_viewer/set_user_defined_layout_as_default_1.png)

![Set default user layout](network_viewer/set_user_defined_layout_as_default_2.png)

From now on, this will be the default layout for this site:

![Default user defined layout](network_viewer/network_default_user_defined_layout.png)

### Choose a Specific Layout for a Selection of Devices

You can now specify which layout you want to use for a set of devices:

![Use specific layout for selected devices](network_viewer/specific_layout_for_selected_devices.gif)

### Choose a Layout to Apply for the Whole Site

Similarly, you can select a layout for the whole site using the layout
selection.

- Circular Layout can be used only for 500 nodes or less.

![Change diagram layout for site](network_viewer/change_diagram_layout_for_site.png)

## Save, Load, and Share View

Each object can have multiple views that can be saved and loaded again
later.

### Save View

Click the **Floppy disk** icon on the menu on the right end side:

![Save View](network_viewer/button_save_view.png)

Enter a name for that view and click **Save**.

!!! info

    The view saved in this way is not the default view for that object.

### Load View

![Select View](network_viewer/button_select_view.png)

The view can be loaded by clicking the **Folder** icon.

Select the desired view and click to load.

### Share View

![Share View](network_viewer/button_share_view.png)

By clicking here, a URL will be displayed, which you can share with
other users, and they will be able to see this view.

### Export Current View To SVG/PNG

The view can be exported in the form of a SVG or PNG image by clicking
**Export** and selecting the format you want.

![Export button](network_viewer/button_export.png)

![Expanded Export menu](network_viewer/export_menu_expanded.png)

!!! info

    The SVG file can be imported into a Visio diagram, or on other drawing
    application.

### Search

Search looks up any text currently present on the diagram. Typing query
filters the view, and clicking the **Search** button focuses and zooms in
on the item.

![Search diagram](network_viewer/button_search_diagram.png)

![Search diagram results](network_viewer/search_diagram_results.png)

If you hover the mouse cursor on one entry, you will see the device on the
diagram:

![Hover over search diagram results](network_viewer/search_diagram_results_hover.png)

## Protocols

You can filter connection protocols between devices of the second
and third layer of ISO OSI by using filters in the **Network Viewer -->
Visualization setup --> Protocols** menu.

![Protocols - Visualization setup](network_viewer/protocols_visualization_setup.png)

You can decide which layer/protocol you want to display/hide and
group/ungroup.

### Default Protocols View

By default, all discovered protocols will be grouped based on the layer
they belong to. This is the **System** view. You can edit this, which
means you are able to ungroup certain protocols. For this, click the
**Settings** icon:

![Configure visualization setup](network_viewer/visualization_setup_settings.png)

Drag and drop protocols you want to put to a custom group to the **Other
Protocols**, click **Save as** and give a name to the new protocol view.

![Drag and drop protocol](network_viewer/protocols_drag_drop.png)

With the example below, you are now able to hide only the DGW protocol
without affecting the other Layer 3 protocols:

![Hide protocol](network_viewer/protocols_hide_dgw.png)

### Link Grouping

![Link grouping](network_viewer/protocols_link_grouping.png)

Link grouping means that protocols of the specific layer are not shown
as separate lines but together as a single line.

### Layer Grouping

![Layer grouping](network_viewer/protocols_layer_grouping.png)

Layer grouping collapses groups of devices according to the types of
links that connect these, either in Layer 2 or 3 groups. Devices
connected with different layer protocols can't be grouped together.

## Devices

You can select/unselect the type of devices you want to see on the
diagram.

![Select type of devices to see](network_viewer/select_device_type.png)

### Device Information Deep Dive

After right-clicking the device, you can display additional
information about it by selecting **Explore**:

![Device - Explore](network_viewer/device_explore.png)
