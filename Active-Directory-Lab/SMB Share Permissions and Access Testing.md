## SMB Share Permissions and Access Testing

### 1. Finance SMB Share Creation

Created an SMB network share on the Domain Controller.

| Property | Value |
|---|---|
| Share Name | Finance |
| Folder Path | `C:\CompanyData\Finance` |
| Network Path | `\\DC01\Finance` |

PowerShell command:

```powershell
New-SmbShare -Name "Finance" `
-Path "C:\CompanyData\Finance" `
-ReadAccess "CORP\Finance_Read" `
-FullAccess "BUILTIN\Administrators"
```

### 2. SMB Share Permissions

Verified share-level permissions using:

```powershell
Get-SmbShareAccess -Name "Finance"
```

| Account | Permission |
|---|---|
| CORP\Finance_Read | Read |
| BUILTIN\Administrators | Full Control |

### 3. NTFS Permissions

Verified filesystem permissions using:

```powershell
Get-Acl "C:\CompanyData\Finance" |
Select-Object -ExpandProperty Access
```

| Account | NTFS Permission |
|---|---|
| NT AUTHORITY\SYSTEM | Full Control |
| BUILTIN\Administrators | Full Control |
| CORP\Finance_Read | Read & Execute |

### 4. Client Access Testing

Logged in to WIN10-CLIENT using the standard domain account:

`CORP\arun.kumar`

Accessed the Finance network share:

```text
\\DC01\Finance
```

Verification:

```powershell
Get-ChildItem "\\DC01\Finance"
Get-Content "\\DC01\Finance\report.txt"
```

**Result:** Arun successfully accessed the Finance share and read `report.txt`.

### 5. Modification Restriction Testing

Attempted to modify the Finance report using Arun's account.

**Result:** Windows denied the modification because the account had read-only effective access.

### 6. Effective Permission Analysis

| Permission Layer | Permission |
|---|---|
| SMB Share | Read |
| NTFS | Read & Execute |
| Effective Network Access | Read |

The more restrictive permission applies when accessing the folder through the SMB network share.

### 7. Password Reset vs Account Unlock

| Operation | Purpose |
|---|---|
| Password Reset | Used when a user forgets their password or requires a password change |
| Account Unlock | Used when an account is locked, commonly after repeated failed authentication attempts |

### 8. Access-Denied Troubleshooting Workflow

When a user cannot access a shared folder, investigate:

1. Verify the user's AD account status.
2. Check the user's security group membership.
3. Verify SMB share permissions.
4. Verify NTFS permissions and inherited ACLs.
5. Check explicit Deny entries.
6. Check whether recent group membership changes require a fresh logon session.
7. Document the findings and resolution.

**Learning Outcome:** Practised group-based access management, SMB share configuration, NTFS permission verification and client-side access testing using Active Directory domain accounts.
