# Application Configuration and Troubleshooting

## 1. Objective

Understand enterprise application configuration, provisioning, access troubleshooting and application lifecycle management.

## 2. Enterprise Application Lifecycle

1. Application onboarding
2. Application integration
3. User and group assignment
4. Provisioning
5. Authentication and access testing
6. Monitoring and maintenance
7. Deprovisioning

## 3. Authentication vs Provisioning

**Authentication:** Verifies the user's identity.

**Provisioning:** Creates, updates or disables the user's account in a target application.

Successful SSO does not automatically mean that a user account has been provisioned in the target application.

## 4. SCIM

System for Cross-domain Identity Management (SCIM) is a standard for automated identity provisioning.

Common operations include:

- Create user
- Update user
- Disable user
- Synchronise attributes
- Manage groups when supported

SAML and OIDC are commonly used for authentication and federation, while SCIM is used for provisioning.

## 5. Application Assignment Troubleshooting

When a user cannot access an application, investigate:

1. Is the Entra user account enabled?
2. Is the user assigned to the Enterprise Application?
3. Is assignment required?
4. Is the correct application role assigned?
5. What do the sign-in logs show?
6. Is SSO configured correctly?
7. Does the target application account exist and remain active?
8. Does the user have the required application-side permissions?

## 6. Provisioning Practical Inspection

Application inspected:

`IAM-Lab-Test-App`

Observed provisioning page:

- No provisioning configuration had been created.
- New configuration option was available.
- Start provisioning was disabled.
- Attribute mapping was not configured.
- Scoping filters were not configured.

No provisioning configuration was created.

## 7. Practical Environment Limitation

`IAM-Lab-Test-App` was a non-gallery test application.

It did not have an external application backend or configured SCIM endpoint.

Therefore:

- No real SCIM provisioning was performed.
- No external application account was created.
- No end-to-end application SSO login was performed.
- The provisioning interface was inspected only.

## 8. Troubleshooting Reference

| Problem | Investigation |
|---|---|
| Invalid audience | Entity ID and audience |
| Invalid ACS URL | Reply URL |
| Invalid signature | Signing certificate |
| User not recognised | Name ID and attributes |
| User authenticated but denied | Assignment and application authorisation |
| Provisioning failure | SCIM endpoint, credentials and attribute mapping |
| Access remains after termination | Deprovisioning and application sessions |

## 9. Integrated Joiner-Mover-Leaver Workflow

### Joiner

- Create the Entra account.
- Add appropriate group membership.
- Assign the application.
- Provision the target account if configured.
- Verify access.

### Mover

- Update department and job information.
- Remove obsolete access.
- Grant appropriate new access.
- Review application roles.
- Verify access.

### Leaver

- Disable the Entra account.
- Revoke sessions according to policy.
- Remove application assignments.
- Deprovision or disable the target application account.
- Verify removal.
- Review audit logs.

## 10. Key IAM Takeaways

- Authentication and authorisation are different.
- Application assignment and provisioning are different.
- Audit logs help reconstruct access changes.
- Sign-in logs help investigate authentication attempts.
- Least privilege must be applied throughout the application lifecycle.
- A successful Entra sign-in does not prove that the target application granted access.

## 11. Conclusion

This lesson connected enterprise application configuration, provisioning, authentication, application assignment and troubleshooting into an integrated IAM workflow.
