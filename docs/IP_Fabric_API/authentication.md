---
description: Information about how you can authenticate your API calls to IP Fabric, enabling you to fetch data from your snapshots.
---

# Authentication

The majority of requests to the IP Fabric platform need to be authenticated. We
provide multiple authentication methods, which differ from each other. Please
review all of them before committing to any.

## API Token

API token needs to be passed as a request header. Please see
[API Tokens](../IP_Fabric_Settings/integration/api_tokens.md) on how to create
an API token in the UI.

- Allows for limiting the scope of API calls. This allows for giving _fewer_
  rights than the account creating the token has.
- Long-lived static token (secure storage is important).

```http
Content-Type: application/json
X-API-Token: YOUR_API_TOKEN_GENERATED_VIA_IPFABRIC_UI
```

## Basic Authentication

Using basic authentication requires Base64 encoding `username:password` and
passing that into the `Authorization` header.

- The call will always have the same rights as the user account. This may not be
  necessary for many use-cases.
- In case this approach is use, we highly encourage the creation of a
  "bot"/"service" user account with a limited access scope.
- Another form of long-lived static token / authentication details (secure
  storage is important).

```bash
osadmin@ipfabric:~$ echo -n "username:password" | base64
dXNlcm5hbWU6cGFzc3dvcmQ=
osadmin@ipfabric:~$ curl -X GET 'https://demo3.ipfabric.io/api/v5.0/snapshots' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ='
```

## Token Authentication

Token authentication allows the exchange of username and password for a pair of
tokens -- access and refresh. The exchange is facilitated via the `login`
endpoint. The access token is then passed to the consecutive API calls in the
`Authorization` header.

- The call will always have the same rights as the user account. This may not be
  necessary for many use-cases.
- In case this approach is used, we highly encourage creation of a
  "bot"/"service" user account with a limited access scope.
- Storage of the refresh token is important as it allows maintaining long-term
  access.

### Types of Tokens

**Access Token**

