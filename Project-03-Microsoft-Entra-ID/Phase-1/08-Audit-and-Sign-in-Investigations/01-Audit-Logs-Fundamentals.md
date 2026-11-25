# Lesson 1 – Audit Logs Fundamentals

## 1. Objective

Understand Microsoft Entra Audit Logs and learn how to investigate directory activities, identify event initiators, examine affected objects and interpret modified properties.

## 2. What are Audit Logs?

Microsoft Entra Audit Logs record activities performed within the directory.

They help administrators investigate:

- Who performed an action?
- What action was performed?
- Which object was affected?
- When did the action happen?
- Did the operation succeed or fail?
- What properties were modified?

Examples include:

- User creation and deletion.
- User attribute updates.
- Group membership changes.
- Application assignment changes.
- Directory role assignments.
- Service-principal creation.

## 3. Audit Logs vs Sign-in Logs

| Audit Logs | Sign-in Logs |
|---|---|
| Record directory activities | Record authentication activity |
| User created | User signs in |
| Group membership changed | Sign-in succeeds or fails |
| Account disabled | Authentication attempt |
| Role assigned | Application or resource access attempt |

Audit Logs explain directory changes, while Sign-in Logs provide authentication context.

## 4. Important Audit Log Fields

| Field | Description |
|---|---|
| Date and time | When the event occurred |
| Activity | Action performed |
| Category | Type of directory activity |
| Initiated by | User or application that initiated the operation |
| Target(s) | Object or objects affected |
| Result | Success or failure |
| Correlation ID | Identifier useful for tracing related operations |
| Modified properties | Properties changed during the operation |

## 5. Practical Investigation 1 – Add Member to Role

### Observed Event

An actual successful `Add member to role` event was inspected.

| Field | Observed value |
|---|---|
| Activity | Add member to role |
| Category | RoleManagement |
| Result | Success |
| Initiator | Microsoft Azure AD Internal - JIT Provisioning |
| Initiator type | Application |
| Target service principal | Microsoft.Azure.SyncFabric |
| Assigned role | Directory Readers |

### Modified Properties

The event contained role-related properties, including:

- Role.ObjectID
- Role.DisplayName
- Role.TemplateId
- Role.WellKnownName

The role display name was Directory Readers.

### Investigation Findings

- The initiator was an application, not a named administrator.
- The target was a service principal.
- The assigned directory role was Directory Readers.
- The operation completed successfully.

The event does not independently establish why the assignment was required or whether it was expected.

## 6. Practical Investigation 2 – Failed Service Principal Creation

### Observed Event

An actual failed `Add service principal` event was inspected.

| Field | Observed value |
|---|---|
| Activity | Add service principal |
| Category | ApplicationManagement |
| Result | Failure |
| Initiator | Microsoft Azure AD Internal - JIT Provisioning |
| Target | Microsoft.Azure.SyncFabric |
| Target type | ServicePrincipal |
| Status reason | Microsoft.Online.Workflows.SpnValidationException |

### Important Properties

The Modified Properties section included:

- AccountEnabled
- AppPrincipalId
- DisplayName
- ServicePrincipalNames
- Credential
- MethodExecution

### Investigation Findings

The operation failed with a service-principal validation exception.

The exception name identifies a validation-related failure but does not independently establish the precise underlying validation rule.

The presence of credential metadata does not prove that a usable credential was successfully created.

## 7. Practical Investigation 3 – Successful Service Principal Creation

Another actual `Add service principal` event was inspected.

| Field | Observed value |
|---|---|
| Activity | Add service principal |
| Category | ApplicationManagement |
| Result | Success |
| Initiator | Microsoft Azure AD Internal - JIT Provisioning |
| Target | PowerApps Service |
| Target type | ServicePrincipal |

### Investigation Findings

- The service-principal creation operation succeeded.
- The target was PowerApps Service.
- The event contained application and service-principal configuration properties.
- Credential metadata was present.

## 8. Event Comparison

The three inspected events had different target objects and correlation IDs.

Although the same named Microsoft internal application initiated all three operations, the available evidence does not establish that they were one transaction.

The failed SyncFabric creation and successful SyncFabric role assignment should not automatically be treated as directly related.

## 9. Important Learning Points

- Always inspect the initiator and target.
- Distinguish user-initiated and application-initiated operations.
- Examine Modified Properties to understand what changed.
- Do not assume that a successful operation is automatically authorised.
- Do not classify every failed operation as malicious.
- Use correlation IDs alongside timestamps, object identifiers and event details.

## 10. Conclusion

This lesson provided practical exposure to Microsoft Entra Audit Logs through the investigation of directory role assignments and service-principal creation events.

It demonstrated how an IAM Analyst can identify the initiator, target object, operation result and modified properties while avoiding conclusions that are not supported by the available evidence.
