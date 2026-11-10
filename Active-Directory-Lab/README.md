# Active Directory IAM Lab

## Project Overview

This project demonstrates hands-on experience with Windows Active Directory Domain Services (AD DS), DNS, domain authentication, organizational units, user accounts, and security groups in an isolated VirtualBox environment.

**Objective:** Build and verify a functional Active Directory lab to practise identity and access management (IAM) administration and troubleshooting.

## Lab Architecture

| Component | Configuration |
|---|---|
| Virtualization | Oracle VirtualBox |
| Domain Controller | DC01 — Windows Server |
| Client | Windows 10 Pro |
| AD Domain | corp.example.com |
| NetBIOS Domain | CORP |
| Network | Internal Network — IAM-LAB |
| DC IP Address | 192.168.10.10 |
| Client IP Address | 192.168.10.20 |
| Client DNS Server | 192.168.10.10 |

Both virtual machines communicate over an isolated internal network.

## Active Directory Configuration

### Organizational Units

- Finance
- HR
- IT

### Domain Users

| Department | User |
|---|---|
| Finance | arun.kumar |
| Finance | rahul.kumar |
| HR | priya.kumari |
| IT | karthik.kumar |

### Security Groups

| Group | Purpose |
|---|---|
| Finance_Read | Finance read access |
| HR_Users | HR group membership |
| IT_Support | IT support group membership |

The `Finance_Read` group contains `arun.kumar` and `rahul.kumar`. It is configured as a Global Security Group.

## Verification and Testing

### Domain Controller Services

```powershell
Get-Service NTDS,DNS,Netlogon
```

**Result:** All three services were running.

### Client IP and DNS

```powershell
ipconfig /all
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
```

**Result:** The client used `192.168.10.20/24` with DNS pointing to `192.168.10.10`.

### Network Connectivity

```powershell
ping 192.168.10.10
```

**Result:** Four successful replies, 0% packet loss.

### DNS Resolution

```powershell
nslookup dc01.corp.example.com
nslookup -type=SRV _ldap._tcp.dc._msdcs.corp.example.com
```

**Result:** DC01 resolved to `192.168.10.10`, and the LDAP SRV record identified DC01 on port 389.

### Group Membership

```powershell
Get-ADGroupMember -Identity "Finance_Read"
Get-ADGroup -Identity "Finance_Read" -Properties GroupScope,GroupCategory
```

**Result:** Arun and Rahul were verified as members of the Global Security Group.

### Domain Membership

```powershell
Get-CimInstance Win32_ComputerSystem |
    Select-Object Name,Domain,PartOfDomain

whoami
```

**Result:** The Windows 10 client was domain-joined, and the domain user identity was verified.

## Troubleshooting Observations

- The initial Windows 10 network configuration required a static IP because the isolated network did not provide DHCP.
- DNS lookups returned correct results, although intermittent timeout messages were observed.
- A domain name typo caused an unsuccessful initial DNS query.
- Correcting the query allowed LDAP SRV record discovery.

## Finance Folder Permissions

The lab includes `C:\CompanyData\Finance`, with NTFS Read & Execute permissions assigned to `CORP\Finance_Read`.

**Status:** SMB share configuration and effective network access testing are pending.

## Skills Demonstrated

- Active Directory administration
- Domain Controller service verification
- DNS and LDAP service discovery
- Organizational Unit and security group management
- PowerShell administration
- Domain membership verification
- Basic network and authentication troubleshooting
- Technical documentation

## Next Steps

- Configure and verify SMB share permissions.
- Test Finance folder access from the domain-joined client.
- Investigate DNS timeout behavior.
- Document account lifecycle and access troubleshooting scenarios.