: An access token is a [JSON Web Token (JWT)](https://jwt.io/) as per RFC-7519,
signed using SHA-256 with RSA encryption. The token expires in 30 minutes since
being generated, and it can't be revoked during its lifetime.

: ??? info "What is inside an access token?"

      An access token is a JWT consisting of three parts separated by dots --
      Header, Payload, and Signature. You don't need to parse any of these
      fields. For inspecting the content of the JWT, you can use
      <https://jwt.io/>. You will not be able to verify its validity as you
      don't have access to the signing key.

      The payload contains an object with the following fields:

      - `id` -- User ID.
      - `exp` -- Token expiration time (in seconds since Unix epoch).
      - `iat` -- Token issued time (in seconds since Unix epoch).
      - `scope` -- Array of strings representing granted user access.
      - `username` -- String containing the username of the user.
      - `isAdmin` -- A Boolean value whether the user is an admin.
      - `aud` -- String containing the recipient for which the JWT is intended.
      - `iss` -- String containing the issuer of the JWT.

**Refresh Token**

: A refresh token is a token that can be used to obtain a renewed access token.
It can be requested for new access tokens until the refresh token is used,
revoked, or expired.

: A refresh token expires 24 hours after not being used for the generation of a
new access token. Refresh tokens must be stored securely by an application
as it creates a new access token and allows access to the system.

: Starting in IP Fabric version `6.1.0`, the `refreshToken` is rotated after
every use, and a new one is issued.

### Token API

!!! info

    The token API is designed for secure usage with the IP Fabric frontend in
    web browsers. The tokens are present only in headers as secure HTTP-only
    cookies and do not appear anywhere in the response body, providing
    protection against XSS attacks.

#### Login

To log in and obtain an access token and a refresh token, see the `curl` example
below:

```bash
curl -D - -X POST 'https://demo3.ipfabric.io/api/v6.1/auth/login' \
  -H 'Content-Type: application/json' \
  --data-raw '{"username":"<USERNAME>","password":"<PASSWORD>"}'
```

This returns an HTTP response with `accessToken` and `refreshToken` cookies:

```
set-cookie: accessToken=eyJhbGc....; Max-Age=1800; Path=/; Expires=Thu, 06 Jun 2024 12:17:09 GMT; HttpOnly; Secure; SameSite=Strict
set-cookie: refreshToken=w2PJG2hA.....12830361114; Max-Age=86400; Path=/api/auth/token; Expires=Fri, 07 Jun 2024 11:47:09 GMT; HttpOnly; Secure; SameSite=Strict
```

#### Using `accessToken`

The `accessToken` is then placed in the `Authorization` header as seen below.
Please ensure it is formatted as `Authorization: Bearer <ACCESS_TOKEN>`.

```bash
curl -X GET 'https://demo3.ipfabric.io/api/v5.0/snapshots' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...'
```

#### Using `refreshToken`

To create a new `accessToken` from the `refreshToken`:

```bash
curl -D - -X POST 'https://demo3.ipfabric.io/api/auth/token' \
  -H 'Content-Type: application/json' \
  --data-raw '{"refreshToken":"YvnTNW..."}'
```

which then returns a new `accessToken` to use in subsequent calls and a new
`refreshToken` to use for requesting the next `accessToken`:

```
set-cookie: accessToken=eyJhbGc....; Max-Age=1800; Path=/; Expires=Thu, 06 Jun 2024 12:17:09 GMT; HttpOnly; Secure; SameSite=Strict
set-cookie: refreshToken=w2PJG2hA.....12830361114; Max-Age=86400; Path=/api/auth/token; Expires=Fri, 07 Jun 2024 11:47:09 GMT; HttpOnly; Secure; SameSite=Strict
```

Starting with version `7.0`, you can no longer reach token endpoints with the
specified API version: `<API_VERSION>/auth/token`. Use `auth/token` instead.

#### Logout

To log out of IP Fabric:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/logout' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...'
```

### Changing Default Token Expiration

The default token expiration is as follows:

- `accessToken` -- 30 minutes (1800 seconds)
- `refreshToken` -- 24 hours (86400 seconds)

Many company standards require shorter expiration times, and this can be
accomplished via the CLI settings.

--8<-- "snippets/cli_root_access.md"

1. Log in to the IP Fabric CLI as `osadmin`.
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create a new file `/opt/nimpee/conf.d/api.json` or extend the existing one
   with the below JSON. In this example, the `accessToken` expires in 10
   minutes, and the `refreshToken` expires in 15 minutes:

   ```json
   {
     "app": {
       "accessToken": {
         "expiresIn": 600
       },
       "refreshToken": {
         "expiresIn": 900,
         "length": 80
       }
     }
   }
   ```

4. Change file permissions: `chmod 644 /opt/nimpee/conf.d/api.json`
5. Restart the API: `systemctl restart nimpee-api.service`

### Disabling Local Authentication

In case you don't want to use local authentication (username/password) and want
to log in only via SSO or LDAP, you can disable it via the CLI settings (both
token and basic authentication will be disabled). Please note that
[API Tokens](../IP_Fabric_Settings/integration/api_tokens.md) will still work.

--8<-- "snippets/cli_root_access.md"

1. Log in to the IP Fabric CLI as `osadmin`.
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create a new file `/opt/nimpee/conf.d/api.json` or extend the existing one
   with the below JSON:

   ```json
   {
     "app": {
       "enableLocalAuthentication": false
     }
   }
   ```

4. Change file permissions: `chmod 644 /opt/nimpee/conf.d/api.json`
5. Restart the API: `systemctl restart nimpee-api.service`

### Token Errors

When an error is encountered, the API returns an object with a machine-readable
error code and a human-readable error message in the response body:

```json
{
  "code": "API_EXPIRED_API_TOKEN",
  "message": "Expired API Token"
}
```

| Code                        | Message                                                                                              |
| :-------------------------- | :--------------------------------------------------------------------------------------------------- |
| `API_EXPIRED_API_TOKEN`     | The provided API key expired.                                                                        |
| `API_INVALID_API_TOKEN`     | The provided API key doesn't exist. It was removed, or it never existed.                             |
| `API_EXPIRED_ACCESS_TOKEN`  | The provided access token (from the Authorization header) is expired.                                |
| `API_INVALID_ACCESS_TOKEN`  | The provided access token (from the Authorization header) is invalid.                                |
| `API_INVALID_REFRESH_TOKEN` | The provided refresh token (typically sent in the request body) is revoked (blacklisted) or expired. |
