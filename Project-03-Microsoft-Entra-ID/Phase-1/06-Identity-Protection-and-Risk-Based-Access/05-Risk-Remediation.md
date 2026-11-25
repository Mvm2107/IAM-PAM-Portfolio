# Risk Remediation

## 1. Overview

Risk remediation is the process of addressing identified identity-related security risks and protecting potentially compromised accounts.

Microsoft Entra ID Protection provides risk-management capabilities that help administrators investigate and respond to suspicious identity activity.

An IAM Analyst must understand when to confirm compromise, dismiss a risk, mark a user safe, block access and initiate credential remediation.

## 2. Risk Management Actions

### 2.1 Confirm User Compromised

This action is used when an investigation establishes that a user account has genuinely been compromised.

**Example:**

An employee reports that they did not perform a particular sign-in. Investigation identifies an unfamiliar device, suspicious IP address and successful authentication.

The administrator may confirm that the user is compromised.

Possible follow-up actions:

1. Contain access if necessary.
2. Secure or reset the user's credentials.
3. Revoke existing sessions.
4. Review authentication activity.
5. Investigate other potentially affected resources.
6. Verify the account's security.

Confirming compromise records the risk decision. It does not automatically complete every remediation action.

### 2.2 Dismiss User Risk

Dismiss user risk is used when the investigation determines that the activity is benign.

**Example:**

An employee signs in from Bengaluru after previously signing in from Chennai. The user confirms travelling, and the available evidence supports the explanation.

An administrator may dismiss the risk when the investigation justifies that decision.

Important points:

- The risk state changes to Dismissed.
- Dismissal does not change the user's password.
- Dismissal does not replace remediation when compromise is confirmed.
- The investigation justification should be documented.

### 2.3 Confirm User Safe

Confirm user safe is used when an investigation determines that a user risk is a false positive.

It is different from confirming compromise or dismissing an actual benign event.

Microsoft documents that this action removes associated risk and detections for the user and places the user in learning mode to relearn usage properties.

### 2.4 Block User

Blocking a user prevents further sign-ins and can be used as a containment measure when unauthorized access is suspected.

**Example:**

An attacker appears to have obtained an employee's credentials and may still have access to the account.

An administrator may block the user while investigating and securing the identity.

Blocking is a containment action. It does not independently resolve every security issue.

## 3. Comparison of Risk Management Actions

| Action | Purpose |
|---|---|
| Confirm user compromised | Record confirmed account compromise |
| Dismiss user risk | Close a risk assessment determined to be benign |
| Confirm user safe | Mark a false-positive user risk |
| Block user | Prevent further sign-ins as a containment measure |

These actions should be selected based on investigation evidence and organizational procedures.

## 4. Password Change vs Password Reset

Password change and password reset are different identity-management processes.

### 4.1 Password Change

A password change generally occurs when a user knows their current password and can authenticate.

Example:

An employee's password is discovered in a known credential leak. The employee can still authenticate and completes a secure password change.

In supported risk-remediation flows, strong authentication may be required before the password change.

### 4.2 Password Reset

A password reset is generally used when a user cannot use their current password.

Examples:

- The employee forgot their password.
- The account requires an administrator-initiated reset.
- The employee uses an eligible Self-Service Password Reset (SSPR) process.

The reset process depends on the organization's configuration and the user's authentication methods.

## 5. Session Revocation

Session revocation is an important security response when an account may have been compromised.

An attacker may have already established an authenticated session using stolen credentials.

Changing the password alone should not be treated as proof that all existing access has ended.

Session revocation invalidates refresh tokens and requires reauthentication as applicable.

Important considerations:

- Revoke sessions when justified by the incident.
- Require users to authenticate again.
- Review recent sign-in activity.
- Investigate suspicious application access.
- Verify that the account is secure.

Some access tokens may remain valid until expiration unless additional controls apply.

## 6. Risk Remediation Workflow

A structured workflow helps IAM and SOC teams respond consistently.

### Step 1: Identify the Risk

Identify the affected account and associated detection.

### Step 2: Investigate

Review available risk information, sign-in history, IP addresses, devices and authentication details.

### Step 3: Determine the Outcome

Decide whether the activity represents:

- Confirmed compromise.
- Benign activity.
- False-positive detection.
- Suspected compromise requiring further investigation.

### Step 4: Contain Access

If active attacker access is suspected, block the account or take other approved containment actions.

### Step 5: Remediate

Depending on the incident:

- Secure or reset credentials.
- Revoke sessions.
- Require reauthentication.
- Secure authentication methods.
- Investigate affected applications.

### Step 6: Verify

Check that the user can securely authenticate and that the relevant risk state has been updated.

### Step 7: Document

Record the evidence, decision, actions, timestamps and verification results.

## 7. Practical IAM Incident Scenarios

### Scenario 1: Confirmed Account Compromise

**Situation:**

An employee denies a successful sign-in from an unfamiliar device. Investigation identifies suspicious IP activity.

**Response:**

- Treat the event as suspected compromise.
- Investigate the available evidence.
- Confirm compromise when established.
- Contain access if necessary.
- Reset credentials and revoke sessions as appropriate.
- Verify the account's security.

### Scenario 2: Benign Activity

**Situation:**

An employee signs in from a different location while travelling. The employee confirms the activity and the available evidence supports the explanation.

**Response:**

- Verify the activity.
- Review device and authentication evidence.
- Determine whether the event is benign.
- Dismiss the risk when justified.
- Document the reason.

### Scenario 3: False-Positive Detection

**Situation:**

A detection incorrectly associates suspicious activity with an employee.

**Response:**

- Investigate the evidence.
- Establish that the detection is a false positive.
- Use Confirm user safe where appropriate.
- Document the findings.

### Scenario 4: Active Attacker Access

**Situation:**

An attacker appears to have control of an employee's credentials and authentication process.

**Response:**

- Contain access through approved procedures.
- Block sign-in where necessary.
- Secure credentials and authentication methods.
- Revoke sessions.
- Investigate application access and potential persistence.
- Verify before restoring access.

## 8. Important Security Considerations

An IAM Analyst should remember:

1. Do not dismiss alerts without investigation.
2. Confirming compromise is not the same as completing remediation.
3. Blocking an account is a containment action.
4. Password changes do not necessarily terminate every existing session.
5. Session revocation helps invalidate refresh tokens.
6. Successful MFA does not guarantee that an account is safe.
7. Verify the remediation outcome before closing an incident.
8. Never include passwords, secret keys, recovery codes or session tokens in incident documentation.

## 9. Licensing and Practical Limitations

The current project uses a free cloud-only Microsoft Entra tenant.

Full Identity Protection risk-management capabilities require eligible premium licensing.

Therefore, the remediation actions described in this document were studied through theory and simulated investigation scenarios.

No risk-management buttons were clicked, no user risk was confirmed or dismissed, and no Identity Protection remediation was performed in the tenant.

## 10. Learning Outcome

After completing this lesson, the following concepts were understood:

- Confirm user compromised.
- Dismiss user risk.
- Confirm user safe.
- Block user.
- Password change versus password reset.
- Session revocation.
- Account containment and remediation.
- Verification and incident documentation.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Topic: Risk Remediation*
