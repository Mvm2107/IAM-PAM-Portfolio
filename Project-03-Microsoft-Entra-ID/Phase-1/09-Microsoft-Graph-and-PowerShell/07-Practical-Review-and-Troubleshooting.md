# Practical Review and Troubleshooting

## 1. Introduction

This document records the practical review and troubleshooting exercises completed during the Microsoft Graph and PowerShell module.

The scenarios focused on common IAM responsibilities:

1. Investigating a disabled user account.
2. Troubleshooting Microsoft Graph permission errors.
3. Reviewing access during an employee transfer (Mover scenario).
4. Troubleshooting authorization failures during user creation.

The objective was to develop a structured investigation approach rather than immediately making changes to user accounts.

## 2. Scenario 1 – Investigating a Disabled User Account

### Scenario

An employee account belonging to Arun Kumar was found to be disabled.

The investigation required identifying the account's current status and determining what should be checked before reactivation.

### Investigation commands

Retrieve the user:

```powershell
Get-MgUser -UserId "<user-id>" -Property `
Id,DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle |
Format-List
```

Alternatively, filter disabled users:

```powershell
Get-MgUser -Filter "accountEnabled eq false" -Property `
DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle
```

### Observed findings

The account information retrieved during the practical review showed:

| Attribute | Observed value |
|---|---|
| Display name | Arun Kumar |
| Account enabled | False |
| Department | Finance Operations |
| Job title | Finance Operations Analyst |

### Investigation approach

Before reactivating an account, the following checks should be performed:

1. Confirm the employee's current employment status with HR.
2. Determine why the account was disabled.
3. Check whether an approved reactivation request exists.
4. Review the user's previous access and group memberships.
5. Check for any security-related reason for the account being disabled.
6. Confirm the required access before making changes.

### Key takeaway

A disabled account should not be enabled automatically.

IAM analysts must verify the business requirement, authorization and security context before changing account status.

---

## 3. Scenario 2 – Troubleshooting a Microsoft Graph 403 Error

### Scenario

A Microsoft Graph PowerShell command used to retrieve groups returned:

`403 Authorization_RequestDenied`

The investigation focused on identifying whether the problem was related to Graph permissions, admin consent or directory authorization.

### Initial troubleshooting

Check the current Graph authentication context:

```powershell
Get-MgContext
```

Inspect the granted scopes:

```powershell
(Get-MgContext).Scopes
```

Attempt to retrieve groups:

```powershell
Get-MgGroup -All -Property `
Id,DisplayName,Description,GroupTypes,SecurityEnabled,MailEnabled
```

### Investigation approach

The following checks were considered:

1. Verify that the Graph session is connected to the intended tenant.
2. Inspect the current delegated scopes.
3. Check whether `Group.Read.All` is available.
4. Verify whether the required consent has been granted.
5. Check whether the signed-in user has sufficient directory authorization.
6. Retry the command after resolving the permission issue.

### Resolution observed during the practical

The initial group retrieval failed because the required group-reading permission was not available in the authentication context.

`Group.Read.All` was requested and consented to. The group retrieval command was then executed successfully.

Two groups were returned:

- GRP-IT-Operations
- GRP-Finance-Operations

Both were identified as security-enabled groups with no mail enabled.

The group membership checks returned zero direct members for both groups.

### Important distinction

Microsoft Graph permissions and Microsoft Entra directory roles are different.

- Graph permissions define what an application or delegated session is allowed to request.
- Directory roles determine what administrative actions the signed-in user is authorized to perform.

Both must be considered when troubleshooting access failures.

### Key takeaway

A 403 error should be investigated systematically. Do not assume that having an administrator account automatically grants every Microsoft Graph permission.

---

## 4. Scenario 3 – Mover Scenario: Employee Department Transfer

### Scenario

An employee moves from one department to another.

For example, an employee transfers from IT Operations to Finance Operations.

The IAM analyst must determine whether the employee's existing access remains appropriate after the transfer.

### Investigation approach

The following steps were identified:

1. Confirm the department transfer with HR.
2. Review the employee's current department and job title.
3. Identify existing group memberships.
4. Review application access and assigned permissions.
5. Determine which old permissions are no longer required.
6. Identify the access required for the new department.
7. Obtain the necessary approvals.
8. Remove obsolete access and provision the approved new access.
9. Verify the changes and document the activity.

### Important considerations

- Do not remove all existing access without reviewing business requirements.
- Apply the principle of least privilege.
- Temporary access should have an appropriate expiry or review date.
- Group membership and application assignments must be checked separately.
- Updating a user's department attribute does not automatically change group memberships or application assignments.

### Practical observation

The Graph lab included updating the test user's department and job title.

The updated attributes were verified using:

```powershell
Get-MgUser -UserId "<user-id>" -Property `
DisplayName,Department,JobTitle |
Format-List
```

