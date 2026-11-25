# User Risk and Sign-in Risk

## 1. Overview

Microsoft Entra ID Protection evaluates identity-related risks using two important categories:

1. User Risk
2. Sign-in Risk

Understanding the difference between these categories is essential for IAM Analysts and SOC Analysts because they represent different types of security concerns.

User risk focuses on the possibility that an account has been compromised, whereas sign-in risk focuses on the possibility that a particular authentication request is not from the legitimate user.

## 2. User Risk

User risk represents the probability that a user's identity or account has been compromised.

It focuses on the security of the user's identity rather than an individual authentication request.

### Example: Leaked Credentials

An employee named Arun uses Microsoft Entra ID to access organizational applications.

His credentials are discovered in a known data leak.

This creates a potential account compromise concern because an attacker may have obtained his username and password.

### Investigation Steps

1. Identify the affected user.
2. Review the associated user risk information.
3. Examine available risk detections.
4. Review recent interactive and non-interactive sign-ins.
5. Check IP addresses, locations and devices.
6. Determine whether the account may be compromised.
7. Initiate appropriate remediation.

## 3. Sign-in Risk

Sign-in risk represents the probability that a particular authentication request is not coming from the legitimate user.

It focuses on an individual sign-in event.

### Example: Anonymous Proxy

An employee attempts to sign in from an anonymous proxy using an unfamiliar device.

The sign-in may be considered suspicious because its characteristics differ from expected authentication activity.

### Investigation Steps

1. Identify the suspicious sign-in.
2. Review the source IP address.
3. Examine the geographic location.
4. Check device information.
5. Review authentication methods and results.
6. Examine the associated risk detection.
7. Determine whether the authentication attempt is legitimate.

## 4. Difference Between User Risk and Sign-in Risk

| Comparison | User Risk | Sign-in Risk |
|---|---|---|
| Focus | User account | Individual authentication request |
| Main concern | Possible identity compromise | Possible fraudulent sign-in |
| Example | Leaked credentials | Anonymous proxy |
| Scope | User identity | Particular sign-in |
| Investigation | Account and identity activity | Sign-in evidence and context |

## 5. Risk Levels

Microsoft Entra uses risk levels to represent the assessed degree of risk.

| Risk level | Interpretation |
|---|---|
| None | No risk assigned or identified for the assessment |
| Low | Lower assessed risk |
| Medium | Moderate assessed risk |
| High | Significant assessed risk |

Risk levels should not be interpreted in isolation. Analysts must consider the available evidence and organizational security requirements.

## 6. Important Risk Detection Examples

### 6.1 Leaked Credentials

Credentials associated with a user are discovered in a known leak.

This is an important indicator of possible user account compromise.

### 6.2 Anonymous IP Address

A sign-in attempt originates from an anonymising service.

This may indicate suspicious authentication activity.

### 6.3 Atypical Travel

Sign-ins occur from geographically unusual locations within a short period.

This is a detection clue and does not automatically prove malicious activity.

### 6.4 Password Spray

An attacker attempts commonly used passwords against multiple user accounts.

This may indicate a coordinated authentication attack.

### 6.5 Suspicious MFA Approval

An unexpected or manipulated MFA approval may indicate an attempt to gain unauthorized access.

## 7. Practical IAM Investigation Scenarios

### Scenario 1: User Risk

**Situation:**

Arun's password is discovered in a known credential leak.

**Risk category:** User Risk

**Reason:**

The concern relates to the possible compromise of Arun's identity and credentials.

**Investigation approach:**

- Review available risk information.
- Examine recent sign-in activity.
- Verify suspicious authentication.
- Determine whether the account is compromised.
- Recommend appropriate remediation.

### Scenario 2: Sign-in Risk

**Situation:**

Arun attempts to sign in through an anonymous proxy using an unfamiliar device.

**Risk category:** Sign-in Risk

**Reason:**

The concern relates to the legitimacy of the particular authentication request.

**Investigation approach:**

- Review IP address and location.
- Examine device information.
- Inspect authentication details.
- Verify the user's activity.
- Determine whether the sign-in is suspicious.

### Scenario 3: Atypical Travel

**Situation:**

Arun signs in from Chennai and subsequently signs in from Bengaluru.

**Risk category:** Potential sign-in risk detection

**Reason:**

The geographically unusual activity may trigger investigation.

However, the user may genuinely be travelling.

**Investigation approach:**

- Verify travel details.
- Examine device and authentication evidence.
- Review other suspicious activity.
- Determine whether the detection is benign.

## 8. Important Investigation Principles

An IAM Analyst should remember:

1. User risk and sign-in risk are different.
2. A successful sign-in does not guarantee that the activity is legitimate.
3. MFA success does not completely eliminate the possibility of compromise.
4. Atypical travel is not proof of an attack.
5. One risky sign-in does not automatically establish account compromise.
6. Risk level None does not guarantee account security.
7. Risk decisions must be supported by investigation evidence.

## 9. Licensing Considerations

Full Identity Protection risk reporting and risk-based Conditional Access capabilities require eligible premium licensing.

The free cloud-only tenant used in this project provides limited visibility.

Therefore, the practical investigation exercises are based on available portal information and simulated scenarios.

No premium licence was purchased or activated.

## 10. Learning Outcome

After completing this lesson, the following concepts were understood:

- User risk.
- Sign-in risk.
- Risk levels.
- Leaked credential detection.
- Anonymous IP detection.
- Atypical travel.
- Password spray.
- MFA-related suspicious activity.
- Practical investigation approaches.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Lesson: User Risk and Sign-in Risk*
