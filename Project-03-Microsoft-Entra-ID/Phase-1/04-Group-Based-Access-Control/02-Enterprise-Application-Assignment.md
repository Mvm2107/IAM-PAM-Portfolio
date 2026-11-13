# Enterprise Application Assignment in Microsoft Entra ID

## 1. Objective

The objective of this practical exercise was to understand how enterprise applications are created and how administrators assign and remove user access in Microsoft Entra ID.

### Learning Objectives

- Understand the Microsoft Entra App Gallery.
- Understand non-gallery enterprise applications.
- Understand service principals.
- Differentiate Application ID and Object ID.
- Assign an individual user to an enterprise application.
- Understand application roles.
- Remove application assignments.
- Verify changes through audit logs.

## 2. Lab Environment

| Component | Configuration |
|---|---|
| Identity platform | Microsoft Entra ID |
| Tenant | Free cloud tenant |
| Enterprise application | IAM-Lab-Test-App |
| Test user | Arun Kumar |
| Security group | GRP-IT-Operations |
| Assignment type | Direct user assignment |

## 3. Understanding the App Gallery

Navigated to:

Microsoft Entra ID → Enterprise applications → All applications

The application list was initially empty.

Opened the Microsoft Entra App Gallery and inspected the available integration options.

Three application integration options were identified:

1. Configure Application Proxy for secure remote access to on-premises applications.
2. Register an application for integration with Microsoft Entra ID.
3. Integrate a non-gallery application.

For this exercise, selected:

**Integrate any other application you don't find in the gallery (Non-gallery).**

Created the application:

`IAM-Lab-Test-App`

## 4. Understanding the Enterprise Application

After creation, inspected the application overview.

Important properties:

| Property | Description |
|---|---|
| Name | Application display name |
| Application ID | Identifies the application |
| Object ID | Identifies the tenant-specific service principal object |

### Service Principal

A service principal is the local representation of an application in a Microsoft Entra tenant.

It allows the organisation to manage application-related configuration, assignments and permissions.

## 5. Exploring Application Management

Inspected the following application management sections:

- Properties
- Owners
- Roles and administrators
- Users and groups
- Single sign-on
- Provisioning
- Application proxy
- Audit logs

The Users and groups section is used to manage application assignments.

Initially, the application had no assigned users or groups.

## 6. Licensing Limitation

Attempted to assign the existing security group:

`GRP-IT-Operations`

The portal displayed:

"Groups are not available for assignment due to your Active Directory plan level. You can assign individual users to the application."

This confirmed that group assignment was unavailable under the tenant's current licensing level.

No paid licence was purchased.

To continue the practical exercise, individual user assignment was used.

## 7. Direct User Assignment

Selected:

User: Arun Kumar

Application: IAM-Lab-Test-App

Application role: User

Confirmed the assignment.

The Users and groups page displayed Arun Kumar with object type User.

### Result

The direct user assignment was successful.

## 8. Audit Log Verification – Application Assignment

Navigated to:

Enterprise applications → IAM-Lab-Test-App → Audit logs

Identified the event:

`Add app role assignment grant to user`

Verified the following fields:

| Field | Observed value |
|---|---|
| Service | Core Directory |
| Category | UserManagement |
| Activity | Add app role assignment grant to user |
| Status | Success |
| Target 1 | IAM-Lab-Test-App |
| Target 2 | Arun Kumar |
| AppRole.DisplayName | User |

### Important Modified Properties

- AppRole.Id
- AppRole.DisplayName
- User.ObjectID
- User.UPN
- Target service principal identifier

This confirmed that the application assignment was successfully recorded.

## 9. Application Assignment Removal

Selected Arun Kumar in the Users and groups section.

Clicked Remove assignment and confirmed the operation.

Verified that the application assignment list displayed:

`No application assignments found`

### Audit Log Verification

Identified the event:

`Remove app role assignment from user`

Verified:
- Category: UserManagement
- Status: Success
- Target: IAM-Lab-Test-App
- Target user: Arun Kumar

The audit log confirmed that the assignment was removed.

## 10. Important IAM Concepts Learned

### Application Assignment vs User Account Deletion

Removing an application assignment does not delete the user's Entra account.

The user account remains available in the directory.

Only the relationship granting that particular application assignment is removed.

### Direct Assignment vs Group Assignment

Direct assignment grants an application role to an individual user.

Group assignment grants an application role to a group, allowing eligible group members to receive access through the group assignment.

Our tenant supported the first method but blocked the second.

## 11. Practical Results

| Exercise | Result |
|---|---|
| Browse App Gallery | Completed |
| Create non-gallery application | Completed |
| Inspect application properties | Completed |
| Understand service principal | Completed |
| Inspect Users and groups | Completed |
| Assign Arun Kumar | Successful |
| Verify assignment audit log | Successful |
| Remove Arun Kumar assignment | Successful |
| Verify removal audit log | Successful |
| Group assignment | Blocked by licensing |

## 12. Conclusion

This exercise demonstrated how Microsoft Entra administrators manage direct user assignments to enterprise applications.

It also demonstrated how application access can be removed without deleting the user's directory account.

Audit logs provided evidence of both granting and removing application access.

Group-based application assignment was investigated but could not be performed because of the tenant's licensing restriction.

**Lab limitation:** IAM-Lab-Test-App was created as a non-gallery application without an external application backend or configured SSO. Therefore, successful assignment verified the Entra assignment workflow, not an actual application login.
