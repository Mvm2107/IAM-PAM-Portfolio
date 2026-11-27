# Lab Architecture – Enterprise PAM Operations Lab

## 1. Overview

This document describes the architecture of the Enterprise PAM Operations Lab.

The environment consists of a Windows Active Directory domain, a Windows domain-joined workstation, an Ubuntu Linux server and Splunk Enterprise for security monitoring.

The lab is designed to demonstrate privileged account discovery, access control, Linux privilege management and privileged activity monitoring.

## 2. Architecture Components

| Component | Operating System / Platform | Hostname | IP Address |
|---|---|---|---|
| Domain Controller | Windows Server | DC01 | 192.168.10.10 |
| Domain Workstation | Windows 10 | DESKTOP-SD075Q6 | 192.168.10.20 |
| Linux Server | Ubuntu 25.04 | soc-ubuntu-VirtualBox | 192.168.10.30 |
| SIEM | Splunk Enterprise | Local Windows Desktop | localhost:8000 |

**Active Directory domain:** corp.example.com

**NetBIOS domain:** CORP

**VirtualBox internal network:** IAM-LAB

## 3. Network Architecture

The virtual machines use a VirtualBox Internal Network named `IAM-LAB` for communication between the lab systems.

### 3.1 Network Configuration

| System | Network Interface | Configuration |
|---|---|---|
| DC01 | Internal Network – IAM-LAB | 192.168.10.10/24 |
| WIN10-CLIENT | Lab network | 192.168.10.20/24 |
| Ubuntu | enp0s8 – IAM-LAB | 192.168.10.30/24 |
| Ubuntu | enp0s3 – NAT | 10.0.2.15/24 |

The Ubuntu VM uses two network interfaces:

- `enp0s3`: NAT interface for external network connectivity.
- `enp0s8`: Internal Network interface for communication with the Windows lab environment.

The Ubuntu IAM-LAB interface was configured with a static IPv4 address of `192.168.10.30/24`.

### 3.2 Network Connectivity Verification

The following connectivity tests were performed:

| Test | Source | Destination | Result |
|---|---|---|---|
| ICMP connectivity | Ubuntu | DC01 | Successful |
| ICMP connectivity | WIN10-CLIENT | DC01 | Successful |
| DNS resolution | Ubuntu | DC01 | Successful |
| Domain Controller discovery | WIN10-CLIENT | DC01 | Successful |
| SSH TCP connectivity | DC01 | Ubuntu | Successful |

The SSH connectivity test confirmed that TCP port 22 was reachable on Ubuntu.

### 3.3 Network Architecture Diagram

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
     Windows Server    Windows 10    Ubuntu 25.04
           |             |             |
     192.168.10.10  192.168.10.20  192.168.10.30
           |             |             |
           +-------------+-------------+
                         |
                  Active Directory
                  corp.example.com
                         |
              DNS / LDAP / Kerberos
                         |
                 Domain Authentication
```

**Additional Ubuntu connectivity:**

Ubuntu has a separate NAT interface (`enp0s3`) configured with the address `10.0.2.15`.

## 4. Active Directory Architecture

DC01 operates as the Active Directory Domain Controller.

### Domain Details

| Property | Value |
|---|---|
| Domain Name | corp.example.com |
| NetBIOS Name | CORP |
| Domain Controller | DC01 |
| Domain Controller IP | 192.168.10.10 |
| Domain Mode | Windows2016Domain |
| Forest Name | corp.example.com |

### Active Directory Services

The following services and functions were verified:

- Active Directory Domain Services
- Domain DNS resolution
- LDAP service discovery
- Kerberos Key Distribution Center discovery
- Domain Controller discovery
- Workstation secure channel

### Domain Authentication Verification

The Windows workstation successfully discovered DC01 using:

```powershell
nltest /dsgetdc:corp.example.com
```

The secure channel was verified using:

```powershell
Test-ComputerSecureChannel -Verbose
```

The command returned `True`, confirming that the workstation's secure channel was in good condition.

## 5. Linux Architecture

The Ubuntu server provides the Linux environment for privileged access management exercises.

### System Details

| Property | Value |
|---|---|
| Operating System | Ubuntu 25.04 |
| Hostname | soc-ubuntu-VirtualBox |
| Internal IP | 192.168.10.30 |
| NAT IP | 10.0.2.15 |
| Administrative Account | soc-ubuntu |
| Root Account | root |

### Linux Administrative Components

The following components were inspected:

- Root account
- UID 0 accounts
- Sudo group membership
- Sudo privileges
- ADM group membership
- OpenSSH Server

### SSH Configuration

OpenSSH Server was installed and enabled.

Service verification:

```bash
sudo systemctl status ssh --no-pager
```

Port verification:

```bash
sudo ss -tlnp | grep ':22'
```

The SSH service was confirmed as active and listening on TCP port 22.

Remote connectivity was verified from DC01:

```powershell
Test-NetConnection 192.168.10.30 -Port 22
```

Result:

```text
TcpTestSucceeded : True
```

This confirms network-level SSH connectivity. An interactive SSH login was not yet documented as tested.

## 6. Splunk Architecture

Splunk Enterprise is installed locally on the Windows desktop rather than inside a VirtualBox VM.

### Splunk Details

| Property | Value |
|---|---|
| Platform | Splunk Enterprise |
| Installation Location | Local Windows Desktop |
| Web Interface | http://localhost:8000 |
| Index Verified | _internal |
| Search Application | Search & Reporting |

### Splunk Verification

The following search was executed:

```spl
index=_internal | head 10
```

The search returned ten internal events, confirming that Splunk Web and its internal search functionality were working.

**Important:** Windows Security Event and Linux authentication log ingestion have not yet been verified. These will be addressed during the security monitoring phase.

## 7. Architecture Design Considerations

The lab architecture supports the following practical exercises:

1. Active Directory privileged account discovery.
2. Windows local administrator discovery.
3. Linux root and sudo privilege discovery.
4. Privileged access restriction and verification.
5. Remote Linux administration using SSH.
6. Windows and Linux security event monitoring.
7. Privileged activity investigation using Splunk.

The use of an isolated VirtualBox Internal Network allows the virtual machines to communicate within the lab environment.

Ubuntu additionally uses NAT for external connectivity.

## 8. Conclusion

The Enterprise PAM Operations Lab uses a combination of Windows Server, Windows 10, Ubuntu Linux and Splunk Enterprise.

The environment provides the foundation for practical privileged account discovery, access control testing and security monitoring.

The initial network, domain connectivity, SSH service and Splunk search functionality checks were successfully completed.

**Project:** Project-05-PAM-Operations-Lab

**Document:** Lab Architecture

**Status:** Initial environment verification completed.
