# Creating and Updating Users – Microsoft Graph PowerShell

## 1. Introduction

Microsoft Graph PowerShell SDK allows IAM administrators to perform user lifecycle operations in Microsoft Entra ID.

Common operations include:

- Creating user accounts
- Updating user attributes
- Enabling and disabling accounts
- Managing identity information
- Verifying directory changes

This practical used a dedicated test account named **Graph Lab User** to demonstrate user lifecycle operations.

## 2. Understanding Read and Write Permissions

Microsoft Graph permissions determine which directory operations an application can request.

| Permission | Purpose |
|---|---|
| User.Read | Read the signed-in user's profile |
| User.Read.All | Read user profiles across the directory |
| User.ReadWrite.All | Read and modify user profiles |

During the practical, `User.ReadWrite.All` was requested and consented to.

The active Graph context was checked using:

```powershell
(Get-MgContext).Scopes | Sort-Object
```

The write permission was verified before attempting user creation.

**Important:** Graph permissions and the signed-in user's directory authorization are separate requirements. Both must be considered before performing a write operation.

## 3. Checking Whether a User Already Exists

Before creating a new account, the proposed username was checked to avoid an unintended duplicate.

Command:

```powershell
Get-MgUser -Filter "startsWith(userPrincipalName,'graph.lab.user')" `
-Property Id,DisplayName,UserPrincipalName,AccountEnabled |
Select-Object DisplayName,UserPrincipalName,AccountEnabled
```

The query returned no matching users.

This indicated that no existing account matched the search criteria at the time of the check.

## 4. Creating a New User

A dedicated test account was created using the `New-MgUser` cmdlet.

### Test account details

| Attribute | Value |
|---|---|
| Display name | Graph Lab User |
| Username | graph.lab.user |
| Department | IT Operations |
| Job title | IAM Lab Analyst |
| Usage location | IN |
| Account enabled | True |
| Force password change | True |

### Preparing a temporary password

A secure string was collected using:

```powershell
$password = Read-Host "Enter a temporary password" -AsSecureString

$plainPassword = [System.Net.NetworkCredential]::new("", $password).Password
```

### Creating the account

```powershell
New-MgUser `
-AccountEnabled:$true `
-DisplayName "Graph Lab User" `
-MailNickname "graph.lab.user" `
-UserPrincipalName "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-UsageLocation "IN" `
-Department "IT Operations" `
-JobTitle "IAM Lab Analyst" `
-PasswordProfile @{
    Password = $plainPassword
    ForceChangePasswordNextSignIn = $true
}
```

After creation, the temporary password variables were cleared:

```powershell
Remove-Variable password,plainPassword
```

### Practical result

The account was successfully created.

The returned user object included:

- Display name
- User principal name
- Object ID
- Account enabled status

## 5. Verifying the Created User

After creation, the account was retrieved using `Get-MgUser`.

```powershell
Get-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-Property Id,DisplayName,UserPrincipalName,AccountEnabled,UsageLocation,Department,JobTitle |
Format-List Id,DisplayName,UserPrincipalName,AccountEnabled,UsageLocation,Department,JobTitle
```

### Verified attributes

| Attribute | Result |
|---|---|
| Display name | Graph Lab User |
| Account enabled | True |
| Usage location | IN |
| Department | IT Operations |
| Job title | IAM Lab Analyst |

The returned object confirmed that the expected attributes were saved.

## 6. Updating User Attributes – Mover Scenario

A Mover scenario was simulated by changing the test user's department and job title.

### Before the update

| Attribute | Value |
|---|---|
| Department | IT Operations |
| Job title | IAM Lab Analyst |

### Update command

```powershell
Update-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-Department "Finance Operations" `
-JobTitle "Finance Operations Analyst"
```

### After the update

| Attribute | Value |
|---|---|
| Department | Finance Operations |
| Job title | Finance Operations Analyst |

The update command completed successfully.

The user's Object ID remained unchanged because the operation modified an existing user object rather than creating a new identity.

**Important:** Updating department and job title does not automatically modify group memberships or application assignments.

## 7. Disabling a User Account

Account disablement was performed using `Update-MgUser`.

Command:

```powershell
Update-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-AccountEnabled:$false
```

The account status was verified:

```powershell
Get-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-Property DisplayName,AccountEnabled |
Format-List DisplayName,AccountEnabled
```

### Practical result

```text
DisplayName    : Graph Lab User
AccountEnabled : False
```

The account was successfully disabled.

## 8. Reactivating a User Account

The account was re-enabled to make it available for further practical exercises.

Command:

```powershell
Update-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-AccountEnabled:$true
```

Verification:

```powershell
Get-MgUser `
-UserId "graph.lab.user@manivannanm2107gmail.onmicrosoft.com" `
-Property DisplayName,AccountEnabled |
Format-List DisplayName,AccountEnabled
```

### Practical result

```text
DisplayName    : Graph Lab User
AccountEnabled : True
```

The account was successfully re-enabled.

## 9. Audit Log Investigation

After performing the lifecycle operations, Microsoft Entra audit logs were inspected.

Navigation:

Microsoft Entra admin center → Identity → Monitoring & health → Audit logs

The relevant user-management events were investigated.

### Observed events

| Activity | Result |
|---|---|
| Add user | Successful |
| Update PasswordProfile | Successful |
| Update user | Successful |
| Disable account | Successful |

The audit records identified:

- Initiating application: Microsoft Graph Command Line Tools
- Target: Graph Lab User
- Activity details
- Modified properties
- Old and new values where available

The account disablement event included:

| Property | Old value | New value |
|---|---|---|
| AccountEnabled | true | false |

The department and job-title changes were also located in the corresponding modified-properties details.

These observations demonstrated how Graph operations can be correlated with Microsoft Entra audit records.

## 10. Important IAM Considerations

Before performing user lifecycle operations in a production environment, an IAM analyst should:

1. Verify the employee's identity.
2. Confirm the business request with HR or an authorized manager.
3. Check the required Graph permissions.
4. Verify the user's current access.
5. Obtain appropriate approval.
6. Perform only the authorized operation.
7. Verify the result.
8. Review audit evidence.
9. Document the change.

Disabling an account does not automatically remove group memberships, application assignments or every existing session.

Similarly, updating a department does not automatically provision or remove access unless separate automation or access-management rules are configured.

## 11. Key Takeaways

- `New-MgUser` creates an Entra user.
- `Update-MgUser` modifies supported user properties.
- `AccountEnabled` controls whether an account is enabled or disabled.
- User attributes can be updated independently of group membership.
- A user's Object ID remains unchanged when their attributes are updated.
- Read and write permissions must be distinguished.
- Microsoft Entra audit logs provide evidence of directory changes.
- User lifecycle operations should follow approval and verification procedures.

## Conclusion

This practical demonstrated user creation, attribute modification, account disablement and reactivation using Microsoft Graph PowerShell.

The operations were performed on a dedicated test account and verified through directory queries and Microsoft Entra audit logs.
