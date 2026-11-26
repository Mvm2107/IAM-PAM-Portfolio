# Identity Governance & Administration (IGA) Simulator

![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## Project Overview

The Identity Governance & Administration (IGA) Simulator is an independently developed Python-based project inspired by enterprise Identity Governance concepts and SailPoint IdentityIQ and Identity Security Cloud capabilities.

It simulates how an organization manages employee identities, application accounts, access permissions, approval workflows, access certifications and governance policies.

The project uses free development tools, synthetic employee data and an existing Active Directory lab where practical.

**Important:** This project is not an actual SailPoint implementation and does not require a SailPoint subscription or licence.

## Business Scenario

The simulator represents a fictional enterprise named **TechNova Solutions**.

The organization has multiple departments:

- Engineering
- Finance
- Human Resources
- Information Technology
- Sales

Its business applications include:

- Microsoft Active Directory
- HR Portal
- Finance Portal
- Customer Relationship Management (CRM)

The simulator acts as a simplified governance layer for managing employee identities and their application access.

## Project Objectives

The project aims to demonstrate the following IGA capabilities:

1. Identity Lifecycle Management (Joiner, Mover and Leaver).
2. Application Onboarding.
3. Access Request and Approval Workflows.
4. Role-Based Access Control (RBAC).
5. Entitlement Management.
6. Access Certification Campaigns.
7. Segregation of Duties (SoD) Checks.
8. Account Provisioning and Deprovisioning.
9. Audit Reporting and Remediation Evidence.

## Technology Stack

| Component | Technology |
|---|---|
| Programming | Python 3.12 |
| Directory Services | Microsoft Active Directory |
| Automation | PowerShell |
| Data Exchange | CSV and JSON |
| Version Control | Git |
| Repository | GitHub |
| Documentation | Markdown |
| Development | Visual Studio Code |
| Testing | Python unittest |

The initial implementation prioritizes Python standard-library modules and existing Windows capabilities.

## Architecture

The simulator follows a modular architecture:

```text
HR Identity Source (CSV)
          |
          v
   Identity Engine
          |
          v
 Identity Lifecycle
          |
          v
  RBAC and Access
      Management
          |
          v
  Governance Engine
          |
          v
 Provisioning Engine
          |
          v
 Target Applications
          |
          v
   Audit and Reports
```

For detailed architecture and component descriptions, refer to:

[Architecture Documentation](docs/architecture/architecture.md)

## Project Structure

```text
Project-04-IGA-Simulator/
│
├── data/
│   ├── identities/
│   ├── applications/
│   ├── roles/
│   ├── entitlements/
│   ├── requests/
│   ├── certifications/
│   └── audit/
│
├── src/
│   ├── identity/
│   ├── applications/
│   ├── access/
│   ├── governance/
│   ├── provisioning/
│   └── audit/
│
├── tests/
│
├── docs/
│   ├── architecture/
│   └── modules/
│
├── scripts/
│
├── README.md
└── .gitignore
```

## SailPoint Conceptual Alignment

| Simulator Component | SailPoint Concept |
|---|---|
| HR CSV | Authoritative Identity Source |
| Identity Engine | Identity Management |
| Application Catalogue | Sources / Applications |
| Account Records | Accounts |
| Entitlement Catalogue | Entitlements |
| RBAC Engine | Roles / Access Profiles |
| Access Request Engine | Access Requests |
| Approval Engine | Approval Workflows |
| Certification Engine | Certifications / Access Reviews |
| Provisioning Engine | Provisioning |
| Audit Engine | Audit Events |

These are conceptual mappings, not claims of actual SailPoint product implementation.

## Implementation Roadmap

| Module | Scope | Status |
|---|---|---|
| 01 | IGA Foundations and Architecture | In Progress |
| 02 | Identity Lifecycle Management | Planned |
| 03 | Application Onboarding and RBAC | Planned |
| 04 | Access Request and Approval | Planned |
| 05 | Access Certification and SoD | Planned |
| 06 | Provisioning, Deprovisioning and Audit | Planned |
| 07 | Integration, Testing and Assessment | Planned |

## Testing Strategy

The simulator will be tested using:

- Successful identity lifecycle scenarios.
- Invalid and duplicate employee records.
- Unauthorized access requests.
- Approval and rejection scenarios.
- Invalid entitlement assignments.
- SoD policy violations.
- Access certification decisions.
- Provisioning and deprovisioning failures.

Both successful and failure scenarios will be documented.

## Security Principles

The implementation will demonstrate:

- Least Privilege.
- Role-Based Access Control.
- Separation of Duties.
- Approval-based access management.
- Periodic Access Reviews.
- Identity Lifecycle Controls.
- Auditability and Accountability.

## Project Limitations

This is an educational IGA simulator, not a commercial enterprise IGA platform.

It does not reproduce the complete functionality of SailPoint IdentityIQ or Identity Security Cloud.

All employee records are synthetic. Any Active Directory integration will be performed in an authorized lab environment.

## Expected Outcome

The completed project will demonstrate practical understanding of enterprise identity governance, lifecycle management, access management, provisioning, compliance controls and audit processes.

It is intended to support practical learning and portfolio development for IAM and IGA Analyst roles.

## Author

**IAM-PAM Portfolio Project**

Developed as part of an enterprise IAM and IGA practical learning portfolio.