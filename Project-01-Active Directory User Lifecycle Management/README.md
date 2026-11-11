# Active Directory User Lifecycle Management Using PowerShell

## 1. Project Overview

### Objective

The objective of this project is to implement and troubleshoot common Identity and Access Management (IAM) operations using Microsoft Active Directory Domain Services (AD DS) and Windows PowerShell.

A virtual enterprise environment was configured to simulate identity administration tasks commonly performed by IAM Operations, Active Directory Administrators, and IT Helpdesk teams.

The project focuses on managing user identities throughout their lifecycle, controlling group-based access, handling password-related requests, and troubleshooting account lockouts.

### Scope

The following operations were implemented:

1. Joiner – New employee account provisioning.
2. Mover – Department transfer and access modification.
3. Leaver – Employee offboarding and access revocation.
4. Password Management – Administrative password reset.
5. Account Management – Enable and disable accounts.
6. Account Lockout – Investigate failed authentication and unlock accounts.
7. Security Policy – Inspect, temporarily modify, and restore domain lockout policy.

**Implementation approach:** All operations were first performed manually using individual PowerShell cmdlets to understand the underlying AD administration process before introducing automation.

---

## 2. Lab Architecture

### Environment Configuration

| Component | Configuration |
|---|---|
| Domain Controller | DC01 |
| Client Machine | WIN10-CLIENT |
| Server Operating System | Windows Server |
| Client Operating System | Windows 10 Pro |
| Domain Name | corp.example.com |
| NetBIOS Name | CORP |
| Domain Controller IP | 192.168.10.10 |
| Client IP | 192.168.10.20 |
| Virtual Network | IAM-LAB |
| Administration Tool | Windows PowerShell |
| PowerShell Module | ActiveDirectory |

### Lab Design

- DC01 hosts Active Directory Domain Services and DNS.
- WIN10-CLIENT is joined to the `corp.example.com` domain.
- Both virtual machines communicate through the VirtualBox internal network named `IAM-LAB`.
- User accounts, organisational units, and security groups are managed through DC01.
- Client-side authentication is tested from WIN10-CLIENT.

### Active Directory Structure

```text
corp.example.com
│
├── Domain Controllers
│
├── Finance
│   ├── arun.kumar
│   ├── rahul.kumar
│   └── meera.sharma (after transfer)
│
├── HR
│   ├── priya.kumari
│   └── leaver.test (disabled)
│
└── IT
    └── karthik.kumar
```

### Security Groups

| Group | Scope | Category | Purpose |
|---|---|---|---|
| Finance_Read | Global | Security | Read access to Finance resources |
| HR_Users | Global | Security | HR department access |
| IT_Support | Global | Security | IT support access |

### Initial Environment Validation

The AD PowerShell module was checked and imported.

```powershell
Get-Module -ListAvailable ActiveDirectory

Import-Module ActiveDirectory

Get-ADDomain
```

Domain connectivity was checked from the client.

```powershell
$env:LOGONSERVER

whoami

nltest /dsgetdc:corp.example.com
```

The client successfully identified DC01 as its domain controller.

---

## 3. Joiner – New Employee Provisioning

### Business Scenario

A new employee named Meera Sharma joins the HR department.

The IAM administrator receives an approved onboarding request and must create the employee's identity with the appropriate attributes and department access.

### Provisioning Requirements

| Attribute | Required Value |
|---|---|
| Employee Name | Meera Sharma |
| Username | meera.sharma |
| UPN | meera.sharma@corp.example.com |
| Department | HR |
| Target OU | HR |
| Security Group | HR_Users |
| Account Status | Enabled |
| Initial Password | Securely supplied |

### Step 1: Validate Existing Identity and Target Resources

Before creating the account, verify whether the username already exists.

```powershell
Get-ADUser -Filter "SamAccountName -eq 'meera.sharma'"
```

Verify the target OU and security group.

```powershell
Get-ADOrganizationalUnit -Identity "OU=HR,DC=corp,DC=example,DC=com"

Get-ADGroup -Identity "HR_Users"
```

**Why is this necessary?**

- Prevents duplicate identity creation.
- Confirms the destination OU exists.
- Confirms the required security group is available.
- Reduces provisioning errors.

### Step 2: Collect the Initial Password Securely

```powershell
$Password = Read-Host "Enter temporary password" -AsSecureString
```

`Read-Host` collects the password interactively, while `-AsSecureString` prevents the password from being displayed as ordinary plaintext input.

Passwords should not be hardcoded in scripts or committed to GitHub.

### Step 3: Create the AD Account

```powershell
New-ADUser `
-Name "Meera Sharma" `
-SamAccountName "meera.sharma" `
-UserPrincipalName "meera.sharma@corp.example.com" `
-Path "OU=HR,DC=corp,DC=example,DC=com" `
-AccountPassword $Password `
-Enabled $false
```

The account is initially created disabled so that the administrator can complete the remaining provisioning checks before enabling it.

### Step 4: Configure Identity Attributes

```powershell
Set-ADUser -Identity "meera.sharma" `
-SamAccountName "meera.sharma" `
-UserPrincipalName "meera.sharma@corp.example.com"
```

The Department attribute is populated separately.

```powershell
Set-ADUser -Identity "meera.sharma" -Department "HR"
```

### Step 5: Configure Password Change at First Logon

```powershell
Set-ADUser -Identity "meera.sharma" -ChangePasswordAtLogon $true
```

