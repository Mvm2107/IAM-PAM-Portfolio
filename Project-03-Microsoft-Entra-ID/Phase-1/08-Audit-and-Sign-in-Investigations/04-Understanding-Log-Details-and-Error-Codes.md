# Lesson 4 – Understanding Log Details and Error Codes

## 1. Objective

Understand common Microsoft Entra authentication error codes and learn how to use them when troubleshooting sign-in failures.

## 2. What is an Authentication Error Code?

Microsoft Entra ID records error information when an authentication or access operation fails or is interrupted.

An error code helps identify the reported problem.

However, an error code should not be interpreted in isolation. The analyst should also examine:

- Failure reason
- Authentication details
- Conditional Access results
- User and application information
- Device information
- Related sign-in activity

## 3. Common Microsoft Entra Error Codes

| Error code | General meaning | Initial investigation |
|---|---|---|
| 50034 | User account not found | Verify username and tenant |
| 50053 | Account locked or sign-in blocked due to suspicious activity, depending on the underlying reason | Examine the detailed failure reason |
| 50055 | Password expired | Follow approved password-reset procedures |
| 50056 | Invalid or inactive password | Verify credentials and account state |
| 50057 | User account disabled | Verify account status and lifecycle |
| 50058 | User is not signed in or an SSO session is unavailable | Examine the authentication session |
| 50074 | Strong authentication required | Complete required MFA |
| 50076 | MFA required due to configuration or policy change | Verify the MFA requirement |
| 50079 | User must register security information | Complete required registration |
| 50126 | Invalid username or password | Verify credentials and investigate repeated failures |
| 53000 | Device is not compliant | Examine device compliance |
| 53001 | Device is not domain joined | Examine device requirements |
| 53003 | Access blocked by Conditional Access | Inspect policy evaluation |
| 500121 | MFA challenge was not successfully completed | Investigate the MFA interaction |
| 700082 | Refresh token expired due to inactivity | Reauthenticate and obtain fresh tokens |

**Important:** The exact failure reason and context determine the appropriate response. In particular, error 50053 can have different underlying causes.

## 4. Sign-in Troubleshooting Workflow

### Step 1 – Identify the user

Verify the account and tenant.

### Step 2 – Identify the application

Determine which application and resource were involved.

### Step 3 – Examine the error code

Read the error code together with the detailed failure reason.

### Step 4 – Inspect authentication details

Review authentication methods, MFA requirements and authentication results.

### Step 5 – Inspect Conditional Access

Identify whether a policy blocked or interrupted access.

### Step 6 – Examine device and location

Review device management, compliance, IP address and approximate location.

### Step 7 – Recommend remediation

Use the least disruptive action appropriate to the evidence and organisation's procedures.

## 5. Simulated Troubleshooting Scenarios

These scenarios were used for training. They were not actual failed sign-in events from the tenant.

### Scenario A – Invalid Credentials

Error code: 50126

Possible cause: The supplied username or password was not accepted.

Recommended investigation:

- Verify the username.
- Examine the failure history.
- Check the account state.
- Investigate repeated attempts.
- Follow the approved password-reset process when appropriate.

### Scenario B – MFA Requirement

Error code: 50076

Possible cause: MFA is required due to a policy or configuration change.

Recommended investigation:

- Verify the authentication requirement.
- Inspect the applicable policy.
- Help the user complete the required authentication.

### Scenario C – Conditional Access Block

Error code: 53003

Possible cause: A Conditional Access evaluation blocked access.

Recommended investigation:

- Inspect the policy result.
- Identify applicable grant controls.
- Examine device conditions.
- Review the failure details.
- Follow approved policy remediation procedures.

### Scenario D – Refresh Token Expiry

Error code: 700082

Possible cause: Refresh token expired due to inactivity.

Recommended investigation:

- Verify the failure reason.
- Inspect the authentication history.
- Determine whether reauthentication is required.

## 6. Important Learning Points

- Error codes identify reported authentication problems.
- Error codes must be interpreted with their failure reasons.
- MFA-related errors have different meanings.
- Conditional Access failures require policy investigation.
- A failed sign-in does not automatically indicate compromise.
- Avoid disruptive remediation before establishing the cause.

## 7. References

- Microsoft Entra authentication error codes: https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes
- Microsoft Entra Conditional Access troubleshooting: https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access

## 8. Conclusion

This lesson introduced common Microsoft Entra authentication error codes and a structured troubleshooting approach.

The simulated cases provided practice in identifying likely causes and recommending appropriate investigation steps without creating artificial failures in the tenant.
