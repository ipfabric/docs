# Authentication

IP Fabric accepts 3 different methods of Authentication:

* [API Token](#api-token)
* [Basic Authentication](#basic-authentication)
* [Token Authentication](#token-authentication)

## API Token

Majority of API calls need to be authenticated. API Token needs to be passed as
a request header. Please see [API Tokens](../IP_Fabric_Settings/api_tokens.md)
on how to create an API Token in the UI.

```http
Content-Type: application/json
X-API-Token: YOUR_API_TOKEN_GENERATED_VIA_IPFABRIC_UI
```

## Basic Authentication

Using Basic Authentication requires Base64 encoding `username:password` and
passing that into the `Authorization` header.

```bash
osadmin@ipfabric:~$ echo -n "username:password" | base64
dXNlcm5hbWU6cGFzc3dvcmQ=
osadmin@ipfabric:~$ curl -X GET 'https://demo3.ipfabric.io/api/v5.0/snapshots' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=' 
```

## Token Authentication

Token Authentication allows a user to submit their Username and Password to the 
`login` endpoint which then returns a JSON Web Token (JWT) for them to use in 
the `Authorization` header.

### Types of Tokens

#### Access Token

An access token is JSON Web Token (JWT) as per RFC-7519 signed using SHA-256
with RSA encryption.

The token expires in 30 minutes since being generated and it can’t be revoked
during its lifetime. It consists of three parts separated by dots:

* Header
* Payload
* Signature

The payload contains an object with the following fields:

* ID - User ID
* EULA - A boolean value whether a user approved EULA or not
* EXP - Token expiration time (in seconds since Unix epoch)
* IAT - Token issued time (in seconds since Unix epoch)
* Scope - Array of strings representing granted user access
* Username - String

#### Refresh Token

A refresh token is a token that can be used to obtain a renewed access token.
It can be requested for new access tokens until the refresh token is revoked
(blacklisted) or expired.

!!! warning "Refresh Tokens"

    **A refresh token expires after 24 hours of not being used for generation
    of a new access token. Refresh tokens must be stored securely by an 
    application because they essentially allow a user to 
    remain authenticated forever.**

### Login

To login and obtain an Access and Refresh token please see the below curl
example:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/login' \
  -H 'Content-Type: application/json' \
  --data-raw '{"username":"<USERNAME>","password":"<PASSWORD>"}'
```

This returns a JSON response with `accessToken` and `refreshToken`:

```json
{
  "accessToken": "eyJhbGc...",
  "refreshToken": "YvnTNW..."
}
```

### Using the accessToken

The `accessToken` is then placed in the `Authorization` header as seen below.
Please ensure it is formatted as `Authorization: Bearer <ACCESS_TOKEN>`.

```bash
curl -X GET 'https://demo3.ipfabric.io/api/v5.0/snapshots' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...' 
```

### Using the refreshToken

To create a new `accessToken` from the `refreshToken`:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/token' \
  -H 'Content-Type: application/json' \
  --data-raw '{"refreshToken":"YvnTNW..."}'
```

Which then returns a new `accessToken` to use in subsequent calls:

```json
{
  "accessToken": "eyJhbGciOi..."
}
```

### Logout

To logout of IP Fabric:

```bash
curl -X POST 'https://demo3.ipfabric.io/api/v5.0/auth/logout' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGc...' 
```

## Changing Default Token Expiration

The default token expiration is as follows:

* accessToken - 30 minutes (1800 seconds)
* refreshToken - 24 hours (86400 seconds)

If the user does any action in the web GUI or requests a new access token
using the API within a 24-hour period IP Fabric will keep the user logged in,
create a new `accessToken`, and reset the `refreshToken` expiration timer for
another 24 hours.

Many company standards requires shorter expiration times and this can be
accomplished via the CLI settings.

!!! warning "CLI Root Access"

    Any action on the CLI as a `root` and/or `autoboss` user may severely 
    damage the product and/or the system itself. Such actions taken without 
    direct communication with the IP Fabric Support or Solution Architect 
    teams can render the system unusable.

!!! warning "SSO Configuration"

    If you previosuly enabled SSO please only edit the `expiresIn` settings of 
    the `/opt/nimpee/conf.d/api.json` file.

1. Log into IP Fabric CLI as `osadmin`
2. Elevate to root using `sudo -s` and `osadmin` password.
3. Create new file `/opt/nimpee/conf.d/api.json` with the below JSON
    1. In this example the `accessToken` expires in 10 minutes and `refreshToken` expires in 15 minutes.
```json
{
  "app": {
    "port": 8100,
    "url": "https://localhost/api",
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

## Token Errors

The API returns an object with a machine-readable error code and a
human-readable error message in response body when an error is encountered:

```json
{
  "code": "API_NOT_FOUND",
  "message": "Requested Resource Not Found"
}
```

COMMON ERRORS:

* API_EXPIRED_API_TOKEN - The provided API key expired.
* API_INVALID_API_TOKEN - The provided API key doesn’t exist. It was removed, or
  it never existed.
* API_MISSING_EULA_APPROVAL - This error occurs when a user hasn’t approved
  EULA. It is REQUIRED to login using the user’s credentials into the
  application user interface and accept EULA.
* API_EXPIRED_ACCESS_TOKEN - The provided access token (from Authorization
  header) is expired.
* API_INVALID_ACCESS_TOKEN - The provided access token (from Authorization
  header) is invalid.
* API_INVALID_REFRESH_TOKEN - The provided refresh token (typically sent in the
  request body) is revoked (blacklisted) or expired.
* API_NOT_FOUND - The requested resource does not exist.
