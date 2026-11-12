# Project 02 – Bulk Active Directory User Provisioning

## Project Overview

This project demonstrates bulk user provisioning in Microsoft Active Directory using PowerShell and CSV input.

The objective was to automate the creation of multiple employee accounts, validate employee details, assign department-specific security groups, and verify account configurations.

## Lab Environment

- **Domain:** corp.example.com
- **Domain Controller:** DC01
- **Operating System:** Windows Server
- **Directory Service:** Active Directory Domain Services
- **Automation:** Windows PowerShell
- **Input:** CSV employee records

## Project Objectives

- Import employee information from a CSV file.
- Validate usernames and identify existing accounts.
- Validate department, OU, and security group mappings.
- Create AD users dynamically using CSV properties.
- Set temporary passwords securely.
- Require password changes at first login.
- Assign department-specific security groups.
- Enable accounts after successful group assignment.
- Implement duplicate detection and error handling.
- Verify provisioned accounts and group memberships.

## CSV Structure

The input file contains the following columns:

| Column | Description |
|---|---|
| FirstName | Employee first name |
| LastName | Employee last name |
| Username | AD logon username |
| UPN | User Principal Name |
| Department | Employee department |
| OU | Target Organizational Unit |
| Group | Department security group |

Passwords are intentionally excluded from the CSV file.

## Provisioning Workflow

1. Import employee records using `Import-Csv`.
2. Identify existing and new users.
3. Validate department-to-OU and group mappings.
4. Collect a temporary password using `Read-Host -AsSecureString`.
5. Create a test account and validate its attributes.
6. Provision remaining employees using a `foreach` loop.
7. Check for duplicate accounts before creation.
8. Create accounts in a disabled state.
9. Assign the appropriate security group.
10. Enable accounts after successful group assignment.
11. Verify account attributes and group memberships.

## PowerShell Concepts Practiced

- Variables and arrays
- CSV import
- `foreach` loops
- Conditional statements (`if`, `else`)
- Pipeline operations
- `Get-ADUser`
- `New-ADUser`
- `Add-ADGroupMember`
- `Enable-ADAccount`
- `Get-ADPrincipalGroupMembership`
- `try/catch`
- `-ErrorAction Stop`
- SecureString password handling
- Duplicate account detection

## Validation Results

Five fictional employee accounts were provisioned and verified.

| Username | Department | Security Group | Account Status |
|---|---|---|---|
| naveen.kumar | HR | HR_Users | Enabled |
| divya.raj | Finance | Finance_Read | Enabled |
| sanjay.kumar | IT | IT_Support | Enabled |
| priya.anand | HR | HR_Users | Enabled |
| kiran.raj | Finance | Finance_Read | Enabled |

All five accounts were verified in Active Directory with their expected departments and group memberships.

## Error Handling and Duplicate Protection

The workflow includes:

- Duplicate username detection before account creation.
- Skipping existing accounts.
- `try/catch` error handling.
- Error reporting for failed operations.

A deliberate nonexistent-user lookup was used to validate error handling.

## Security Considerations

- Passwords were not stored in the CSV file.
- A SecureString was used for temporary password input.
- Accounts were initially created in a disabled state.
- Security group membership was assigned before enabling accounts.
- The same temporary password was used for the remaining lab accounts for convenience. This is not a production recommendation.
- Production provisioning should use unique temporary passwords, secure delivery, appropriate delegated permissions, and audit logging.

## Project Outcome

Successfully demonstrated CSV-driven bulk provisioning of five fictional Active Directory users using PowerShell.

This project provided practical exposure to IAM Joiner processes, user lifecycle administration, group-based access assignment, duplicate detection, and basic automation error handling.

## Repository Structure

```text
Project-02-Bulk-User-Provisioning/
├── CSV/
│   └── bulk_users_sample.csv
├── Scripts/
│   └── BulkUserProvisioning.ps1
├── Screenshots/
└── README.md
```

## Disclaimer

This project was performed in a controlled virtual Active Directory lab environment using fictional employee data. It is intended for learning and portfolio demonstration, not as a production-ready provisioning solution.
