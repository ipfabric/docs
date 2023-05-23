---
description: The IP Fabric Solution Architects will setup the SSO configuration as it is complex to implement.
---

# Single Sign-On (SSO)

!!! warning "Outdated SSO user records in IP Fabric might cause login issues"

    With SSO configured, each sign-in of a new user into IP Fabric via SSO will
    create a new (non-local) user record in **Settings --> Administration -->
    Local Users** -- with the user's current username and email from the
    Identity Provider (IdP).

    If the user's username or email change on the IdP side, the user will
    encounter `Authentication Failure` while logging into IP Fabric via SSO --
    due to username/email mismatch between the IdP and IP Fabric.

    In that case, please remove the outdated user record of that user in
    **Settings --> Administration --> Local Users**.

IP Fabric includes support for single sign-on. We have opted for
[Dex (A Federated OpenID Connect Provider)](https://dexidp.io/) as a key
building block to allow a broader set of Identity Providers (IdP).

```mermaid
sequenceDiagram
  IPF->>IPF: User selects SSO on the IPF login screen.
  IPF->>Dex: Redirect after starting SSO auth.
  Dex->>IdP: Dex redirects to selected and cofigured IdP.
  IdP->>IdP: User authenticates, provides MFA etc.
  IdP->>Dex: User is redirected back to Dex with code.
  Dex->>IdP: Dex fetches token from IdP.
  Dex->>IPF: Dex redirects the user back to IPF with code.
  IPF->>Dex: IPF fetches token from Dex.
```

!!! warning "Complex Configuration"

    Implementation of SSO configuration can be complex, and because of that, it
    is recommended to be configured for you by our Solution Architects. If you
    are unsure who your Solution Architect is, please contact our Support Team.

## Requirements

### Certificate

Prior to configuring SSO, the IP Fabric server must not be using a self-signed
certificate. To create a new signed TLS certificate, please see the instructions
located at [IPF Certificates](../system/ipf_cert.md).

!!! information "Private Certificate Authority (CA)"

    IP Fabric only trusts certificates issued by CAs listed in the system
    `openssl` trust-store. If your company uses certificates signed by an
    internal CA, please reach out to your Solution Architect or open a Support
    ticket for further configuration in order to properly enable SSO.

### CLI Access

In order to make changes to certain files, you must have access to the `osadmin`
account to log into the CLI and gain root access. For more information, please
see [CLI Overview](../../System_Administration/Command_Line_Interface/index.md).

```bash
justin@ubuntu:~$ ssh osadmin@demo.ipfabric.io
osadmin@demo:~$ sudo -s
[sudo] password for osadmin:
root@demo:/home/osadmin#
```

## API Configuration `api.json`

The IP Fabric API configuration is stored in `/opt/nimpee/conf.d/api.json`. This
file needs to be created during the first configuration as it does not exist in
the default image. It will also be persistent during upgrades and will not be
changed. Below is a full example of the `api.json` config file:

```json
{
  "app": {
    "url": "https://<FQDN>/api"
  },
  "web": {
    "url": "https://<FQDN>"
  },
  "dex": {
    "url": "https://<FQDN>/dex",
    "providers": [
      {
        "name": "sso",
        "clientId": "ipfabric",
        "clientSecret": "<RANDOM_SECRET>",
        "roleAssignments": [
          {
            "groupName": "any",
            "roleId": null
          },
          {
            "groupName": "admin",
            "roleId": "admin"
          },
          {
            "groupName": "read",
            "roleId": "2356575453"
          },
          {
            "groupName": "read-only-users",
            "roleName": "read-only-users"
          }
        ]
      }
    ]
  }
}
```

!!! note "roleName"

    In IP Fabric version `6.1.0`, the ability to use `roleName` in the SSO
    configuration was added. It is recommended to switch from using `roleId` to
    `roleName` for consistency and human readability.

??? example "JSON Validation"

    The example below is a malformed JSON due to the comma after `app.url`:

    ```json
    {
      "app": {
        "url": "https://demo.ipfabric.io/api",
      },
      "web": {
        "url": "https://demo.ipfabric.io"
      },
      "dex": {
        "url": "https://demo.ipfabric.io/dex",
        "providers": []
      }
    }
    ```

    Using the `jq` command, it is easy to discover JSON errors instead of
    searching through log files or `journalctl` output.

    ```bash
    root@demo:~$ jq . /opt/nimpee/conf.d/api.json
    parse error: Expected another key-value pair at line 4, column 3
    ```
    
    You can reformat and prettify the JSON file by running:
    
    ```commandline
    echo "$(jq < /opt/nimpee/conf.d/api.json)" > /opt/nimpee/conf.d/api.json
    ```

### URL Configuration

Inside the `app`, `web` and `dex` sections, the `url` fields need to be updated
with the FQDN of the IP Fabric system.

`dex.url` must match the [`ipf-dex.yaml`](#issuer) issuer URL.

Example:

```json
{
  "app": {
    "url": "https://demo.ipfabric.io/api"
  },
  "web": {
    "url": "https://demo.ipfabric.io"
  },
  "dex": {
    "url": "https://demo.ipfabric.io/dex"
  }
}
```

### Providers Configuration

The `providers` section has to contain at least one SSO provider (which
corresponds to `staticClient` in the Dex configuration).

```json
{
  "dex": {
    "providers": [
      {
        "name": "sso",
        "clientId": "ipfabric",
        "clientSecret": "jqv-W_khLSwJdJMHCjhJefyu-QdeXq9kcz8sAfMrO1Q",
        "roleAssignments": [
          {
            "groupName": "any",
            "roleId": null
          },
          {
            "groupName": "admin",
            "roleId": "admin"
          },
          {
            "groupName": "read",
            "roleId": "2356575453"
          },
          {
            "groupName": "read-only-users",
            "roleName": "read-only-users"
          }
        ]
      }
    ]
  }
}
```

- `name` -- User-defined name of the Identity Provider (IdP) displayed in the
  GUI.
  - Can only contain `a-z0-9_`. **Do not use uppercase.**
  - Used in [`ipf-dex.yaml`](#static-clients) for `redirectURIs` under
    `staticClients`.
  - This name will be displayed on the login page of the GUI. This name will be
    capitalized (`sso` --> `Sso`), therefore it is recommended to use names such
    as `azure` or `okta`.
  - ![SSO Button](sso_button_name.png)
- `clientId` -- User-defined value (suggested to keep `ipfabric`).
  - Used in [`ipf-dex.yaml`](#static-clients) for `id` under `staticClients`.
- `clientSecret` -- User-defined value for a shared secret between IP Fabric and
  Dex only.
  - Can be randomly created for instance using Python:
    `python -c "import secrets; print(secrets.token_urlsafe())"`
  - Used in [`ipf-dex.yaml`](#static-clients) for `secret` under
    `staticClients`.
- `roleAssignments` -- An array of objects.
  - Objects are in the format of
    `{groupName: string, roleId?: string|null, roleName?: string|null }`
    - `groupName` -- The name of the group that is configured on the SSO side.
      - `any` will provide access to any user by default.
      - Multiple mappings with the same `groupName` will get merged (so the user
        will receive all corresponding roles on the IP Fabric side).
    - `roleId` -- The ID of the IP Fabric role.
      - A value of `null` will provide no access.
      - Either `roleId` or `roleName` property must be specified, not both.
      - **Please do not confuse `roleId` with `roleName` as these are different
        values. `roleId` must be retrieved using the browser Developer Tools or
        using the API (example below).**
    - `roleName` -- The name of the IP Fabric role.
      - A value of `null` will provide no access.
      - Either `roleName` or `roleId` property must be specified, not both.
      - **Since version `6.1`, you can opt to only use `roleName` instead of 
        `roleId` in your configuration.**
      - **Since version `6.3`, `roleName` can only contain `a-zA-Z0-9_-`.
        Previously created roles will be automatically modified by removing 
        not-allowed characters from role name according to the new validation rules.
        Make sure specified `roleName` refers to the existing role in the system.**

Example how to find `roleId`:

![Role ID](roles_id.png)

## SSO Configuration `ipf-dex.yaml`

While Dex supports various connectors, we strongly recommend using OpenID
Connect (OIDC) for SSO integration (Azure uses a special `microsoft` connector
and an example is provided below along with SAML). Please check the
[official Dex documentation](https://dexidp.io/docs/connectors) for their
overview.

Dex configuration is located in `/etc/ipf-dex.yaml` on the IP Fabric appliance.
It has several configuration sections and a full example of the file is located
below. Please note that OIDC, SAML, and Azure have different syntaxes for the
`connectors` configuration portion, which are covered separately.

```yaml
# /etc/ipf-dex.yaml
# example config in both devOps/etc/ipf-dex.yaml and devOps-install/install/ipf-dex.yaml
issuer: https://<FQDN>/dex

staticClients:
  - id: ipfabric
    redirectURIs:
      - "https://<FQDN>/api/<API_VERSION>/auth/external/<API-DEX-PROVIDERS-NAME>"
    name: IP Fabric
    secret: <RANDOM_SECRET>

storage:
  type: memory

logger:
  level: debug

web:
  http: 127.0.0.1:5556

telemetry:
  http: 127.0.0.1:5558

grpc:
  addr: 127.0.0.1:5557

oauth2:
  skipApprovalScreen: true

connectors:
  - type: oidc
    id: sso_oidc
    name: SSO OIDC
    config:
      issuer: <SSO_ISSUER>
      redirectURI: https://<FQDN>/dex/callback
      clientID: <SSO_CLIENT_ID>
      clientSecret: <SSO_CLIENT_SECRET>
      getUserInfo: true
      insecureEnableGroups: true
      scopes:
        - openid
        - profile
        - email
        - groups
```

!!! note "Keep Default Values"

    The following lines should be left to the default values:

    ```yaml
    storage:
      type:
        memory

    logger:
      level: debug

    web:
      http: 127.0.0.1:5556

    telemetry:
      http: 127.0.0.1:5558

    grpc:
      addr: 127.0.0.1:5557
    ```

### Issuer

Dex configuration has at the very top an attribute called `issuer`. This needs
to be configured to be equal to the `url` under `dex` in
[`api.json`](#providers-configuration).

For example:

```yaml
issuer: https://demo.ipfabric.io/dex
```

### Skip Approval Screen

The following lines of the configuration control if you would like a `Grant
Access` screen to be presented to your users on every login. By setting it to 
true, the message below won't be displayed.

```yaml
oauth2:
  skipApprovalScreen: true
```

![Grant Access](sso_approval.png)

### Static Clients

The `staticClients` section contains the configuration for the IP Fabric portal
which acts as a client to `dex`.

```yaml
staticClients:
  - id: ipfabric
    redirectURIs:
      - "https://demo.ipfabric.io/api/v5.0/auth/external/sso"
    name: IP Fabric
    secret: jqv-W_khLSwJdJMHCjhJefyu-QdeXq9kcz8sAfMrO1Q
```

- `id` -- Unique ID of the client within the Dex configuration.
  - Found in [`api.json`](#providers-configuration) for `clientId` under
    `providers`.
- `redirectURIs` -- Full path to the callback endpoint of the IP Fabric client.
  - It is in the format of
    `https://<FQDN>/api/<API_VERSION>/auth/external/<API-DEX-PROVIDERS-NAME>`
  - `API-DEX-PROVIDERS-NAME` is found in [`api.json`](#providers-configuration)
    for `name` under `providers`.
    - Can only contain `a-z0-9_`. **Do not use uppercase.**
  - Please be aware of the `API_VERSION` property.
    - Needs to be updated with **every IPF release** (i.e. after IP Fabric is
      upgraded to `v6.1`, leaving the URL at `v6.0` will no longer work).
    - Unlike other API calls, this has to be set with `v{major}.{minor}` and
      cannot use `v{major}` (i.e. `/api/v6/auth` will not work, it must be
      `/api/v6.0/auth`).
    - This will require manual changes when going from `v6.0` --> `v6.1` -->
      `v6.2`.
- `name` -- Arbitrary name of the client.
  - This will be displayed in the
    [`Grant Access` screen](#skip-approval-screen).
- `secret` -- User-defined secret.
  - Found in [`api.json`](#providers-configuration) for `clientSecret` under
    `providers`.
  - It is a shared secret between IP Fabric and Dex only.

### Config File Mapping

Here is a nice illustration of how the `/opt/nimpee/conf.d/api.json` values map
to `/etc/ipf-dex.yaml`:

![JSON yaml mapping](sso_api_dex_mapping.png)

### OpenID Connect (OIDC)

Please review the
[Dex documentation on OIDC](https://dexidp.io/docs/connectors/oidc/) for all
configuration options and potential caveats.

!!! note "Well-known Configuration"

    Many of the variables required can be found in the OIDC well-known
    configuration endpoint. For example take a look at Google:
    [`.well-known/openid-configuration`](https://accounts.google.com/.well-known/openid-configuration).

```yaml
connectors:
  - type: oidc
    id: sso_oidc
    name: SSO OIDC
    config:
      issuer: <SSO_ISSUER>
      redirectURI: https://<FQDN>/dex/callback
      clientID: <SSO_CLIENT_ID>
      clientSecret: <SSO_CLIENT_SECRET>
      getUserInfo: true
      insecureEnableGroups: true
      scopes:
        - openid
        - profile
        - email
        - groups
      claimMapping:
        groups: roles
```

- `type` -- Dex connector type.
- `id` -- User-defined arbitrary ID (not used anywhere).
- `name` -- User-defined arbitrary name (not used anywhere).
- `redirectURI` -- `issuer` URL with `/callback` appended.
  - Can be found in [`api.json`](#url-configuration) under `dex`, OR
  - can be found in [`ipf-dex.yaml`](#issuer).
- `getUserInfo` -- When enabled, the OpenID Connector will query the UserInfo
  endpoint for additional claims.
- `insecureEnableGroups` -- Groups claims only refresh when the id token is
  refreshed, meaning the regular refresh flow doesn't update the groups claim.
  As such, by default the OIDC connector doesn't allow groups claims. If you are
  okay with having potentially stale group claims, you can use this option to
  enable groups claims through the OIDC connector on a per-connector basis.
- `clientID` -- A client ID configured or generated on the Identity Provider.
- `clientSecret` -- A client secret configured or generated on the Identity
  Provider.
- `scopes` -- A list of scopes to be returned from the Identity Provider.
  - The ones listed above are the most common. However, these can differ from
    provider to provider.
  - Scopes are normally found in `.well-known/openid-configuration` which is
    discussed in the [OIDC](#openid-connect-oidc) section.
- `claimMapping` -- Some providers return non-standard claims (i.e. roles), use
  claimMapping to map those claims to standard claims.

### Azure

!!! warning "Azure"

    Please review the
    [Dex documentation on Azure](https://dexidp.io/docs/connectors/microsoft/)
    for all configuration options and potential caveats as Azure requires
    special configuration for proper enablement.

```yaml
connectors:
  - type: microsoft
    id: sso_azure
    name: SSO Azure
    config:
      clientID: <SSO_CLIENT_ID>
      clientSecret: <SSO_CLIENT_SECRET>
      redirectURI: https://<FQDN>/dex/callback
      tenant: <TENANT_ID>
      scopes:
        - openid
        - profile
        - email
        - groups
      claimMapping:
        groups: roles
```

- `type` -- Dex connector type.
- `id` -- User-defined arbitrary ID (not used anywhere).
- `name` -- User-defined arbitrary name (not used anywhere).
- `redirectURI` -- `issuer` URL with `/callback` appended.
  - Can be found in [`api.json`](#url-configuration) under `dex`, OR
  - can be found in [`ipf-dex.yaml`](#issuer).
- `tenant` -- UUID or Name of specific tenant accounts belong to.
  - **Required in order to obtain `groups` claim from Azure.**
- `clientID` -- A client ID configured or generated on the Identity Provider.
- `clientSecret` -- A client secret configured or generated on the Identity
   Provider.
- `scopes` -- A list of scopes to be returned from the Identity Provider.
  - The ones listed above are the most common. However, these can differ from
    provider to provider.
  - Scopes are normally found in `.well-known/openid-configuration` which is
    discussed in the [OIDC](#openid-connect-oidc) section.
- `claimMapping` -- Some providers return non-standard claims (i.e. roles), use
  claimMapping to map those claims to standard claims.

### SAML Connector

Please review the
[Dex documentation on SAML](https://dexidp.io/docs/connectors/saml/) for all
configuration options and potential caveats.

```yaml
connectors:
  - type: saml
    id: sso_saml
    name: SSO SAML
    config:
      ssoURL: <SSO_URL>
      ssoIssuer: <SSO_ISSUER>
      redirectURI: https://<FQDN>/dex/callback
      caData: "LS0t ... 0tLS0tCg=="
      # ca: /path/to/file
      usernameAttr: name
      emailAttr: email
      groupsAttr: groups
      nameIDPolicyFormat: emailAddress
```

- `type` -- Dex connector type.
- `id` -- User-defined arbitrary ID (not used anywhere).
- `name` -- User-defined arbitrary name (not used anywhere).
- `redirectURI` -- `issuer` URL with `/callback` appended.
  - Can be found in [`api.json`](#url-configuration) under `dex`, OR
  - can be found in [`ipf-dex.yaml`](#issuer).
- `ssoURL` -- SSO URL used for POST value.
- `ssoIssuer` -- Optional: Issuer value expected in the SAML response.
- Pick and use one option to validate the signature of the SAML response:
  - `caData` -- Base64 encoded certification chain.
  - `ca` -- File location of containing certification chain.
- `usernameAttr` -- Maps SAML `name` value to IP Fabric's `username`.
- `emailAttr` -- Maps SAML `email` value to IP Fabric's `email`.
- `groupsAttr` -- Maps SAML `groups` value to IP Fabric's `groupName`.
- `nameIDPolicyFormat` -- The connector uses the value of the NameID element as
  the user's unique identifier which Dex assumes is both unique and
  never-changing. Use `nameIDPolicyFormat` to ensure this is set to a value
  which satisfies these requirements.

### YAML Validation

While the validity of the actual configuration is determined by Dex itself, it
can be handy to verify parsing of the configuration YAML. You can use the
following to get a JSON representation of `/etc/ipf-dex.yaml`:

```commandline
python3 -c 'import sys, yaml, json; y=yaml.safe_load(sys.stdin.read()); print(json.dumps(y))' < /etc/ipf-dex.yaml  | jq .
```

??? example "Correct YAML"

    Let's assume the following YAML fragment as an input:

    ```yaml
    connectors:
      - type: microsoft
        id: sso_azure
        config:
          scopes:
            - openid
            - profile
            - email
            - groups
    ```

    The output of the command will be:

    ```json
    {
      "connectors": [
        {
          "type": "microsoft",
          "id": "sso_azure",
          "config": {
            "scopes": [
              "openid",
              "profile",
              "email",
              "groups"
            ]
          }
        }
      ]
    }
    ```

    As you can see, `scopes` has been correctly parsed as a list.

??? example "Incorrect YAML"

    Let's assume the following YAML fragment as an input:

    ```yaml
    connectors:
      - type: microsoft
        id: sso_azure
        config:
          scopes:
          - openid
            - profile
            - email
            - groups
    ```

    The output of the command will be:

    ```json
    {
      "connectors": [
        {
          "type": "microsoft",
          "id": "sso_azure",
          "config": {
            "scopes": [
              "openid - profile - email - groups"
            ]
          }
        }
      ]
    }
    ```

    As you can see, `scopes` has been completely incorrectly parsed as a
    multiline string.

## Restarting Services

After making changes to `/opt/nimpee/conf.d/api.json`, it is required to restart
the API service:

```commandline
systemctl restart nimpee-api.service
```

Consequently, after making changes to `/etc/ipf-dex.yaml`, the Dex service needs
to be restarted:

```commandline
systemctl restart ipf-dex.service
```
