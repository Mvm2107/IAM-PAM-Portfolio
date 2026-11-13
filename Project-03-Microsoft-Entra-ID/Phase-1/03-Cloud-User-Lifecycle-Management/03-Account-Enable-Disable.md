# Account Enablement and Disablement – Microsoft Entra ID

## 1. Objective

Understand how an IAM administrator can enable and disable a cloud-only user account in Microsoft Entra ID and investigate these actions using Audit Logs.

## 2. Environment

- Platform: Microsoft Entra ID
- Portal: Microsoft Entra admin center
- Environment: Cloud-only tenant
- User: Arun Kumar (Lab account)
- User type: Member

## 3. Practical Exercise 1 – Disable User Account

### Steps performed

1. Navigated to **Users → All users**.
2. Selected Arun Kumar.
3. Opened the user's Properties.
4. Navigated to Settings.
5. Changed **Account enabled** from Yes to No.
6. Saved the changes.

### Audit Log Investigation

Navigated to Users → Audit logs and inspected the generated events.

| Field | Observed value |
|---|---|
| Service | Core Directory |
| Category | UserManagement |
| Activity | Disable account |
| Status | Success |
| Time | 7:57:29 PM |

### Modified Properties

| Property | Old value | New value |
|---|---|---|
| AccountEnabled | true | false |

**Observation:** The audit logs recorded two related events:

- Disable account
- Update user

The Update user event captured the property-level change.

## 4. Practical Exercise 2 – Enable User Account

### Steps performed

1. Opened Arun Kumar's user profile.
2. Navigated to Properties → Settings.
3. Changed **Account enabled** from No to Yes.
4. Saved the changes.
5. Navigated to Audit Logs to verify the operation.

### Audit Log Investigation

| Field | Observed value |
|---|---|
| Service | Core Directory |
| Category | UserManagement |
| Activity | Enable account |
| Status | Success |
| Time | 8:03:40 PM |

**Observation:** Two related events appeared:

- Enable account
- Update user

The audit logs confirmed that the account was successfully re-enabled.

## 5. Understanding the Audit Logs

The two related event types provide different information:

- **Enable account / Disable account:** Identifies the specific administrative action.
- **Update user:** Records changes to user properties.

The AccountEnabled property indicates the account state:

| Value | Meaning |
|---|---|
| true | Account enabled |
| false | Account disabled |

Audit log records may take some time to appear after an administrative operation.

## 6. Disable vs Delete

| Disable account | Delete account |
|---|---|
| Prevents user sign-in | Removes user from active users |
| User object remains | User enters deleted state |
| Can be re-enabled | Can be restored during retention period |
| Useful for temporary suspension | Used during authorized account removal |

Microsoft Entra ID normally retains deleted users for 30 days before permanent deletion.

## 7. IAM Use Case

When an employee leaves an organization, an IAM administrator may need to:

1. Disable the employee account.
2. Revoke active sessions.
3. Review and remove access to assigned applications and groups.
4. Follow the organization's offboarding and data-retention policies.
5. Delete the account when authorized.

Disabling an account is an important immediate access-control measure during employee offboarding.

## 8. Key Learnings

- Learned how to enable and disable cloud-only user accounts.
- Understood the AccountEnabled property.
- Investigated successful account-management operations.
- Learned how to interpret Old Value and New Value.
- Understood the relationship between Enable/Disable account and Update user audit events.
- Practiced investigating identity lifecycle operations.

## 9. Conclusion

Successfully performed account disablement and re-enablement in Microsoft Entra ID.

Verified both operations through Audit Logs and confirmed the corresponding AccountEnabled property changes.

**Project:** Microsoft Entra ID – Cloud-only IAM Practical Lab  
**Phase:** Phase 1 – Cloud-only  
**Module:** 03 – Cloud User Lifecycle Management  
**Exercise:** Account Enablement and Disablement
