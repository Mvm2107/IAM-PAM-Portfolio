# Module 01 — Microsoft Entra ID Fundamentals

## 1. Objective

Understand Microsoft Entra ID architecture, cloud identity management concepts, and the differences between traditional on-premises Active Directory and cloud-based identity management.

## 2. Environment

- Platform: Microsoft Entra ID
- Edition: Microsoft Entra ID Free
- Environment: Cloud-only
- Administration: Microsoft Entra Admin Center
- Tenant: Default Directory

## 3. What is Microsoft Entra ID?

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based Identity and Access Management (IAM) service.

It enables organisations to:

- Create and manage cloud identities.
- Authenticate users.
- Manage access to cloud applications.
- Assign administrative permissions.
- Configure authentication methods.
- Monitor sign-in and identity activities.

## 4. Understanding Microsoft Entra ID Tenant

A tenant is a dedicated instance of Microsoft Entra ID representing an organisation.

Each tenant has its own:

- Tenant ID (unique GUID).
- Organisation name.
- Primary domain.
- Users and groups.
- Applications.
- Directory roles.

### Example

Organisation: IAM Learning Lab

Default domain: iamlearninglab.onmicrosoft.com

Example user: arun@iamlearninglab.onmicrosoft.com

A tenant can also have multiple verified domains.

## 5. Active Directory DS vs Microsoft Entra ID

| Active Directory DS | Microsoft Entra ID |
|---|---|
| On-premises directory service | Cloud identity service |
| Domain Controller | Microsoft-managed cloud service |
| Kerberos authentication | OAuth 2.0 / OpenID Connect |
| LDAP / LDAPS | Microsoft Graph API |
| Organizational Units | Groups and administrative units |
| Group Policy | Cloud-based device and access management |
| Domain Join | Microsoft Entra Join |

### Key learning

Active Directory DS and Microsoft Entra ID are different technologies. They can work together in a hybrid identity environment.

## 6. Understanding Authentication and Authorization

### Authentication (AuthN)

Authentication verifies the identity of a user.

Example:

1. Employee enters username.
2. Employee provides authentication credentials.
3. Identity service validates the credentials.
4. Access token or authentication result is issued as appropriate.

### Authorization (AuthZ)

Authorization determines what an authenticated identity is permitted to access.

Example:

- Employee can access the HR application.
- Employee cannot access the Finance application without the required permissions.

### Difference

Authentication answers: Who are you?

Authorization answers: What are you allowed to access?

## 7. Important Identity Concepts

### Tenant ID

A unique identifier assigned to an Entra tenant.

### User Principal Name (UPN)

The user identity generally used for signing in.

Example: arun@iamlearninglab.onmicrosoft.com

### Object ID

A unique GUID assigned to each directory object.

It helps identify users, groups and other directory objects.

### Member and Guest

- Member: An identity classified as belonging to the organisation.
- Guest: An external identity invited to collaborate with the organisation.

### Directory Roles

Administrative permissions assigned to users or groups.

Examples:

- Global Administrator
- User Administrator
- Groups Administrator
- Application Administrator

## 8. Understanding Microsoft Graph

Microsoft Graph is Microsoft's unified API platform for accessing and managing Microsoft cloud services.

It can be used for:

- Creating users.
- Updating user properties.
- Managing groups.
- Managing directory objects.
- Retrieving identity information.

Microsoft Graph PowerShell provides PowerShell cmdlets for interacting with Microsoft Graph.

It will be used in a later practical module.

**Important:** Microsoft Graph is an API platform, not an authentication protocol or a direct replacement for LDAP.

## 9. Practical Learning Environment

Created and accessed a Microsoft Entra ID Free tenant.

Verified the following:

- Tenant creation.
- Tenant overview.
- Tenant ID.
- Primary domain.
- Microsoft Entra ID Free license.

Accessed the Microsoft Entra Admin Center successfully.

## 10. Key Takeaways

1. Microsoft Entra ID is a cloud-based IAM service.
2. A tenant represents an organisation's dedicated cloud identity directory.
3. AD DS and Entra ID have different architectures and capabilities.
4. Authentication and authorization serve different purposes.
5. UPN and Object ID identify directory users in different ways.
6. Directory roles control administrative permissions.
7. Microsoft Graph enables programmatic management of Microsoft cloud identities.

## 11. Module Status

**Completed — Microsoft Entra ID Fundamentals**

Next module: Microsoft Entra Admin Center Navigation and Identity Investigation.
