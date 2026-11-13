# Exercise 01 – Cloud User Provisioning

## 1. Objective

Provision a new employee identity in Microsoft Entra ID using the Entra admin center, configure employee attributes, and verify successful account creation through user properties and audit logs.

## 2. Practical Scenario

The IAM team receives an onboarding request from HR to create an account for a newly hired employee.

**Employee Details**

| Attribute | Value |
|---|---|
| Employee Name | Arun Kumar |
| Employee ID | EMP1001 |
| Department | IT |
| Job Title | Junior IT Support Analyst |
| Company | IAM Learning Lab |
| Employee Type | Employee |
| Office Location | Remote |
| Usage Location | India |

## 3. Lab Environment

- Microsoft Entra ID Free
- Microsoft Entra admin center
- Cloud-only identity
- User type: Member
- Administrator account with Global Administrator privileges

## 4. Implementation Steps

### Step 1 – Navigate to Users

1. Open Microsoft Entra admin center.
2. Navigate to Entra ID → Users → All Users.
3. Select New user.
4. Choose Create new user.

### Step 2 – Configure Basic Information

Configure the following:

| Field | Configuration |
|---|---|
| User Principal Name | arun.kumar |
| Display Name | Arun Kumar |
| Mail Nickname | arun.kumar |
| Password | Manually configured |
| Account Enabled | Yes |

The User Principal Name (UPN) is the primary sign-in name for the user.

### Step 3 – Configure Employee Properties

Navigate to the Properties tab.

**Identity**

- First Name: Arun
- Last Name: Kumar
- User Type: Member

**Job Information**

- Job Title: Junior IT Support Analyst
- Company Name: IAM Learning Lab
- Department: IT
- Employee ID: EMP1001
- Employee Type: Employee
- Office Location: Remote

**Settings**

- Usage Location: India

### Step 4 – Configure Assignments

No additional assignments were configured.

- Group assignments: None
- Administrative roles: None
- Administrative units: None

This follows the principle of least privilege.

### Step 5 – Review and Create

Reviewed the configured information and submitted the user creation request.

The account was successfully provisioned.

## 5. User Verification

Navigated to All Users and confirmed that Arun Kumar appeared in the directory.

Opened the user's profile and verified:

| Attribute | Result |
|---|---|
| Display Name | Arun Kumar |
| User Type | Member |
| Object ID | Automatically generated |
| Account Enabled | Yes |
| On-premises Sync | No |

The account was confirmed as a cloud-only identity.

## 6. Audit Log Investigation

Navigated to:

Users → Audit Logs

Located the corresponding user creation event.

**Audit Event Details**

| Field | Observed Result |
|---|---|
| Activity Type | Add user |
| Category | UserManagement |
| Status | Success |
| Initiated By | Administrator |
| Target Type | User |
| Target | Arun Kumar |

### Modified Properties Analysis

Inspected the Modified Properties tab.

The following properties were recorded:

| Property | Recorded Value |
|---|---|
| AccountEnabled | true |
| DisplayName | Arun Kumar |
| GivenName | Arun |
| Surname | Kumar |
| Department | IT |
| JobTitle | Junior IT Support Analyst |
| EmployeeId | EMP1001 |
| EmployeeType | Employee |
| CompanyName | IAM Learning Lab |
| UsageLocation | IN |
| UserType | Member |

The audit event also contained the User Principal Name and other provisioning attributes.

## 7. Key IAM Concepts Learned

**User Principal Name (UPN)**

The sign-in identifier used by an employee to authenticate to Microsoft Entra ID.

**Object ID**

A unique identifier automatically assigned to each directory object. It is used to identify the user within the Entra tenant.

**Member User**

An internal organizational identity, as opposed to an external Guest identity.

**Cloud-only Identity**

An identity created and managed directly in Microsoft Entra ID without synchronization from an on-premises Active Directory environment.

**Account Enabled**

Determines whether the account is enabled for authentication.

**Audit Logs**

Records administrative and directory activities for investigation, accountability and compliance.

**Modified Properties**

Displays the properties associated with an operation and their recorded values.

## 8. Security Considerations

- Follow the principle of least privilege.
- Do not assign unnecessary administrative roles.
- Validate employee information against the HR request.
- Use secure initial password handling.
- Never store passwords in GitHub.
- Review audit logs after provisioning.

## 10. Outcome

Successfully provisioned a cloud-only employee identity in Microsoft Entra ID.

Verified the account configuration, employee attributes, unique Object ID and successful provisioning event through Entra Audit Logs.

**Exercise Status:** Completed

**Module:** 03 – Cloud User Lifecycle Management

**Project:** 03 – Microsoft Entra ID Identity Management
