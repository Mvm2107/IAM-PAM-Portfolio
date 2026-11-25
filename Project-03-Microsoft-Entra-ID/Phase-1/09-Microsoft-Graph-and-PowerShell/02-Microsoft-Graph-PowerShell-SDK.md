# Microsoft Graph PowerShell SDK

## 1. Introduction

Microsoft Graph PowerShell SDK is a collection of PowerShell modules that allows administrators to interact with Microsoft Graph.

It provides PowerShell cmdlets for managing and investigating Microsoft Entra ID resources without manually constructing every REST API request.

For IAM analysts, it is useful for:

- Retrieving user and group information
- Managing user lifecycle operations
- Investigating directory objects
- Automating identity administration
- Generating identity reports

## 2. Practical Environment

The SDK was installed and tested using:

| Component | Version / Environment |
|---|---|
| Operating System | Windows |
| PowerShell | Windows PowerShell 5.1 |
| PowerShellGet | 2.2.6 |
| Microsoft Graph PowerShell SDK | 2.41.2 |
| Repository | PowerShell Gallery |
| Installation scope | CurrentUser |

All practical exercises were performed using the PowerShell command line.

## 3. Installing PowerShellGet

PowerShellGet is used to discover, install and manage PowerShell modules.

The following command was initially attempted:

```powershell
Install-Module PowerShellGet -Repository PSGallery -Force -AllowClobber
```

### Installation issue

The installation returned an administrator-rights error because it attempted to install modules into the system-wide PowerShell modules directory.

The error indicated that administrator privileges were required for that installation location.

### Resolution

The module was installed for the current user instead:

```powershell
Install-Module PowerShellGet -Repository PSGallery -Scope CurrentUser -Force -AllowClobber
```

PowerShell requested the NuGet provider to continue the installation.

The NuGet provider installation was accepted.

The installed module was checked using:

```powershell
Get-Module PowerShellGet -ListAvailable |
Select-Object Name,Version,Path
```

The installed PowerShellGet version was:

`2.2.6`

The module was then imported:

```powershell
Import-Module PowerShellGet -RequiredVersion 2.2.6 -Force
```

Its availability was verified:

```powershell
Get-Module PowerShellGet
```

The output confirmed that PowerShellGet version 2.2.6 was imported.

## 4. Installing Microsoft Graph PowerShell SDK

Microsoft Graph PowerShell SDK was installed using:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
```

The installation ran without requiring a system-wide installation.

The installed version was verified:

```powershell
Get-InstalledModule Microsoft.Graph
```

Observed version:

`2.41.2`

The available module was checked using:

```powershell
Get-Module Microsoft.Graph -ListAvailable |
Select-Object Name,Version,Path
```

The output confirmed that Microsoft.Graph version 2.41.2 was installed under the current user's PowerShell modules directory.

## 5. Verifying Graph Commands

The availability of the Graph authentication cmdlet was checked:

```powershell
Get-Command Connect-MgGraph
```

The output confirmed that `Connect-MgGraph` was available.

This verified that the Microsoft Graph authentication command could be discovered by PowerShell.

## 6. Important PowerShell Commands

| Command | Purpose |
|---|---|
| Install-Module | Install a PowerShell module |
| Get-InstalledModule | Display installed module information |
| Get-Module -ListAvailable | Find available modules |
| Import-Module | Load a module into the session |
| Get-Command | Find available commands |
| Update-Module | Update an installed module |
| Uninstall-Module | Uninstall a module |

## 7. Installation Scope: CurrentUser vs AllUsers

PowerShell modules can be installed at different scopes.

### CurrentUser

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
```

Installs the module for the currently signed-in Windows user.

Administrator privileges are generally not required.

### AllUsers

```powershell
Install-Module Microsoft.Graph -Scope AllUsers
```

Installs the module for all users on the computer.

This normally requires an elevated PowerShell session.

For this lab, CurrentUser installation was sufficient.

## 8. Troubleshooting Observations

### Issue 1: Administrator rights required

**Cause:** The initial installation attempted to use a system-wide module directory.

**Resolution:** Used `-Scope CurrentUser`.

### Issue 2: NuGet provider required

**Cause:** PowerShellGet required the NuGet provider to interact with the PowerShell Gallery.

**Resolution:** Accepted the provider installation prompt.

### Issue 3: Module installation appeared to take time

**Observation:** The Microsoft Graph installation initially displayed no immediate command prompt.

**Verification:** Used `Get-InstalledModule Microsoft.Graph` to confirm that installation had completed.

## 9. Practical Outcome

Successfully installed and verified:

- PowerShellGet 2.2.6
- Microsoft Graph PowerShell SDK 2.41.2

Verified that `Connect-MgGraph` was available and ready for authentication exercises.

## 10. Key Takeaways

- PowerShell modules can be installed from repositories such as PowerShell Gallery.
- `-Scope CurrentUser` avoids the need for system-wide installation privileges in this lab.
- NuGet may be required when installing modules from NuGet-based repositories.
- `Get-InstalledModule` and `Get-Module -ListAvailable` help verify module installation.
- `Import-Module` loads a module into the current PowerShell session.
- `Get-Command` verifies whether a specific cmdlet is available.

## Conclusion

The Microsoft Graph PowerShell SDK was successfully installed and verified in Windows PowerShell 5.1.

This established the environment required for subsequent authentication, directory investigation and IAM automation exercises.
