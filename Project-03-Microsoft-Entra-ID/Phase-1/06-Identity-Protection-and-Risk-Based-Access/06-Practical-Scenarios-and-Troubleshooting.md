# Practical Scenarios and Troubleshooting

## 1. Overview

This document covers practical identity security scenarios involving Microsoft Entra ID Protection.

The exercises focus on how IAM and SOC Analysts investigate suspicious authentication activity, identify possible account compromise, determine appropriate remediation and document incident findings.

The scenarios are simulated exercises designed to develop practical investigation and decision-making skills.

## 2. Investigation Methodology

A structured investigation methodology helps analysts evaluate identity-related security incidents.

### Investigation Checklist

1. Identify the affected user.
2. Identify the risk detection and risk category.
3. Review the associated sign-in event.
4. Examine the source IP address and location.
5. Inspect device information.
6. Review authentication methods and results.
7. Examine application access.
8. Correlate related audit activity.
9. Determine whether the activity is legitimate or suspicious.
10. Recommend containment and remediation.
11. Verify the outcome.
12. Document the investigation.

## 3. Practical Scenario 1 – Suspicious Sign-in

### Incident Details

**Incident ID:** INC-1001

**User:** Arun Kumar

**Department:** IT Operations

**Situation:**

Arun normally signs in from Chennai using his Windows laptop.

The SOC team receives an alert involving a sign-in from an unfamiliar location.

### Evidence

| Attribute | Observation |
|---|---|
| Sign-in location | Unfamiliar |
| IP address | Anonymous proxy |
| Device | Unfamiliar device |
| Authentication | Successful |
| Sign-in risk | High |
| User risk | Not established |

### Investigation

The analyst should:

1. Verify whether Arun was expected to sign in.
2. Investigate the anonymous IP address.
3. Examine the geographic location.
4. Check whether the device is recognised.
5. Review authentication details.
6. Examine the applications accessed.
7. Correlate relevant audit activity.

### Expected Response

The available evidence is suspicious but should be investigated before concluding that the account is compromised.

If compromise is established, contain access and initiate the approved remediation process.

## 4. Practical Scenario 2 – Leaked Credentials

### Incident Details

**Incident ID:** INC-1002

**User:** Priya Sharma

**Situation:**

Priya's credentials are discovered in a known credential leak.

### Evidence

| Attribute | Observation |
|---|---|
| Detection | Leaked credentials |
| User risk | High |
| Recent sign-in | Successful |
| Device | Previously registered device |
| User confirmation | Not obtained |

### Investigation

1. Review the leaked-credential detection.
2. Examine recent interactive sign-ins.
3. Examine non-interactive sign-ins.
4. Check IP addresses and locations.
5. Review authentication methods.
6. Contact Priya through a verified communication channel.
7. Determine whether the account is compromised.

### Expected Response

If compromise is confirmed:

- Contain access when necessary.
- Secure or reset credentials.
- Revoke sessions as appropriate.
- Investigate application access.
- Verify the account's security.

A known device does not guarantee that an account is safe.

## 5. Practical Scenario 3 – False-Positive Risk Detection

### Incident Details

**Incident ID:** INC-1003

**User:** Arun Kumar

**Situation:**

Atypical travel detection is generated when Arun signs in from Bengaluru after previously signing in from Chennai.

Arun confirms that he is travelling.

### Evidence

| Attribute | Observation |
|---|---|
| Detection | Atypical travel |
| Current location | Bengaluru |
| Previous location | Chennai |
| Device | Known device |
| User confirmation | Confirms travelling |
| Other suspicious activity | None identified in the scenario |

### Investigation

1. Verify the user's travel information.
2. Examine the sign-in details.
3. Check device information.
4. Review authentication evidence.
5. Look for other suspicious activity.

### Expected Response

If the investigation supports legitimate activity, the risk can be dismissed according to the organization's procedures.

The justification should be documented.

Atypical travel alone does not prove malicious activity.

## 6. Practical Scenario 4 – Successful MFA but Suspicious Activity

### Incident Details

**Incident ID:** INC-1004

**User:** Priya Sharma

**Situation:**

A successful authentication occurs from an unfamiliar location and unknown device.

