# Enterprise Applications Fundamentals

## 1. Objective

Understand how Microsoft Entra ID integrates with enterprise applications and manages application access.

## 2. Enterprise Applications

An Enterprise Application in Microsoft Entra ID represents an application instance in a tenant. It is commonly represented by a service principal.

Enterprise applications are used to manage:

- Application access assignments
- Single Sign-On (SSO)
- Application roles
- Provisioning
- Conditional Access integration
- Application audit and sign-in monitoring

## 3. Application Registration vs Enterprise Application

| App Registration | Enterprise Application |
|---|---|
| Represents the application definition | Represents the application's instance in a tenant |
| Contains Application (Client) ID | Uses the same Application (Client) ID |
| Has its own Object ID | Has its own Object ID |
| Defines authentication and API configuration | Manages tenant-level application access |

### Important observation

The Application (Client) ID was the same in the App Registration and Enterprise Application.

However, their Object IDs were different because they identify separate directory objects.

## 4. Service Principal

A service principal is the local representation of an application within a Microsoft Entra tenant.

It enables the tenant to manage the application's access and configuration.

## 5. Lab Application

Application used:

`IAM-Lab-Test-App`

The application was inspected through:

- Enterprise Applications
- App Registration
- Overview
- Properties

## 6. Key Learning

- An App Registration and Enterprise Application are related but different objects.
- The service principal represents the application in the tenant.
- Application ID and Object ID serve different purposes.
- Enterprise Applications are central to application access management.

## 7. Security Considerations

- Assign only authorised users and groups.
- Follow least privilege.
- Monitor application assignments.
- Review application permissions.
- Protect application credentials.

## 8. Conclusion

This exercise established the relationship between App Registrations, Enterprise Applications and service principals in Microsoft Entra ID.
