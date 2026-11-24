# App Registration and Service Principals

## 1. Objective

Understand application identity, application credentials, API permissions and application roles.

## 2. App Registration Inspection

Inspected the App Registration for:

`IAM-Lab-Test-App`

Reviewed:

- Application ID
- Object ID
- Authentication configuration
- Certificates and secrets
- API permissions
- App roles

## 3. Certificates and Secrets

The application credential page showed:

| Credential | Observed count |
|---|---:|
| Certificates | 0 |
| Client secrets | 0 |
| Federated credentials | 0 |

No credentials were created during this exercise.

### Client Secret

A client secret is a password-like credential used by a confidential application to authenticate.

### Certificate

A certificate-based credential uses public/private key cryptography.

The application uses its private key, while the corresponding public certificate is registered with the identity provider.

### Federated Credentials

Federated credentials allow an application or workload to establish trust with an external identity provider without requiring a long-lived client secret.

## 4. API Permissions

The API permissions page showed:

`No permissions added`

No API permissions were configured or granted during this exercise.

### Delegated Permissions

Allow an application to access resources on behalf of a signed-in user, within the granted permissions.

### Application Permissions

Allow an application to access resources using its own identity, without a signed-in user.

### Admin Consent

Admin consent is an approval process that allows an administrator to grant permissions on behalf of an organisation when required.

Adding a permission and granting consent are separate operations.

## 5. App Roles

The App Registration contained two existing app roles:

- User
- msiam_access

The second role was inspected without modification.

App roles define application-specific permissions that the application can interpret during authorisation.

### App Roles vs Directory Roles

| App Roles | Directory Roles |
|---|---|
| Application-specific permissions | Entra administrative permissions |
| Defined by the application | Defined by Microsoft Entra |
| Example: HR-Admin | Example: Global Administrator |

## 6. Practical Observations

- No client secrets were created.
- No certificates were uploaded.
- No federated credentials were configured.
- No API permissions were added.
- Existing app roles were inspected.
- No configuration changes were made.

## 7. Security Considerations

- Prefer secure credential approaches appropriate to the workload.
- Protect private keys and client secrets.
- Avoid unnecessary API permissions.
- Apply least privilege.
- Review application role assignments regularly.

## 8. Conclusion

The exercise provided practical exposure to App Registration configuration, application credentials, API permissions and application roles.
