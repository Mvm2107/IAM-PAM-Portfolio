# Microsoft Graph Fundamentals

## 1. Introduction

Microsoft Graph is Microsoft's unified API endpoint for accessing and managing data across Microsoft cloud services.

In Microsoft Entra ID, Microsoft Graph allows administrators and IAM analysts to interact with directory objects such as:

- Users
- Groups
- Applications
- Service principals
- Directory roles
- Devices

Microsoft Graph can be accessed through REST API requests and tools such as Microsoft Graph PowerShell SDK.

## 2. Why Microsoft Graph Is Important in IAM

Identity and Access Management involves managing user identities, permissions, group memberships and application access.

Microsoft Graph helps IAM analysts perform these operations programmatically.

Common IAM use cases include:

| IAM Activity | Microsoft Graph Use |
|---|---|
| User investigation | Retrieve user attributes |
| User provisioning | Create user accounts |
| User modification | Update user properties |
| Account deactivation | Disable user accounts |
| Group investigation | Retrieve security groups |
| Membership investigation | Inspect group membership |
| Access administration | Manage supported assignments and permissions |
| Reporting | Retrieve directory information for reports |

## 3. Microsoft Graph Architecture

Microsoft Graph provides a unified API endpoint:

`https://graph.microsoft.com`

The API uses resource-based endpoints to access directory information.

Examples:

| Endpoint | Purpose |
|---|---|
| `/v1.0/users` | Retrieve users |
| `/v1.0/groups` | Retrieve groups |
| `/v1.0/me` | Retrieve the signed-in user's profile |
| `/v1.0/users/{id}` | Retrieve a specific user |

The `{id}` value represents a user identifier, such as an object ID or supported user principal name.

## 4. HTTP Methods

Microsoft Graph uses standard HTTP methods to perform operations.

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve information | Read a user |
| POST | Create a resource or perform an action | Create a user |
| PATCH | Update resource properties | Update a department |
| PUT | Replace a resource or relationship where supported | Update a supported resource |
| DELETE | Delete a resource or relationship where supported | Remove a supported resource |

The exact operation and required permissions depend on the API endpoint.

## 5. Authentication and Authorization

Microsoft Graph requires authentication using Microsoft identity platform.

After authentication, the application or tool operates with the permissions granted to it.

Two important concepts are:

### Authentication

Authentication establishes the identity of the user or application making the request.

### Authorization

Authorization determines whether that identity and its granted permissions allow the requested operation.

Successful authentication does not automatically provide permission to perform every Graph operation.

## 6. Microsoft Graph Permissions

Microsoft Graph permissions define what an application can do with directory information.

Examples:

| Permission | General purpose |
|---|---|
| User.Read | Read the signed-in user's profile |
| User.Read.All | Read user profiles across the directory |
| User.ReadWrite.All | Read and modify user profiles |
| Group.Read.All | Read group information |
| Group.ReadWrite.All | Read and manage groups |

Permissions must be considered alongside the authentication type, admin consent requirements and the signed-in user's directory authorization.

### Delegated Permissions

Delegated permissions allow an application to act on behalf of a signed-in user, within the permissions granted to the application and the user's own authorization.

### Application Permissions

Application permissions allow an application to access resources using its own identity, without a signed-in user.

Application permissions generally require administrator consent.

## 7. Microsoft Graph PowerShell SDK

Microsoft Graph PowerShell SDK provides PowerShell commands for interacting with Microsoft Graph.

Examples:

| Cmdlet | Purpose |
|---|---|
| Connect-MgGraph | Authenticate to Microsoft Graph |
| Disconnect-MgGraph | Disconnect the current Graph context |
| Get-MgContext | Inspect the current authentication context |
| Get-MgUser | Retrieve users |
| New-MgUser | Create a user |
| Update-MgUser | Update a user |
| Get-MgGroup | Retrieve groups |
| Get-MgGroupMember | Retrieve group members |

The SDK provides a PowerShell interface to Microsoft Graph API operations.

## 8. API Versions

Microsoft Graph provides different API versions.

### v1.0

The production API endpoint for generally available functionality.

### beta

Provides preview functionality that may change and is not recommended for production workloads without careful evaluation.

Example endpoints:

- `https://graph.microsoft.com/v1.0/users`
- `https://graph.microsoft.com/beta/users`

## 9. Practical Learning

During this module, Microsoft Graph was used to:

- Retrieve the signed-in user's profile.
- Retrieve Entra ID users.
- Retrieve security groups.
- Inspect user and group properties.
- Create a dedicated test user.
- Update user attributes.
- Disable and re-enable a test account.
- Investigate audit events generated by directory operations.
- Generate IAM reports using PowerShell.

The practical exercises demonstrated how Microsoft Graph can support identity administration and automation.

## 10. Key Takeaways

- Microsoft Graph provides a unified API for Microsoft cloud services.
- Entra ID directory objects can be accessed through Graph endpoints.
- Graph supports read and write operations.
- Authentication and authorization are separate concepts.
- Graph permissions must match the intended operation.
- Microsoft Graph PowerShell SDK simplifies directory administration through PowerShell.
- API operations should be verified and audited.

## Conclusion

Microsoft Graph is an important tool for modern IAM administration. Understanding its endpoints, HTTP methods, authentication and permission model provides the foundation for automating identity lifecycle management and directory investigations.
