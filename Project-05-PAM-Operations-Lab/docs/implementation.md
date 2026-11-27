# Implementation – Enterprise PAM Operations Lab

## 1. Overview

This document records the practical implementation and verification activities performed during the Enterprise PAM Operations Lab.

The implementation covers:

- Lab environment verification.
- Ubuntu network configuration.
- OpenSSH Server installation and verification.
- Active Directory privileged group discovery.
- Domain user inventory.
- Windows workstation local administrator discovery.
- Ubuntu privileged account discovery.
- Splunk Enterprise verification.

All activities documented here were performed using the existing lab environment.

**Important:** This project demonstrates PAM-related administration and operational controls. It does not represent a full CyberArk PAM deployment.

---

## 2. Lab Environment Verification

The following systems were verified before beginning the implementation.

| Component | Hostname | IP Address | Status |
|---|---|---|---|
| Domain Controller | DC01 | 192.168.10.10 | Working |
| Windows Client | DESKTOP-SD075Q6 | 192.168.10.20 | Working |
| Ubuntu | soc-ubuntu-VirtualBox | 192.168.10.30 | Working |
| Splunk | Local Windows Desktop | localhost:8000 | Working |

Active Directory domain:

```text
corp.example.com
```

NetBIOS domain:

```text
CORP
```

---

## 3. Ubuntu Network Configuration

### 3.1 Initial Network Inspection

The following commands were used to inspect Ubuntu network interfaces and routing.

```bash
ip -br addr
```

```bash
ip route
```

Initial observations:

- Ubuntu had a NAT interface named `enp0s3`.
- The NAT interface received IPv4 address `10.0.2.15`.
- The internal lab interface `enp0s8` was initially disconnected.

### 3.2 Internal Network Configuration

Ubuntu was configured with a second VirtualBox network adapter attached to the Internal Network named `IAM-LAB`.

A NetworkManager connection was created for the interface `enp0s8`.

**Configuration command:**

```bash
sudo nmcli connection add \
type ethernet \
con-name IAM-LAB \
ifname enp0s8 \
ipv4.method manual \
ipv4.addresses 192.168.10.30/24 \
ipv4.never-default yes \
ipv6.method disabled
```

The connection was activated:

```bash
sudo nmcli connection up IAM-LAB
```

### 3.3 Network Verification

```bash
ip -br addr
```

Observed configuration:

| Interface | IPv4 Address | Purpose |
|---|---|---|
| enp0s3 | 10.0.2.15/24 | NAT |
| enp0s8 | 192.168.10.30/24 | IAM-LAB |

The routing table was checked using:

```bash
ip route
```

The internal network route was available through `enp0s8`.

The NAT interface remained the default route.

### 3.4 Connectivity Verification

Ubuntu connectivity to DC01 was tested using:

```bash
ping -c 4 192.168.10.10
```

After resolving an initial connectivity issue, all four packets were received successfully.

The ARP neighbor entry was inspected using:

```bash
ip neigh show dev enp0s8
```

DC01 was identified as a reachable neighbor.

### 3.5 Active Directory DNS Resolution

The following commands were executed:

```bash
nslookup dc01.corp.example.com 192.168.10.10
```

```bash
nslookup corp.example.com 192.168.10.10
```

Both names resolved to:

```text
192.168.10.10
```

Some DNS queries experienced initial timeouts before returning the expected records. This behavior was noted for further troubleshooting.

---

## 4. OpenSSH Server Installation and Configuration

### 4.1 Initial Service Inspection

The SSH service was initially unavailable.

The installed package was inspected:

```bash
dpkg -l openssh-server
```

The package was not installed.

### 4.2 Package Installation

Package information was refreshed:

```bash
sudo apt update
```

OpenSSH Server was installed:

```bash
sudo apt install openssh-server -y
```

### 4.3 Enable and Start SSH

The SSH service was enabled and started:

```bash
sudo systemctl enable --now ssh
```

Service status was verified:

```bash
systemctl status ssh --no-pager
```

Observed result:

```text
Active: active (running)
Loaded: loaded
enabled
```

### 4.4 SSH Port Verification

The listening port was inspected:

```bash
sudo ss -tlnp | grep ':22'
```

The output confirmed that SSH was listening on TCP port 22.

### 4.5 Remote Connectivity Test

From DC01, Windows PowerShell was used to test the Ubuntu SSH port.

```powershell
Test-NetConnection 192.168.10.30 -Port 22
```

Observed result:

```text
ComputerName     : 192.168.10.30
RemotePort       : 22
SourceAddress    : 192.168.10.10
TcpTestSucceeded : True
```

**Result:** DC01 successfully established a TCP connection to the Ubuntu SSH service.

Note: This verifies network-level SSH connectivity. An interactive SSH authentication session was not documented as completed.

---

## 5. Active Directory Privileged Group Discovery

All Active Directory discovery activities were performed on DC01 using elevated Windows PowerShell.

### 5.1 Domain Admins Discovery

Command:

```powershell
Get-ADGroupMember -Identity "Domain Admins" -Recursive |
Select-Object Name, SamAccountName, ObjectClass
```

