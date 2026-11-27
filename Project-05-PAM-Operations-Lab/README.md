# Enterprise PAM Operations Lab

A hands-on Privileged Access Management (PAM) operations project demonstrating privileged account discovery, administrative access reviews, Linux privilege management, network configuration and security monitoring fundamentals.

## 1. Project Overview

Privileged accounts provide elevated access to critical systems and infrastructure. Improperly managed privileged identities can increase the risk of unauthorized access, credential compromise and privilege escalation.

This project demonstrates practical PAM-related administration across a Windows Active Directory environment, Windows workstation and Ubuntu Linux server.

The project focuses on identifying privileged identities, understanding their permissions, reviewing administrative group memberships and establishing a baseline for privileged activity monitoring.

**Project Type:** Enterprise PAM Operations Lab

**Primary Focus:** Privileged Account Discovery and Access Control

**Environment:** VirtualBox-based lab

**SIEM:** Splunk Enterprise

**Programming:** No Python required

## 2. Project Objectives

The main objectives are:

- Discover privileged accounts across Windows and Linux environments.
- Identify membership of sensitive Active Directory groups.
- Review local Windows administrator accounts.
- Identify Linux root and sudo-enabled accounts.
- Understand administrative privilege assignments.
- Apply least-privilege principles.
- Test authorized and unauthorized administrative access.
- Monitor privileged activities using Splunk.
- Investigate authentication and administrative activity.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Windows Server | Active Directory Domain Controller |
| Active Directory | Centralized identity and access management |
| Windows 10 | Domain-joined workstation |
| Ubuntu Linux | Linux privileged account administration |
| VirtualBox | Virtualized lab infrastructure |
| OpenSSH Server | Remote Linux administration |
| Splunk Enterprise | Security monitoring and investigation |
| PowerShell | Windows administrative discovery |
| Linux CLI | Linux account and privilege discovery |

## 4. Lab Architecture

### Environment Details

| Component | Hostname | IP Address |
|---|---|---|
| Domain Controller | DC01 | 192.168.10.10 |
| Windows Client | DESKTOP-SD075Q6 | 192.168.10.20 |
| Ubuntu Server | soc-ubuntu-VirtualBox | 192.168.10.30 |
| Splunk Enterprise | Local Windows Desktop | localhost:8000 |

**Active Directory Domain:** corp.example.com

**NetBIOS Domain:** CORP

**VirtualBox Internal Network:** IAM-LAB

### Network Design

```text
                  ENTERPRISE PAM LAB
                         |
                  VirtualBox Environment
                         |
                  Internal Network
                      IAM-LAB
                         |
           +-------------+-------------+
           |             |             |
           |             |             |
        DC01         WIN10-CLIENT     Ubuntu
     Windows Server    Windows 10    Ubuntu Linux
           |             |             |
     192.168.10.10  192.168.10.20  192.168.10.30
           |             |             |
           +-------------+-------------+
                         |
                  Active Directory
                  corp.example.com
                         |
                DNS / LDAP / Kerberos
```

Ubuntu uses an additional NAT adapter for external connectivity.

Splunk Enterprise runs locally on the Windows desktop and is not installed inside a virtual machine.

## 5. Project Modules

### Module 01 – Lab Environment Verification

- Verify Windows Server and Active Directory.
- Verify domain workstation connectivity.
- Configure Ubuntu networking.
- Verify Active Directory DNS resolution.
- Install and verify OpenSSH Server.
- Verify Splunk Web and internal search functionality.

### Module 02 – Privileged Account Discovery

- Identify Domain Admins membership.
- Identify Enterprise Admins membership.
- Inspect the built-in Administrators group.
- Discover domain user accounts.
- Identify local Windows administrator accounts.
- Discover Linux root and UID 0 accounts.
- Identify sudo-enabled users.
- Inspect Linux administrative group membership.

### Module 03 – Privileged Access Control

Planned activities:

- Review administrative account assignments.
- Apply least-privilege principles.
- Configure appropriate administrative access restrictions.
- Test authorized and unauthorized access.
- Verify access-control outcomes.

### Module 04 – Linux Privileged Access

Planned activities:

- Review root access.
- Inspect sudo permissions.
- Evaluate restricted administrative access.
- Test privileged command execution.
- Review SSH authentication controls.

### Module 05 – Splunk Monitoring

Planned activities:

- Collect Windows Security events.
- Collect Linux authentication logs.
- Monitor successful and failed logins.
- Investigate privileged account activity.
- Create relevant saved searches and monitoring views.

### Module 06 – Security Investigation and Documentation

Planned activities:

- Investigate suspicious authentication activity.
- Analyze privileged account usage.
- Document security observations.
- Prepare troubleshooting records.
- Complete the final security assessment.

## 6. Completed Practical Activities

The following activities have been performed and verified.

### Active Directory

