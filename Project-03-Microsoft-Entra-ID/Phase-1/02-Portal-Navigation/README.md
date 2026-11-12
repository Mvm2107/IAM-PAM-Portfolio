# Module 02 — Microsoft Entra Admin Center Navigation

## 1. Objective

Explore the Microsoft Entra Admin Center and understand how an IAM Analyst navigates the portal to manage identities, inspect user properties, review administrative permissions, and investigate identity-related activities.

## 2. Environment

- Platform: Microsoft Entra ID
- Tenant edition: Microsoft Entra ID Free
- Administration interface: Microsoft Entra Admin Center
- Environment: Cloud-only
- User accounts: 1 initial administrator account

## 3. Tenant Overview

Explored the following tenant information:

- Tenant name
- Tenant ID
- Primary domain
- Total users
- Total groups
- Registered devices
- Enterprise applications
- Tenant license information

## 4. User Profile Exploration

Navigated to:

**Entra ID → Users → All Users → Select User**

Explored the following properties:

| Property | Description |
|---|---|
| Display Name | Name displayed in the directory |
| User Principal Name | Identity used for signing in |
| Object ID | Unique identifier of the directory object |
| User Type | Member or Guest classification |
| Account Enabled | Indicates whether the account is enabled |
| Creation Date | Date and time the user was created |
| Usage Location | User's configured usage location |
| Department | Department associated with the user |
| Employee ID | Organisation's employee identifier |
| Job Title | User's organisational designation |

## 5. Administrative Roles

Explored the Assigned Roles section.

Identified the Global Administrator role assigned to the initial administrator account.

**Key learning:** Directory roles grant administrative permissions. They are different from group memberships.

## 6. Group Memberships

Explored the Groups section of the user profile.

Observation: The initial administrator account was not a member of any groups.

**Key learning:** Group membership is separate from administrative role assignment.

## 7. Authentication Methods

Explored the Authentication Methods section.

Observed the default sign-in method and authentication-method management options.

Learned the distinction between authentication methods and directory roles.

## 8. Sign-in Log Investigation

Navigation:

**Entra ID → Users → Select User → Sign-in Logs**

Observed successful sign-in events involving:

- Azure Portal
- Microsoft Azure Sign-in

Explored interactive and non-interactive sign-in logs.

Important fields:

- Date and time
- User
- Application
- Status
- Sign-in error code
- Request ID

**Key learning:** Sign-in logs help investigate authentication activity and identify potential access issues.

## 9. Audit Log Investigation

Navigation:

**Entra ID → Users → Audit Logs**

Initially, the UserManagement category filter returned no records.

After changing Category to All, multiple records appeared.

Observed activities included:

| Category | Activity | Status |
|---|---|---|
| ApplicationManagement | Add service principal | Success |
| ApplicationManagement | Add service principal | Failure |
| Authentication | Validate user authentication | Success |
| GroupManagement | Features_GetFeaturesAsync | Success |
| Policy | Add policy | Success |

## 10. Audit Event Investigation

Investigated a failed Add service principal event.

Observed:

- Service: Core Directory
- Category: ApplicationManagement
- Activity: Add service principal
- Status: Failure
- Initiating actor: Microsoft Azure AD Internal - JIT Provisioning
- Status reason: Microsoft.Online.Workflows.SpnValidationException
- Provisioning type: DefaultMicrosoft

Compared it with a successful Add service principal event.

### Investigation Findings

Both events contained:

- The same application ID
- The same initiating actor
- The same provisioning type

However, they had different correlation IDs.

### Conclusion

The events indicate that a Microsoft-managed provisioning workflow produced both successful and failed operations.

The exact cause of the failed validation was not established.

The available evidence did not establish malicious activity or an unauthorised administrator action.

## 11. Important Concepts Learned

- Tenant and directory structure
- User Principal Name (UPN)
- Object ID
- Member versus Guest
- Account enabled status
- Directory roles
- Group membership
- Authentication methods
- Interactive versus non-interactive sign-ins
- Audit logs versus sign-in logs
- Service principals
- Just-In-Time provisioning
- Correlation IDs
- Successful versus failed operations

## 12. Practical Skills Demonstrated

- Navigated Microsoft Entra Admin Center.
- Explored user properties.
- Identified administrative role assignments.
- Reviewed group memberships.
- Inspected authentication settings.
- Investigated sign-in activity.
- Filtered audit records.
- Compared successful and failed audit events.

## 13. Module Status

**Completed — Portal Navigation and Basic Identity Investigation**

Next module: Cloud User Lifecycle Management.
