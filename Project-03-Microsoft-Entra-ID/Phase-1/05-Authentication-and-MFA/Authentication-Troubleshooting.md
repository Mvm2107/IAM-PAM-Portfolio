# Authentication Troubleshooting

## 1. Objective

The objective of this practical exercise was to understand how an IAM Analyst investigates authentication problems using Microsoft Entra ID sign-in logs.

The exercise covered:

- Investigating interactive sign-in events.
- Understanding authentication requirements and results.
- Examining location and device information.
- Reviewing authentication details.
- Understanding Conditional Access and Security Defaults results.
- Distinguishing audit logs from sign-in logs.
- Identifying common authentication error codes.

## 2. Authentication Troubleshooting Workflow

A systematic troubleshooting process helps identify the cause of authentication failures.

### Investigation steps

1. Understand the reported issue.
2. Identify the affected user and application.
3. Open Microsoft Entra ID sign-in logs.
4. Select the appropriate sign-in category.
5. Review the sign-in status and failure reason.
6. Inspect authentication details.
7. Examine device, location and Conditional Access information.
8. Identify the likely cause.
9. Apply an approved corrective action.
10. Verify the result and document the investigation.

## 3. Sign-in Logs

Navigation:

`Microsoft Entra admin center → Entra ID → Monitoring & health → Sign-in logs`

Sign-in log categories include:

- User sign-ins (interactive)
- User sign-ins (non-interactive)
- Service principal sign-ins
- Managed identity sign-ins

### Interactive sign-ins

Interactive sign-ins involve user interaction during authentication, such as entering credentials or responding to an authentication prompt.

### Non-interactive sign-ins

Non-interactive sign-ins generally occur without a user actively entering credentials, such as background token-based authentication.

## 4. Common Authentication Error Codes

| Error code | General meaning |
|---|---|
| 50074 | Strong authentication required |
| 50076 | MFA required due to configuration or policy change |
| 50079 | User needs to register MFA/security information |
| 50126 | Invalid username or password |
| 53003 | Conditional Access blocked the sign-in |

**Important:** Error codes are investigation clues. Always inspect the actual failure reason and authentication details in the sign-in event before deciding on a resolution.

## 5. Practical Exercise – Investigating a Successful Sign-in

### 5.1 Sign-in log selection

Selected:

- Log category: User sign-ins (interactive)
- Date range: Last 7 days
- Application observed: Azure Portal

The displayed records included successful interactive sign-ins.

### 5.2 Basic information

The selected sign-in event showed:

| Field | Observed result |
|---|---|
| Authentication requirement | Single-factor authentication |
| Status | Success |
| Is Agent | No |
| Agent type | Not Agentic |
| Continuous access evaluation | No |
| Additional details | MFA requirement satisfied by claim in the token |

#### Interpretation

The event was recorded as single-factor authentication, while the additional details indicated that an MFA requirement was satisfied by a claim in the token.

This can happen when Entra accepts an existing authentication claim rather than requiring a new MFA challenge during that particular sign-in.

Therefore, this event does not establish that a fresh MFA prompt occurred.

### 5.3 Location information

The location tab displayed:

- Location: Coimbatore, Tamil Nadu, India.
- IP address: Recorded in the sign-in event.
- Autonomous System Number: Recorded in the sign-in event.
- Through Global Secure Access: No.

#### Interpretation

Location and IP information can help an analyst identify unusual access patterns.

However, IP-based location is approximate and should not be treated as definitive proof of a user's physical location.

### 5.4 Device information

| Field | Observed result |
|---|---|
| Browser | Chrome 157.0.0 |
| Operating system | Windows 10 |
| Compliant | No |
| Managed | No |

#### Interpretation

The device was reported as neither compliant nor managed.

This does not automatically indicate that the device is compromised.

If an organization configures Conditional Access to require a compliant or managed device, these attributes may affect whether access is permitted.

### 5.5 Authentication details

The authentication details tab showed:

- Succeeded: Yes
- Authentication method: Previously satisfied
- Result detail: First factor requirement satisfied

