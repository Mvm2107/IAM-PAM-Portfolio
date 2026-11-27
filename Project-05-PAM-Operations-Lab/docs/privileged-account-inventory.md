# Privileged Account Inventory

## 1. Overview

This document records the privileged account discovery performed as part of the Enterprise PAM Operations Lab.

The objective is to identify privileged identities across the Windows Active Directory environment, Windows workstation and Ubuntu Linux system.

The inventory establishes a baseline for privileged access reviews, least-privilege assessment and security monitoring.

## 2. Lab Environment

| Component | Details |
|---|---|
| Active Directory Server | DC01 |
| Domain | corp.example.com |
| NetBIOS Name | CORP |
| Domain Controller IP | 192.168.10.10 |
| Windows Client | DESKTOP-SD075Q6 |
| Windows Client IP | 192.168.10.20 |
| Ubuntu Hostname | soc-ubuntu-VirtualBox |
| Ubuntu IAM-LAB IP | 192.168.10.30 |
| SIEM | Splunk Enterprise |

## 3. Active Directory Privileged Groups

The following privileged security groups were inspected using PowerShell and Active Directory module commands.

### 3.1 Domain Admins

**Command:**

```powershell
Get-ADGroupMember -Identity "Domain Admins" -Recursive
```

**Discovery result:**

| Member | Account Type |
|---|---|
| Administrator | User |

**Group properties:**

| Property | Value |
|---|---|
| Group Name | Domain Admins |
| Group Scope | Global |
| Group Category | Security |
| Description | Designated administrators of the domain |

### 3.2 Enterprise Admins

**Command:**

```powershell
Get-ADGroupMember -Identity "Enterprise Admins" -Recursive
```

**Discovery result:**

| Member | Account Type |
|---|---|
| Administrator | User |

**Group properties:**

| Property | Value |
|---|---|
| Group Name | Enterprise Admins |
| Group Scope | Universal |
| Group Category | Security |
| Description | Designated administrators of the enterprise |

### 3.3 Administrators

**Command:**

```powershell
Get-ADGroupMember -Identity "Administrators" -Recursive
```

**Discovery result:**

| Member | Account Type |
|---|---|
| Administrator | User |

**Group properties:**

| Property | Value |
|---|---|
| Group Name | Administrators |
| Group Scope | Domain Local |
| Group Category | Security |
| Description | Administrators have complete and unrestricted access to the computer/domain |

### 3.4 Privileged Group Summary

| Group | Scope | Members Discovered |
|---|---|---:|
| Domain Admins | Global | 1 |
| Enterprise Admins | Universal | 1 |
| Administrators | Domain Local | 1 |

The built-in Administrator account was found in all three inspected groups.

## 4. Active Directory User Inventory

**Command:**

```powershell
Get-ADUser -Filter * -Properties Enabled, Description |
Select-Object Name, SamAccountName, Enabled, Description
```

A total of 15 domain user accounts were discovered.

### 4.1 Enabled Accounts

| Display Name | SamAccountName | Status |
|---|---|---|
| Administrator | Administrator | Enabled |
| Arun Kumar | arun.kumar | Enabled |
| Rahul Kumar | rahul.kumar | Enabled |
| Priya Kumari | priya.kumari | Enabled |
| Karthik Kumar | karthik.kumar | Enabled |
| Meera Sharma | meera.sharma | Enabled |
| Unlock Test | unlock.test | Enabled |
| Naveen Kumar | naveen.kumar | Enabled |
| Divya Raj | divya.raj | Enabled |
| Sanjay Kumar | sanjay.kumar | Enabled |
| Priya Anand | priya.anand | Enabled |
| Kiran Raj | kiran.raj | Enabled |

**Total enabled accounts: 12**

### 4.2 Disabled Accounts

| Display Name | SamAccountName | Status |
|---|---|---|
| Guest | Guest | Disabled |
| krbtgt | krbtgt | Disabled |
| Leaver Test | leaver.test | Disabled |

**Total disabled accounts: 3**

### 4.3 Account Status Summary

| Category | Count |
|---|---:|
| Total domain users | 15 |
| Enabled accounts | 12 |
| Disabled accounts | 3 |

Note: Account status was recorded from the Active Directory `Enabled` property. No account modifications were performed.

## 5. Windows Workstation Privileged Accounts

