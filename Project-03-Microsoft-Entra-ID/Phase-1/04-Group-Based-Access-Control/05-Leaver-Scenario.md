# Leaver Scenario – Employee Offboarding

## 1. Objective

Demonstrate the employee offboarding process using Microsoft Entra ID by disabling an account, revoking sessions, removing group memberships, and removing application assignments.

## 2. Scenario

An employee, Arun Kumar, leaves the organization.

**Employee ID:** EMP1001

**Department:** Finance Operations

**Identity platform:** Microsoft Entra ID (Cloud-only)

## 3. Initial State

Before offboarding, Arun had:

- An enabled Microsoft Entra ID account.
- Membership in GRP-Finance-Operations.
- A direct assignment to IAM-Lab-Test-App.

## 4. Activities Performed

### Step 1 – Disable User Account

Navigated to the user's account settings and changed:

| Property | Value |
|---|---|
| Account enabled | No |

This prevents the user from initiating new sign-ins.

### Step 2 – Revoke Active Sessions

Used the **Revoke sessions** action from the user's profile.

Purpose:
- Invalidate refresh tokens.
- Require the user to authenticate again.
- Reduce the risk of continued access through existing sessions.

### Step 3 – Remove Group Memberships

Removed Arun Kumar from:

- GRP-Finance-Operations

Verified the user's Groups page displayed:

`Not a member of any groups`

### Step 4 – Remove Application Assignment

Navigated to:

Enterprise Applications → IAM-Lab-Test-App → Users and groups

Removed Arun Kumar's direct application assignment.

Verified that the page displayed:

`No application assignments found`

## 5. Verification

| Verification | Expected result | Observed result |
|---|---|---|
| Account enabled | No | Confirmed |
| Group memberships | None | Confirmed |
| Application assignments | None | Confirmed |
| Active sessions | Revoked | Action performed |

## 6. Audit Log Verification

Reviewed Microsoft Entra Audit Logs and confirmed that the offboarding activities were recorded.

Events inspected:

| Activity | Category |
|---|---|
| Disable account | UserManagement |
| Update StsRefreshTokenValidFrom Timestamp | UserManagement |
| Remove member from group | GroupManagement |
| Remove app role assignment | UserManagement |

## 7. Security Concepts Learned

- Disabling an account prevents new sign-ins.
- Revoking sessions helps invalidate existing refresh-token-based sessions.
- Removing group memberships eliminates group-derived access.
- Direct application assignments must be removed separately.
- Audit logs provide evidence of identity lifecycle operations.
- Account disabling and access removal should be performed promptly during employee offboarding.

## 8. Important Considerations

Disabling an account and revoking sessions are important offboarding controls, but they do not automatically guarantee immediate termination of every possible access path.

Additional checks may be necessary for:
- Application-specific sessions and tokens.
- Direct permissions outside Entra group membership.
- Azure resource role assignments.
- Service accounts and privileged credentials.
- External applications and third-party access.

The identity should be retained according to the organization's retention and investigation policies before permanent deletion.

## 9. Conclusion

Successfully completed the Leaver scenario using Microsoft Entra ID.

The employee account was disabled, sessions were revoked, group memberships were removed, and the direct enterprise application assignment was removed. The corresponding audit events were also reviewed.

This exercise demonstrated the importance of timely access revocation during employee offboarding.
