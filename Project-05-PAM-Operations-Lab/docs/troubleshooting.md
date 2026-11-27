# Troubleshooting – Enterprise PAM Operations Lab

## 1. Overview

This document records the technical issues encountered during the setup and verification of the Enterprise PAM Operations Lab.

The troubleshooting activities covered:

- VirtualBox network configuration.
- Ubuntu internal network connectivity.
- Active Directory DNS resolution.
- OpenSSH Server installation and verification.
- Windows domain connectivity.
- Windows local administrator discovery.
- PowerShell command execution errors.

Each issue includes the observed symptoms, investigation steps, resolution and final verification where available.

---

## 2. Ubuntu Network Adapter Connectivity Issue

### 2.1 Problem

Initially, the Ubuntu VM had an operational NAT interface but its second network interface was not connected to the internal lab network.

Initial network inspection:

```bash
ip -br addr
```

Observed:

```text
enp0s3    UP    10.0.2.15/24
enp0s8    UP
```

The `enp0s8` interface did not have an IPv4 address.

### 2.2 Investigation

The network configuration was inspected using:

```bash
ip route
```

```bash
nmcli device status
```

The output showed:

```text
enp0s3    ethernet    connected
enp0s8    ethernet    disconnected
```

The Ubuntu VM's VirtualBox network adapter settings were also inspected.

### 2.3 Resolution

The second network adapter was configured to use the VirtualBox Internal Network named `IAM-LAB`.

A NetworkManager connection was created:

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

### 2.4 Verification

```bash
ip -br addr
```

Final configuration:

```text
enp0s3    UP    10.0.2.15/24
enp0s8    UP    192.168.10.30/24
```

**Result:** The Ubuntu VM successfully obtained its static internal lab IP address.

---

## 3. Ubuntu-to-DC01 Connectivity Failure

### 3.1 Problem

Ubuntu initially failed to communicate with DC01.

Test command:

```bash
ping -c 4 192.168.10.10
```

Observed result:

```text
Destination Host Unreachable
```

### 3.2 Investigation

The following checks were performed:

```bash
ip -br addr
```

```bash
ip route
```

```bash
nmcli device status
```

The internal network interface was checked, and the DC01 VM's operating state was reviewed.

During the initial failed connectivity test, DC01 was powered off.

### 3.3 Resolution

DC01 was powered on, allowing the two virtual machines to communicate through the `IAM-LAB` internal network.

### 3.4 Verification

The connectivity test was repeated:

```bash
ping -c 4 192.168.10.10
```

Observed result:

```text
4 packets transmitted
4 received
0% packet loss
```

The ARP neighbor entry was also inspected:

```bash
ip neigh show dev enp0s8
```

DC01 was identified as a reachable neighbor.

**Result:** Ubuntu-to-DC01 network connectivity was successfully established.

---

## 4. DNS Query Timeouts

### 4.1 Problem

DNS queries from the Windows client and Ubuntu initially displayed timeout messages.

Example:

```text
DNS request timed out.
timeout was 2 seconds.
```

However, the queries eventually returned the expected domain controller address.

### 4.2 Investigation

On Ubuntu:

```bash
nslookup dc01.corp.example.com 192.168.10.10
```

```bash
nslookup corp.example.com 192.168.10.10
```

On WIN10-CLIENT:

```powershell
nslookup dc01.corp.example.com
```

The returned address was:

```text
192.168.10.10
```

The LDAP SRV record was also inspected:

```powershell
nslookup -type=SRV _ldap._tcp.dc._msdcs.corp.example.com 192.168.10.10
```

The query returned the domain controller hostname and LDAP port.

### 4.3 Resolution Status

DNS resolution eventually returned the expected records, but intermittent query timeouts remained.

The issue was not conclusively diagnosed or permanently resolved during the environment verification stage.

### 4.4 Recommendation

Further investigation should include:

- DNS Server service status on DC01.
- DNS Server event logs.
- DNS response times.
- UDP and TCP port 53 connectivity.
- DNS client configuration.

**Result:** Domain DNS resolution was functional, with intermittent timeouts requiring further investigation.

---

## 5. OpenSSH Server Not Installed on Ubuntu

### 5.1 Problem

The SSH service was initially unavailable.

Service inspection:

```bash
systemctl status ssh --no-pager
```

Observed:

```text
Unit ssh.service could not be found.
```

The installed package was inspected:

```bash
dpkg -l openssh-server
```

The package was not installed.

### 5.2 Resolution

Package information was refreshed:

```bash
sudo apt update
```

OpenSSH Server was installed:

```bash
sudo apt install openssh-server -y
```

The SSH service was enabled and started:

```bash
sudo systemctl enable --now ssh
```

### 5.3 Verification

Service status:

```bash
systemctl status ssh --no-pager
```

The service returned:

```text
Active: active (running)
```

Listening port:

```bash
sudo ss -tlnp | grep ':22'
```

The output confirmed that SSH was listening on TCP port 22.

From DC01, connectivity was tested using:

```powershell
Test-NetConnection 192.168.10.30 -Port 22
```

Observed result:

```text
TcpTestSucceeded : True
```

**Result:** OpenSSH Server was successfully installed, enabled and verified through a remote TCP connectivity test.

---

## 6. Windows Domain Connectivity and Secure Channel Verification

### 6.1 Initial Concern

During earlier lab troubleshooting, the Windows client had returned:

```text
ERROR_NO_SUCH_DOMAIN
```

The secure channel test had also previously returned False.

This raised concerns about domain connectivity.

### 6.2 Investigation

The following commands were executed on WIN10-CLIENT:

