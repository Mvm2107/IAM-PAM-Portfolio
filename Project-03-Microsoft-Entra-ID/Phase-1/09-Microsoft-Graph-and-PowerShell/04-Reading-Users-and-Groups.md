# Reading Users and Groups – Microsoft Graph PowerShell

## 1. Introduction

IAM analysts regularly investigate user accounts, security groups and group memberships in Microsoft Entra ID.

Microsoft Graph PowerShell SDK provides cmdlets to retrieve directory objects and inspect their properties.

This practical focused on reading directory information without making unnecessary changes to existing accounts or groups.

## 2. Retrieving Entra ID Users

The `Get-MgUser` cmdlet retrieves user objects from Microsoft Entra ID.

Basic command:

```powershell
Get-MgUser
```

To retrieve all users:

```powershell
Get-MgUser -All
```

The `-All` parameter retrieves all available results by handling pagination.

To retrieve selected properties:

```powershell
Get-MgUser -All -Property Id,DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle
```

### Practical observation

The tenant inventory returned four user objects:

- Arun Kumar
- Graph Lab User
- Manivannan M
- Priya Sharma

The user inventory included account status and other directory attributes.

## 3. Selecting Specific User Properties

PowerShell's `Select-Object` cmdlet displays only the properties required for an investigation.

Example:

```powershell
Get-MgUser -All |
Select-Object DisplayName,UserPrincipalName,AccountEnabled
```

To display additional employment attributes:

```powershell
Get-MgUser -All -Property DisplayName,Department,JobTitle |
Select-Object DisplayName,Department,JobTitle
```

This helps IAM analysts focus on relevant identity information rather than displaying every available property.

## 4. Filtering Enabled and Disabled Accounts

The `-Filter` parameter supports filtering users using Microsoft Graph OData filter expressions.

### Enabled accounts

```powershell
Get-MgUser -Filter "accountEnabled eq true" `
-Property DisplayName,UserPrincipalName,AccountEnabled |
Select-Object DisplayName,UserPrincipalName,AccountEnabled
```

### Disabled accounts

```powershell
Get-MgUser -Filter "accountEnabled eq false" `
-Property DisplayName,UserPrincipalName,AccountEnabled |
Select-Object DisplayName,UserPrincipalName,AccountEnabled
```

### Practical observation

The tenant contained:

- Two enabled accounts
- Two disabled accounts

The results were consistent with the user inventory retrieved during the exercise.

## 5. Retrieving a Specific User

The `-UserId` parameter can identify a user using a supported user identifier, such as the user's object ID or user principal name.

Example:

```powershell
Get-MgUser -UserId "user@contoso.com" `
-Property Id,DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle |
Format-List DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle
```

This is useful when investigating a specific identity.

### Practical investigation: Arun Kumar

The user object was inspected using `Get-MgUser`.

Observed attributes:

| Attribute | Value |
|---|---|
| Display name | Arun Kumar |
| Account enabled | False |
| Department | Finance Operations |
| Job title | Finance Operations Analyst |

The account was disabled, and the department and job title reflected the Finance Operations role.

The investigation did not re-enable the account.

## 6. Retrieving Security Groups

The `Get-MgGroup` cmdlet retrieves group objects.

Basic command:

```powershell
Get-MgGroup -All
```

To retrieve selected group properties:

```powershell
Get-MgGroup -All -Property Id,DisplayName,Description,GroupTypes,SecurityEnabled,MailEnabled |
Select-Object DisplayName,Description,GroupTypes,SecurityEnabled,MailEnabled |
Format-List
```

### Practical observation

Two security groups were retrieved:

| Group | Description |
|---|---|
| GRP-IT-Operations | Security group for IT Operations employees |
| GRP-Finance-Operations | Security group for Finance Operations employees |

Both groups showed:

- SecurityEnabled: True
- MailEnabled: False
- GroupTypes: Empty

The empty GroupTypes property was consistent with the groups being security groups rather than Microsoft 365 groups.

## 7. Investigating Group Membership

The `Get-MgGroupMember` cmdlet retrieves the direct members of a group.

First, retrieve a group:

```powershell
$group = Get-MgGroup -Filter "displayName eq 'GRP-IT-Operations'"
```

Then retrieve its members:

```powershell
Get-MgGroupMember -GroupId $group.Id -All
```

To count direct members:

```powershell
Get-MgGroupMember -GroupId $group.Id -All |
Measure-Object
```

### Practical observation

Both inspected groups returned zero direct members.

The Finance Operations group was checked separately, and its membership count was also zero.

This was an actual tenant observation, not an assumption based on the group names.

## 8. Investigating User Group Membership

The `Get-MgUserMemberOf` cmdlet retrieves the directory objects of which a user is a direct member.

Example:

```powershell
Get-MgUserMemberOf -UserId "user@contoso.com" -All
```

To count the returned membership objects:

```powershell
Get-MgUserMemberOf -UserId "user@contoso.com" -All |
Measure-Object
```

### Practical observation

Priya Sharma's membership investigation returned a count of zero.

This confirmed that the command did not return any direct membership objects for that user in the practical exercise.

A zero result should be interpreted in the context of the query and permissions. It should not automatically be treated as proof that no access exists anywhere in the tenant.

## 9. Understanding Group Membership

A security group can be used to organize users and assign access to resources.

Examples:

| Group | Intended purpose |
|---|---|
| GRP-IT-Operations | Organize IT Operations identities |
| GRP-Finance-Operations | Organize Finance Operations identities |

IAM analysts should investigate:

- Group purpose and description
- Group type
- Security-enabled status
- Direct membership
- Nested membership where applicable
- Application assignments
- Whether access is still required

Group membership and application assignment are separate concepts. Membership in a group does not automatically prove that the group has access to a particular application.

## 10. Troubleshooting and Permission Requirements

During the practical exercise, an attempt to retrieve groups initially returned:

```text
Status: 403 Forbidden
ErrorCode: Authorization_RequestDenied
Insufficient privileges to complete the operation.
```

The active Graph scopes were inspected:

```powershell
(Get-MgContext).Scopes | Sort-Object
```

The `Group.Read.All` permission was subsequently requested and granted through the Graph authentication consent process.

Afterward, group retrieval succeeded:

```powershell
Get-MgGroup -All
```

This demonstrated the importance of checking the active Graph authentication context and delegated permissions when troubleshooting authorization errors.

## 11. Important Cmdlets

| Cmdlet | Purpose |
|---|---|
| Get-MgUser | Retrieve user objects |
| Get-MgGroup | Retrieve group objects |
| Get-MgGroupMember | Retrieve direct group members |
| Get-MgUserMemberOf | Retrieve a user's direct membership objects |
| Select-Object | Select specific properties |
| Where-Object | Filter PowerShell objects |
| Measure-Object | Count or measure returned objects |
| Format-List | Display object properties vertically |
| Format-Table | Display results in tabular form |

## 12. Key Takeaways

- `Get-MgUser` retrieves Entra ID user objects.
- `-All` handles retrieval across paginated results.
- `-Filter` supports filtering with OData expressions.
- `Get-MgGroup` retrieves directory groups.
- `Get-MgGroupMember` investigates direct group membership.
- `Get-MgUserMemberOf` investigates a user's direct membership objects.
- Graph permissions must support the requested operation.
- Group membership and application access should be investigated separately.

## Conclusion

This practical demonstrated how to retrieve and investigate users, security groups and membership information using Microsoft Graph PowerShell.

These skills provide an important foundation for IAM investigations, access reviews and user lifecycle management.
