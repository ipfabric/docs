# User Management

The default user ***admin*** with password ***netHero!123*** is used for
the initial login to the system. This user has administrative privileges
to create or manage other users and to perform network management tasks.
It is recommended to change the password for the admin user and to use a
standard user account for access to the system. If you are unable to
login with the default admin account after the first startup, please
follow this guideline [Invalid default username and
password](Invalid_default_username_and_password)

Main user management tab allows you to create a new local account with
various user permissions or modify already existing users including
default admin account. Only a user with User Management permission can
access the User Management menu.

## Adding New Local User

A new user is added to the system by filling out his/her user details

<img src="attachments/79462445/1931804688.png" class="image-left" loading="lazy" data-image-src="attachments/79462445/1931804688.png" data-height="476" data-width="422" data-unresolved-comment-count="0" data-linked-resource-id="1931804688" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210128-115359.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79462445" data-linked-resource-container-version="8" data-media-id="4fafea76-4d7c-4fea-8656-4cd6db9d7edc" data-media-type="file" />

### Following are the pre-defined user roles:

**READ** – a user can view the discovered data, load diagram views, view
stored configurations, but cannot launch a discovery themselves or
modify or delete existing views. He is also unable to execute basic
snapshot operations like loading and unloading snapshots.

**DISCOVERY** – a user can launch a discovery, save new view or modify
existing diagram view.

**USER MANAGEMENT** – an administrative right that specifically grants a
privilege to a user to create, delete or modify other users.

**SETTINGS** – an administrative right that enables access to the global
settings of the system.

## Users

Within this table, all user accounts can be modified or deleted. It also
transparently shows user permissions and emails.

<img src="attachments/79462445/1931804696.png" class="image-center" loading="lazy" data-image-src="attachments/79462445/1931804696.png" data-height="223" data-width="1522" data-unresolved-comment-count="0" data-linked-resource-id="1931804696" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210128-121525.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79462445" data-linked-resource-container-version="8" data-media-id="dd3241f8-2dc5-4f47-9f79-f16a89f671e6" data-media-type="file" />

When an edit menu for a specific user account is opened, user
permissions or a password can be updated.

<img src="attachments/79462445/1931804702.png" class="image-left" loading="lazy" data-image-src="attachments/79462445/1931804702.png" data-height="601" data-width="424" data-unresolved-comment-count="0" data-linked-resource-id="1931804702" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210128-125129.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79462445" data-linked-resource-container-version="8" data-media-id="58c45a4a-1db1-4587-81dc-08697347b052" data-media-type="file" />

The password of the default admin account can also be changed here.

# LDAP Authentication

Only LDAP user authentication is supported. Users need to be assigned
the appropriate permissions locally or default user permissions for
authenticated users need to be set.

User synchronization or import capabilities **are not supported** **at
this time**. LDAP hence work in an **on-demand** state - **users are
added to the IP Fabric after they log in for the first time.**

### Supported LDAP servers are:

-   Microsoft Active Directory

-   OpenLDAP

## Enable LDAP authentication

1.  Log in to the IP Fabric as a user with admin rights.

2.  Go to ***Settings → User Management → LDAP Settings*** tab.

3.  Select ***+Add Domain***.

4.  Choose LDAP server type in the ***Type*** drop-down menu. Only
    ***Microsoft Active Directory*** or ***Open LDAP*** servers are
    supported.

