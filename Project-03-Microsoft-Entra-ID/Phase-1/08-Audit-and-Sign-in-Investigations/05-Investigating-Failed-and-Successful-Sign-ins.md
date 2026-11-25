# Lesson 5 – Investigating Failed and Successful Sign-ins

## 1. Objective

Develop a structured approach to investigating successful and failed authentication attempts in Microsoft Entra ID.

## 2. Why Sign-in Investigation Matters

IAM Analysts investigate authentication activity to identify:

- Repeated failed authentication attempts.
- Unexpected successful sign-ins.
- Unfamiliar locations and devices.
- MFA-related issues.
- Application access problems.
- Potential account compromise.

A successful sign-in is not automatically legitimate, and a failed sign-in is not automatically malicious.

## 3. Standard Investigation Workflow

1. Identify the user and affected account.
2. Determine the sign-in type.
3. Examine the application and resource.
4. Check the authentication result.
5. Review the error code and failure reason.
6. Examine IP address and location.
7. Inspect device information.
8. Review authentication and Conditional Access details.
9. Correlate related activity.
10. Document findings and recommend appropriate actions.

## 4. Investigation Pattern A – Repeated Failed Sign-ins

### Simulated Incident: INC-1011

An employee reports that their account is temporarily blocked.

| Field | Simulated observation |
|---|---|
| Sign-in type | Interactive |
| Application | Microsoft 365 |
| Status | Failure |
| Error code | 50126 |
| Attempts | 18 attempts in 10 minutes |
| Source IP | Same unfamiliar IP |
| Location | Outside employee's usual region |
| Authentication | Invalid username or password |

### Investigation

Repeated failed attempts from an unfamiliar IP require further examination.

Possible explanations:

- Employee repeatedly entering an incorrect password.
- Automated password-guessing activity.
- Password spraying or another credential attack.

The available simulated evidence does not establish which explanation is correct.

### Recommended Actions

- Verify the employee's activity.
- Examine other affected accounts.
- Investigate the source IP and attempt pattern.
- Check account protection and lockout information.
- Escalate suspected credential attacks.
- Follow approved containment procedures when compromise is suspected.

## 5. Investigation Pattern B – Successful Sign-in from an Unfamiliar Location

### Simulated Incident: INC-1012

The employee receives a notification about a successful sign-in from an unfamiliar country.

| Field | Simulated observation |
|---|---|
| Sign-in type | Interactive |
| Application | Azure Portal |
| Status | Success |
| Location | Unfamiliar country |
| Device | Unknown Windows device |
| Authentication | MFA satisfied |
| Conditional Access | Success |

### Investigation

Possible explanations:

- Legitimate travel.
- VPN or proxy usage.
- Incorrect location attribution.
- Compromised credentials.
- Stolen session or authentication token.

Successful MFA does not independently establish that the sign-in was legitimate.

### Recommended Actions

1. Verify the activity with the employee through an approved channel.
2. Compare the location and IP with normal activity.
3. Inspect device and authentication details.
4. Examine related sign-ins and audit events.
5. Escalate if the user denies the activity or evidence indicates compromise.

## 6. Investigation Conclusion

For each incident, document:

- Incident identifier.
- Affected user.
- Application.
- Sign-in type.
- Authentication result.
- Error code, if available.
- IP address and location.
- Device information.
- Authentication details.
- Conditional Access result.
- Investigation findings.
- Recommended action.

## 7. Important Learning Points

- Investigate patterns rather than isolated fields.
- Successful MFA does not guarantee legitimate activity.
- Unfamiliar location alone is not proof of compromise.
- Repeated failures deserve further investigation.
- User confirmation is useful but should be combined with technical evidence.
- Escalate incidents based on the evidence and organisation's procedures.

## 8. Conclusion

This lesson combined the previous modules' knowledge to investigate repeated failed authentication attempts and successful sign-ins that may require further examination.

The scenarios were simulated training incidents and were not actual tenant events.
