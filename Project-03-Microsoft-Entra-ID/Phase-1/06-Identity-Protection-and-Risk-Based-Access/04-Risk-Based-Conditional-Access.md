# Risk-Based Conditional Access

## 1. Overview

Microsoft Entra Conditional Access is an identity and access management capability that evaluates signals associated with authentication requests and applies access controls based on configured policies.

Risk-Based Conditional Access uses identity risk signals from Microsoft Entra ID Protection to make access decisions.

It helps organizations respond to potentially compromised accounts and suspicious authentication attempts.

## 2. How Risk-Based Conditional Access Works

The general process is:

1. A user attempts to sign in.
2. Microsoft Entra evaluates available identity and authentication signals.
3. Identity risk information is evaluated where supported.
4. Conditional Access evaluates applicable policies.
5. The configured access controls are applied.

Possible access outcomes include:

- Allow access.
- Require multifactor authentication.
- Require additional authentication or remediation.
- Block access.

The actual outcome depends on the configured policies, available signals and licensing.

## 3. Types of Risk-Based Conditional Access Policies

There are two important types of risk-based policies.

### 3.1 Sign-in Risk Policy

A sign-in risk policy evaluates the risk associated with a particular authentication attempt.

**Example:**

An employee attempts to sign in using an anonymous proxy from an unfamiliar location.

Microsoft Entra identifies elevated sign-in risk.

An organization may configure a policy to require MFA or block access depending on its security requirements.

Typical policy considerations:

- Target users or groups.
- Target cloud applications.
- Sign-in risk condition.
- Selected risk levels.
- Access controls.
- Policy state.

### 3.2 User Risk Policy

A user risk policy evaluates the probability that a user's account has been compromised.

**Example:**

An employee's credentials are discovered in a known password leak.

Microsoft Entra identifies potential user risk.

An organization may require the user to complete risk remediation, such as a secure password change, or block access according to its security policy.

Typical policy considerations:

- Target users or groups.
- Target cloud applications.
- User risk condition.
- Selected risk levels.
- Access controls.
- Policy state.

## 4. Difference Between User Risk and Sign-in Risk Policies

| Comparison | User Risk Policy | Sign-in Risk Policy |
|---|---|---|
| Evaluates | User account risk | Individual authentication risk |
| Main concern | Possible identity compromise | Possible fraudulent sign-in |
| Example | Leaked credentials | Anonymous proxy |
| Focus | User identity | Authentication request |
| Possible response | Risk remediation | MFA or access restriction |

These policies address different security concerns and should be designed according to the organization's requirements.

## 5. Report-Only Mode

Report-only mode allows administrators to evaluate the expected impact of a Conditional Access policy without enforcing its access controls.

It is useful when introducing new security policies.

### Recommended Deployment Process

1. Create the proposed policy.
2. Select the intended users and resources.
3. Configure conditions.
4. Configure grant controls.
5. Set the policy to Report-only.
6. Review policy evaluation results.
7. Investigate unexpected outcomes.
8. Make necessary corrections.
9. Obtain the required approval.
10. Enable the policy when ready.

Report-only mode reduces the risk of unexpected access disruption during policy deployment.

## 6. Emergency-Access Accounts

Emergency-access accounts, also known as break-glass accounts, help organizations recover administrative access when normal authentication or access controls become unavailable.

Conditional Access policies must be designed carefully to avoid accidentally locking out all administrators.

Important considerations:

- Maintain appropriately protected emergency-access accounts.
- Apply suitable exclusions where required.
- Monitor emergency-account activity.
- Test emergency access periodically.
- Protect credentials and authentication methods.
- Document emergency-access procedures.

Exclusions should be limited and carefully governed. Emergency accounts should not become a general way to bypass security controls.

## 7. Risk-Based Policy Examples

### Example 1: High Sign-in Risk

**Policy name:** Require MFA for Risky Sign-ins

| Configuration | Example |
|---|---|
| Users | All applicable users |
| Target resources | Selected or all cloud applications |
| Condition | Sign-in risk |
| Risk levels | Medium and High |
| Access control | Require MFA |
| Initial state | Report-only |

Purpose:

Require additional authentication when a sign-in is assessed as risky.

### Example 2: High User Risk

**Policy name:** Remediate High-Risk Users

| Configuration | Example |
|---|---|
| Users | All applicable users |
| Target resources | Selected or all cloud applications |
| Condition | User risk |
| Risk level | High |
| Access control | Require risk remediation |
| Initial state | Report-only |

Purpose:

Require users with high account risk to complete the required remediation process.

These are conceptual policy designs. They were not created or enabled in the practical tenant.

## 8. Licensing Requirements

Risk-based Conditional Access requires eligible premium licensing.

The full risk-based Conditional Access experience requires Microsoft Entra ID P2 or Microsoft Entra Suite.

Standard Conditional Access functionality generally requires Microsoft Entra ID P1 or an eligible bundle.

The current project uses a free cloud-only Entra tenant.

Therefore, risk-based policy creation and enforcement were not performed.

## 9. Practical Portal Inspection

The Conditional Access page was inspected in the Microsoft Entra admin center.

Navigation:

`Microsoft Entra ID → Conditional Access → Policies`

### Observed Result

The page displayed a licensing warning:

"Your organization does not have sufficient licensing to access this product."

It also indicated that premium licensing is required to create policies targeting conditions such as cloud applications, sign-in risk and device platforms.

### Practical Findings

| Feature | Observation |
|---|---|
| Conditional Access page | Accessible |
| Policies navigation | Visible |
| Policy creation | Licensing restricted |
| Policy templates | Visible |
| Risk-based policy creation | Not available |
| Existing policy list | No policy entries shown in the inspected screenshot |

The screenshot did not establish whether policies exist elsewhere or whether Security Defaults is enabled.

No policy was created, edited, enabled or deleted.

## 10. Important Security Considerations

An IAM Analyst should understand:

1. User risk and sign-in risk policies address different security concerns.
2. Successful MFA does not guarantee that an authentication request is legitimate.
3. Report-only mode helps evaluate policies before enforcement.
4. Emergency-access accounts must be considered during policy design.
5. Policy exclusions should be carefully controlled.
6. Risk-based Conditional Access depends on eligible licensing.
7. Policy implementation should follow organizational approval and change-management processes.

## 11. Learning Outcome

After completing this lesson, the following concepts were understood:

- Conditional Access fundamentals.
- Risk-based Conditional Access.
- User risk policies.
- Sign-in risk policies.
- Report-only mode.
- Emergency-access accounts.
- Policy design and deployment considerations.
- Conditional Access licensing requirements.
- Practical inspection of the Conditional Access portal.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Topic: Risk-Based Conditional Access*
