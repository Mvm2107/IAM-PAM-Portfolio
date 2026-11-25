# Identity Protection and Risk-Based Access

## 1. Overview

This module focuses on Microsoft Entra ID Protection and its role in identity security.

It covers identity risk detection, user risk, sign-in risk, risk-based Conditional Access, risk remediation and practical identity investigation scenarios.

The objective is to understand how IAM and SOC teams identify suspicious identity activity, investigate potential account compromise and respond through appropriate security controls.

## 2. Learning Objectives

- Understand Microsoft Entra ID Protection.
- Differentiate user risk and sign-in risk.
- Understand identity risk detection mechanisms.
- Learn real-time and offline detections.
- Understand Risky users, Risky sign-ins and Risk detections reports.
- Understand risk-based Conditional Access.
- Learn risk remediation and session revocation.
- Practise identity incident investigation.
- Understand licensing limitations in Microsoft Entra.

## 3. Module Contents

| File | Topic | Description |
|---|---|---|
| 01-Identity-Protection-Fundamentals.md | Identity Protection Fundamentals | Introduction to identity security and risk management |
| 02-User-Risk-and-Sign-in-Risk.md | User Risk and Sign-in Risk | Differences between account risk and authentication risk |
| 03-Risk-Detection-and-Investigation.md | Risk Detection and Investigation | Detection mechanisms, reports and investigation workflow |
| 04-Risk-Based-Conditional-Access.md | Risk-Based Conditional Access | Risk policies, report-only mode and access controls |
| 05-Risk-Remediation.md | Risk Remediation | Compromise confirmation, risk dismissal, blocking and session revocation |
| 06-Practical-Scenarios-and-Troubleshooting.md | Practical Scenarios and Troubleshooting | Simulated IAM/SOC incidents and troubleshooting |

## 4. Key Technical Concepts

### Identity Protection

Microsoft Entra ID Protection helps organisations detect, investigate and remediate identity-related risks.

### User Risk

Represents the probability that a user's identity or account has been compromised.

Example: Credentials discovered in a known data leak.

### Sign-in Risk

Represents the probability that a particular authentication request is not coming from the legitimate user.

Example: A sign-in attempt from an anonymous proxy.

### Risk-Based Conditional Access

Uses identity risk signals to determine whether additional authentication, remediation or access restrictions should apply.

### Risk Remediation

Addresses identified identity risks through appropriate actions such as securing credentials, revoking sessions and blocking suspicious access.

## 5. Identity Investigation Workflow

The general investigation workflow covered in this module is:

1. Identify the affected user.
2. Identify the risk type.
3. Review available risk detections.
4. Examine sign-in evidence.
5. Investigate IP address, location and device information.
6. Review authentication and application activity.
7. Determine whether the activity is legitimate or suspicious.
8. Apply approved containment and remediation actions.
9. Verify the outcome.
10. Document the investigation.

## 6. Practical Environment

**Platform:** Microsoft Entra admin center  
**Environment:** Free cloud-only Entra tenant  
**Project:** Microsoft Entra ID – Identity and Access Management Portfolio

### Portal Areas Inspected

- Identity Protection dashboard.
- Risky users.
- Risky sign-ins.
- Risk policy impact analysis.
- Conditional Access policies.

### Practical Observations

| Area | Observation |
|---|---|
| Identity Protection dashboard | Accessible; no metric data displayed |
| Risky users | Three users displayed, all classified as No Risk |
| Risky sign-ins | HTTP 401 – access denied |
| Risk policy impact analysis | HTTP 401 – content inaccessible |
| Conditional Access | Licensing restriction displayed |
| Risk detections | Not independently available for inspection |

### Practical Limitations

The free cloud-only tenant did not provide the full premium Identity Protection investigation and risk-based Conditional Access experience.

Therefore:

- Full risk detection investigation was not performed.
- Risky sign-in records could not be accessed.
- Risk policy impact analysis could not be accessed.
- Risk-based Conditional Access policies were not created.
- Risk confirmation, dismissal and remediation actions were not performed.

Investigation and remediation workflows were practised using simulated scenarios.

No paid licence was purchased or activated.

## 7. Practical Scenario Coverage

The following simulated scenarios were studied:

1. Suspicious sign-in from an anonymous proxy.
2. Leaked credentials and potential account compromise.
3. Atypical travel and false-positive investigation.
4. Successful MFA with suspicious authentication activity.
5. Suspicious account access involving an unknown device and unusual application activity.

These scenarios helped develop evidence-based investigation and response skills.

## 8. Important Security Takeaways

- User risk and sign-in risk are different.
- Successful authentication does not guarantee legitimate access.
- MFA success does not completely eliminate the possibility of compromise.
- Atypical travel is not proof of malicious activity.
- Risk dismissal must be supported by investigation.
- Password changes do not necessarily invalidate every existing session.
- Session revocation is an important containment measure.
- Incident decisions must be supported by evidence.
- Risk reports and policies depend on licensing.

## 9. Learning Outcomes

After completing this module, the following areas were studied:

- Microsoft Entra ID Protection fundamentals.
- User risk and sign-in risk.
- Risk detection mechanisms.
- Real-time and offline detections.
- Identity investigation workflow.
- Risky users and risky sign-ins reports.
- Risk-based Conditional Access.
- Report-only mode.
- Risk remediation.
- Password change and password reset.
- Session revocation.
- IAM/SOC incident investigation.
- Security incident documentation.
- Microsoft Entra licensing limitations.

## 10. Module Conclusion

This module developed an understanding of identity threat detection, risk investigation and remediation within Microsoft Entra ID.

The theoretical lessons and simulated scenarios provided an understanding of how IAM and SOC teams investigate suspicious authentication activity and respond to potential identity compromise.

Practical portal inspection also demonstrated the limitations of using a free cloud-only Entra tenant for advanced Identity Protection capabilities.

---

*Project: Microsoft Entra ID – Identity and Access Management Portfolio*  
*Phase: Phase 1 – Cloud-Only Identity Management*  
*Module: Identity Protection and Risk-Based Access*
