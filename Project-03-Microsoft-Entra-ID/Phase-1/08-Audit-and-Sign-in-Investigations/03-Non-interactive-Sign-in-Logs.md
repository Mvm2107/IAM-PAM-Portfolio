# Lesson 3 – Non-interactive Sign-in Logs

## 1. Objective

Understand non-interactive authentication and investigate background authentication activity in Microsoft Entra ID.

## 2. What are Non-interactive Sign-ins?

A non-interactive sign-in occurs when an application or client performs authentication without requiring the user to actively enter credentials or respond to an authentication prompt at that moment.

Examples include:

- Background token acquisition.
- Refresh-token requests.
- Application authentication on behalf of a user.
- Silent authentication using an existing session.

Non-interactive sign-ins are not limited to refresh-token operations.

## 3. Access Tokens and Refresh Tokens

### Access Token

An access token is issued by Microsoft Entra ID and allows an application to access a particular resource, subject to the token's permissions and claims.

### Refresh Token

A refresh token allows an application to request new access tokens without requiring the user to repeat the entire interactive authentication process, subject to token validity and applicable policies.

Access tokens and refresh tokens have different purposes and security properties.

## 4. Interactive vs Non-interactive Sign-ins

| Feature | Interactive | Non-interactive |
|---|---|---|
| User participation | Active | Usually background |
| Credential entry | May be required | Usually not repeated |
| MFA prompt | May appear | May use existing authentication claims |
| Example | Browser login | Background token acquisition |

## 5. Practical Investigation

An actual successful non-interactive sign-in was inspected.

### Basic Information

| Field | Observed value |
|---|---|
| Date | 25 November 2026 |
| Time | 14:28:40 UTC |
| Status | Success |
| Application | Mobility Management Policy Service |
| Resource | Windows Azure Active Directory |
| Client app | Browser |
| Authentication requirement | Single-factor authentication |
| Client credential type | Federated identity credential |
| Token issuer type | Microsoft Entra ID |
| User type | Member |
| Latency | 128 ms |

## 6. Federated Identity Credential

A Federated Identity Credential enables an application or workload to establish trust with Microsoft Entra ID through an external identity provider.

It can eliminate the need to store long-lived client secrets for supported workload identity scenarios.

Example:

1. A workload requests an identity token from a trusted external identity provider.
2. The workload presents the token to Microsoft Entra ID.
3. Entra validates the configured federation relationship.
4. Entra may issue an access token for the requested resource.

### Practical Observation

The inspected sign-in record displayed:

`Client credential type: Federated identity credential`

This identifies the credential type recorded for the sign-in.

It does not independently prove that a particular GitHub Actions or other external workload authentication flow occurred.

A federated identity credential should not be confused with a refresh token.

## 7. Authentication Details

The inspected Authentication Details tab displayed:

`No authentication events were triggered as part of the authentication.`

The Basic Information tab also displayed:

`MFA requirement satisfied by claim in the token`

These observations indicate that the record did not contain individual authentication-step events and recognised an existing MFA-related token claim.

They do not establish that a fresh MFA challenge occurred.

## 8. Location Investigation

| Field | Observation |
|---|---|
| Location | Coimbatore, Tamil Nadu, India |
| Network | IPv6 |
| ASN | 55836 |
| Global Secure Access | No |

IP-based location is approximate.

## 9. Device Investigation

| Field | Observed value |
|---|---|
| Browser/client | Rich Client 4.90.0.0 |
| Operating system | Windows |
| Managed | No |
| Compliant | No |
| Join type | Not displayed |

## 10. Conditional Access

The inspected sign-in record showed:

| Policy | Result |
|---|---|
| Security Defaults | Success |

## 11. Failed Non-interactive Sign-ins

The non-interactive sign-in logs were filtered for failures over the selected seven-day period.

Observation:

No failed non-interactive sign-in records were available under the selected filter and time range.

A simulated refresh-token failure scenario was used for learning.

## 12. Simulated Troubleshooting Scenario

Error code: `700082`

Scenario: An employee reports repeated background authentication failures.

Training interpretation: The refresh token expired due to inactivity.

Recommended investigation:

- Verify the error code and failure details.
- Examine the authentication history.
- Determine whether reauthentication is required.
- Confirm that the user can obtain fresh tokens.

This was a simulated exercise, not an actual tenant event.

## 13. Important Learning Points

- Non-interactive sign-ins can involve user identities.
- Not every non-interactive sign-in is a refresh-token operation.
- Existing token claims can satisfy authentication requirements.
- Federated identity credentials are different from refresh tokens.
- Successful background authentication does not automatically prove legitimacy.
- Repeated authentication failures require examination of the underlying reason and pattern.

## 14. Conclusion

This lesson provided practical exposure to non-interactive sign-in records and introduced workload federation concepts.

The investigation demonstrated how to inspect authentication, application, resource, location, device and Conditional Access information while distinguishing observed evidence from theoretical authentication flows.
