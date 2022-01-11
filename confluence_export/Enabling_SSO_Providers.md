# Enabling SSO Providers

### DEX Configuration

DEX configuration is in `/etc/ipf-dex.yaml`. Follow DEX documentation to
set it up <https://dexidp.io/docs/connectors/saml/> .

Make sure to set `redirectURIs` to
`{{apiServer}}/v1/auth/external/{{name}}` where `name` is the `name`
from API config file for the given IdP.

### IP Fabric API Configuration

API configuration is in `/root/api/config.json` or
`/home/autoboss/api/config.json`.

In order to enable SSO providers, please change the following
configuration fields:

-   public API server URL - `api.url`, for example:
    `https://my-cloud/api`

-   public frontend server URL - `web.url`, for example:
    `https://my-cloud`

-   dex URL - `dex.url`

-   add SSO providers such as into `dex.providers`. Every provider is an
    object that consists of:

    -   `name` - name of the IdP, it can only contain `a-zA-Z0-9_`,

    -   `clientId` - defined in DEX config for the given provider,

    -   `clientSecret` - defined in DEX config for the given provider,

    -   `defaultScope` - user scope that is used if user isn’t member of
        any group listed in `groupScope` object,

    -   `groupScope` - object where key is a group name and values are
        IP Fabric scopes.

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` jscript
"providers": [
  {
    name": "okta",
    clientId": "xxxxxx",
    clientSecret": "xxxxx",
    defaultScope": ["read"],
    groupScope": {
      group01": ["read", "settings", "team", "write"]
    }
  }
]
```

</div>

</div>

<div>

<div>

`name` in `providers` will be used in API endpoint
`/v1/auth/external/{{name}}`. It can only contain letters.

</div>

</div>

<div>

<div>

IP Fabric has 4 different user permissions:

-   `read` - access to the application,

-   `settings` - ability to change application and snapshot settings,

-   `team` - ability to manage user accounts,

-   `write` - ability to start discovery.

</div>

</div>