Priya confirms that she did not perform the sign-in.

### Evidence

| Attribute | Observation |
|---|---|
| Sign-in | Successful |
| MFA | Successful |
| IP address | Unfamiliar |
| Device | Unknown |
| User confirmation | Denies the sign-in |
| Application access | Unusual |

### Investigation

Possible explanations include:

- MFA fatigue attacks.
- Adversary-in-the-middle phishing.
- Stolen session tokens.
- Compromised authentication methods.

### Expected Response

1. Treat the event as suspected compromise.
2. Contain access when necessary.
3. Revoke sessions.
4. Secure credentials and authentication methods.
5. Investigate application activity.
6. Review related audit events.
7. Verify the account before restoring access.

Successful MFA does not guarantee that the legitimate user performed the authentication.

## 7. Practical Scenario 5 – Suspicious Account Access

### Incident Details

**Incident ID:** INC-1005

**User:** Arun Kumar

**Application:** Microsoft 365

### Evidence

| Attribute | Observation |
|---|---|
| Location | Unknown country |
| IP address | Anonymous proxy |
| Device | Unregistered |
| Password | Valid |
| MFA | Successful |
| Sign-in | Successful |
| User confirmation | Denies sign-in |
| Application access | Unusual |

### Investigation Outcome

The combination of an anonymous proxy, unfamiliar device, successful authentication, unusual application access and user's denial indicates suspected account compromise.

### Recommended Response

1. Treat the incident as suspected compromise.
2. Contain access through the approved incident-response process.
3. Investigate authentication and session activity.
4. Secure credentials and authentication methods.
5. Revoke sessions as appropriate.
6. Review application access and audit activity.
7. Verify the account's security.

**Note:** This is a simulated incident. No actual compromise, sign-in or remediation was performed in the Entra tenant.

## 8. Troubleshooting Risk-Related Issues

| Issue | Investigation approach |
|---|---|
| Risk remains High after password change | Check whether additional remediation is required |
| Risky sign-in remains visible | Determine whether it is a historical event or a new sign-in |
| Detection appears after sign-in | Consider offline detection processing |
| User risk changes to High | Review associated detections and authentication evidence |
| Risky users displays No Risk | Do not interpret it as a guarantee of security |
| Risky sign-ins returns HTTP 401 | Investigate licensing and authorization restrictions |
| Risk policy impact analysis returns HTTP 401 | Investigate tenant licensing and access restrictions |

## 9. Practical Investigation Documentation

An incident record should contain the following information:

| Field | Description |
|---|---|
| Incident ID | Unique incident reference |
| Affected user | Identity involved |
| Detection | Type of suspicious activity |
| Risk level | Available risk classification |
| Evidence | IP, location, device and authentication information |
| User confirmation | Whether the user recognises the activity |
| Investigation decision | Legitimate, suspicious or confirmed compromise |
| Containment | Actions taken to prevent further access |
| Remediation | Credentials, sessions and authentication actions |
| Verification | Evidence that the issue has been addressed |
| Closure | Incident resolution and approval |

Never record passwords, secret keys, recovery codes or session tokens in incident documentation.

## 10. Practical Environment and Limitations

The practical environment used for this project is a free, cloud-only Microsoft Entra tenant.

The following limitations were observed:

- The Identity Protection dashboard was accessible but displayed no metric data.
- The Risky users page displayed three users, all classified as No Risk.
- The Risky sign-ins page returned HTTP 401.
- The Risk policy impact analysis page returned HTTP 401.
- Full risk detection reporting was not available for independent investigation.
- Risk-based Conditional Access policy creation was restricted by licensing.

The investigation scenarios in this document were simulated learning exercises.

No actual security incident was generated, and no risk confirmation, dismissal, blocking or remediation action was performed.

## 11. Key Learning Outcomes

This exercise developed an understanding of:

- Suspicious sign-in investigation.
- Leaked-credential incidents.
- False-positive analysis.
- MFA-related attack scenarios.
- Session revocation.
- Account containment.
- Risk-state troubleshooting.
- Evidence-based incident documentation.
- Practical limitations of a free Entra tenant.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Topic: Practical Scenarios and Troubleshooting*