The group retrieval exercise also demonstrated that both queried security groups had zero direct members at the time of inspection.

### Key takeaway

A department attribute update is not the same as completing a Mover access-management process. The analyst must review and manage actual access separately.

---

## 5. Scenario 4 – Troubleshooting User-Creation Authorization

### Scenario

An IAM analyst attempts to create a new Entra user through Microsoft Graph PowerShell but receives a 403 authorization error.

The current Graph session has `User.Read.All`.

### Investigation approach

The following checks were identified:

1. Inspect the current Graph authentication context.
2. Verify whether the session contains an appropriate write permission.
3. Check whether `User.ReadWrite.All` has been requested and consented to.
4. Verify the signed-in user's directory authorization.
5. Confirm that the correct tenant and account are being used.
6. Retry the operation only after the required authorization is established.

### Relevant permission distinction

| Permission | Purpose |
|---|---|
| User.Read.All | Read user information across the directory |
| User.ReadWrite.All | Read and update user information across the directory |

`User.Read.All` is a read permission. It does not by itself authorize user creation.

The signed-in user must also have sufficient directory authorization for the requested operation.

### Key takeaway

When an operation requires write access, check both the required Graph permission and the signed-in user's authorization. A read-only permission is insufficient for user creation.

---

## 6. Troubleshooting Commands Practised

The following commands were used or reviewed during the practical exercises.

| Command | Purpose |
|---|---|
| `Get-MgContext` | Inspect the current Graph connection |
| `(Get-MgContext).Scopes` | Review available delegated scopes |
| `Connect-MgGraph` | Establish a Graph session |
| `Disconnect-MgGraph` | Disconnect the current Graph session |
| `Get-MgUser` | Retrieve user information |
| `Get-MgGroup` | Retrieve group information |
| `Get-MgGroupMember` | Retrieve direct group members |
| `Get-MgUserMemberOf` | Retrieve user membership objects |
| `Update-MgUser` | Update user attributes or account status |
| `New-MgUser` | Create a user |
| `Format-List` | Display object properties in list format |
| `Where-Object` | Filter returned objects |

## 7. Important Lessons from Module 9

### Authentication and authorization

- A successful Graph connection does not guarantee that every API operation will succeed.
- Required scopes must be available in the session.
- Admin consent may be required for particular permissions.
- Directory roles and Graph permissions are separate authorization considerations.

### User and group management

- Explicitly select the properties required when retrieving user information.
- Use filters to identify enabled and disabled accounts.
- Updating user attributes does not automatically update group memberships.
- Group membership and enterprise application assignments are separate access checks.

### Automation

- Use `-ErrorAction Stop` when an error needs to be handled by a `catch` block.
- Use `try/catch` to handle failures.
- Validate exported reports.
- Protect CSV reports because they may contain organisational and personal information.

### Session management

The Graph session in the practical was configured with `ContextScope: Process`.

When the PowerShell process terminates, its process-scoped context normally ends with it. Explicitly using `Disconnect-MgGraph` is still a good practice when finishing a session.

## 8. Practical Review Summary

| Scenario | Main learning outcome |
|---|---|
| Disabled user investigation | Verify the business and security reason before reactivation |
| Graph 403 troubleshooting | Check scopes, consent and directory authorization |
| Mover scenario | Review old and new access independently |
| User-creation authorization | Understand read versus write permissions |

## 9. Conclusion

The practical review covered common IAM investigation and troubleshooting situations using Microsoft Graph PowerShell.

The exercises reinforced the importance of verifying authorization, reviewing account status, understanding group memberships, managing access changes carefully and documenting administrative activities.

These investigation methods are relevant to entry-level IAM Analyst and Identity Operations responsibilities.
