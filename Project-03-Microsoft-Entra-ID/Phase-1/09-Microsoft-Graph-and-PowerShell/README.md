# Module 9 – Microsoft Graph and PowerShell

## Overview

This module focuses on using Microsoft Graph PowerShell SDK to interact with Microsoft Entra ID.

The practical exercises covered directory authentication, user and group retrieval, user lifecycle operations, audit-log investigation, and PowerShell automation.

The objective was to understand how IAM analysts can perform directory operations and automate repetitive identity-management tasks.

## Learning Objectives

- Understand Microsoft Graph and its role in Microsoft Entra ID.
- Install and configure Microsoft Graph PowerShell SDK.
- Authenticate using delegated permissions.
- Understand Microsoft Graph scopes and authorization.
- Retrieve users and security groups.
- Create and update Entra ID users.
- Enable and disable user accounts.
- Investigate directory audit logs.
- Automate IAM reporting using PowerShell.
- Handle errors using `try`, `catch`, and `-ErrorAction Stop`.

## Module Contents

| File | Topic |
|---|---|
| 01-Microsoft-Graph-Fundamentals.md | Microsoft Graph fundamentals |
| 02-Microsoft-Graph-PowerShell-SDK.md | SDK installation and configuration |
| 03-Connecting-and-Authentication.md | Graph authentication and permissions |
| 04-Reading-Users-and-Groups.md | Retrieving users and groups |
| 05-Creating-and-Updating-Users.md | User lifecycle operations |
| 06-Automating-IAM-Tasks.md | IAM reporting automation |
| 07-Practical-Review-and-Troubleshooting.md | Practical investigation and troubleshooting |

## Practical Environment

- Microsoft Entra ID cloud-only tenant
- Windows PowerShell 5.1
- Microsoft Graph PowerShell SDK
- PowerShellGet 2.2.6
- Microsoft Graph PowerShell SDK 2.41.2
- Windows command-line environment

## Practical Exercises

### 1. Microsoft Graph SDK Setup

- Inspected the installed PowerShell version.
- Checked PowerShell execution policies.
- Installed PowerShellGet.
- Installed Microsoft Graph PowerShell SDK.
- Verified the installed SDK version and available commands.

### 2. Authentication and Permissions

- Connected to Microsoft Graph using delegated authentication.
- Inspected the authentication context using `Get-MgContext`.
- Examined delegated scopes.
- Requested and verified `User.ReadWrite.All`.
- Investigated the relationship between Graph permissions and directory authorization.

### 3. User and Group Investigation

- Retrieved Entra ID users using `Get-MgUser`.
- Filtered enabled and disabled accounts.
- Retrieved security groups using `Get-MgGroup`.
- Investigated direct group membership.
- Identified groups with zero direct members.
- Investigated user membership using `Get-MgUserMemberOf`.

### 4. User Lifecycle Operations

Created a dedicated test account named **Graph Lab User**.

Performed the following operations:

- Created the test user.
- Verified the user object and attributes.
- Updated department and job title.
- Disabled the account.
- Re-enabled the account.
- Verified each change using Microsoft Graph PowerShell.

### 5. Audit Log Investigation

Inspected Microsoft Entra audit logs for the Graph operations.

Observed successful events including:

- Add user
- Update PasswordProfile
- Update user
- Disable account

Identified Microsoft Graph Command Line Tools as the initiating application and inspected the target user and modified properties.

### 6. IAM Reporting Automation

Created a local reporting workspace:

`Documents/IAM-Automation`

Developed a PowerShell automation script named:

`IAM-User-Reporting.ps1`

Generated four CSV reports:

- Entra-User-Inventory.csv
- Disabled-Users-Report.csv
- Missing-Department-Report.csv
- IAM-Summary-Report.csv

The automation retrieved directory users, calculated account statistics, identified missing department information, and exported reports.

### 7. Error Handling

Practised PowerShell error handling using:

- `try`
- `catch`
- `-ErrorAction Stop`
- `$_.Exception.Message`

Also investigated Microsoft Graph authorization and resource-not-found errors.

## Important Practical Findings

- The tenant contained four users during the reporting exercise.
- Two accounts were enabled.
- Two accounts were disabled.
- One user record had no department value.
- Both inspected security groups had zero direct members.
- The dedicated Graph Lab User was successfully created and updated.
- Microsoft Entra audit logs recorded the user lifecycle operations.
- The consolidated reporting script executed successfully.

These findings represent the tenant state observed during the practical exercises, not permanent directory conditions.

## Licensing and Environment Limitations

- The exercises used a cloud-only Entra tenant.
- Group-based enterprise application assignment was unavailable under the tenant's licensing level.
- Some Graph operations required additional delegated permissions.
- Successful Graph authentication did not automatically grant authorization for every directory operation.

## Key IAM Concepts Learned

- Microsoft Graph API
- Microsoft Graph PowerShell SDK
- Delegated permissions
- Graph scopes
- Directory roles and authorization
- User lifecycle management
- Security group membership
- Account enablement and deactivation
- Audit-log investigation
- PowerShell automation
- CSV reporting
- Error handling

## Outcome

Completed practical exercises involving Microsoft Graph PowerShell and Microsoft Entra ID.

Developed a reusable IAM reporting script and gained hands-on experience retrieving directory information, performing controlled user lifecycle operations, and investigating audit events.

## Repository

**Project:** IAM-PAM-Portfolio

**Section:** Project 03 – Microsoft Entra ID

**Phase:** Phase 1 – Cloud-only Identity Management
