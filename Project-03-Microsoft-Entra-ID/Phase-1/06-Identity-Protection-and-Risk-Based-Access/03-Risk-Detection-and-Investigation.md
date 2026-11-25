# Risk Detection and Investigation

## 1. Overview

Microsoft Entra ID Protection identifies potentially suspicious identity activity through risk detection mechanisms.

Risk detection helps IAM and SOC teams identify unusual authentication behaviour and possible account compromise.

The investigation process involves examining risk information, correlating sign-in evidence and determining whether the activity is legitimate or suspicious.

## 2. Types of Risk Detections

Risk detections can be associated with individual authentication events or potential compromise of a user account.

### 2.1 Sign-in Risk Detections

Sign-in risk detections relate to a particular authentication request.

Examples include:

| Detection | Description |
|---|---|
| Anonymous IP address | Sign-in from an anonymising service |
| Atypical travel | Geographically unusual sign-ins within a short period |
| Password spray | Attempts to guess passwords across multiple accounts |
| Suspicious MFA approval | Potentially suspicious or manipulated MFA approval |
| Unfamiliar sign-in properties | Authentication characteristics that differ from expected activity |
| Anomalous token | Potentially suspicious token characteristics |

### 2.2 User Risk Detections

User risk detections relate to possible compromise of an identity.

Examples include:

| Detection | Description |
|---|---|
| Leaked credentials | Credentials discovered in a known leak |
| Suspicious credential activity | Potentially suspicious changes involving authentication credentials |
| Attacker-in-the-Middle activity | Authentication activity associated with a malicious intermediary |
| Anomalous user activity | Unusual activity associated with a user identity |

Detection availability depends on the tenant's licensing and applicable Microsoft security capabilities.

## 3. Real-Time and Offline Detections

Microsoft Entra ID Protection can identify risk at different stages.

### 3.1 Real-Time Detection

Real-time detection identifies suspicious activity during authentication using available signals.

Example:

A user attempts to sign in through an anonymous proxy. Entra evaluates the available sign-in information and may identify risk during the authentication process.

A Conditional Access policy can respond to available risk information when the required licensing and configuration are in place.

### 3.2 Offline Detection

Offline detection identifies suspicious activity after authentication by analysing additional information.

Example:

A user successfully signs in. Additional evidence is subsequently analysed and a risk detection may appear later.

Important points:

- A successful sign-in does not guarantee that no risk will be detected later.
- Risk information may change as additional evidence becomes available.
- Detection processing times can vary.

## 4. Identity Protection Reports

Microsoft Entra ID Protection provides reports that support identity risk investigation.

### 4.1 Risk Detections

This report provides information about individual risk events.

An analyst can use it to understand:

- What type of detection occurred.
- Which user was affected.
- When the event occurred.
- What risk information is available.

### 4.2 Risky Sign-ins

This report focuses on authentication attempts associated with risk.

Investigation may involve:

- Sign-in status.
- Source IP address.
- Geographic location.
- Device information.
- Authentication details.
- Associated risk information.

### 4.3 Risky Users

This report focuses on user accounts associated with risk.

It helps identify users who may require further investigation or remediation.

A user may have multiple associated risk events.

## 5. Risk Investigation Workflow

A structured investigation process helps IAM and SOC analysts evaluate suspicious identity activity.

### Step 1: Identify the User

Determine which account is associated with the detection.

### Step 2: Identify the Risk Type

Determine whether the concern relates to user risk or sign-in risk.

### Step 3: Review the Detection

Examine the available detection details and risk information.

### Step 4: Examine Sign-in Evidence

Review:

- IP address.
- Geographic location.
- Device information.
- Authentication method.
- Sign-in result.
- Application accessed.

### Step 5: Correlate Evidence

Compare the suspicious event with the user's expected activity and other available security information.

### Step 6: Determine the Outcome

Classify the activity based on the investigation:

- Legitimate activity.
- Suspicious activity requiring further investigation.
- Confirmed or suspected account compromise.
- False-positive detection.

### Step 7: Recommend Remediation

Follow the organization's incident-response process to address the identified risk.

### Step 8: Document Findings

Record the evidence, investigation outcome and actions taken.

## 6. Practical Portal Inspection

The Microsoft Entra ID Protection dashboard was inspected using the cloud-only free tenant.

### 6.1 Identity Protection Dashboard

The dashboard was accessible.

The following metrics were displayed:

| Dashboard metric | Displayed value |
|---|---:|
| Number of attacks blocked | 0 |
| Number of users protected | 0 |
| Mean time to remediate high-risk users | 0 hours |
| Number of high-risk users | 0 |

The dashboard displayed no data for these metrics.

**Observation:** The displayed zero values and absence of data do not establish that no attacks have occurred. They indicate that the dashboard had no available data for the displayed metrics and period.

### 6.2 Risky Users Report

The Risky users page was accessible.

Observed information:

| Field | Observation |
|---|---|
| Users displayed | 3 |
| High risk | 0 |
| Medium risk | 0 |
| Low risk | 0 |
| No risk | 3 |

All three displayed users were classified as No Risk.

**Observation:** No Risk does not guarantee that an account is completely secure. It indicates that no risk was assigned or identified for the displayed assessment.

No risk-management actions were performed.

### 6.3 Risky Sign-ins Report

The Risky sign-ins page returned an HTTP 401 access error.

Displayed message:

`You don't have access to this data.`

**Observation:** The report data could not be accessed in the current tenant.

The error does not establish that an account has been compromised or that a suspicious sign-in occurred.

### 6.4 Risk Policy Impact Analysis

The Risk policy impact analysis page was also inspected.

It returned an HTTP 401 access error with the message:

`Error loading your content.`

**Observation:** The page was visible in the navigation, but its content was inaccessible.

### 6.5 Risk Detections

The Risk detections report was not independently available for inspection in the current tenant navigation and licensing experience.

No actual risk detection records were retrieved or investigated.

## 7. Practical Findings

| Feature | Result |
|---|---|
| Identity Protection dashboard | Accessible; no metric data displayed |
| Risky users | Accessible; 3 users displayed as No Risk |
| Risky sign-ins | HTTP 401 – data inaccessible |
| Risk policy impact analysis | HTTP 401 – content inaccessible |
| Risk detections | Not independently inspected |

These observations represent the actual portal inspection performed during this project.

No risk detections were fabricated, and no risk-management actions were performed.

## 8. Licensing Limitations

Microsoft Entra ID Protection capabilities depend on the tenant's licensing level.

The full premium risk investigation and risk-based policy capabilities require eligible premium licensing.

The current project uses a free cloud-only Entra tenant.

Consequently:

- Full risk detection reporting was not available for practical investigation.
- Risky sign-in data could not be accessed.
- Risk policy impact analysis could not be accessed.
- Risk-based Conditional Access configuration was not performed.

Investigation workflows and scenarios were practised theoretically and through simulated exercises.

No paid licence was purchased or activated.

## 9. Learning Outcome

This exercise provided an understanding of:

- Sign-in risk and user risk detections.
- Real-time and offline detections.
- Risky users, risky sign-ins and risk detections reports.
- Identity investigation workflow.
- Correlation of authentication evidence.
- Practical portal inspection.
- Licensing-related access restrictions.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Module: Identity Protection and Risk-Based Access*  
*Topic: Risk Detection and Investigation*