This requires the user to change the temporary password at their next eligible interactive logon.

### Step 6: Enable the Account

```powershell
Enable-ADAccount -Identity "meera.sharma"
```

### Step 7: Assign HR Group Membership

```powershell
Add-ADGroupMember -Identity "HR_Users" -Members "meera.sharma"
```

### Step 8: Verify the Provisioned Account

```powershell
Get-ADUser -Identity "meera.sharma" -Properties Department, Enabled |
Select-Object Name, SamAccountName, UserPrincipalName, Department, Enabled, DistinguishedName
```

Verify group membership.

```powershell
Get-ADPrincipalGroupMembership -Identity "meera.sharma" |
Select-Object Name, GroupScope, GroupCategory
```

### Expected Final State

- Correct username and UPN.
- Department set to HR.
- Account located in the HR OU.
- Account enabled.
- HR_Users membership assigned.
- Domain Users membership retained.

### Evidence

![Joiner verification](Screenshots/01-joiner-verification.png)

---

## 4. Mover – Department Transfer and Access Modification

### Business Scenario

Meera Sharma transfers from the HR department to Finance.

The approved lab scenario requires the administrator to update the department attribute, move the user to the Finance OU, grant the approved Finance_Read group membership, and remove obsolete HR_Users membership.

### Required Changes

| Attribute | Before | After |
|---|---|---|
| Department | HR | Finance |
| OU | HR | Finance |
| HR_Users | Member | Removed |
| Finance_Read | Not a member | Member |
| Account Status | Enabled | Enabled |

### Step 1: Inspect Existing User Attributes

```powershell
Get-ADUser -Identity "meera.sharma" -Properties Department, Title |
Select-Object Name, SamAccountName, Department, Title, DistinguishedName
```

### Step 2: Inspect Existing Group Memberships

```powershell
Get-ADPrincipalGroupMembership -Identity "meera.sharma" |
Select-Object Name, GroupScope, GroupCategory
```

### Step 3: Update Department

```powershell
Set-ADUser -Identity "meera.sharma" -Department "Finance"
```

**Important:** Updating the Department attribute does not move the user to another OU or automatically grant new access.

### Step 4: Move the User to Finance OU

```powershell
Get-ADUser -Identity "meera.sharma" |
Move-ADObject -TargetPath "OU=Finance,DC=corp,DC=example,DC=com"
```

### Step 5: Grant Finance Group Access

```powershell
Add-ADGroupMember -Identity "Finance_Read" -Members "meera.sharma"
```

This grants the group membership defined by the approved lab scenario.

### Step 6: Remove Obsolete HR Access

```powershell
Remove-ADGroupMember -Identity "HR_Users" `
-Members "meera.sharma" -Confirm:$true
```

The confirmation prompt provides an additional opportunity to verify the intended access change before execution.

### Step 7: Verify Final State

```powershell
Get-ADUser -Identity "meera.sharma" -Properties Department, Enabled |
Select-Object Name, SamAccountName, Department, Enabled, DistinguishedName
```

```powershell
Get-ADPrincipalGroupMembership -Identity "meera.sharma" |
Select-Object Name, GroupScope, GroupCategory
```

### Final Verification

| Check | Expected Result |
|---|---|
| Department | Finance |
| OU | Finance |
| Finance_Read | Member |
| HR_Users | Removed |
| Domain Users | Retained |
| Enabled | True |

### Evidence

![Mover verification](Screenshots/02-mover-verification.png)

---

## 5. Leaver – Employee Offboarding

### Business Scenario

An employee named Leaver Test leaves the organisation.

A separate disposable account is used to demonstrate the offboarding process without affecting existing lab users.

### Offboarding Requirements

- Disable the AD account.
- Revoke the employee's HR group membership.
- Retain the AD object for audit and retention handling.
- Verify that the account remains disabled.
- Verify that the obsolete group membership is removed.

### Step 1: Create a Disposable Test Account

```powershell
$Password = Read-Host "Enter temporary password" -AsSecureString
```

```powershell
New-ADUser `
-Name "Leaver Test" `
-SamAccountName "leaver.test" `
-UserPrincipalName "leaver.test@corp.example.com" `
-Path "OU=HR,DC=corp,DC=example,DC=com" `
-Department "HR" `
-AccountPassword $Password `
-Enabled $true
```

### Step 2: Assign Initial HR Group Access

```powershell
Add-ADGroupMember -Identity "HR_Users" -Members "leaver.test"
```

Verify initial membership.

```powershell
Get-ADPrincipalGroupMembership -Identity "leaver.test" |
Select-Object Name, GroupScope, GroupCategory
```

### Step 3: Disable the Account

```powershell
Disable-ADAccount -Identity "leaver.test"
```

Disabling prevents normal account authentication while preserving the AD object.

### Step 4: Inspect Group Membership

```powershell
Get-ADPrincipalGroupMembership -Identity "leaver.test" |
Select-Object Name, GroupScope, GroupCategory
```

Disabling an account does not automatically remove its group memberships.

### Step 5: Revoke HR Access

```powershell
Remove-ADGroupMember -Identity "HR_Users" `
-Members "leaver.test" -Confirm:$true
```

### Step 6: Verify Offboarding

```powershell
Get-ADUser -Identity "leaver.test" -Properties Department, Enabled |
Select-Object Name, SamAccountName, Department, Enabled, DistinguishedName
```

```powershell
