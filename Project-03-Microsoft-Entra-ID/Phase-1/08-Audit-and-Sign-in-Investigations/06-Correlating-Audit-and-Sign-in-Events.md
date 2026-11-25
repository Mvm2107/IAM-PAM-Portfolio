# Lesson 6 – Correlating Audit and Sign-in Events

## 1. Objective

Understand how to analyse Audit Logs and Sign-in Logs together to reconstruct identity-related activities.

## 2. What is Event Correlation?

Event correlation is the process of connecting multiple events to understand the sequence and context of activities.

For example:

- A user account is disabled.
- The same user attempts to sign in afterward.
- The authentication attempt fails.

Examining the events together provides more context than investigating each event independently.

## 3. Audit Logs vs Sign-in Logs

| Audit Logs | Sign-in Logs |
|---|---|
| Record directory changes | Record authentication activity |
| User created | User signs in |
| User disabled | User attempts authentication |
| Group membership changed | User accesses an application |
| Role assigned | User authenticates to a resource |
| Application assignment changed | User attempts application access |

## 4. Four Correlation Techniques

### A. User Identity

Use the User Principal Name (UPN) or Object ID to identify the same account across records.

### B. Timestamp

Compare event timestamps to establish the sequence of activities.

Always account for time-zone differences, especially when records are displayed in UTC.

### C. Target Object

Compare the affected objects in Audit Logs with the user or application involved in Sign-in Logs.

### D. Correlation ID

Correlation IDs help trace related operations.

Important considerations:

- Matching IDs can help identify related operations.
- Different IDs do not automatically mean events are unrelated.
- A broader workflow can contain several separate operations with different IDs.
- Correlation IDs should not be used as the only matching criterion.

## 5. Practical Learning

The module included comparison of actual Audit Log and Sign-in Log records inspected in the tenant.

Previously examined Audit Log events included:

- Successful Add member to role.
- Failed Add service principal.
- Successful Add service principal.

Previously examined Sign-in Log events included:

- Successful interactive Azure Portal sign-in.
- Successful non-interactive Mobility Management Policy Service sign-in.

These records were examined independently and compared using event attributes and context.

The available records did not establish that the separate operations were part of one transaction.

## 6. Simulated Correlation Scenario

### Incident: Employee Account Disabled

| Time (UTC) | Event | Source |
|---|---|---|
| 09:00 | Account disabled | Audit Log |
| 09:04 | Azure Portal sign-in attempted | Sign-in Log |
| 09:04 | Authentication failed | Sign-in Log |

Additional simulated evidence:

- Same employee identity.
- Successful account-disable operation.
- Failure reason identifies the disabled account.

### Investigation Conclusion

The supplied evidence supports the conclusion that the employee attempted to authenticate after account deactivation and the sign-in was rejected because the account was disabled.

This is a simulated scenario, not an actual tenant event.

## 7. Important Learning Points

- Correlate events using multiple attributes.
- Establish the order of events through timestamps.
- Use user and object identifiers to identify affected identities.
- Use correlation IDs as supporting evidence.
- Do not assume two events are directly related merely because they occurred close together.
- Distinguish actual tenant observations from simulated scenarios.

## 8. Conclusion

This lesson introduced the use of event correlation in IAM investigations.

It demonstrated how identity changes and authentication events can be analysed together to reconstruct activity and support investigation conclusions.
