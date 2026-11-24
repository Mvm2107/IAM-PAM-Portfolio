# Single Sign-On and SAML Authentication

## 1. Objective

Understand Single Sign-On, Identity Providers, Service Providers and SAML 2.0 authentication.

## 2. Single Sign-On

Single Sign-On (SSO) allows users to access multiple connected applications using an established authentication experience.

### Main Components

**Identity Provider (IdP)**

Authenticates the user and provides identity information.

Example: Microsoft Entra ID.

**Service Provider (SP)**

The application the user wants to access.

Examples: Salesforce, ServiceNow and Workday.

## 3. SSO Initiation Methods

### SP-Initiated SSO

1. User opens the application.
2. Application redirects the browser to the IdP.
3. IdP authenticates the user.
4. IdP returns an authentication response.
5. Application validates the response.
6. Application establishes a session.

### IdP-Initiated SSO

1. User signs in to the Identity Provider.
2. User opens the application from the IdP portal.
3. IdP sends an authentication response.
4. Application validates the response.
5. Application establishes a session.

## 4. SAML 2.0

Security Assertion Markup Language (SAML) is an XML-based standard used to exchange authentication and identity information between an IdP and SP.

## 5. SAML Authentication Flow

1. User opens the Service Provider.
2. SP sends an AuthnRequest.
3. IdP authenticates the user.
4. IdP creates a SAML Response containing an assertion.
5. Browser sends the response to the SP's ACS endpoint.
6. SP validates the response.
7. Application establishes a session if validation and authorisation succeed.

## 6. Important SAML Components

| Component | Purpose |
|---|---|
| Entity ID | Identifies the Service Provider |
| ACS URL | Receives the SAML response |
| Name ID | Identifies the user in the assertion |
| SAML Assertion | Contains identity and authentication statements |
| Signing Certificate | Enables the SP to validate the signature |

## 7. Signing Certificate

The Identity Provider signs the SAML response or assertion using its private signing key.

The Service Provider uses the trusted public certificate to validate the signature.

Private signing keys must never be shared publicly.

## 8. Common SAML Troubleshooting

| Symptom | Investigation |
|---|---|
| Invalid audience | Entity ID and audience configuration |
| Invalid reply URL | ACS URL configuration |
| Invalid signature | Signing certificate and signature validation |
| User not recognised | Name ID and attribute mapping |
| Expired assertion | Assertion validity timestamps |
| Authentication succeeds but access is denied | Application assignment and application-side authorisation |

## 9. SAML vs Password Synchronisation

SAML provides federated authentication and SSO.

Password synchronisation synchronises password information between identity systems.

They are different identity mechanisms.

## 10. Practical Limitation

The lab application `IAM-Lab-Test-App` did not have a configured external Service Provider or working SAML backend.

Therefore, the SAML flow was studied theoretically. An end-to-end SAML login was not performed.

## 11. Conclusion

This lesson covered SSO architecture, initiation methods, SAML authentication flow, assertions, identifiers, ACS URLs and signing certificates.
