# Identity Protection Fundamentals

## 1. Overview

Microsoft Entra ID Protection is an identity security capability that helps organizations detect, investigate and remediate identity-related risks.

It analyses identity-related signals and identifies potentially suspicious authentication activities or compromised accounts.

Identity Protection helps security and IAM teams identify potential threats before they result in further unauthorized access.

## 2. Objectives

The objectives of this module are:

- Understand Microsoft Entra ID Protection.
- Understand identity-related security risks.
- Differentiate user risk and sign-in risk.
- Understand risk levels and detection examples.
- Learn the identity risk investigation workflow.
- Understand the relationship between detection, investigation and remediation.

## 3. Core Activities of Identity Protection

Identity Protection involves three main activities.

### 3.1 Detection

Detection identifies suspicious identity activity using available signals and detection mechanisms.

Examples:

- Sign-in from an anonymous IP address.
- Credentials discovered in a known data leak.
- Atypical travel patterns.
- Suspicious authentication behaviour.
- Potentially compromised session tokens.

### 3.2 Investigation

Investigation involves analysing the available evidence to determine whether an identity-related event is legitimate or suspicious.

An IAM Analyst may examine:

- User identity.
- Sign-in history.
- IP address.
- Geographic location.
- Device information.
- Authentication methods.
- Sign-in result.
- Related audit activity.

### 3.3 Remediation

Remediation involves taking appropriate action to address identified identity risks.

Possible actions include:

- Secure password change.
- Password reset.
- Session revocation.
- Blocking sign-in.
- Requiring reauthentication.
- Confirming or dismissing risk after investigation.

## 4. Types of Identity Risk

Microsoft Entra ID Protection primarily evaluates two important categories of identity risk.

### 4.1 User Risk

User risk represents the probability that a user's identity or account has been compromised.

Example:

An employee's password is discovered in a known credential leak.

This may indicate that an attacker has obtained the employee's credentials.

Possible investigation steps:

1. Identify the affected user.
2. Review associated risk detections.
3. Examine recent sign-in activity.
4. Verify suspicious authentication events.
5. Determine whether the account is compromised.
6. Initiate appropriate remediation.

### 4.2 Sign-in Risk

Sign-in risk represents the probability that a particular authentication request is not coming from the legitimate user.

Example:

An employee attempts to sign in through an anonymous proxy using an unfamiliar device.

The authentication request may be considered suspicious.

Possible investigation steps:

1. Identify the sign-in event.
2. Examine the source IP address.
3. Review geographic location.
4. Inspect device information.
5. Review authentication details.
6. Determine whether the sign-in is legitimate.

## 5. Risk Levels

Identity Protection uses different risk levels to represent the assessed level of identity risk.

| Risk level | Meaning |
|---|---|
| None | No risk has been assigned or identified for the assessment |
| Low | Lower assessed risk |
| Medium | Moderate assessed risk |
| High | Significant assessed risk |

**Important:** A risk level of None does not guarantee that an account is completely secure.

Risk levels should always be interpreted alongside the available evidence.

## 6. Examples of Risk Detections

Some examples of identity-related risk detections include:

| Detection | Description |
|---|---|
| Anonymous IP address | Authentication attempt from an anonymising service |
| Atypical travel | Geographically unusual sign-ins within a short period |
| Leaked credentials | Credentials discovered in a known leak |
| Password spray | Attempts to guess passwords across multiple accounts |
| Suspicious MFA approval | Potentially malicious or manipulated MFA approval |
| Anomalous token | Potentially suspicious authentication token characteristics |

Detection availability depends on the Microsoft Entra licensing level and the applicable detection capabilities.

Not every detection is available in every tenant.

## 7. Identity Protection Investigation Workflow

A structured investigation workflow helps IAM and SOC teams handle identity-related incidents.

1. Identify the affected user.
2. Identify the risk type.
3. Review the associated detection.
4. Examine sign-in evidence.
5. Review IP address, location and device information.
6. Examine authentication details.
7. Determine whether the activity is legitimate or suspicious.
8. Perform appropriate remediation through the approved process.
9. Verify the result.
10. Document the investigation and actions.

## 8. Important Concepts

### Detection vs Investigation vs Remediation

| Activity | Purpose |
|---|---|
| Detection | Identifies suspicious activity |
| Investigation | Analyses evidence |
| Remediation | Addresses the identified risk |

### User Risk vs Sign-in Risk

| Comparison | User Risk | Sign-in Risk |
|---|---|---|
| Focus | User account | Authentication request |
| Main concern | Possible account compromise | Possible fraudulent sign-in |
| Example | Leaked credentials | Anonymous proxy |
| Scope | Identity | Individual sign-in |

## 9. Licensing Considerations

Microsoft Entra ID Protection has licensing-dependent capabilities.

The full Identity Protection experience, including advanced risk reporting and risk-based Conditional Access, requires eligible premium licensing such as Microsoft Entra ID P2 or Microsoft Entra Suite.

A free tenant may expose limited information but does not provide the complete premium risk investigation and policy functionality.

This project uses a free cloud-only Entra tenant. Therefore, some practical exercises are limited to portal inspection and simulated investigation scenarios.

No paid licence or upgrade was used.

## 10. Learning Outcome

After completing this lesson, the following concepts were understood:

- Microsoft Entra ID Protection.
- Detection, investigation and remediation.
- User risk and sign-in risk.
- Risk levels.
- Common identity risk detection examples.
- Identity investigation workflow.
- Licensing-dependent capabilities.

**Assessment Result:** 5/5

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Lesson: Identity Protection Fundamentals*
