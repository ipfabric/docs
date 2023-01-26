# Authentication

Majority of requests to IP Fabric platform need to be authenticated. We provide
multiple authentication methods. They differ to each other, please review all of
them before committing to any.

## API Token

API Token needs to be passed as a request header. Please
see [API Tokens](../IP_Fabric_Settings/api_tokens.md) on how to create an API
Token in the UI.

- Allows for limiting the scope of API calls. This allows for giving _less_
  rights than has account creating the token.
- Long-lived static token (secure storage is important).

```http
Content-Type: application/json
X-API-Token: YOUR_API_TOKEN_GENERATED_VIA_IPFABRIC_UI
```

## Basic Authentication

Using Basic Authentication requires Base64 encoding `username:password` and
passing that into the `Authorization` header.

- Call will always have the same rights as the user account. This may be really
  unnecessary for many use-cases.
- In case this approach is use, we highly encourage creation of a "bot"/"
  service" user account with limited access scope.
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

Token authentication allows to exchange username and password for pair of tokens
-- access and refresh. Exchange is facilitated via `login` endpoint. Access
token is then passed to the consecutive API calls in the `Authorization` header.

- Call will always have the same rights as the user account. This may be really
  unnecessary for many use-cases.
- In case this approach is use, we highly encourage creation of a "bot"/"
  service" user account with limited access scope.
- Storage of refresh token is important as it allows for maintaining long-term
  access.

### Types of Tokens

**Access Token**

: An access token is [JSON Web Token (JWT)](https://jwt.io/) as per RFC-7519
signed using SHA-256 with RSA encryption. The token expires in 30 minutes since
being generated and it can’t be revoked during its lifetime.

: ??? info "What is inside access token?"

      Access token is a JWT which concists of three parts separated by dots -- Header, Payload, and Signature. You don't need to parse any of these fields. You can use [https://jwt.io/](https://jwt.io/) for inspecting content of JWT. You will not be able to verify its validity as you don't have access to signing key.

      The payload contains an object with the following fields:

      - `id` -- User ID
      - `exp` -- Token expiration time (in seconds since Unix epoch)
      - `iat` -- Token issued time (in seconds since Unix epoch)
      - `scope` -- Array of strings representing granted user access
      - `username` -- String containing the username of the user
      - `isAdmin` -- A boolean value whether a user is an admin
      - `aud` -- String containing the recipient for which the JWT is intended
      - `iss` -- String containing the issuer of the JWT

**Refresh Token**

: A refresh token is a token that can be used to obtain a renewed access token.
It can be requested for new access tokens until the refresh token is used, 
revoked, or expired.

: A refresh token expires after 24 hours of not being used for generation of a
new access token. Refresh tokens must be stored securely by an application
as it creates a new Access Token and allowing access to the system.

: Starting in IP Fabric version `v6.1.0` the `refreshToken` is rotated after 
every use and a new one is issued.

### Token API

#### Login

To login and obtain an Access and Refresh token please see the below curl
example:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v6.1/auth/login' \
  -H 'Content-Type: application/json' \
  --data-raw '{"username":"<USERNAME>","password":"<PASSWORD>"}'
```

This returns a JSON response with `accessToken` and `refreshToken`:

```json
{
  "eula": false,
  "scope": ["read"],
  "id": "2473545443652",
  "accessToken": "eyJhbGc...",
  "refreshToken": "YvnTNW..."
}
```

#### Using the accessToken

The `accessToken` is then placed in the `Authorization` header as seen below.
Please ensure it is formatted as `Authorization: Bearer <ACCESS_TOKEN>`.

```bash
curl -X GET 'https://demo3.ipfabric.io/api/v5.0/snapshots' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...'
```

#### Using the refreshToken

To create a new `accessToken` from the `refreshToken`:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/token' \
  -H 'Content-Type: application/json' \
  --data-raw '{"refreshToken":"YvnTNW..."}'
```

Which then returns a new `accessToken` to use in subsequent calls and a new 
`refreshToken` to use for request the next `accessToken`:

```json
{
  "eula": false,
  "scope": ["read"],
  "id": "2473545443652",
  "accessToken": "eyJhbGc...",
  "refreshToken": "bofZw..."
}
```

#### Logout

To logout of IP Fabric:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/logout' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...'
```

### Changing Default Token Expiration

The default token expiration is as follows:

- `accessToken` -- 30 minutes (1800 seconds)
- `refreshToken` -- 24 hours (86400 seconds)

Many company standards requires shorter expiration times and this can be
accomplished via the CLI settings.

--8<-- "snippets/cli_root_access.md"

1. Log into IP Fabric CLI as `osadmin`
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create new file `/opt/nimpee/conf.d/api.json` with the below JSON. In this
   example the `accessToken` expires in 10 minutes and `refreshToken` expires in
   15 minutes:

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

4. Change file permissions `chmod 644 /opt/nimpee/conf.d/api.json`
5. Restart API `systemctl restart nimpee-api.service`

### Token Errors

The API returns an object with a machine-readable error code and a
human-readable error message in response body when an error is encountered:

```json
{
  "code": "API_EXPIRED_API_TOKEN",
  "message": "Expired API Token"
}
```

| Code                      | Message                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API_EXPIRED_API_TOKEN     | The provided API key expired.                                                                                                                                 |
| API_INVALID_API_TOKEN     | The provided API key doesn’t exist. It was removed, or it never existed.                                                                                      |
| API_EXPIRED_ACCESS_TOKEN  | The provided access token (from Authorization header) is expired.                                                                                             |
| API_INVALID_ACCESS_TOKEN  | The provided access token (from Authorization header) is invalid.                                                                                             |
| API_INVALID_REFRESH_TOKEN | The provided refresh token (typically sent in the request body) is revoked (blacklisted) or expired.                                                          |
