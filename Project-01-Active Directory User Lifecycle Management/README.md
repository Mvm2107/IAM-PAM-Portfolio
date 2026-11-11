# Active Directory User Lifecycle Management

## Project Overview

This project demonstrates practical Identity and Access Management (IAM) operations using Microsoft Active Directory Domain Services (AD DS) and PowerShell.

The objective was to simulate common IAM helpdesk and identity administration responsibilities in a virtual lab environment.

The project covers the Joiner-Mover-Leaver (JML) lifecycle, password management, account lockout troubleshooting, and Active Directory group membership administration.

## Lab Environment

| Component | Configuration |
|---|---|
| Domain Controller | DC01 |
| Client Machine | WIN10-CLIENT |
| Server OS | Windows Server |
| Client OS | Windows 10 Pro |
| Domain | corp.example.com |
| NetBIOS | CORP |
| Domain Controller IP | 192.168.10.10 |
| Client IP | 192.168.10.20 |
| Virtual Network | IAM-LAB |
| Administration | PowerShell / Active Directory Module |

## 1. Joiner Process – New Employee Provisioning

### Scenario
A new employee, Meera Sharma, joins the HR department.

### Tasks performed
- Checked whether the username already existed.
- Verified the target OU and security group.
- Created the Active Directory user.
- Configured the username and UPN.
- Set an initial password using a SecureString.
- Moved the user into the HR OU.
- Configured password change at next logon.
- Enabled the account.
- Added the user to the HR_Users security group.
- Verified account attributes and group membership.

### PowerShell commands

```powershell
New-ADUser -Name "Meera Sharma" `
-SamAccountName "meera.sharma" `
-UserPrincipalName "meera.sharma@corp.example.com" `
-Path "OU=HR,DC=corp,DC=example,DC=com" `
-AccountPassword $Password `
-Enabled $false

Set-ADUser -Identity "Meera Sharma" `
-SamAccountName "meera.sharma" `
-UserPrincipalName "meera.sharma@corp.example.com"

Move-ADObject -Identity (Get-ADUser "meera.sharma").DistinguishedName `
-TargetPath "OU=HR,DC=corp,DC=example,DC=com"

Set-ADUser -Identity "meera.sharma" -ChangePasswordAtLogon $true

Enable-ADAccount -Identity "meera.sharma"

Add-ADGroupMember -Identity "HR_Users" -Members "meera.sharma"
```

### Verification
Confirmed:
- Correct username and UPN.
- Correct HR OU placement.
- Account enabled.
- HR_Users membership assigned.

## 2. Mover Process – Department Transfer

### Scenario
Meera Sharma transfers from HR to Finance.

### Approved changes
- Department: HR → Finance
- OU: HR → Finance
- Group membership: HR_Users → Finance_Read
- Account remains enabled.

### Tasks performed
- Inspected existing user attributes.
- Updated the Department attribute.
- Moved the user from HR OU to Finance OU.
- Added the user to Finance_Read.
- Removed obsolete HR_Users membership.
- Verified final account attributes and group memberships.

### PowerShell commands

```powershell
Set-ADUser -Identity "meera.sharma" -Department "Finance"

Get-ADUser -Identity "meera.sharma" |
Move-ADObject -TargetPath "OU=Finance,DC=corp,DC=example,DC=com"

Add-ADGroupMember -Identity "Finance_Read" -Members "meera.sharma"

Remove-ADGroupMember -Identity "HR_Users" `
-Members "meera.sharma" -Confirm:$true
```

### Verification
Confirmed:
- Department = Finance.
- OU = Finance.
- Finance_Read membership assigned.
- HR_Users membership removed.
- Domain Users membership retained.
- Account remained enabled.

## 3. Leaver Process – Employee Offboarding

### Scenario
A test employee, Leaver Test, leaves the organisation.

### Tasks performed
- Created a disposable test account.
- Assigned HR department attributes.
- Added the account to HR_Users.
- Disabled the account.
- Inspected existing group memberships.
- Removed HR_Users membership.
- Retained Domain Users membership.
- Verified account status and remaining access.

### PowerShell commands

```powershell
Disable-ADAccount -Identity "leaver.test"

Get-ADUser -Identity "leaver.test" -Properties Enabled

