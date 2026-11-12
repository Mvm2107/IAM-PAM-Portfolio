<#
.SYNOPSIS
    Bulk Active Directory User Provisioning

.DESCRIPTION
    Creates Active Directory user accounts using employee
    information imported from a CSV file.

.AUTHOR
    IAM-PAM Portfolio Lab

.ENVIRONMENT
    Windows Server Active Directory
#>

# Import Active Directory module
Import-Module ActiveDirectory -ErrorAction Stop

# Define CSV file path
$CsvPath = "C:\IAM-Lab\bulk_users.csv"

# Validate CSV file
if (-not (Test-Path -Path $CsvPath)) {
    Write-Host "CSV file not found: $CsvPath" -ForegroundColor Red
    return
}

# Import employee records
$Users = Import-Csv -Path $CsvPath -ErrorAction Stop

# Validate imported employee records
if ($null -eq $Users -or $Users.Count -eq 0) {
    Write-Host "CSV file contains no employee records." -ForegroundColor Red
    return
}

# Validate required CSV columns
$RequiredColumns = @(
    "FirstName",
    "LastName",
    "Username",
    "UPN",
    "Department",
    "OU",
    "Group"
)

$MissingColumns = $RequiredColumns | Where-Object {
    $_ -notin $Users[0].PSObject.Properties.Name
}

if ($MissingColumns) {
    Write-Host "Missing CSV columns: $($MissingColumns -join ', ')" -ForegroundColor Red
    return
}

# Validate duplicate usernames within CSV
$DuplicateUsernames = $Users |
    Group-Object -Property Username |
    Where-Object { $_.Count -gt 1 }

if ($DuplicateUsernames) {
    Write-Host "Duplicate usernames found in CSV:" -ForegroundColor Red

    $DuplicateUsernames | ForEach-Object {
        Write-Host $_.Name -ForegroundColor Red
    }

    return
}

# Validate individual employee records
foreach ($User in $Users) {

    # Check for blank employee fields
    if (
        [string]::IsNullOrWhiteSpace($User.FirstName) -or
        [string]::IsNullOrWhiteSpace($User.LastName) -or
        [string]::IsNullOrWhiteSpace($User.Username) -or
        [string]::IsNullOrWhiteSpace($User.UPN) -or
        [string]::IsNullOrWhiteSpace($User.Department) -or
        [string]::IsNullOrWhiteSpace($User.OU) -or
        [string]::IsNullOrWhiteSpace($User.Group)
    ) {
        Write-Host "Incomplete employee record: $($User.Username)" -ForegroundColor Red
        return
    }

    # Validate department, OU and group mapping
    if (
        ($User.Department -eq "HR" -and $User.OU -eq "OU=HR,DC=corp,DC=example,DC=com" -and $User.Group -eq "HR_Users") -or
        ($User.Department -eq "Finance" -and $User.OU -eq "OU=Finance,DC=corp,DC=example,DC=com" -and $User.Group -eq "Finance_Read") -or
        ($User.Department -eq "IT" -and $User.OU -eq "OU=IT,DC=corp,DC=example,DC=com" -and $User.Group -eq "IT_Support")
    ) {
        Write-Host "$($User.Username) - Mapping VALID" -ForegroundColor Green
    }
    else {
        Write-Host "$($User.Username) - Mapping INVALID" -ForegroundColor Red
        return
    }
}

# Validate AD Organizational Units and Security Groups
foreach ($User in $Users) {

    try {
        Get-ADOrganizationalUnit -Identity $User.OU -ErrorAction Stop |
            Out-Null

        Get-ADGroup -Identity $User.Group -ErrorAction Stop |
            Out-Null

        Write-Host "$($User.Username) - OU and Group exist" -ForegroundColor Green
    }
    catch {
        Write-Host "Invalid AD configuration for $($User.Username)" -ForegroundColor Red
        Write-Host $_.Exception.Message
        return
    }
}

Write-Host "Successfully imported $($Users.Count) employee records." -ForegroundColor Green

# Collect temporary password securely
$Password = Read-Host "Enter temporary password" -AsSecureString


# Process each employee record
foreach ($User in $Users) {
    $Stage = "Duplicate account check"
    try {

        # Check whether the account already exists
        $ExistingUser = Get-ADUser -Filter "SamAccountName -eq '$($User.Username)'" -ErrorAction Stop

        if ($ExistingUser) {
            Write-Host "$($User.Username) already exists. Skipping." -ForegroundColor Yellow
            continue
        }
        else {
        $Stage = "Account creation"
        # Create AD user account
        New-ADUser `
            -Name "$($User.FirstName) $($User.LastName)" `
            -GivenName $User.FirstName `
            -Surname $User.LastName `
            -SamAccountName $User.Username `
            -UserPrincipalName $User.UPN `
            -Department $User.Department `
            -Path $User.OU `
            -AccountPassword $Password `
            -ChangePasswordAtLogon $true `
            -Enabled $false `
            -ErrorAction Stop
    
        $Stage = "Group assignment"
        # Assign department security group
        Add-ADGroupMember `
            -Identity $User.Group `
            -Members $User.Username `
            -ErrorAction Stop
            
       $Stage = "Account enablement"
        # Enable the AD account
        Enable-ADAccount `
            -Identity $User.Username `
            -ErrorAction Stop
    
        # Display success message
        Write-Host "$($User.Username) provisioned successfully." -ForegroundColor Green
          
            }
    
      }
    catch {
        Write-Host "Provisioning failed for $($User.Username)" -ForegroundColor Red
        Write-Host "Failed stage: $Stage" -ForegroundColor Yellow
        Write-Host $_.Exception.Message
        continue
         }
}
