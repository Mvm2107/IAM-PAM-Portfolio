# Module 8 – Audit and Sign-in Investigations

## Overview

This module focuses on investigating identity-related activities and authentication events in Microsoft Entra ID.

The objective is to understand how IAM Analysts use Audit Logs and Sign-in Logs to investigate directory changes, authentication failures, successful sign-ins, access issues and potentially suspicious activities.

## Learning Objectives

- Understand Microsoft Entra Audit Logs.
- Differentiate interactive and non-interactive sign-ins.
- Interpret authentication details and sign-in error codes.
- Investigate successful and failed authentication attempts.
- Correlate audit events with sign-in events.
- Analyse identity-related security incidents.
- Document investigation findings and recommend appropriate actions.

## Module Contents

| File | Topic |
|---|---|
| 01 | Audit Logs Fundamentals |
| 02 | Interactive Sign-in Logs |
| 03 | Non-interactive Sign-in Logs |
| 04 | Understanding Log Details and Error Codes |
| 05 | Investigating Failed and Successful Sign-ins |
| 06 | Correlating Audit and Sign-in Events |
| 07 | Practical Investigation Scenarios |

## Practical Environment

- Microsoft Entra ID Free tenant
- Microsoft Entra admin center
- Audit Logs
- Interactive user sign-in logs
- Non-interactive user sign-in logs

## Practical Work Completed

1. Inspected actual directory audit events.
2. Investigated a successful directory role assignment.
3. Examined failed and successful service-principal creation events.
4. Inspected an actual successful interactive Azure Portal sign-in.
5. Examined authentication details, location, device information and Security Defaults results.
6. Inspected an actual successful non-interactive sign-in.
7. Examined federated identity credential information in the sign-in record.
8. Practised interpreting authentication errors.
9. Completed simulated IAM incident investigations.

## Important Tenant Observations

- Audit Logs contained successful and failed directory activities.
- The selected interactive Azure Portal sign-in was successful.
- The selected non-interactive sign-in was successful.
- No failed interactive sign-in records were available under the selected seven-day filter.
- No failed non-interactive sign-in records were available under the selected seven-day filter.
- The inspected sign-in records reported Security Defaults as successful.
- The inspected device records reported the devices as unmanaged and non-compliant.

These are observations from the inspected records and time ranges, not conclusions about all historical tenant activity.

## Practical Limitations

- Failed sign-in investigations were practised using simulated scenarios because no failed records were available in the selected period.
- Risk assessments were based on available sign-in evidence.
- The absence of a log record does not prove that an event never occurred.
- A successful sign-in does not automatically establish that the activity was legitimate.
- Correlation between events requires multiple supporting attributes and should not rely exclusively on correlation IDs.

## Key Learning Outcomes

After completing this module, I can:

- Navigate Microsoft Entra Audit Logs and Sign-in Logs.
- Identify event initiators and affected directory objects.
- Interpret authentication results and error codes.
- Differentiate interactive and non-interactive authentication.
- Examine device, location and Conditional Access information.
- Correlate identity changes with authentication activity.
- Prepare structured IAM investigation summaries.

## Conclusion

This module provided practical exposure to Microsoft Entra monitoring and investigation capabilities. It strengthened my understanding of identity auditing, authentication troubleshooting, access investigation and security incident analysis.

The practical exercises combined actual tenant observations with clearly identified simulated investigation scenarios.