```powershell
Get-CimInstance Win32_ComputerSystem |
Select-Object Name, Domain, PartOfDomain
```

Observed result:

```text
Name: DESKTOP-SD075Q6
Domain: corp.example.com
PartOfDomain: True
```

DC01 connectivity was tested:

```powershell
ping 192.168.10.10
```

All four packets were received.

Domain controller discovery was tested:

```powershell
nltest /dsgetdc:corp.example.com
```

The command successfully identified:

```text
DC: \\DC01.corp.example.com
Address: \\192.168.10.10
```

### 6.3 Secure Channel Verification

Command:

```powershell
Test-ComputerSecureChannel -Verbose
```

Observed result:

```text
True
```

The verbose output confirmed that the secure channel between the workstation and domain was in good condition.

### 6.4 KDC Discovery

Command:

```powershell
nltest /dsgetdc:corp.example.com /KDC
```

The command successfully discovered the domain controller and KDC.

**Result:** The workstation was already domain-joined, and its secure channel and domain controller discovery were functioning.

No domain rejoining operation was required.

---

## 7. Windows Local Administrator Discovery Error

### 7.1 Problem

The following command initially failed on WIN10-CLIENT:

```powershell
Get-LocalGroupMember -Group "Administrators" |
Select-Object Name, ObjectClass, PrincipalSource
```

Observed error:

```text
An unspecified error occurred: error code = 1789
```

### 7.2 Investigation

The local Administrators group was inspected using an alternative Windows command:

```powershell
net localgroup Administrators
```

The command successfully displayed:

```text
Members

Administrator
LabAdmin
```

The domain controller was kept running, and the local group discovery command was retried.

### 7.3 Resolution and Verification

The command subsequently executed successfully:

```powershell
Get-LocalGroupMember -Group "Administrators"
```

Observed results:

| Name | Principal Source | Object Class |
|---|---|---|
| CORP\Domain Admins | ActiveDirectory | Group |
| DESKTOP-SD075Q6\Administrator | Local | User |
| DESKTOP-SD075Q6\LabAdmin | Local | User |

The initial error was no longer reproduced.

The exact underlying cause of error 1789 was not conclusively established.

**Result:** Local administrator membership was successfully discovered.

---

## 8. Windows PowerShell Command Executed in Ubuntu

### 8.1 Problem

The following Windows PowerShell command was accidentally executed in the Ubuntu terminal:

```powershell
Test-NetConnection 192.168.10.30 -Port 22
```

Ubuntu returned:

```text
Test-NetConnection: command not found
```

### 8.2 Cause

`Test-NetConnection` is a Windows PowerShell cmdlet and is not a standard Linux command.

### 8.3 Resolution

The command was executed from DC01 using Windows PowerShell instead.

```powershell
Test-NetConnection 192.168.10.30 -Port 22
```

Observed result:

```text
TcpTestSucceeded : True
```

**Result:** The SSH connectivity test was successfully completed from the correct operating system.

---

## 9. Splunk Verification

### 9.1 Initial Verification

Splunk Enterprise was installed locally on the Windows desktop.

The web interface was accessed:

```text
http://localhost:8000
```

The Administrator account successfully accessed Search & Reporting.

### 9.2 Internal Search

Command:

```spl
index=_internal | head 10
```

The search returned ten events.

### 9.3 Result

Splunk Web and internal search functionality were operational.

No Windows Security Event Log or Ubuntu authentication log ingestion failure was investigated during this initial verification.

Those activities remain part of the later monitoring phase.

---

## 10. Troubleshooting Summary

| Issue | Investigation | Final Status |
|---|---|---|
| Ubuntu internal interface disconnected | VirtualBox and NetworkManager inspection | Resolved |
| Ubuntu unable to reach DC01 | DC01 operating state and network checks | Resolved |
| DNS query timeouts | DNS and SRV record queries | Functional, intermittent timeouts remain |
| SSH service unavailable | Package inspection and installation | Resolved |
| Initial domain connectivity concern | Domain membership and secure channel tests | Verified healthy |
| Local group discovery error 1789 | Alternative command and retry | Command succeeded; root cause unconfirmed |
| PowerShell command used in Ubuntu | Correct command execution environment | Resolved |
| Splunk verification | Internal index search | Successful |

---

## 11. Lessons Learned

The troubleshooting activities demonstrated several important operational practices:

1. Verify virtual machine network configuration before investigating higher-level connectivity problems.
2. Confirm that the destination virtual machine is running before diagnosing connection failures.
3. Distinguish DNS resolution success from DNS response performance.
4. Verify service installation, service state and listening ports separately.
5. Confirm Active Directory domain membership and secure channel before attempting to rejoin a workstation.
6. Use alternative Windows commands when a PowerShell cmdlet fails.
7. Execute operating-system-specific commands in the correct terminal.
8. Record actual results instead of assuming that a successful command means the entire service is functioning.

## 12. Conclusion

The troubleshooting activities helped establish reliable communication between the lab systems and verified the required infrastructure services.

Ubuntu networking and SSH configuration were completed successfully.

The Windows workstation's domain membership and secure channel were verified.

The initial Windows local group enumeration error was overcome, allowing the local administrator inventory to be completed.

DNS query timeouts remain an outstanding observation for further investigation.

Splunk's internal search functionality was also verified.

These troubleshooting experiences provide practical examples of infrastructure verification and operational problem-solving relevant to PAM administration.

---

**Project:** Project-05-PAM-Operations-Lab

**Document:** Troubleshooting

**Phase:** Environment Verification and Privileged Account Discovery

**Status:** Initial troubleshooting documented; DNS response delay remains under investigation.
