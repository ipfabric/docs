# Verifying the Network

Verifying the Network

<div class="conf-macro output-block">

You can verify a lot of technologies and configuration parts with IP
Fabric. You can simply go through technologies in IP Fabric menu (for
example MAC table):

<img src="attachments/1878327375/1878327432.png?height=400" loading="lazy" data-image-src="attachments/1878327375/1878327432.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327432" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-24 14_14_14-Discovery - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="6686a1b0-e21b-4367-bfc7-32793e385741" data-media-type="file" height="400" />

or quickly find particular technology you are interested in using search
(for example MAC table):

<img src="attachments/1878327375/1878327429.png?height=150" loading="lazy" data-image-src="attachments/1878327375/1878327429.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327429" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-24 14_17_21-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="4060ea40-cbfc-44bd-8cf0-32bc814dc0e4" data-media-type="file" height="150" />

Today's goal is to check all port channels in our network.

### Step 1 - Find the proper technology table

As described above we can simply browse IP Fabric menu and find a
particular technology table but in our case as we know exactly what we
are looking for, search menu will be a better choice.

In the upper right corner click to search field and type your request.
We are looking for port channels, ether channels or just link
aggregation. Because I'm from Cisco world I would type in "*port
channel*".

Search returns more results because there are more technology tables
with port channels. We are interested in the last one in this case
"*Link Aggregation (LAG)/Portchannel/Etherchannel Member status table*".
Just click on it and we are there.

### Step 2 - Look for malfunctions

</div>

For your convenience IP Fabric has predefined a lot of rules and
reports. In our particular case port channels are colored green if
everything is OK and other color is used when some malfunction is in
place. You can easily sort the table by clicking the desired field in
the header. In the example below we clicked on "***Members (Status)***".

<img src="attachments/1878327375/1878327426.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327426.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327426" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-26 10_54_57-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="30d0b0ce-6196-4ab3-a947-160895e5805f" data-media-type="file" height="250" />

We can instantly see that some port channels have interface down (blue
color) or individual port (yellow color).

You can also filter colors by clicking them above in ***Reports*** box.
When clicked small eye icon is displayed and items are filtered only to
the selected color. Click again to the same color to clear filter.

<img src="attachments/1878327375/1878327411.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327411.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327411" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 13_39_19-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="074595cd-360d-4dd4-825f-4cd35ed90018" data-media-type="file" height="250" />

#### Customize predefined rules

Predefined coloring rules can be fully customized. To do that click on
predefined rule name in ***Reports*** box above the technology table
which is "***Port-channel members state***" in our case.

<img src="attachments/1878327375/1878327423.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327423.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327423" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-26 11_11_45-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="8dfeaae8-0fda-477c-a428-7da68ac345af" data-media-type="file" height="250" />

  

Now you can check and change predefined colorization rules.

<img src="attachments/1878327375/1878327420.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327420.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327420" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-26 11_28_52-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="eb7ba154-4325-4d15-896c-93eb6af8f368" data-media-type="file" height="250" />

Let's change coloring from blue to red when port in port-channel is
down:

1.  Remove rules from blue color. Click on blue color and then trash
    icon:  
    <img src="attachments/1878327375/1878327417.png" loading="lazy" data-image-src="attachments/1878327375/1878327417.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327417" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-26 11_32_33-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="88712ca3-56dd-4e69-9033-4403af1d155f" data-media-type="file" />
2.  Click to red color and ***Add rule***.
3.  Select logical ***OR*** because we want mark member red if any of
    defined rules apply.
4.  We are interested in ***Members (Status)*** table row.
5.  We would like to check if this row ***contains*** specific string.
6.  Specify string we are looking for like ***(D)*** or ***(DOWN)  
    <img src="attachments/1878327375/1878327402.png" loading="lazy" data-image-src="attachments/1878327375/1878327402.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327402" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-26 11_34_05-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="998b73cf-3a43-4785-85f7-708c7d75ce0c" data-media-type="file" />  
    ***
7.  Click ***Preview*** to see if you rule works
8.  If you are satisfied with the result click ***Update rule***.

You can also add new set of coloring rules. For example you want to
check used aggregation protocol. Please check
[Tables](Navigate_in_Tables) [documentation](Navigate_in_Tables) section
***Colorize column***.

### Step 3 - Fix it