Observed member:

```text
Administrator
```

### 5.2 Enterprise Admins Discovery

Command:

```powershell
Get-ADGroupMember -Identity "Enterprise Admins" -Recursive |
Select-Object Name, SamAccountName, ObjectClass
```

Observed member:

```text
Administrator
```

### 5.3 Administrators Group Discovery

Command:

```powershell
Get-ADGroupMember -Identity "Administrators" -Recursive |
Select-Object Name, SamAccountName, ObjectClass
```

Observed member:

```text
Administrator
```

### 5.4 Group Properties Inspection

The properties of each group were inspected.

Domain Admins:

```powershell
Get-ADGroup "Domain Admins" -Properties Description, GroupScope, GroupCategory |
Select-Object Name, Description, GroupScope, GroupCategory
```

Enterprise Admins:

```powershell
Get-ADGroup "Enterprise Admins" -Properties Description, GroupScope, GroupCategory |
Select-Object Name, Description, GroupScope, GroupCategory
```

Administrators:

```powershell
Get-ADGroup "Administrators" -Properties Description, GroupScope, GroupCategory |
Select-Object Name, Description, GroupScope, GroupCategory
```

Observed results:

| Group | Scope | Category |
|---|---|---|
| Domain Admins | Global | Security |
| Enterprise Admins | Universal | Security |
| Administrators | Domain Local | Security |

The built-in Administrator account was identified in all three inspected groups.

---

## 6. Active Directory User Discovery

All domain user accounts were retrieved using:

```powershell
Get-ADUser -Filter * -Properties Enabled, Description |
Select-Object Name, SamAccountName, Enabled, Description
```

The discovery returned 15 accounts.

### 6.1 Results

| Account | Status |
|---|---|
| Administrator | Enabled |
| arun.kumar | Enabled |
| rahul.kumar | Enabled |
| priya.kumari | Enabled |
| karthik.kumar | Enabled |
| meera.sharma | Enabled |
| Guest | Disabled |
| krbtgt | Disabled |
| leaver.test | Disabled |
| unlock.test | Enabled |
| naveen.kumar | Enabled |
| divya.raj | Enabled |
| sanjay.kumar | Enabled |
| priya.anand | Enabled |
| kiran.raj | Enabled |

### 6.2 Results Summary

| Category | Count |
|---|---:|
| Total accounts | 15 |
| Enabled | 12 |
| Disabled | 3 |

The account status was recorded without changing any account properties.

---

## 7. Windows Workstation Privileged Account Discovery

The Windows workstation was identified as:

```text
DESKTOP-SD075Q6
```

The workstation's local Administrators group was inspected.

### 7.1 Local Administrators Group

Command:

```powershell
Get-LocalGroupMember -Group "Administrators" |
Select-Object Name, ObjectClass, PrincipalSource
```

Observed results:

| Name | Object Class | Principal Source |
|---|---|---|
| CORP\Domain Admins | Group | ActiveDirectory |
| DESKTOP-SD075Q6\Administrator | User | Local |
| DESKTOP-SD075Q6\LabAdmin | User | Local |

This confirmed that the domain Domain Admins group was included in the workstation's local Administrators group.

### 7.2 Local User Discovery

Command:

```powershell
Get-LocalUser |
Select-Object Name, Enabled, LastLogon, PasswordRequired
```

Observed results:

| Account | Enabled | Password Required |
|---|---|---|
| Administrator | False | True |
| DefaultAccount | False | False |
| Guest | False | False |
| LabAdmin | True | False |
| WDAGUtilityAccount | False | True |

Additional observation:

LabAdmin was last logged in on November 18, 2026, at 4:02:02 AM.

The PasswordRequired property returned False for LabAdmin. This property alone does not establish whether the account currently has a configured password.

### 7.3 Current User Identity and Group Membership

The logged-in identity was inspected:

```powershell
whoami
```

Observed identity:

```text
corp\administrator
```

The current security token was inspected:

```powershell
whoami /groups
```

The output included:

```text
BUILTIN\Administrators
```

with enabled group membership attributes.

This confirmed that the current session had administrative group membership.

---

## 8. Ubuntu Privileged Account Discovery

Linux account discovery was performed on the Ubuntu server.

### 8.1 Root Account Identification

Command:

```bash
getent passwd root
```

Observed result:

```text
root:x:0:0:root:/root:/bin/bash
```

This identified root as the primary Linux superuser.

### 8.2 UID 0 Account Discovery

Command:

```bash
getent passwd | awk -F: '$3 == 0 {print $1, $3, $6, $7}'
```

Observed result:

```text
root 0 /root /bin/bash
```

Only one UID 0 account was identified.

### 8.3 Sudo Group Membership

Command:

```bash
getent group sudo
```

Observed result:

```text
sudo:x:27:soc-ubuntu
```

The `soc-ubuntu` account was identified as a member of the sudo group.

### 8.4 Sudo Permission Inspection

Command:

```bash
sudo -l
```

Observed result:

```text
User soc-ubuntu may run the following commands:
(ALL : ALL) ALL
```