The local Administrators group on WIN10-CLIENT was inspected.

**Command:**

```powershell
Get-LocalGroupMember -Group "Administrators"
```

### 5.1 Local Administrators Group Membership

| Account | Principal Source | Object Type |
|---|---|---|
| CORP\Domain Admins | ActiveDirectory | Group |
| DESKTOP-SD075Q6\Administrator | Local | User |
| DESKTOP-SD075Q6\LabAdmin | Local | User |

The domain Domain Admins group is a member of the workstation's local Administrators group.

### 5.2 Local User Inventory

**Command:**

```powershell
Get-LocalUser |
Select-Object Name, Enabled, LastLogon, PasswordRequired
```

| Account | Enabled | Password Required |
|---|---|---|
| Administrator | False | True |
| DefaultAccount | False | False |
| Guest | False | False |
| LabAdmin | True | False |
| WDAGUtilityAccount | False | True |

Additional observation:

- LabAdmin was last logged in on November 18, 2026, at 4:02:02 AM.
- LabAdmin is a member of the local Administrators group.
- The `PasswordRequired` property for LabAdmin returned `False`.

**Important:** `PasswordRequired = False` does not establish whether a password is currently configured. This requires further verification.

## 6. Ubuntu Linux Privileged Account Inventory

The Ubuntu environment was inspected using Linux account and group discovery commands.

### 6.1 Root Account

**Command:**

```bash
getent passwd root
```

**Result:**

```text
root:x:0:0:root:/root:/bin/bash
```

| Attribute | Value |
|---|---|
| Account | root |
| UID | 0 |
| GID | 0 |
| Home Directory | /root |
| Login Shell | /bin/bash |

The root account is the primary administrative identity on the Linux system.

### 6.2 UID 0 Account Discovery

**Command:**

```bash
getent passwd | awk -F: '$3 == 0 {print $1, $3, $6, $7}'
```

**Result:**

```text
root 0 /root /bin/bash
```

Only one UID 0 account was discovered: root.

### 6.3 Sudo Group Membership

**Command:**

```bash
getent group sudo
```

**Result:**

```text
sudo:x:27:soc-ubuntu
```

The `soc-ubuntu` account is a member of the sudo group.

### 6.4 Sudo Privilege Verification

**Command:**

```bash
sudo -l
```

**Result:**

```text
User soc-ubuntu may run the following commands:
(ALL : ALL) ALL
```

This indicates unrestricted sudo permissions.

The `soc-ubuntu` account can execute commands as other users, including root.

### 6.5 ADM Group Membership

**Command:**

```bash
getent group adm
```

**Result:**

```text
adm:x:4:syslog,soc-ubuntu
```

The following accounts were identified as members:

- syslog
- soc-ubuntu

The `adm` group provides access to certain system log files.

## 7. Consolidated Privileged Account Inventory

| Environment | Account / Group | Privilege | Observation |
|---|---|---|---|
| Active Directory | Administrator | Domain Admin | Privileged |
| Active Directory | Administrator | Enterprise Admin | Privileged |
| Active Directory | Administrator | Administrators | Privileged |
| Windows Client | CORP\Domain Admins | Local Administrator membership | Privileged |
| Windows Client | Administrator | Local Administrator | Disabled |
| Windows Client | LabAdmin | Local Administrator | Enabled |
| Ubuntu | root | UID 0 | Full system privilege |
| Ubuntu | soc-ubuntu | Sudo | Unrestricted sudo |
| Ubuntu | soc-ubuntu | adm | Log access |
| Ubuntu | syslog | adm | Log access |

## 8. Security Observations

### Finding 1: Concentration of Active Directory Privileges

The built-in Administrator account belongs to Domain Admins, Enterprise Admins and Administrators.

**Recommendation:**
- Review privileged group memberships.
- Use separate administrative identities where appropriate.
- Restrict interactive use of highly privileged accounts.
- Monitor privileged authentication and group membership changes.

### Finding 2: Domain Admins Membership on Workstation

The CORP\Domain Admins group is included in the local Administrators group on WIN10-CLIENT.

**Recommendation:**
- Review whether workstation administration requires this level of privilege.
- Consider dedicated workstation administrator groups.
- Apply least-privilege principles.

### Finding 3: Local LabAdmin Account

The LabAdmin account is enabled and belongs to the local Administrators group.

