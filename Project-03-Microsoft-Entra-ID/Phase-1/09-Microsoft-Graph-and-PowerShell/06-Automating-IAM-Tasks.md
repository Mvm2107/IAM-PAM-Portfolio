# Automating IAM Tasks with PowerShell

## 1. Introduction

IAM teams regularly perform repetitive activities such as:

- Preparing user inventories
- Identifying disabled accounts
- Finding incomplete user records
- Reviewing account status
- Generating operational reports

Microsoft Graph PowerShell SDK can automate these activities by retrieving directory information and processing it using PowerShell.

This practical focused on developing a reusable IAM user-reporting script.

## 2. Practical Environment

| Component | Details |
|---|---|
| Platform | Windows PowerShell |
| Directory | Microsoft Entra ID |
| API interface | Microsoft Graph PowerShell SDK |
| Reporting format | CSV |
| Report workspace | Documents/IAM-Automation |
| Automation script | IAM-User-Reporting.ps1 |

## 3. Creating the Reporting Workspace

A dedicated folder was created to store the automation script and generated reports.

```powershell
$ReportPath = "$env:USERPROFILE\Documents\IAM-Automation"

New-Item -Path $ReportPath -ItemType Directory -Force

Get-Item $ReportPath
```

The folder was successfully created and verified.

## 4. Retrieving the User Inventory

All available Entra users were retrieved using:

```powershell
$Users = Get-MgUser -All -Property `
Id,DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle,CreatedDateTime

$Users.Count
```

The `-All` parameter handles pagination and retrieves all available user records.

The retrieved data was inspected using:

```powershell
$Users |
Select-Object DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle |
Format-Table -AutoSize
```

### Practical observation

Four user records were retrieved:

- Arun Kumar
- Graph Lab User
- Manivannan M
- Priya Sharma

## 5. Calculating Account Statistics

PowerShell's `Where-Object` and `Count` properties were used to calculate account statistics.

### Enabled accounts

```powershell
($Users | Where-Object {
    $_.AccountEnabled -eq $true
}).Count
```

### Disabled accounts

```powershell
($Users | Where-Object {
    $_.AccountEnabled -eq $false
}).Count
```

### Users with missing department information

```powershell
$MissingDepartment = $Users | Where-Object {
    [string]::IsNullOrWhiteSpace($_.Department)
}

$MissingDepartment.Count
```

### Practical results

| Metric | Observed result |
|---|---:|
| Total users | 4 |
| Enabled users | 2 |
| Disabled users | 2 |
| Missing department | 1 |

These figures represent the user inventory retrieved during the exercise.

## 6. Exporting the Complete User Inventory

The retrieved user records were exported into CSV format.

```powershell
$Users |
Select-Object DisplayName,UserPrincipalName,AccountEnabled,Department,JobTitle,CreatedDateTime |
Export-Csv -Path "$ReportPath\Entra-User-Inventory.csv" -NoTypeInformation -Encoding UTF8
```

The generated file was verified using:

```powershell
Get-Item "$ReportPath\Entra-User-Inventory.csv"
```

Its contents were inspected using:

```powershell
Import-Csv "$ReportPath\Entra-User-Inventory.csv" |
Format-Table DisplayName,AccountEnabled,Department,JobTitle -AutoSize
```

The file was successfully created and its records were displayed.

## 7. Generating a Disabled-User Report

Disabled accounts were filtered from the previously retrieved user inventory.

```powershell
$DisabledUsers = $Users | Where-Object {
    $_.AccountEnabled -eq $false
}
```

The disabled-user report was exported:

```powershell
$DisabledUsers |
Select-Object DisplayName,UserPrincipalName,Department,JobTitle |
Export-Csv -Path "$ReportPath\Disabled-Users-Report.csv" -NoTypeInformation -Encoding UTF8
```

The report was verified:

```powershell
Import-Csv "$ReportPath\Disabled-Users-Report.csv" |
Format-Table -AutoSize
```

### Practical observation

The report contained:

- Arun Kumar
- Priya Sharma

A total of two disabled accounts were identified.

## 8. Identifying Missing Department Information

Incomplete user attributes can affect access reviews and identity provisioning workflows.

Users without a department value were identified using:

```powershell
$MissingDepartment = $Users | Where-Object {
    [string]::IsNullOrWhiteSpace($_.Department)
}
```

The results were exported:

```powershell
$MissingDepartment |
Select-Object DisplayName,UserPrincipalName,AccountEnabled |
Export-Csv -Path "$ReportPath\Missing-Department-Report.csv" -NoTypeInformation -Encoding UTF8
```

Verification:

```powershell
Import-Csv "$ReportPath\Missing-Department-Report.csv" |
Format-Table -AutoSize
```

### Practical observation

The report identified Manivannan M as having no department value populated.

One user record with missing department information was found.

## 9. PowerShell Error Handling

Error handling helps automation scripts respond to unexpected failures.

Three important concepts were practised:

| Concept | Purpose |
|---|---|
| try | Executes the main operation |
| catch | Handles a terminating error |
| -ErrorAction Stop | Converts a command error into a terminating error that can be handled by catch |

A test was performed using an invalid user identifier:

```powershell
try {
    Get-MgUser -UserId "invalid-user-id" -ErrorAction Stop
}
catch {
    Write-Host "User lookup failed."
    Write-Host "Error: $($_.Exception.Message)"
}
```

### Practical result

The command returned a resource-not-found error.

The catch block handled the error and displayed the message instead of allowing the test operation to terminate without the intended error handling.

This demonstrated how automation scripts can handle individual command failures.

## 10. Generating a Consolidated IAM Summary

A summary object was created using PowerShell's `[PSCustomObject]`.

```powershell
$TotalUsers = $Users.Count

