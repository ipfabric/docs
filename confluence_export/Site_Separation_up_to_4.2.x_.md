# Site Separation (up to 4.2.x)

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

<img src="attachments/2887843853/2888105993.png?width=374" class="image-left" loading="lazy" data-image-src="attachments/2887843853/2888105993.png" data-height="445" data-width="1350" data-unresolved-comment-count="0" data-linked-resource-id="2888105993" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="image2020-1-10_16-57-15.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2887843853" data-linked-resource-container-version="1" data-media-id="d13c5cb7-79e1-4a8f-8d89-8a204ab04acf" data-media-type="file" width="374" />

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
options and provides the users with full flexibility.

Go to ***Settings → Site separation*** and select **Manual site
separation** from drop down menu and save changes.

In **Inventory → Sites → Manual Separation** any device can be adjusted
based on more attributes and new sites can be created.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-57-15.png](attachments/2887843853/2887811094.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-56-3.png](attachments/2887843853/2887811088.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-10_16-57-15.png](attachments/2887843853/2888105993.png)
(image/png)  

</div>
