# Lesson 2 – Interactive Sign-in Logs

## 1. Objective

Understand interactive user sign-ins and investigate authentication activity using Microsoft Entra Sign-in Logs.

## 2. What are Interactive Sign-ins?

An interactive sign-in occurs when a user actively participates in an authentication process.

Examples:

- Entering credentials in a browser.
- Signing in to the Azure Portal.
- Completing an MFA prompt.
- Signing in to a Microsoft 365 application.

## 3. Important Sign-in Fields

| Field | Description |
|---|---|
| Date | Time of the authentication attempt |
| User | Account involved |
| Application | Application accessed |
| Resource | Service being accessed |
| Status | Success, failure or interruption |
| IP address | Source network address |
| Location | Approximate geographic location |
| Client app | Browser or other client |
| Authentication requirement | Single-factor or multifactor |
| Correlation ID | Identifier useful for tracing activity |

## 4. Practical Investigation – Azure Portal Sign-in

An actual successful interactive sign-in was inspected in the tenant.

### Basic Information

| Field | Observed value |
|---|---|
| Date | 25 November 2026 |
| Time | 14:28:22 UTC |
| Application | Azure Portal |
| Resource | Azure Resource Manager |
| Client app | Browser |
| Status | Success |
| Authentication requirement | Single-factor authentication |
| Is Agent | No |
| Continuous Access Evaluation | No |

The application and resource are different:

- Azure Portal is the application accessed.
- Azure Resource Manager is the resource requested.

### Authentication Details

The inspected record showed:

- Authentication requirement: Single-factor authentication.
- Additional details: MFA requirement satisfied by claim in the token.
- Authentication method: Previously satisfied.
- Succeeded: Yes.
- Result detail: First factor requirement satisfied.

### Interpretation

The event recognised an existing MFA-related claim in the authentication token.

It does not establish that the user received a fresh MFA prompt during this particular sign-in.

## 5. Location Investigation

The Location tab showed:

| Field | Observation |
|---|---|
| Location | Coimbatore, Tamil Nadu, India |
| Network | IPv6 |
| ASN | 55836 |
| Global Secure Access | No |

IP-based location is approximate and does not prove the user's physical location.

ASN stands for Autonomous System Number and identifies an autonomous network system responsible for routing internet traffic.

## 6. Device Investigation

| Field | Observed value |
|---|---|
| Browser | Chrome 158.0.0 |
| Operating system | Windows 10 |
| Compliant | No |
| Managed | No |
| Device ID | Redacted in documentation |
| Join type | Not displayed |

### Interpretation

The device was reported as unmanaged and non-compliant in this sign-in record.

This alone does not prove that the device was compromised or personally owned.

## 7. Conditional Access

The inspected record displayed:

| Policy | Result |
|---|---|
| Security Defaults | Success |

This records a successful Security Defaults evaluation for the selected sign-in.

It does not prove that every possible security control was evaluated.

## 8. Failed Sign-in Investigation

The interactive sign-in logs were filtered for failures over the selected seven-day period.

Observation:

No failed interactive sign-in records were available under the selected filter and time range.

This does not establish that no failed authentication attempts have ever occurred in the tenant.

A simulated failure scenario was used separately for learning.

## 9. Important Learning Points

- Successful authentication does not automatically prove legitimacy.
- Existing MFA claims are different from a fresh MFA challenge.
- Device compliance and management are separate attributes.
- IP-based locations are approximate.
- Application and resource fields have different meanings.
- Investigate the full sign-in context before reaching a conclusion.

## 10. Conclusion

This practical exercise demonstrated how to inspect a successful Azure Portal interactive sign-in and understand its authentication, location, device and Conditional Access information.

The available evidence showed a successful authentication but did not independently establish that all aspects of the activity were risk-free.
