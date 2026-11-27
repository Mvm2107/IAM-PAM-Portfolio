# Security Assessment Report – Enterprise PAM Operations Lab

## 1. Executive Summary

This report presents the security assessment conducted as part of the Enterprise PAM Operations Lab.

The assessment focused on identifying privileged accounts, reviewing administrative group memberships and evaluating privilege assignments across:

- Microsoft Active Directory
- Windows 10 Workstation
- Ubuntu Linux Server

Splunk Enterprise was also verified as the SIEM platform for future security monitoring activities.

The assessment identified several areas requiring security review, including privileged account concentration, workstation administrative access and unrestricted Linux sudo permissions.

No account modifications, privilege removals or password changes were performed during this assessment.

## 2. Assessment Scope

### 2.1 Systems Assessed

| System | Hostname | IP Address |
|---|---|---|
| Windows Server | DC01 | 192.168.10.10 |
| Windows Workstation | DESKTOP-SD075Q6 | 192.168.10.20 |
| Ubuntu Linux | soc-ubuntu-VirtualBox | 192.168.10.30 |
| Splunk Enterprise | Local Windows Desktop | localhost:8000 |

### 2.2 Assessment Objectives

1. Identify privileged Active Directory accounts.
2. Review membership of sensitive administrative groups.
3. Identify local Windows administrator accounts.
4. Identify Linux root and sudo-enabled accounts.
5. Evaluate privilege concentration and excessive access.
6. Recommend appropriate PAM security controls.
7. Establish a baseline for future privileged activity monitoring.

## 3. Assessment Methodology

The assessment used read-only administrative discovery commands.

### Windows and Active Directory

| Command | Assessment Purpose |
|---|---|
| Get-ADGroupMember | Identify privileged group members |
| Get-ADUser | Discover domain accounts |
| Get-ADGroup | Inspect security group properties |
| Get-LocalGroupMember | Identify workstation administrators |
| Get-LocalUser | Inspect local user accounts |
| whoami /groups | Inspect current security token |
| Test-ComputerSecureChannel | Verify domain trust |

### Linux

| Command | Assessment Purpose |
|---|---|
| getent passwd | Discover Linux accounts |
| getent group | Inspect group membership |
| getent passwd root | Identify root account |
| UID 0 enumeration | Identify root-equivalent accounts |
| sudo -l | Inspect effective sudo privileges |

## 4. Assessment Findings

### Finding 01 – Concentration of Active Directory Privileges

**Observation**

The built-in Administrator account was identified in all three inspected privileged groups:

- Domain Admins
- Enterprise Admins
- Administrators

**Security Impact**

Compromise of this identity could provide extensive administrative access across the Active Directory environment.

Concentrating multiple administrative responsibilities in one identity increases the potential impact of credential compromise.

**Risk Assessment:** High

**Recommendations**

- Review privileged group membership periodically.
- Use dedicated administrative identities.
- Avoid using highly privileged accounts for routine activities.
- Protect privileged credentials using appropriate access controls.
- Monitor privileged authentication and group membership modifications.

### Finding 02 – Domain Admins Membership on Windows Workstation

**Observation**

The CORP\Domain Admins group was identified as a member of the local Administrators group on WIN10-CLIENT.

**Security Impact**

Members of Domain Admins can inherit local administrative access to the workstation.

This increases the number of systems exposed if a highly privileged domain identity is compromised.

**Risk Assessment:** High

**Recommendations**

- Review whether workstation administration requires Domain Admin privileges.
- Use dedicated workstation administrator groups.
- Apply least-privilege access.
- Restrict privileged account usage on ordinary workstations.
- Monitor local Administrators group membership changes.

### Finding 03 – Enabled Local Administrator Account

**Observation**

The local account LabAdmin was identified as:

- Enabled.
- A member of the local Administrators group.
- Last logged in on November 18, 2026.
- Reporting PasswordRequired = False.

**Security Impact**

An enabled local administrative identity with an unverified password configuration requires further review.

The PasswordRequired property alone does not establish whether the account has a configured password.

**Risk Assessment:** Medium – Pending verification

**Recommendations**

