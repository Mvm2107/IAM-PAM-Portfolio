# Group-Based Access Control (GBAC)

## 1. Introduction

Group-Based Access Control (GBAC) is an identity and access management approach in which permissions are assigned to groups rather than individually assigning permissions to every user.

In Microsoft Entra ID, administrators can use security groups to organise users and manage access to applications and resources.

### Objectives

- Understand Group-Based Access Control.
- Understand the relationship between users, groups and applications.
- Differentiate group membership from application assignment.
- Understand direct user assignment versus group assignment.
- Understand the principle of least privilege.

## 2. Core Concepts

### 2.1 Users

A user represents an individual identity in Microsoft Entra ID.

Example:
- Arun Kumar
- Priya Sharma

Users authenticate using their assigned credentials and receive access according to their permissions and assignments.

### 2.2 Security Groups

A security group is a collection of user or other supported directory objects used to manage access collectively.

Example:

`GRP-IT-Operations`

Members:
- Arun Kumar

Instead of configuring access individually for every employee, administrators can manage users through groups.

### 2.3 Enterprise Applications

An enterprise application represents an application's identity within an Entra tenant. It is commonly represented by a service principal.

Administrators can manage:
- User and group assignments
- Application roles
- Single sign-on configuration
- Provisioning
- Application-related audit logs

## 3. Group Membership vs Application Assignment

These are two different operations.

**Group membership:**

A user is added to a security group.

Example:

Arun Kumar → GRP-IT-Operations

**Application assignment:**

A user or group is assigned to an enterprise application.

Example:

GRP-IT-Operations → IAM-Lab-Test-App

Group membership alone does not automatically grant access to every enterprise application.

The group must be assigned to the application, and the application must support the relevant access configuration.

## 4. Direct User Assignment vs Group Assignment

| Direct user assignment | Group assignment |
|---|---|
| Assign an individual user | Assign a security group |
| Manage assignments individually | Manage access through group membership |
| Suitable for individual access requirements | Suitable for managing access across teams |
| More administrative effort at scale | Easier to maintain at scale |

## 5. Application Roles

An application role defines a role that an application makes available for assignment.

For example:
- User
- Administrator
- Reader

The actual roles depend on the application's configuration.

In our lab, the non-gallery application exposed the default `User` assignment role.

## 6. Least Privilege

The principle of least privilege means providing users only the access necessary to perform their assigned responsibilities.

Example:

An IT Support employee should not automatically receive Finance application permissions.

Access should be based on:
- Job responsibilities
- Department
- Business requirements
- Approved access requests

## 7. Microsoft Entra Licensing Limitation

During the practical exercise, the tenant displayed this warning:

"Groups are not available for assignment due to your Active Directory plan level."

Therefore, group-based enterprise application assignment could not be completed in our free tenant.

We used direct user assignment to understand the application assignment workflow.

No paid licence was purchased or activated.

## 8. Key Takeaways

- Groups simplify access management.
- Group membership and application assignment are different.
- Direct user assignment is different from group assignment.
- Application roles define the access role available for assignment.
- Least privilege is an important IAM principle.
- Audit logs help investigate access changes.
- Licensing determines which Entra features are available.

## 9. Conclusion

This module introduced Group-Based Access Control and its importance in enterprise identity management.

The practical exercises demonstrated direct application assignment, access removal and audit verification. Group-based application assignment was studied conceptually, with the tenant licensing restriction documented as a lab limitation.