$EnabledCount = ($Users | Where-Object {
    $_.AccountEnabled -eq $true
}).Count

$DisabledCount = ($Users | Where-Object {
    $_.AccountEnabled -eq $false
}).Count

$MissingDepartmentCount = ($Users | Where-Object {
    [string]::IsNullOrWhiteSpace($_.Department)
}).Count

[PSCustomObject]@{
    TotalUsers = $TotalUsers
    EnabledUsers = $EnabledCount
    DisabledUsers = $DisabledCount
    MissingDepartment = $MissingDepartmentCount
} | Format-List
```

### Observed summary

| Metric | Result |
|---|---:|
| Total users | 4 |
| Enabled users | 2 |
| Disabled users | 2 |
| Missing department | 1 |

The summary was exported:

```powershell
$Summary = [PSCustomObject]@{
    TotalUsers = $TotalUsers
    EnabledUsers = $EnabledCount
    DisabledUsers = $DisabledCount
    MissingDepartment = $MissingDepartmentCount
}

$Summary | Export-Csv `
-Path "$ReportPath\IAM-Summary-Report.csv" `
-NoTypeInformation -Encoding UTF8
```

It was verified using:

```powershell
Import-Csv "$ReportPath\IAM-Summary-Report.csv" |
Format-List
```

## 11. Building the Reusable Automation Script

The individual reporting operations were combined into a reusable PowerShell script:

`IAM-User-Reporting.ps1`

The script performs the following operations:

1. Checks and prepares the reporting folder.
2. Checks the Microsoft Graph authentication context.
3. Connects to Graph if no context is available.
4. Retrieves Entra users.
5. Exports the complete user inventory.
6. Identifies disabled accounts.
7. Identifies missing department attributes.
8. Calculates account statistics.
9. Exports the consolidated summary.
10. Displays the report-generation result.
11. Handles errors using try/catch.

The script was saved using Notepad and executed from PowerShell.

Execution command:

```powershell
& "$ReportPath\IAM-User-Reporting.ps1"
```

The automation executed successfully and displayed the expected summary.

## 12. Generated Files

The following files were created and verified in the reporting folder:

| File | Purpose |
|---|---|
| IAM-User-Reporting.ps1 | Reusable automation script |
| Entra-User-Inventory.csv | Complete user inventory |
| Disabled-Users-Report.csv | Disabled account report |
| Missing-Department-Report.csv | Missing department report |
| IAM-Summary-Report.csv | Consolidated IAM statistics |

All five files were verified in the local reporting workspace.

## 13. Understanding the PowerShell Concepts

| Command / Concept | Purpose |
|---|---|
| Variables | Store retrieved objects and values |
| Get-MgUser | Retrieve Entra users |
| Where-Object | Filter user records |
| Select-Object | Select required attributes |
| Count | Count returned objects |
| Measure-Object | Measure or count pipeline objects |
| PSCustomObject | Create structured custom objects |
| Export-Csv | Export data into CSV format |
| Import-Csv | Read CSV files |
| Test-Path | Check whether a path exists |
| New-Item | Create a directory |
| try/catch | Handle errors |
| Write-Host | Display script messages |

## 14. Important Automation Considerations

### Point-in-time reporting

The user inventory was retrieved once and stored in `$Users`.

The subsequent reports were generated from that same dataset. They therefore represent a snapshot of the directory at retrieval time.

For fresh reporting, the script should retrieve users again.

### Read-only reporting

The reporting script retrieves directory information and exports files.

It does not create, update, disable or delete user accounts.

### Permissions

The script requires appropriate delegated Microsoft Graph permissions to read users.

The current authentication context and directory authorization should be verified before execution.

### Sensitive information

User inventory reports may contain personal and organisational information.

Reports should be stored securely and shared only with authorized personnel.

## 15. Key Takeaways

- Microsoft Graph can be combined with PowerShell to automate IAM reporting.
- `Get-MgUser -All` retrieves paginated user records.
- `Where-Object` supports account filtering.
- `Export-Csv` generates reusable reports.
- `Import-Csv` verifies exported data.
- `[PSCustomObject]` creates structured reporting objects.
- `try/catch` improves script error handling.
- Reusable scripts reduce repetitive administrative work.
- IAM reports must be protected because they contain directory information.

## Conclusion

This practical developed a reusable Entra ID user-reporting automation script using Microsoft Graph PowerShell SDK.

The exercise covered user inventory retrieval, disabled-account identification, missing-attribute detection, CSV reporting, consolidated statistics and error handling.

The final script executed successfully and generated four verified CSV reports.