- Verify the account's password configuration.
- Confirm account ownership and operational purpose.
- Review whether permanent administrative access is necessary.
- Consider managed local administrator password solutions.
- Monitor local account authentication.

### Finding 04 – Unrestricted Linux Sudo Permissions

**Observation**

The Ubuntu account soc-ubuntu belongs to the sudo group.

The sudo permission inspection returned:

```text
(ALL : ALL) ALL
```

This indicates that the account can execute commands as any user, including root.

**Security Impact**

Compromise of this account could provide complete administrative control over the Ubuntu system.

**Risk Assessment:** High

**Recommendations**

- Review administrative responsibilities.
- Apply restricted sudo rules where operationally appropriate.
- Avoid granting unrestricted administrative access to routine accounts.
- Monitor sudo command execution.
- Review sudoers configuration periodically.

### Finding 05 – Linux Root Account

**Observation**

The root account was identified with UID 0.

UID 0 enumeration returned only one account: root.

**Security Impact**

The root account has unrestricted administrative privileges over the Linux system.

An exposed or compromised root credential could result in complete system compromise.

**Risk Assessment:** High – Privileged identity requiring protection

**Recommendations**

- Restrict direct root login where operationally appropriate.
- Prefer controlled sudo-based administrative access.
- Monitor root authentication attempts.
- Protect privileged credentials.
- Review SSH configuration and authentication policies.

### Finding 06 – DNS Response Timeouts

**Observation**

DNS queries occasionally returned timeout messages before eventually resolving the expected domain records.

The domain controller address was successfully returned.

**Security Impact**

Intermittent DNS response delays can affect domain discovery and authentication reliability.

**Risk Assessment:** Medium – Operational issue requiring investigation

**Recommendations**

- Inspect DNS Server service health.
- Review DNS event logs.
- Check UDP and TCP port 53 connectivity.
- Investigate DNS response times.
- Verify DNS client configuration.

## 5. Consolidated Findings Register

| ID | Finding | Risk Assessment | Status |
|---|---|---|---|
| F-01 | Concentration of AD privileges | High | Review required |
| F-02 | Domain Admins on workstation | High | Review required |
| F-03 | Enabled LabAdmin account | Medium | Verification required |
| F-04 | Unrestricted Linux sudo | High | Review required |
| F-05 | Root privileged identity | High | Protection required |
| F-06 | Intermittent DNS timeouts | Medium | Investigation pending |

Risk ratings in this report are preliminary qualitative assessments for the lab, not results of a formal enterprise risk-scoring methodology.

## 6. Recommended PAM Security Controls

The following controls are recommended for improving privileged access security.

### 6.1 Privileged Account Management

- Maintain an accurate privileged account inventory.
- Identify privileged account owners.
- Document the business justification for administrative access.
- Review privileged group memberships periodically.
- Separate administrative identities from standard user identities.

### 6.2 Least Privilege

- Restrict unnecessary Domain Admin membership.
- Avoid permanent administrative access where possible.
- Review local workstation administrator accounts.
- Apply restricted Linux sudo permissions.
- Remove unnecessary privileges only after authorization and validation.

### 6.3 Credential Protection

- Enforce strong authentication policies.
- Protect privileged credentials.
- Avoid shared administrator credentials.
- Implement controlled password rotation.
- Consider privileged credential vaulting.

### 6.4 Monitoring and Auditing

- Monitor privileged authentication events.
- Monitor Windows administrator group membership changes.
- Monitor Linux sudo activity.
- Investigate failed authentication attempts.
- Forward relevant Windows and Linux logs to Splunk.
- Maintain an auditable record of privileged operations.

## 7. Monitoring Opportunities with Splunk

Splunk Enterprise was verified through its internal index.

The following monitoring activities are planned for the next monitoring phase:

| Monitoring Area | Data Source | Objective |
|---|---|---|
| Windows authentication | Windows Security Events | Detect successful and failed logins |
| Privileged group changes | Active Directory Security Events | Detect administrative membership modifications |
| Linux authentication | Linux authentication logs | Monitor SSH login activity |
| Sudo execution | Linux authentication logs | Investigate privileged command execution |
| Failed login attempts | Windows and Linux logs | Identify suspicious authentication patterns |

**Important:** These monitoring integrations and detections have not yet been implemented or verified.

