# Joiner-Mover-Leaver (JML) Lifecycle Management

## 1. Introduction

Joiner-Mover-Leaver (JML) is an important Identity and Access Management process used by organisations to manage employee identities throughout their employment lifecycle.

The three stages are:

1. Joiner – A new employee joins the organisation.
2. Mover – An existing employee changes department or job responsibilities.
3. Leaver – An employee leaves the organisation.

The purpose of this practical exercise was to simulate these three scenarios using Microsoft Entra ID.

## 2. Lab Environment

| Component | Configuration |
|---|---|
| Identity platform | Microsoft Entra ID |
| Enterprise application | IAM-Lab-Test-App |
| Application role | User |
| Initial test employee | Arun Kumar |
| JML test employee | Priya Sharma |
| Employee ID | EMP1002 |

Group-based application assignment was unavailable because of the free tenant's licensing level. Direct user assignment was used for the practical scenarios.

---

# Scenario 1 – Joiner

## 3. Business Scenario

A new employee, Priya Sharma, joined the IT Operations department as a Junior IT Support Analyst.

HR submitted a request to create the employee's identity and provide access to the required enterprise application.

### Employee Information

| Attribute | Value |
|---|---|
| Display name | Priya Sharma |
| First name | Priya |
| Last name | Sharma |
| UPN prefix | priya.sharma |
| User type | Member |
| Job title | Junior IT Support Analyst |
| Department | IT Operations |
| Company | IAM Learning Lab |
| Employee ID | EMP1002 |
| Employee type | Employee |
| Usage location | India |
| Account enabled | Yes |

## 4. User Provisioning

Navigated to:

Microsoft Entra ID → Users → All users → New user → Create new user

Entered Priya's employee information and created the account.

Verified the following:
- User account created successfully.
- User type was Member.
- Account enabled was Yes.
- Employee information was populated.
- User profile was accessible.

Temporary credentials were kept private and excluded from documentation.

## 5. Application Access Assignment

Navigated to:

Enterprise applications → IAM-Lab-Test-App → Users and groups

Selected Priya Sharma.

Selected application role:

`User`

Confirmed the assignment.

The Users and groups page displayed Priya Sharma as an assigned user.

### Audit Verification

Checked the application's audit logs.

Identified:

`Add app role assignment grant to user`

Verified the successful status and the target user.

### Joiner Result

- Priya's account was created.
- Employee attributes were populated.
- Application assignment was successful.
- Audit event was recorded.

**Outcome: Joiner process completed successfully.**

---

# Scenario 2 – Mover

## 6. Business Scenario

Priya Sharma transferred from IT Operations to the Finance department.

HR submitted an employee information change request.

### HR Change Request

| Attribute | Previous value | New value |
|---|---|---|
| Department | IT Operations | Finance |
| Job title | Junior IT Support Analyst | Finance Operations Analyst |
| Employee ID | EMP1002 | EMP1002 |
| Account status | Enabled | Enabled |

## 7. Update Employee Attributes

Navigated to:

Microsoft Entra ID → Users → All users → Priya Sharma → Properties

Updated:

- Department: Finance
- Job title: Finance Operations Analyst

Kept the Employee ID unchanged.

Saved the changes.

### Verification

Reopened Priya's user profile.

Verified:

| Attribute | Verified value |
|---|---|
| Department | Finance |
| Job title | Finance Operations Analyst |
| Employee ID | EMP1002 |
| Account enabled | Yes |

The user identity remained unchanged.

## 8. Review Existing Application Access

Navigated to:

Enterprise applications → IAM-Lab-Test-App → Users and groups

Priya was still assigned to the application after her department change.

For this lab scenario, IAM-Lab-Test-App was treated as an IT Operations application.

The new Finance role no longer required this application access.

Therefore, the assignment was reviewed and identified for removal.

## 9. Remove Unnecessary Application Access

Selected Priya Sharma.

Clicked Remove assignment and confirmed the operation.

Verified that the application assignment was removed.

### Audit Verification

Identified the event:

`Remove app role assignment from user`

Verified the successful status and the target user.

### Mover Result

- Department updated.
- Job title updated.
- Employee ID retained.
- Existing application access reviewed.
- Unnecessary application assignment removed.
- Audit event verified.

**Outcome: Mover process completed successfully.**