In step 2 we found few malfunctioned port channels. You can gather more
information in IP Fabric like check [network
diagrams](Diagrams_up_to_3.8.x_) or directly connect to device with
problematic port channel.

1.  Click on device host name.
2.  You can go to network diagram (click to switching domain number).
3.  You can connect to device.  
    <img src="attachments/1878327375/1878327414.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327414.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327414" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 11_08_21-LAG_channel Status - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="fed65b6b-7b95-48ab-9039-3104cb5191a9" data-media-type="file" height="250" />

  

### Step 4 - An overall overview

Dashboard is the right place where you can see the overall status of
your network. There are predefined widgets for user convenience but you
can also add, remove or edit it.

For our example with port channels you can go to ***Dashboard***, widget
Neighborship compliance and there is report called Port Channel members
states. By clicking selected color you are redirected to technology
table with color filter applied.

#### Adding custom Report to the Dashboard

First let's create new coloring rule which will be then added to the
Dashboard.

1.  Go to ***Technology → Port Channels → Member status table.***
2.  Click to ***Colorize columns*** button in the right toolbox menu.  
    <img src="attachments/1878327375/1878327405.png" loading="lazy" data-image-src="attachments/1878327375/1878327405.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327405" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 14_27_38-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="d1176bd8-54b6-4108-97dd-4e1f86613f38" data-media-type="file" />
3.  Specify ***Rule name***, for example *Check protocol.*
4.  Select ***Colorized column***, it's *Protocol* in our case.
5.  Leave ***Widgets*** empty for now.
6.  Click on ***blue.***
7.  Create rule *Protocol regex (LACP\|lacp).*
8.  Click on ***yellow.***
9.  Create rule *Protocol equal static.*
10. Click ***Create rule.  
    <img src="attachments/1878327375/1878327399.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327399.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327399" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 14_34_43-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="b8e02c7a-c402-4796-83a4-f720ef230ef2" data-media-type="file" height="250" />  
    ***

  

We crated new coloring rule but we would like to see status of port
channel protocol on the Dashboard. We can add it like this:

1.  Go to Dashboard → Overview.
2.  Click Edit in the upper right corner.
3.  Click +Add row.
4.  Choose row style what you would like to add.
5.  Click on ***Untitled*** and enter some name for example "Port
    channels".
6.  Click ***+Add Widget.***
7.  Select widget type in our case it's ***Table Colors.***
8.  Name widget for example "Port channels".
9.  Look for ***Table color rules*** and add it to Widget. For example
    Technology → Port channels → Member status table → Protocol check.
    We created this rule it the previous steps.
10. Switch ***Select Widget View*** to percentage (default) or absolute
    numbers.
11. Select view type (graph or summary table)  
    <img src="attachments/1878327375/1878327396.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327396.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327396" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 14_52_19-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="02f0215e-9448-460b-8060-df175e105ed9" data-media-type="file" height="250" />
12. Click ***Save ***in the upper right corner.

  

And here we are, our new Dashboard widget.

<img src="attachments/1878327375/1878327393.png?height=250" loading="lazy" data-image-src="attachments/1878327375/1878327393.png" data-unresolved-comment-count="0" data-linked-resource-id="1878327393" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-10-29 14_58_06-Window.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="1878327375" data-linked-resource-container-version="3" data-media-id="5ac366d7-54af-46d3-839a-b64289d0d03b" data-media-type="file" height="250" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 14_58_06-Window.png](attachments/1878327375/1878327393.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 14_52_19-Window.png](attachments/1878327375/1878327396.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 14_34_43-Window.png](attachments/1878327375/1878327399.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-26 11_34_05-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327402.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 14_27_38-Window.png](attachments/1878327375/1878327405.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 13_48_38-Window.png](attachments/1878327375/1878327408.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 13_39_19-Window.png](attachments/1878327375/1878327411.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-29 11_08_21-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327414.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-26 11_32_33-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327417.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-26 11_28_52-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327420.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-26 11_11_45-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327423.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-26 10_54_57-LAG_channel Status - IP Fabric network
infrastructure controller -
IPFabric.png](attachments/1878327375/1878327426.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-24 14_17_21-Window.png](attachments/1878327375/1878327429.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-10-24 14_14_14-Discovery - IP Fabric network infrastructure
controller - IPFabric.png](attachments/1878327375/1878327432.png)
(image/png)  

</div>
