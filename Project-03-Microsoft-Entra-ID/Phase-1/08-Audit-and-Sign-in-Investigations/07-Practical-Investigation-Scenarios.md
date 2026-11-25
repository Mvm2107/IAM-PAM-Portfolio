# Lesson 7 – Practical IAM Investigation Scenarios

## 1. Objective

Apply Microsoft Entra monitoring and investigation concepts to realistic IAM incidents.

The purpose is to develop the ability to:

- Identify relevant evidence.
- Analyse authentication and access.
- Assess potential security risks.
- Recommend appropriate remediation.
- Document investigation conclusions.

## 2. Investigation Framework

The following workflow was used:

1. Incident identification.
2. Evidence collection.
3. Technical analysis.
4. Risk assessment.
5. Recommended remediation.
6. Investigation documentation.

## 3. Incident INC-1014 – Employee Unable to Access an Application

**Scenario:** An employee reports that they could access an application yesterday but cannot access it today.

### Simulated Evidence

| Field | Value |
|---|---|
| User | Arun Kumar |
| Application | IAM-Lab-Test-App |
| Sign-in result | Failure |
| Error code | 53003 |
| Conditional Access | Blocked |
| Device | Unmanaged |
| Location | Usual location |

### Investigation

The sign-in indicates a Conditional Access block.

The device is reported as unmanaged.

The investigation should examine:

- Conditional Access policy evaluation.
- Grant controls.
- Device requirements.
- Application access requirements.
- Failure details.

### Recommended Action

Identify the policy condition responsible for the block and follow approved access-policy remediation procedures.

Do not reset the password without evidence of a credential problem.

## 4. Incident INC-1015 – Suspicious Successful Sign-in

**Scenario:** The security team reports a successful sign-in from an unfamiliar country.

### Simulated Evidence

| Field | Value |
|---|---|
| User | Priya Sharma |
| Sign-in type | Interactive |
| Application | Microsoft 365 |
| Result | Success |
| Location | Unfamiliar country |
| Device | Unknown device |
| Authentication | MFA satisfied |
| User confirmation | Employee denies activity |

### Investigation

The combination of an unfamiliar location, unknown device and employee denial warrants further investigation.

Possible explanations include:

- Compromised credentials.
- Stolen session or token.
- MFA abuse.
- Inaccurate location attribution.

### Recommended Action

- Investigate related authentication activity.
- Verify the employee's account activity.
- Examine device, location and authentication details.
- Escalate suspected compromise.
- Follow approved containment procedures.

Successful MFA does not independently prove legitimate access.

## 5. Incident INC-1016 – Privileged Role Assignment

**Scenario:** A user is unexpectedly assigned the Global Administrator role.

### Simulated Evidence

| Field | Value |
|---|---|
| Activity | Add member to role |
| Target | Employee account |
| Assigned role | Global Administrator |
| Initiator | Application |
| Result | Success |
| Change approval | Not found in supplied evidence |

### Investigation

The event represents a high-impact privileged identity change.

The analyst should:

1. Identify the initiating application.
2. Verify the target user.
3. Confirm the assigned role.
4. Examine Modified Properties.
5. Check whether the operation was authorised.
6. Escalate if the assignment cannot be explained.

### Recommended Action

Validate the application initiator, assignment approval and affected identity.

If the assignment is unexplained, escalate through the organisation's privileged-access incident procedures.

Do not automatically assume that an application-initiated role assignment is legitimate.

## 6. Investigation Documentation Template

For future IAM investigations, use the following structure:

### Incident Information

- Incident ID:
- Date and time:
- Affected user:
- Application:
- Incident type:

### Evidence

- Audit Log events:
- Sign-in Log events:
- Authentication result:
- Error code:
- IP address and location:
- Device information:
- Conditional Access result:

### Analysis

- What happened?
- Who initiated the action?
- Which identity or application was affected?
- What evidence supports the conclusion?
- What information is still missing?

### Risk Assessment

- Expected activity
- Configuration issue
- Suspicious activity
- Insufficient evidence

### Recommended Action

- Verify
- Monitor
- Remediate
- Escalate

### Conclusion

Document the findings without claiming compromise or authorisation unless the evidence supports that conclusion.

## 7. Important Learning Points

- Investigate access failures using policy and authentication details.
- Successful sign-ins may still require security investigation.
- Privileged role assignments require careful validation.
- User denial is important evidence but should be combined with technical findings.
- Use appropriate escalation and containment procedures.
- Document evidence, limitations and conclusions separately.

## 8. Conclusion

This lesson brought together the concepts from Module 8 through three simulated IAM incidents involving application access, suspicious authentication and privileged role assignment.

The exercises developed a structured approach to investigating identity-related security events and documenting findings.

These incidents were training scenarios and were not actual events performed in the Microsoft Entra tenant.