Important lesson: Changing an employee's department does not automatically remove existing application permissions. Access must be reviewed against the employee's new responsibilities.

---

# Scenario 3 – Leaver

## 10. Business Scenario

Priya Sharma resigned from the organisation.

HR confirmed that her last working day had passed and requested account deactivation.

The IAM administrator was responsible for disabling the account, revoking active sessions and verifying the offboarding actions.

## 11. Disable the User Account

Navigated to:

Microsoft Entra ID → Users → All users → Priya Sharma → Properties

Changed:

`Account enabled: Yes → No`

Saved the change.

### Verification

Reopened the user profile.

Confirmed:

`Account enabled: No`

### Audit Verification

Opened Priya's audit logs.

Identified the event:

`Disable account`

Verified that the operation was successful.

## 12. Revoke Active Sessions

Returned to Priya's user overview.

Selected:

`Revoke sessions`

Confirmed the operation.

The portal displayed a confirmation message explaining that the user's sessions would be revoked and the user would need to sign in again.

### Understanding Session Revocation

Revoking sessions updates the refresh-token validity boundary.

Previously issued refresh tokens should no longer be usable to obtain new access tokens.

However, some already-issued access tokens may remain valid until they expire.

### Audit Verification

Identified these events:

- Update user
- Update StsRefreshTokenValidFrom Timestamp

Verified successful status.

The Modified Properties section showed that the refresh-token validity timestamp had moved forward.

## 13. Sign-in Log Verification

Navigated to:

Users → Priya Sharma → Sign-in logs

Selected the Last 24 hours date range.

Checked both categories:

### Interactive Sign-ins

Result:

`No sign-ins found`

### Non-interactive Sign-ins

Result:

`No sign-ins found`

This confirmed that no sign-in records were available for Priya in the selected period.

Important distinction: No sign-ins found does not prove that an attempted sign-in was blocked. It means no records were returned for the selected period.

## 14. Account Disable vs Session Revocation vs Account Deletion

| Operation | Purpose |
|---|---|
| Disable account | Prevents new sign-in attempts |
| Revoke sessions | Invalidates refresh-token-based sessions |
| Remove application assignment | Removes a specific application assignment |
| Delete account | Removes the user from the active directory and places it into the deleted-user recovery process |

These operations have different purposes and should not be treated as interchangeable.

The account was disabled, not deleted, in this lab.

## 15. Leaver Result

- User account disabled.
- Disable operation verified in audit logs.
- Active sessions revoked.
- Refresh-token validity timestamp updated.
- Interactive sign-in logs inspected.
- Non-interactive sign-in logs inspected.
- Application assignment had already been removed during the Mover scenario.

**Outcome: Leaver offboarding steps completed successfully.**

---

# 16. JML Lifecycle Summary

| Lifecycle stage | Actions performed | Result |
|---|---|---|
| Joiner | Create account, populate attributes, assign application access | Successful |
| Mover | Update department and job title, review and remove unnecessary access | Successful |
| Leaver | Disable account, revoke sessions and inspect sign-in logs | Successful |

## 17. IAM Skills Practised

Through this exercise, the following practical skills were demonstrated:

- Microsoft Entra user provisioning.
- Employee attribute management.
- Enterprise application assignment.
- Application access removal.
- Account enable and disable operations.
- Session revocation.
- Interactive sign-in log investigation.
- Non-interactive sign-in log investigation.
- Audit log investigation.
- Joiner-Mover-Leaver lifecycle management.

## 18. Important Lab Limitations

1. Group-based application assignment was unavailable because of the tenant's current licensing level.
2. Direct user assignment was used instead.
3. IAM-Lab-Test-App was a non-gallery test application without a functioning backend or configured SSO.
4. Sign-in logs showed no records for Priya in the selected 24-hour period; this was not treated as proof of blocked sign-ins.
5. Credentials and sensitive identifiers were excluded from the documentation.

## 19. Conclusion

This practical exercise demonstrated the Joiner-Mover-Leaver identity lifecycle using Microsoft Entra ID.

The Joiner scenario covered account creation and application access assignment.

The Mover scenario covered employee attribute changes and removal of application access that was no longer required.

The Leaver scenario covered account disabling, session revocation and sign-in log investigation.

The exercise demonstrated how IAM administrators maintain appropriate access throughout an employee's lifecycle while using audit logs to verify administrative actions.