Remove-ADGroupMember -Identity "HR_Users" `
-Members "leaver.test" -Confirm:$true

Get-ADPrincipalGroupMembership -Identity "leaver.test"
```

### Verification
Confirmed:
- Account still exists.
- Enabled = False.
- HR_Users membership removed.
- Domain Users membership retained.
- Original AD object information preserved.

## 4. Password Management

### Scenario
A user requests an administrative password reset.

### Tasks performed
- Collected a temporary password securely.
- Reset the user's password.
- Verified PasswordLastSet.
- Checked PasswordExpired.
- Confirmed password reset did not automatically enable a disabled account.

### PowerShell commands

```powershell
$NewPassword = Read-Host "Enter new password" -AsSecureString

Set-ADAccountPassword -Identity "leaver.test" `
-NewPassword $NewPassword -Reset

Get-ADUser -Identity "leaver.test" `
-Properties PasswordLastSet, PasswordExpired, Enabled
```

## 5. Account Lockout and Unlock Troubleshooting

### Scenario
A domain user experiences account lockout after repeated failed authentication attempts.

### Initial domain policy

| Setting | Original value |
|---|---|
| LockoutThreshold | 0 |
| LockoutDuration | 30 minutes |
| LockoutObservationWindow | 30 minutes |

### Lab procedure

1. Inspected the original domain password policy.
2. Saved the original policy in a PowerShell variable.
3. Temporarily changed LockoutThreshold to 3.
4. Generated three controlled failed authentication attempts using unlock.test from WIN10-CLIENT.
5. Monitored BadPwdCount on DC01.
6. Confirmed LockedOut = True.
7. Restarted WIN10-CLIENT and observed that login was rejected.
8. Executed Unlock-ADAccount.
9. Verified LockedOut = False and BadPwdCount = 0.
10. Restored the original LockoutThreshold of 0.

### PowerShell commands

```powershell
Get-ADDefaultDomainPasswordPolicy

Set-ADDefaultDomainPasswordPolicy `
-Identity "corp.example.com" `
-LockoutThreshold 3

Get-ADUser -Identity "unlock.test" `
-Properties BadPwdCount, LockedOut, Enabled

Unlock-ADAccount -Identity "unlock.test"

Get-ADUser -Identity "unlock.test" `
-Properties BadPwdCount, LockedOut, Enabled

Set-ADDefaultDomainPasswordPolicy `
-Identity "corp.example.com" `
-LockoutThreshold 0
```

### Verification

| Property | Before unlock | After unlock |
|---|---|---|
| Enabled | True | True |
| LockedOut | True | False |
| BadPwdCount | 3 | 0 |

The original domain lockout policy was successfully restored.

## 6. Important PowerShell Commands Learned

| Command | Purpose |
|---|---|
| Get-ADUser | Retrieve user information |
| New-ADUser | Create user accounts |
| Set-ADUser | Modify user attributes |
| Move-ADObject | Move AD objects |
| Enable-ADAccount | Enable accounts |
| Disable-ADAccount | Disable accounts |
| Add-ADGroupMember | Grant group membership |
| Remove-ADGroupMember | Revoke group membership |
| Get-ADPrincipalGroupMembership | Inspect user group memberships |
| Set-ADAccountPassword | Reset passwords |
| Unlock-ADAccount | Unlock accounts |
| Get-ADDefaultDomainPasswordPolicy | Inspect domain password policy |
| Set-ADDefaultDomainPasswordPolicy | Modify domain password policy |

## 7. IAM Concepts Demonstrated

- Identity lifecycle management (Joiner-Mover-Leaver).
- Active Directory user administration.
- Organizational Unit management.
- Role and group-based access management.
- Least privilege and access revocation.
- Password reset procedures.
- Account enablement and disabling.
- Account lockout investigation.
- PowerShell-based IAM administration.
- Verification and troubleshooting.

## 8. Security and Lab Considerations

- All operations were performed in an isolated VirtualBox lab.
- Disposable accounts were used for testing.
- Passwords were collected using SecureString rather than hardcoded in commands.
- Group membership changes were verified after execution.
- Domain-wide lockout policy changes were temporary and restored after testing.
- No production accounts or systems were involved.


---

**Project type:** Hands-on IAM Lab  
**Technology:** Active Directory, PowerShell, Windows Server, Windows 10, VirtualBox  
**Status:** Manual JML and account management exercises completed.
