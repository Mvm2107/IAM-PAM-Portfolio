# Exercise-02 – Update-User-Attributes

## Objective
Update employee attributes in Microsoft Entra ID and investigate the changes using Audit Logs.

## Scenario

HR submits change request CR-1001 to update Arun Kumar's employment information following an internal role change.

## Change Request

| Attribute | Previous Value | New Value |
|---|---|---|
| Job Title | Junior IT Support Analyst | IT Support Analyst |
| Department | IT | IT Operations |
| Office Location | Remote | Chennai |
| Employee ID | EMP1001 | No Change |

## Environment

- Microsoft Entra ID Free
- Microsoft Entra admin center
- Existing cloud-only employee account
- User: Arun Kumar

## Procedure

1. Navigate to Entra ID → Users → All Users.
2. Select Arun Kumar.
3. Select Edit properties.
4. Select the required properties.
5. Enter the new values.
6. Review the changes.
7. Save the modifications.

## Updated Properties

| Attribute | Updated Value |
|---|---|
| Job Title | IT Support Analyst |
| Department | IT Operations |
| Office Location | Chennai |
| Employee ID | EMP1001 |

## Verification

Opened Arun Kumar's Properties page and verified:

- Job title updated successfully.
- Department updated successfully.
- Office location updated successfully.
- Employee ID remained unchanged.
- Account remained enabled.
- On-premises sync remained disabled.

## Audit Log Investigation

Located the corresponding event under Audit Logs.

| Field | Result |
|---|---|
| Activity | Update user |
| Category | UserManagement |
| Status | Success |
| Initiated By | Administrator |
| Target | Arun Kumar |

## Modified Properties Analysis

Inspected the Modified Properties section.

| Property | Old Value | New Value |
|---|---|---|
| Department | IT | IT Operations |
| JobTitle | Junior IT Support Analyst | IT Support Analyst |
| PhysicalDeliveryOfficeName | Remote | Chennai |

The audit event recorded the previous and updated values.

## Result

Successfully updated the employee's attributes and verified the changes through the Entra user profile and audit logs.

## IAM Concepts Learned

- Employee attribute management
- HR-driven change requests
- User profile modification
- Audit trail investigation
- Old Value vs New Value
- Correlation ID
- Target identity identification

## Security Considerations

- Verify HR authorization before making changes.
- Modify only the requested attributes.
- Avoid unnecessary changes to employee identifiers.
- Maintain audit evidence for administrative operations.

## Evidence

Add screenshots showing:

1. Edit properties interface.
2. Updated employee properties.
3. Update user audit event.
4. Target user details.
5. Modified Properties showing old and new values.

**Change Request:** CR-1001

**Status:** Completed