## 8. Assessment Limitations

The assessment was limited to the lab environment and the discovery activities performed.

The following were not implemented or tested:

- CyberArk Vault deployment.
- Privileged credential vaulting.
- Automated password rotation.
- Privileged session brokering.
- Privileged session recording.
- Automated access approval workflows.
- Windows and Linux log ingestion into Splunk.
- Production-level security policy enforcement.

This assessment should not be interpreted as a full enterprise PAM security audit or a CyberArk product assessment.

## 9. Overall Security Assessment

The discovery activities identified privileged identities and several areas requiring additional access review.

The most important observations were:

1. The built-in Active Directory Administrator account has extensive privileged group membership.
2. The Domain Admins group is included in the Windows workstation's local Administrators group.
3. LabAdmin is an enabled local administrator account requiring password configuration review.
4. The Ubuntu soc-ubuntu account has unrestricted sudo privileges.
5. DNS response timeouts require further investigation.

The findings provide a baseline for the next stage of the project: privileged access control and least-privilege testing.

## 10. Conclusion

The Enterprise PAM Operations Lab successfully established a privileged account inventory across Windows Active Directory, Windows workstation and Ubuntu Linux environments.

The assessment identified areas where privileged access controls, account reviews and monitoring could be strengthened.

The next stage will focus on implementing and testing appropriate privileged access restrictions, validating authorized and unauthorized administrative operations, and collecting security events for investigation using Splunk.

---

**Project:** Project-05-PAM-Operations-Lab

**Document:** Security Assessment Report

**Assessment Type:** Privileged Account Discovery and Access Review

**Environment:** Active Directory, Windows 10, Ubuntu Linux and Splunk Enterprise

**Status:** Initial assessment completed; remediation and monitoring activities pending.

## Phase 3 – Privileged Access Security Assessment

### Assessment Scope

Reviewed privileged access on the Windows 10 domain-joined workstation (WIN10-CLIENT) and validated standard-user and administrator access.

### Findings and Remediation

| ID | Finding | Initial Priority | Status |
|---|---|---|---|
| PAM-01 | Domain Admins had local administrator access on WIN10-CLIENT | High | Remediated |
| PAM-02 | Built-in Administrator belonged to multiple privileged AD groups | High | Retained for lab; review required |
| PAM-03 | LabAdmin was an enabled local administrator with an unclear business purpose | Medium | Pending review |
| PAM-04 | Dedicated local recovery administrator was initially absent | Medium | Remediated |

### Remediation Details

**PAM-01 – Excessive workstation privileges**

- Identified CORP\Domain Admins in the workstation's local Administrators group.
- Created and tested a dedicated local recovery account.
- Removed CORP\Domain Admins from the workstation's local Administrators group.
- Verified that the recovery account retained administrative access.
- Retested the standard domain account after the change.

Result: Successful.

**PAM-02 – Built-in Administrator privilege review**

- Identified Administrator in Domain Admins, Enterprise Admins and Administrators.
- No domain-level group memberships were modified.
- Further review is recommended to assess the need for these privileges.

**PAM-03 – Local LabAdmin account**

- Confirmed that LabAdmin was enabled and belonged to the local Administrators group.
- Its ownership and purpose were not established.
- No changes were made because the account may be used by other lab projects.

**PAM-04 – Recovery administrator**

- Created the local PAM-Recovery account.
- Added it to the local Administrators group.
- Verified interactive login and elevated administrative access.
- Confirmed that administrative access remained available after the least-privilege change.

### Validation Results

| Test | Result |
|---|---|
| Standard-user authentication | Successful |
| Standard-user administrative operation | Access denied |
| Recovery administrator login | Successful |
| Recovery administrator elevated operation | Successful |
| Domain Admins removal from workstation | Successful |
| Post-change standard-user test | Access denied |

### Conclusion

The assessment demonstrated practical privileged-account discovery, access validation, least-privilege implementation and recovery-account management.

The workstation's local administrative access was reduced without changing domain-level privileged group memberships.

Remaining review items include the built-in Administrator's domain privileges and the ownership and purpose of LabAdmin.

This assessment represents a controlled lab exercise and not a formal enterprise security audit.