Its `PasswordRequired` property returned False.

**Recommendation:**
- Verify password configuration.
- Review account ownership and purpose.
- Confirm whether permanent administrative privileges are necessary.

### Finding 4: Unrestricted Linux Sudo Permissions

The soc-ubuntu account has unrestricted sudo permissions.

**Recommendation:**
- Review administrative access requirements.
- Consider restricted sudo permissions for operational accounts.
- Monitor privileged command execution.

## 9. Discovery Methodology

The following tools and commands were used:

| Platform | Tool / Command | Purpose |
|---|---|---|
| Windows Server | Get-ADGroupMember | Privileged group discovery |
| Windows Server | Get-ADUser | Domain user inventory |
| Windows Server | Get-ADGroup | Group property inspection |
| Windows Client | Get-LocalGroupMember | Local administrator discovery |
| Windows Client | Get-LocalUser | Local account inventory |
| Ubuntu | getent passwd | User account discovery |
| Ubuntu | getent group | Group membership discovery |
| Ubuntu | sudo -l | Effective sudo privilege inspection |
| Ubuntu | awk | UID 0 account identification |

## 10. Conclusion

The discovery exercise successfully identified privileged identities across Active Directory, a Windows workstation and Ubuntu Linux.

The inventory established:

- Three inspected privileged Active Directory groups.
- Fifteen domain user accounts.
- Three local Windows Administrators group members.
- Local Windows account status.
- The Linux root account and UID 0 identities.
- Sudo and ADM group membership.

The results provide a baseline for the next phase of the Enterprise PAM Operations Lab: privileged access control and least-privilege assessment.

No accounts, passwords, group memberships or permissions were modified during this discovery exercise.

---

**Project:** Project-05-PAM-Operations-Lab  
**Document:** Privileged Account Inventory  
**Phase:** Phase 2 – Privileged Account Discovery  
**Environment:** Active Directory, Windows Client and Ubuntu Linux  
**Status:** Discovery completed; evidence screenshots pending upload.



## Phase 3 – Updated Privileged Account Inventory

### 1. Active Directory Privileged Groups

The following direct memberships were verified on DC01.

| Group | Scope | Category | Direct Member |
|---|---|---|---|
| Domain Admins | Global | Security | Administrator |
| Enterprise Admins | Universal | Security | Administrator |
| Administrators | Domain Local | Security | Administrator |

No domain-level privileged group memberships were modified during Phase 3.

### 2. WIN10-CLIENT Local Administrators

**Initial membership:**

| Account | Source |
|---|---|
| CORP\Domain Admins | Active Directory |
| DESKTOP-SD075Q6\Administrator | Local |
| DESKTOP-SD075Q6\LabAdmin | Local |

**Final membership after Phase 3:**

| Account | Source | Status |
|---|---|---|
| DESKTOP-SD075Q6\Administrator | Local | Retained |
| DESKTOP-SD075Q6\LabAdmin | Local | Retained |
| DESKTOP-SD075Q6\PAM-Recovery | Local | Created and retained |
| CORP\Domain Admins | Active Directory | Removed |

### 3. Standard Domain User

| Account | Group Membership | Validation |
|---|---|---|
| unlock.test | Domain Users | Standard-user access confirmed |

The account successfully authenticated to WIN10-CLIENT. The `net session` command returned System error 5 – Access is denied, both before and after the least-privilege change.

### 4. Recovery Administrator

| Property | Value |
|---|---|
| Account | PAM-Recovery |
| Account type | Local |
| Enabled | Yes |
| Group membership | Local Administrators |
| Purpose | Dedicated PAM lab recovery administrator |
| Interactive login | Verified |
| Elevated administrative access | Verified |

Windows UAC token filtering was observed during the initial non-elevated session. Administrative access was successfully verified after opening PowerShell with Run as administrator.

### 5. Inventory Assessment Notes

- Domain Admins no longer has local administrator access through direct membership on WIN10-CLIENT.
- Domain-level privileges remain unchanged.
- LabAdmin remains enabled and requires ownership and purpose verification.
- The built-in Administrator account remains a member of the inspected AD privileged groups.
- PAM-Recovery provides a tested local administrative recovery path.

**Assessment scope:** DC01 Active Directory privileged groups and WIN10-CLIENT local privileged accounts.