- Discovered Domain Admins membership.
- Discovered Enterprise Admins membership.
- Inspected the built-in Administrators group.
- Identified 15 domain user accounts.
- Recorded 12 enabled and 3 disabled accounts.
- Inspected privileged group properties.

### Windows Workstation

- Verified domain membership.
- Verified connectivity to DC01.
- Verified the domain secure channel.
- Verified LDAP and KDC discovery.
- Discovered local Administrators group membership.
- Inspected local Windows user accounts.

### Ubuntu Linux

- Configured a second network adapter.
- Assigned a static IP address.
- Verified communication with DC01.
- Verified Active Directory DNS resolution.
- Installed and enabled OpenSSH Server.
- Verified SSH service status.
- Verified TCP port 22 connectivity.
- Identified the root account and UID 0 accounts.
- Inspected sudo and ADM group membership.

### Splunk

- Verified Splunk Enterprise installation.
- Accessed Splunk Web.
- Executed an internal index search.
- Retrieved internal Splunk events.

**Note:** Splunk verification currently covers internal events only. Windows and Linux security log ingestion remains pending.

## 7. Key Security Findings

The discovery exercise identified several areas requiring additional review.

| Finding | Observation | Priority |
|---|---|---|
| AD Privilege Concentration | Built-in Administrator belongs to three inspected privileged groups | High |
| Workstation Administration | Domain Admins is included in local Administrators | High |
| Local Administrator | LabAdmin is enabled and has local administrative privileges | Medium |
| Linux Sudo Access | soc-ubuntu has unrestricted sudo permissions | High |
| Root Account | Root has UID 0 | Privileged identity requiring protection |
| DNS Performance | Intermittent DNS query timeouts | Medium |

These are preliminary lab security observations, not findings from a formal enterprise security audit.

Detailed analysis and recommendations are available in `reports/security-assessment.md`.

## 8. Repository Structure

```text
Project-05-PAM-Operations-Lab/
│
├── README.md
│
├── docs/
│   ├── architecture.md
│   ├── implementation.md
│   ├── privileged-account-inventory.md
│   └── troubleshooting.md
│
├── evidence/
│   ├── active-directory/
│   ├── linux/
│   ├── access-control/
│   └── splunk/
│
└── reports/
    └── security-assessment.md
```

## 9. Documentation

| Document | Description |
|---|---|
| [Architecture](docs/architecture.md) | Lab infrastructure and network architecture |
| [Implementation](docs/implementation.md) | Practical implementation and verification steps |
| [Privileged Account Inventory](docs/privileged-account-inventory.md) | Windows and Linux privileged account discovery |
| [Troubleshooting](docs/troubleshooting.md) | Technical issues, investigation and resolutions |
| [Security Assessment](reports/security-assessment.md) | Findings, risk observations and recommendations |

## 10. Security Recommendations

Based on the discovery results, the following controls are recommended:

- Maintain an accurate privileged account inventory.
- Separate standard and administrative identities.
- Review Domain Admins and Enterprise Admins membership.
- Restrict unnecessary workstation administrator access.
- Review local administrator accounts.
- Apply least-privilege sudo permissions.
- Protect privileged credentials.
- Monitor administrative authentication and activity.
- Investigate suspicious login attempts.
- Review privileged group membership periodically.

## 11. Project Scope and Limitations

This project demonstrates PAM-related operational practices using native Windows and Linux administration tools.

It is not a full CyberArk PAM implementation.

The following capabilities are not implemented in the current discovery stage:

- CyberArk Digital Vault.
- CyberArk PVWA.
- CyberArk CPM automated password rotation.
- CyberArk PSM privileged session recording.
- Automated credential vaulting.
- Enterprise access approval workflows.
- Verified Windows and Linux log ingestion into Splunk.

These capabilities are outside the current implementation scope and may be studied separately.

## 12. Learning Outcomes

Through this project, the following practical skills are demonstrated:

- Active Directory privileged group administration.
- Windows local administrator discovery.
- Domain authentication and secure channel verification.
- Linux root and sudo privilege inspection.
- Network troubleshooting using VirtualBox and Linux tools.
- OpenSSH service administration.
- PowerShell-based security discovery.
- Splunk internal search and monitoring fundamentals.
- Privileged access risk identification.
- Technical documentation and security reporting.

## 13. Conclusion

The Enterprise PAM Operations Lab establishes a practical foundation for understanding privileged identity management across Windows and Linux environments.

The completed discovery activities identified privileged accounts, administrative group memberships and areas requiring access-control improvements.

The next stages will focus on implementing least-privilege controls, validating administrative access and integrating Windows and Linux security events with Splunk.

The project provides practical experience relevant to PAM administration, IAM operations and cybersecurity analyst roles.

---

**Project:** Project-05-PAM-Operations-Lab

**Category:** Identity and Access Management / Privileged Access Management

**Status:** Environment verification and privileged account discovery completed; access-control and monitoring phases pending.