This demonstrated unrestricted sudo privileges for the `soc-ubuntu` account.

### 8.5 ADM Group Membership

Command:

```bash
getent group adm
```

Observed result:

```text
adm:x:4:syslog,soc-ubuntu
```

The accounts `syslog` and `soc-ubuntu` were identified as members of the ADM group.

---

## 9. Splunk Enterprise Verification

Splunk Enterprise was running locally on the Windows desktop.

The web interface was accessed at:

```text
http://localhost:8000
```

The Administrator account successfully accessed Splunk Search & Reporting.

### 9.1 Internal Index Search

The following search was executed:

```spl
index=_internal | head 10
```

Observed result:

- Search completed successfully.
- Ten internal events were returned.
- Splunk internal logging events were visible.
- The search interface and internal index were functioning.

**Result:** Splunk Enterprise installation and internal search functionality were verified.

Windows Security Event Log and Ubuntu authentication log ingestion were not verified during this initial environment check. Those activities remain part of the later monitoring phase.

---

## 10. Implementation Summary

The following implementation activities were completed.

| Activity | Result |
|---|---|
| Lab environment verification | Completed |
| Ubuntu internal network configuration | Completed |
| Ubuntu static IP assignment | Completed |
| Ubuntu connectivity to DC01 | Successful |
| Active Directory DNS resolution from Ubuntu | Successful, with intermittent timeouts |
| OpenSSH installation | Completed |
| SSH service activation | Successful |
| DC01-to-Ubuntu TCP 22 connectivity | Successful |
| AD privileged group discovery | Completed |
| AD user inventory | Completed |
| Windows local administrator discovery | Completed |
| Ubuntu root and sudo discovery | Completed |
| Splunk internal search verification | Successful |

## 11. Implementation Limitations

The following activities were not completed as part of this implementation stage:

- CyberArk installation or deployment.
- Password vault implementation.
- Automated privileged password rotation.
- Privileged session recording or brokering.
- Interactive SSH login verification.
- Windows Security Event Log ingestion into Splunk.
- Ubuntu authentication log ingestion into Splunk.
- Actual privilege restriction or account modification.

These capabilities are outside the scope of the completed discovery activities and will be addressed separately where applicable.

## 12. Conclusion

The implementation established a functioning lab environment for practical PAM operations.

Active Directory privileged groups, domain users, workstation local administrators and Ubuntu administrative identities were successfully discovered.

The Ubuntu SSH service was installed and verified through a remote TCP connectivity test.

Splunk Enterprise was also verified through a successful internal index search.

The completed work establishes the technical baseline for subsequent privileged access control, least-privilege testing and security monitoring activities.

---

**Project:** Project-05-PAM-Operations-Lab  
**Document:** Implementation  
**Phase:** Phase 1 – Environment Verification and Phase 2 – Privileged Account Discovery  
**Status:** Discovery implementation completed; access-control and monitoring activities pending.


## Phase 3 – Privileged Access Control

### Objective
Review privileged access on the Windows 10 domain-joined workstation and demonstrate least-privilege access management.

### 1. Initial privileged access review

Inspected the local Administrators group on WIN10-CLIENT.

Initial membership:
- CORP\Domain Admins
- DESKTOP-SD075Q6\Administrator
- DESKTOP-SD075Q6\LabAdmin

The Domain Admins group provided workstation administrator access through its membership in the local Administrators group.

### 2. Standard-user validation

Selected the existing domain account `unlock.test` for the standard-user test.

Verified:
- Domain authentication was successful.
- No enabled local Administrators membership appeared in the user's session.
- The `net session` command returned System error 5 – Access is denied.

### 3. Recovery administrator account

Created a dedicated local account:
- Account: PAM-Recovery
- Purpose: Local administrative recovery for the PAM lab.
- Added to the local Administrators group.

Tested the account through an interactive login.

The initial non-elevated PowerShell session showed the Administrators group as deny-only due to Windows UAC token filtering.

After opening PowerShell with Run as administrator:
- The Administrators group was enabled.
- `net session` completed successfully.

### 4. Least-privilege implementation

Removed `CORP\Domain Admins` from the local Administrators group on WIN10-CLIENT.

No changes were made to Domain Admins membership on the domain controller.

Final local Administrators membership:
- DESKTOP-SD075Q6\Administrator
- DESKTOP-SD075Q6\LabAdmin
- DESKTOP-SD075Q6\PAM-Recovery

### 5. Post-change validation

Retested the `unlock.test` account after the membership change.

Results:
- Domain authentication successful.
- No enabled local Administrators membership appeared.
- `net session` returned System error 5 – Access is denied.

Verified that PAM-Recovery retained local administrative access after the change.

### Outcome

Successfully demonstrated:
- Privileged group membership inspection.
- Standard-user versus administrator access comparison.
- Windows UAC administrator token filtering.
- Creation and validation of a local recovery administrator.
- Removal of unnecessary domain administrator access from a workstation.
- Post-change access validation.

All changes were limited to the WIN10-CLIENT lab workstation.
