# OAuth 2.0 and OpenID Connect

## 1. Objective

Understand modern application authorisation and authentication using OAuth 2.0 and OpenID Connect.

## 2. OAuth 2.0

OAuth 2.0 is an authorisation framework that enables applications to obtain limited access to protected resources without collecting the user's password.

## 3. OAuth Participants

| Participant | Meaning |
|---|---|
| Resource Owner | Owns the protected resource |
| Client | Application requesting access |
| Authorization Server | Issues tokens |
| Resource Server | Hosts protected resources |

Example: Microsoft Entra ID can act as the authorization server, while Microsoft Graph acts as a resource server.

## 4. Authentication vs Authorisation

Authentication verifies identity.

Authorisation determines what resources or actions are permitted.

OAuth 2.0 primarily addresses authorisation.

## 5. Token Types

| Token | Purpose |
|---|---|
| Access Token | Provides access to a protected API |
| ID Token | Provides authentication information to the OIDC client |
| Refresh Token | Used to obtain new tokens when permitted |

Tokens must be protected and validated according to their intended purpose.

## 6. Scopes

Scopes represent requested permissions.

Examples of Microsoft Graph delegated scopes:

- User.Read
- Mail.Read
- Files.Read

Applications should request only the permissions required for their business purpose.

## 7. Delegated vs Application Permissions

**Delegated Permissions**

An application acts on behalf of a signed-in user.

**Application Permissions**

An application acts using its own identity, without a signed-in user.

Application permissions generally require administrator consent.

## 8. Authorization Code Flow

1. User opens the application.
2. Application redirects the browser to the authorization server.
3. User authenticates and provides consent when required.
4. Authorization server returns an authorization code.
5. Application exchanges the code at the token endpoint.
6. Authorization server validates the request.
7. Application receives tokens.

## 9. PKCE

Proof Key for Code Exchange protects the authorization code flow.

It uses a code verifier and code challenge.

PKCE is especially important for public clients such as mobile and single-page applications.

## 10. OpenID Connect

OpenID Connect is an authentication layer built on OAuth 2.0.

It introduces:

- ID tokens
- Standard identity claims
- UserInfo endpoint
- Discovery metadata
- Standard authentication requests

## 11. Important OIDC Claims

| Claim | Meaning |
|---|---|
| sub | Subject identifier |
| iss | Token issuer |
| aud | Intended audience |
| exp | Expiration time |
| iat | Issued-at time |
| email | Email, when supplied |
| name | Name, when supplied |

The application must validate the ID token, including its signature, issuer, audience and expiration.

## 12. OAuth and OIDC Troubleshooting

| Error | Investigation |
|---|---|
| invalid_client | Client ID and credential configuration |
| invalid_scope | Requested scopes and API permissions |
| invalid_grant | Authorization code, redirect URI, PKCE or refresh token |
| invalid_redirect_uri | Redirect URI mismatch |
| 401 Unauthorized | Token validity and authentication |
| 403 Forbidden | Permissions and application authorisation |

## 13. Protocol Comparison

| Protocol | Primary Purpose |
|---|---|
| SAML 2.0 | Federated SSO |
| OAuth 2.0 | Authorisation |
| OpenID Connect | Authentication |

## 14. Practical Limitation

The lab application did not have a working application backend.

OAuth/OIDC concepts and configuration areas were studied, but a complete token-based application login was not implemented.

No client credentials or API permissions were created.

## 15. Conclusion

This lesson covered OAuth 2.0, tokens, scopes, consent, delegated and application permissions, Authorization Code Flow, PKCE and OIDC.
