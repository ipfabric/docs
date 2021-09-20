# 05 - Site Separation

The site represents a separate collection of devices. A site can be a branch, a factory, a production floor, a campus, or anything that might represent a logical group for a user.

By default, the Site distribution is generated automatically after the discovery process ends and is based on the rules described below. It can also be triggered manually without the need for the whole discovery process by going to **Settings → Advanced → Discovery → Site separation** (in global or Snapshot settings).

## Routing and switching domain

!!! note

    With this setting, you can manually edit the distribution of sites later. Sites can be also renamed.

By default, the site is comprised of the topology of all contiguously interconnected protocols, and the boundary of a site is formed by the network protocol relation that is not under management using the provided authentication credentials. The default separation is useful for MPLS networks where directly connected routing infrastructure at the site’s edge is not accessible. For situations where an inaccessible routed firewall is used at the site (i.e. device under different management team), an option **Firewall at site** can be turned on so the infrastructure before and behind the firewall is not separated into two different sites.

For networks that have direct routing connectivity between sites, such as DMVPN or Leased Lines (usually over Serial or MFR interfaces), an option to separate the site using **tunnel** and/or **serial** the interface should be selected.

For configuration go to **Settings → Advanced → Discovery → Site separation**.

![Site separation](site_separation_rs.png)

## Regular expression on `hostname`

!!! note

    Site distribution cannot be changed manually when regex rules are used. Sites cannot be renamed.

Alternatively, site separation can follow a specific Regular Expression (RegEx) where separation will be performed based on portion of a device `hostname`.

Go to **Settings → Advanced → Discovery → Site separation** and change **Site boundary calculation** to **RegEx based on `hostname`**.

**Transform `hostname`** is used to normalize site names based on hostname:

- Upper case (default) -- having first hostname `PRAGUE-RTR1` and second hostname `prague-rtr2`, results in having both devices at one site named `PRAGUE`.

- Lower case -- having first hostname `PRAGUE-RTR1` and second hostname `prague-rtr2`, results in having both devices at one site named `prague`.

- No transformation -- having first hostname `PRAGUE-RTR1` and second hostname `prague-rtr2`, results in having every device located in its own site named `PRAGUE` and `prague` respectively.

In the last step, introduce the **Regular Expression**. Use [regex101](https://regex101.com/) for validation and parentheses to extract the site from the `hostname` correctly.

!!! hint

    If you cannot cover the names of the sites with one regex, you can use logical **or**. Use `|` (pipe) between RegEx rules.

The change in the regex is displayed as a live preview. Once the regex is ready, click **Site overview with this RegEx** and
observe results. Click **Save** (in the upper right corner).

![Site separation regex](site_separation_regex.png)

!!! example

    We have several locations whose name is logically designed as one letter with one to three numbers. From the point of view of a regex, such a site can generally be expressed as `^(\[a-zA-Z\]\\d{1,3})`. Unfortunately, we have two other sites that do not fit into this schema. These sites can be defined with their own regex and this can be added to the original one using the logical operator **or**:

    ```
    ^([a-zA-Z\]\d{1,3}|HWLAB|static\d{1})
    ```

    to combine these 3 separate options together.

For devices that do not match the RegEx, IP Fabric automatically adds those to the site based on protocol relation (CDP, LLDP, STP, L3) under the condition that there's only a single relation to one particular site. This feature is especially useful for Access Points and similar devices, that do not follow the standard naming conventions and are linked to one specific location.

## Manual Site Separation

!!! note

    With this setting, you can manually edit the distribution of sites.

The Manual Site Separation option is complementary to two previous options and provides the users with full flexibility. It can be enabled in **Inventory > Sites > Manual Separation** where any device's site can be adjusted based on more attributes.
