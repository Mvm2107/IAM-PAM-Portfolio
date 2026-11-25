# Connecting and Authentication – Microsoft Graph PowerShell

## 1. Introduction

Microsoft Graph requires authentication before PowerShell can access directory resources.

The Microsoft Graph PowerShell SDK provides the `Connect-MgGraph` cmdlet to establish an authenticated session.

During this practical exercise, delegated authentication was used to connect to the Microsoft Entra ID tenant.

## 2. Connecting to Microsoft Graph

The initial connection command was:

```powershell
Connect-MgGraph -Scopes "User.Read.All","Group.Read.All"
```

This requested delegated permissions to read user and group information.

After successful authentication, PowerShell displayed:

```text
Welcome to Microsoft Graph!

Connected via delegated access
```

This confirmed that the authentication process completed successfully.

## 3. Understanding Delegated Authentication

Delegated authentication allows an application or tool to access resources on behalf of a signed-in user.

The effective access depends on:

- Permissions granted to the application
- The signed-in user's own authorization
- The resource being accessed
- Any applicable tenant restrictions

Successful authentication alone does not guarantee access to every directory operation.

## 4. Inspecting the Authentication Context

The current Graph connection was inspected using:

```powershell
Get-MgContext
```

The output included:

| Property | Meaning |
|---|---|
| ClientId | Application identifier used for authentication |
| TenantId | Microsoft Entra tenant identifier |
| Scopes | Delegated permissions available in the context |
| AuthType | Authentication type |
| TokenCredentialType | Credential method |
| AppName | Application used for authentication |
| ContextScope | Lifetime and scope of the authentication context |
| WamEnabled | Indicates whether Web Account Manager is enabled |

The practical session showed:

- AuthType: Delegated
- TokenCredentialType: InteractiveBrowser
- AppName: Microsoft Graph Command Line Tools
- ContextScope: Process
- WamEnabled: True

## 5. Inspecting Delegated Scopes

The delegated permissions in the current session were inspected using:

```powershell
(Get-MgContext).Scopes | Sort-Object
```

The initial connection included:

- email
- openid
- profile
- User.Read
- User.Read.All

During later exercises, additional permissions were requested and consented to.

The practical session subsequently included:

- Group.Read.All
- User.ReadWrite.All

The scopes shown by `Get-MgContext` were used to verify the permissions available in the active Graph context.

## 6. Requesting Additional Permissions

During the practical exercise, group membership investigation and user lifecycle operations required permissions beyond basic profile reading.

An additional permission was requested through a new Graph authentication request.

For example:

```powershell
Connect-MgGraph -Scopes "User.Read.All","Group.Read.All","User.ReadWrite.All"
```

The Microsoft sign-in page displayed a permissions-request screen for Microsoft Graph Command Line Tools.

The requested permissions were reviewed and consented to.

After successful consent, the authentication context was inspected again.

### Important distinction

Requesting a scope does not independently guarantee authorization.

The permission must be granted through the appropriate consent process, and the signed-in identity must have sufficient authorization for the requested operation.

## 7. Web Account Manager (WAM)

During authentication, PowerShell displayed a warning explaining that Web Account Manager (WAM) was enabled by default on Windows.

WAM is a Windows authentication component used to manage account sign-in experiences.

The practical environment used interactive browser authentication.

The authentication output also indicated that the interactive sign-in window might appear behind other windows when using an embedded terminal.

## 8. Authentication Context and Process Scope

The authentication context was inspected and showed:

```text
ContextScope : Process
```

This means the Graph context was associated with the current PowerShell process.

The practical connection was therefore not intended to be treated as a permanent system-wide session.

When the PowerShell process is terminated, its in-memory Graph context is no longer available to that process.

A new PowerShell process may require a new authentication session.

## 9. Disconnecting from Microsoft Graph

The following command was used to disconnect:

```powershell
Disconnect-MgGraph
```

The context was then checked:

```powershell
Get-MgContext
```

The command returned no active Graph context.

Explicit disconnection is a useful practice at the end of an administrative session.

Closing the PowerShell process also ends its process-scoped Graph context.

## 10. Authentication Troubleshooting

### Issue 1: Sign-in method limit reached

During a later authentication attempt, the Microsoft sign-in page displayed:

```text
You've reached your limit with this sign-in method
```

This indicated that the selected sign-in method could not be used for that attempt.

The practical exercise was paused rather than repeatedly attempting the same sign-in method.

### Issue 2: Existing authentication context

After a failed authentication attempt, `Get-MgContext` was used to inspect the current session.

The available scopes were checked using:

```powershell
(Get-MgContext).Scopes | Sort-Object
```

The existing context was inspected before continuing with further Graph requests.

### Issue 3: Missing permission

A Graph operation may fail when the active session does not contain the required delegated scope or when the signed-in identity lacks sufficient authorization.

The following commands help investigate the authentication context:

```powershell
Get-MgContext | Format-List Account,TenantId,Scopes,AuthType,ContextScope
```

```powershell
(Get-MgContext).Scopes | Sort-Object
```

## 11. Practical Outcome

The following activities were completed:

- Connected to Microsoft Graph using delegated authentication.
- Inspected the Graph authentication context.
- Identified the tenant and application context.
- Examined delegated scopes.
- Requested additional Graph permissions.
- Reviewed and accepted the permissions request.
- Verified the updated authentication context.
- Disconnected from Microsoft Graph.

## 12. Key Takeaways

- `Connect-MgGraph` establishes an authenticated Graph session.
- Delegated permissions allow an application to act on behalf of a signed-in user.
- `Get-MgContext` helps investigate the active authentication context.
- Graph scopes define the permissions requested and granted to the session.
- Authentication and authorization are separate concepts.
- WAM supports Windows authentication experiences.
- `Disconnect-MgGraph` explicitly disconnects the current Graph context.
- Process-scoped authentication ends with the associated PowerShell process.

## Conclusion

The practical exercise demonstrated how to authenticate to Microsoft Graph, inspect delegated permissions, understand the authentication context and troubleshoot sign-in issues.

These skills are important for IAM analysts who use Microsoft Graph PowerShell for directory administration and automation.