#### Interpretation

The authentication details provide additional information about how the authentication requirement was satisfied.

An analyst should inspect this information rather than assuming every successful sign-in involved a new password or MFA challenge.

### 5.6 Conditional Access

The Conditional Access tab displayed:

| Field | Observed result |
|---|---|
| Policy name | Security Defaults |
| Result | Success |

#### Interpretation

Security Defaults were reported as successful for the selected sign-in.

This observation does not mean that a custom Conditional Access policy was configured.

Security Defaults provide baseline identity security protections, including MFA-related protections.

## 6. Audit Logs vs Sign-in Logs

| Audit logs | Sign-in logs |
|---|---|
| Record changes to Entra resources | Record authentication and access attempts |
| Used to investigate administrative activities | Used to investigate authentication activities |
| Example: User account updated | Example: User sign-in failed |
| Example: Group membership changed | Example: MFA requirement encountered |

**Remember:**

- Audit logs answer: What changed?
- Sign-in logs answer: Who attempted to access what, and what happened?

## 7. Common IAM Troubleshooting Scenarios

### Scenario 1 – Authenticator notification not received

Investigation:

1. Confirm that the user has registered the correct device.
2. Check notification permissions.
3. Check internet connectivity.
4. Verify the Microsoft Authenticator application configuration.
5. Follow the organization's approved recovery procedure if necessary.

### Scenario 2 – Repeated MFA prompts

Investigation:

1. Inspect the sign-in logs.
2. Review authentication details.
3. Check session controls and sign-in frequency.
4. Investigate token/session-related issues.

### Scenario 3 – Lost or stolen phone

Investigation:

1. Verify the user's identity.
2. Follow the incident response procedure.
3. Secure the account if compromise is suspected.
4. Revoke sessions when appropriate.
5. Handle the lost authentication method through the approved recovery process.
6. Help the user register a replacement method.

### Scenario 4 – Conditional Access blocks sign-in

Investigation:

1. Open the failed sign-in event.
2. Review the failure reason.
3. Inspect the Conditional Access tab.
4. Identify the policy responsible.
5. Verify the user, application, device and location conditions.
6. Follow the approved remediation process.

## 8. Practical Assessment

**Question:** A sign-in succeeds, but the device shows:

- Compliant: No
- Managed: No

**Correct answer:** The sign-in succeeded, and the device was reported as neither compliant nor managed.

An unmanaged device is not automatically a compromised device.

## 9. Lab Outcome

The following activities were completed:

- Inspected interactive sign-in events.
- Opened an individual sign-in record.
- Reviewed basic sign-in information.
- Examined location information.
- Examined device information.
- Reviewed authentication details.
- Inspected the Conditional Access tab.
- Identified Security Defaults in the event.
- Distinguished audit logs from sign-in logs.
- Completed the practical knowledge check.

**Knowledge assessment:** 6/6 MCQs and 1/1 practical knowledge check.

## 10. Limitations and Observations

- The investigation used a successful sign-in event rather than a deliberately generated authentication failure.
- No Conditional Access configuration was created or modified.
- No authentication methods were changed.
- The device was reported as unmanaged and non-compliant.
- The selected event showed an existing MFA claim in the token; it did not prove that a fresh MFA challenge occurred.
- The Security Defaults result was observed for this event only.
- No remediation action was required for the selected successful sign-in.

## 11. Key Learning Points

1. Sign-in logs are essential for authentication troubleshooting.
2. Audit logs and sign-in logs serve different investigation purposes.
3. Authentication requirement and authentication details must be interpreted together.
4. An unmanaged device is not automatically a compromised device.
5. Conditional Access results help explain access decisions.
6. Error codes provide clues but must be verified against the complete sign-in record.
7. IAM Analysts should follow a systematic investigation and documentation process.

---

**Module:** 05 – Authentication and MFA  
**Lesson:** 05 – Authentication Troubleshooting  
**Practical Environment:** Microsoft Entra ID – Cloud-only tenant  
**Status:** Completed