5.  Enter all the aliases/suffixes for this domain in the ***Account
    suffixes*** field. Each suffix must begin with @. If the same user
    can log in with other suffixes, for example, <joe@europe.domain.com>
    and <joe@domain.com> then fill in
    @[europe.domain.com](http://europe.domain.com) and
    @[domain.com](http://domain.com).

6.  Add servers for the domain:

    1.  as an **explicit list of addresses**

        1.  Choose ***Use pre-configured LDAP servers*** in Servers
            dropdown

        2.  Specify FQDN or IP address of the LDAP server including the
            protocol prefix (such as ldap://your.domain.com or
            ldaps://your.domain.com)

        3.  Specify the port (default LDAP port is 389 and default LDAPS
            port is 636)

        4.  For LDAP over SSL, also upload a CA certificate used for the
            LDAP certificate signature

        5.  Click on ***+Add Server*** if you want to add backup servers

    2.  using **DNS service records**

        1.  Choose ***Use DNS to find LDAP servers ***in Servers
            dropdown

        2.  Choose/upload a certificate (recommended in the production
            environment)

        3.  Define the DNS address

        4.  Define Service location name (common names are *ldap* and
            *ldaps*). This is the network service that constructs the
            final name of the record. The construction is done as
            follows: "\_{{service location name}}.\_tcp.{{dns address}}"

7.  Specify service account with LDAP read permissions in the ***Bind
    DN*** field. This field must be an <u>escaped</u> LDAP-style
    <u>distinguished name</u>. (for example
    `CN=Doe\, Joe,OU=europe,DC=your,DC=domain,DC=com` or
    `CN=User,OU=europe,DC=your,DC=domain,DC=com`)

8.  Enter the bind user's password (defined in step 7) in the ***Bind
    credentials*** field.

9.  Enter a whole domain or specific organization unit (container) in
    ***Search base*** to specify where users and groups can be found in
    the LDAP tree. (for example
    `OU=NetworkAdmins,DC=your,DC=domain,DC=com`)

10. Enter an attribute where email is stored in the LDAP user object
    into ***Search email attribute**.*

11. Only for “*Microsoft Active Directory*”: Tick ***Allow nested
    groups*** for nested group permission lookup. This uses [Extensible
    Match](https://ldapwiki.com/wiki/ExtensibleMatch) Rule
    ([LDAP_MATCHING_RULE_IN_CHAIN](https://ldapwiki.com/wiki/LDAP_MATCHING_RULE_IN_CHAIN))
    which might be slow in your local setup.

12. Click ***Confirm***.

<div>

<div>

If the LDAP server is not reachable or credentials to the service
account are not correct, LDAP authentication cannot be set.

</div>

</div>

## LDAP Group Permissions

After the LDAP server is added, default permissions for authenticated
users can be set. By default, all permissions are denied. This means
that a user even with the correct LDAP username and password won't be
able to log in since he/she won't even have read-only permission. It is
recommended to create new LDAP groups (such as IP_FABRIC_ADMINISTRATORS,
IP_FABRIC_USERS, ...) and assign to them users to which you want to
grand access.

<div>

<div>

Primary user groups are not supported. It is recommended to create new
LDAP groups (such as IP_FABRIC_ADMINISTRATORS, IP_FABRIC_USERS, ...) and
assign them permissions.

</div>

</div>

<img src="attachments/79626273/1401454603.png?width=442" class="image-center" loading="lazy" data-image-src="attachments/79626273/1401454603.png" data-height="459" data-width="1529" data-unresolved-comment-count="0" data-linked-resource-id="1401454603" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20200811-123747.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="79626273" data-linked-resource-container-version="19" data-media-id="53ce403e-1c59-47bc-8f6a-e577058f1f8c" data-media-type="file" width="442" alt="Setting LDAP group permissions" />

## Disable LDAP authentication

Remove all LDAP configuration domains in ***Settings → User Management →
LDAP Settings ***to disable LDAP authentication.

## Local vs LDAP authentication

By default, local authentication (or in other words information stored
in the local database) is the preferred authentication method, where
LDAP is used as a backup authentication method. If a user is not found
in the local database and LDAP authentication is defined, IP Fabric will
redirect the authentication attempt to an LDAP server. If a user is
successfully authenticated through LDAP, basic information about this
user is then passed from LDAP and stored in the local database.

## Troubleshooting

Before contacting our support, please make sure that inputs entered into
IP Fabric user interface are correct. This can be done using
`ldapsearch` command utility:

<div>

<div>

`ldapsearch` is present in IP Fabric image (access it via ssh) or it can
be installed locally as part of `ldap-utils` Linux package. It is
recommended to **always test LDAP configuration from the IP Fabric
image**.

</div>

</div>

### CLI Example

<div>

<div>

The following example doesn’t verify SSL certificate if LDAPS is used

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` bash
LDAPTLS_REQCERT=ALLOW ldapsearch \
  -W -H "ldaps://your-ldap-server:636" \
  -D "$LDAP_BIND_DN" \
  -b "$LDAP_SEARCH_BASE" \
  -s sub
```

</div>

</div>

Your fields are correctly set when exit-code of your command is zero.

The use of nested groups can also be tested by adding the following line
to the CLI example:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
(member:1.2.840.113556.1.4.1941:=$USER.DN)
```

</div>

</div>

The CLI example can be followed by a query. Useful LDAP queries to find
a user follow:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
(uid=$LOGIN_INPUT)
(|(sAMAccountName=$LOGIN_INPUT)(userPrincipalName=$LOGIN_INPUT))
```

</div>

</div>

### Error Codes

All LDAP errors regarding server connection and user binding are
returned as “*LDAP as provided is not reachable*” due to security
concerns. Please check your *Search base* and *Search login attribute*
when “*LDAP Search Failed*“ error is shown.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210128-115359.png](attachments/79462445/1931804688.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210128-121525.png](attachments/79462445/1931804696.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210128-125129.png](attachments/79462445/1931804702.png)
(image/png)  

</div>
