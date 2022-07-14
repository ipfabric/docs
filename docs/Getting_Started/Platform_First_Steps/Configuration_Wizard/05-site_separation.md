# 05 - Site Separation

## Site separation
The site represents a separate collection of devices. A site can be a branch, a factory, a production floor, a campus, or anything that might represent a logical group for a user.

By default, the Site distribution is generated automatically after the discovery process ends and is based on the rules described below. It can also be triggered manually without the need for the whole discovery process by going to **Settings → Site separation (In global or Snapshot settings)**.

### Manual Site Separation (Device Attributes)

The Manual Site Separation enables the **Device Attributes** feature to create manual separation if a device does not follow a standard hostname rule or perhaps the hostname is duplicated in multiple locations.

To configure **Device Attributes** first enable the toggle in the Site Separation Menu and select Configure or the Device Attributes menu under settings.
![Site separation manual site separtion](site_separation_manual_site_separation.png)

#### Device Attributes

![Site separation device attributes](site_separation_device_attributes.png)

- **Serial Number** is IP Fabric’s "Unique Serial Number" (API column `sn`); this is not the column "Serial Number" which represents the Hardware SN (API column `snHw`)
    - Devices discovered via API can also be assigned using Device Attributes.
- **Hostname** is populated by IP Fabric when a device matching the **Serial Number** is found
- **Attribute** is the Device Attribute to assign, since we want to set the Site based on the serial number set it to **Site name**
- **Value** is the attribute’s value to assign, in this case we want to split site L35 into separate sites named 35COLO, 35PRODUCTION, 35HEADOFFICE

#### Creating Rules In The UI

You are able to create rules in the UI by selecting the **Add attribute** button. This will provide you a form to fill out.
![Site separation add attribute](site_separation_add_attribute.png)

The dropdown is intuitive and will let you search based on SN or hostname. Currently there is an issue where IP Fabric will not search for devices discovered via an API in the UI. Even though it appears no devices match the SN it will still perform the site separation correctly on the next snapshot.

![Site separation add attribute dropdown](site_separation_add_attribute_dropdown.png)

#### Creating Rules Via The API

This is the preferred method of creating rules as it allows for bulk importing.

Method | PUT
---|---
URL| `https://<IPF_URL>/api/v5.0/attributes/global`
Data | `{"attributes": [{"sn": "<IPF SERIAL NUMBER>", "value": "<SITE NAME>", "name": "siteName"}]}`

### Routing And Switching Domain

!!! note

    With this setting, you can manually edit the distribution of sites later. Sites can be also renamed.

By default, the site is comprised of the topology of all contiguously interconnected protocols, and the boundary of a site is formed by the network protocol relation that is not under management using the provided authentication credentials.

The default separation is useful for MPLS networks where directly connected routing infrastructure at the site’s edge is not accessible.

For situations where an inaccessible routed firewall is used at the site (i.e. device under different management team), an option **Firewall at site** can be turned on so the infrastructure before and behind the firewall is not separated into two different sites.

For networks that have direct routing connectivity between sites, such as DMVPN or Leased Lines (usually over Serial or MFR interfaces), an option to separate the site using **tunnel** and/or **serial** the interface should be selected.

![Routing and switching domain site separation](routing_and_switching.png)

### Regular Expression Site Separation

!!! hint

    Site distribution cannot be changed manually when regex rules are used. Sites cannot be renamed.
Alternatively, site separation can follow a specific Regular Expression (RegEx) where separation will be performed based on portion of a device hostname or SNMP location.

!!! note

    If you cannot cover the names of the sites with one regex, you can use logical or. Use | (pipe) the character between RegEx rules or use the Device Attributes method shown below.

#### Hostname Regex

Go to **Settings → Site separation** and change **Routing & Switching Domain** to **RegEx based on hostname** or create a new rule by **Add rule** button.

**Transform hostname** is used to normalize site names based on hostname:

- Upper case (default) - first hostname `PRAGUE-RTR1`, second hostname `prague-rtr2` => result is that both devices in one site named `PRAGUE`

- Lower case - first hostname `PRAGUE-RTR1`, second hostname `prague-rtr2` => result is that both devices in one site named `prague`

- No transformation - first hostname `PRAGUE-RTR1`, second hostname `prague-rtr2` => result is that each device has its own site named `PRAGUE` and `prague`
![Site separation hostname regex](site_separation_hostname_regex.png)

In this example the regular expression will match items such as PRAGUE-, LONDON-, etc.

#### SNMP Location Regex

Go to **Settings → Site separation** and change **Routing & Switching Domain** to **RegEx based on SNMP location** or create a new rule by **Add rule** button.
![Site separation SNMP regex](site_separation_snmp_regex.png)

#### Testing

The UI now allows you to edit and test your rules directly in the browser when selecting the **Test rule** option. Here you can see a live preview of devices that will match the regex you created.
![Site separation testing](site_separation_testing.png)

You can also test SNMP location rules:

![Site separation testing snmp](site_separation_testing_snmp.png)

#### Regex Example

We have several locations whose name is logically designed as one letter with one to three numbers. From the point of view of a regex, such a site can generally be expressed as "**^([a-zA-Z]\d{1,3})**". Unfortunately, we have two other sites that do not fit into this schema. These sites can be defined with their own regex and this can be added to the original one using the logical operator **or**:

**^([a-zA-Z]\d{1,3}|HWLAB|static\d{1})** - 1st option OR 2nd option OR 3rd option

### Device Neighborship

![Site separtion device neighborship](site_separation_device_neighborship.png)

This option will try to define a device based on its neighbor relationship if a device does not match any previous rule.  Perhaps you have devices in your environment that do not follow the normal standard like in a DMZ zone or Day 0 devices that have not been fully configured.  If that device is connected to a device that did match a rule, IP Fabric will intelligently group it to the correct site.

#### Creating Rules With `python-ipfabric` Package

Please see example located on [Community Fabric GitHub](https://github.com/community-fabric/python-ipfabric/blob/main/examples/settings/attributes.py).

## Rule Priority

![Site separation rule priority](site_separation_rule_priority.png)

Rule precedence are followed in a top down manner.

1. **Manual site separation** (if enabled) will look at the **Device Attributes** and try to first assign a device based on serial number if a match is found.
2. Rules you define. In the example above it will check the following
   1. If SNMP Location matches "IPFABRIC, (LAB01)" → Site LAB01
   2. If hostname matches "^L21" → Site MPLS 
   3. If hostname matches "^(L\d{1,2})" → Site L2-99
3. Try to assign devices without sites based on [device neighborship](../../../IP_Fabric_Settings/site_separation.md) (if enabled)

