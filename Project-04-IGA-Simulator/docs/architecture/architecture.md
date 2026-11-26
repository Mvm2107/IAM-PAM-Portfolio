# Identity Governance & Administration (IGA) Simulator

## 1. Project Overview

The Identity Governance & Administration (IGA) Simulator is a Python-based enterprise identity governance project inspired by SailPoint IdentityIQ and SailPoint Identity Security Cloud concepts.

The project simulates how an enterprise manages employee identities, application accounts, access permissions, approvals, access reviews and compliance policies.

The solution is developed using free development tools and existing lab infrastructure. No paid SailPoint subscription or commercial IGA platform is required. Existing Windows Server and Active Directory infrastructure is used where available and subject to applicable licensing.

## 2. Project Objectives

The primary objectives are:

- Implement Joiner, Mover and Leaver (JML) identity lifecycle management.
- Simulate enterprise application onboarding.
- Implement access request and approval workflows.
- Demonstrate Role-Based Access Control (RBAC).
- Manage application entitlements.
- Conduct access certification campaigns.
- Detect Segregation of Duties (SoD) violations.
- Simulate account provisioning and deprovisioning.
- Generate audit reports and remediation evidence.

## 3. Business Scenario

The simulator represents a fictional enterprise named TechNova Solutions.

The company has multiple departments:

- Engineering
- Finance
- Human Resources
- Information Technology
- Sales

The organization uses multiple business applications, including:

- Microsoft Active Directory
- HR Portal
- Finance Portal
- Customer Relationship Management (CRM)

The simulator manages employee identities and governs their access to these applications.

All employee information used in the project is synthetic.

## 4. High-Level Architecture

The architecture consists of the following components:

### 4.1 Authoritative Identity Source

The HR department acts as the authoritative source of employee information.

Employee records are initially supplied through CSV files.

### 4.2 Identity Governance Engine

The Python-based governance engine processes employee records and manages identity-related operations.

### 4.3 Identity Lifecycle Management

The lifecycle component handles:

- Joiner: New employee onboarding.
- Mover: Employee department or job-role changes.
- Leaver: Employee termination and access removal.

### 4.4 Application Management

The application catalogue maintains information about enterprise applications and their available access permissions.

### 4.5 Role-Based Access Control

The RBAC component maps business roles to application entitlements.

### 4.6 Access Request and Approval

Employees can request additional application access.

The simulator evaluates requests and supports approval and rejection workflows.

### 4.7 Identity Governance

The governance component handles access certification, policy evaluation and Segregation of Duties checks.

### 4.8 Provisioning Engine

The provisioning engine simulates granting, updating and removing application access.

PowerShell and Active Directory will be used for practical directory integration where appropriate.

### 4.9 Audit and Reporting

The audit component maintains records of important identity and access activities and generates reports for governance review.

### 4.10 Identity, Account and Entitlement Relationships

The simulator maintains a logical separation between identities, application accounts and entitlements.

- Identity: Represents an employee within the organization.
- Account: Represents the employee's account in a target application.
- Entitlement: Represents a permission or access right assigned to an application account.

One identity can be associated with multiple accounts across different applications. Each account can hold one or more entitlements.

The simulator uses the employee ID as the primary identity correlation attribute.

Example:

- Identity: EMP001 – Arun Kumar
- Active Directory Account: arun.kumar
- CRM Account: akumar01
- Entitlement: Engineering_Read

### 4.11 Identity and Access Data Flow

The simulator follows this logical processing sequence:

1. HR employee information is supplied through CSV files.
2. The identity engine reads and validates employee records.
3. Identity records are created or updated.
4. Lifecycle events are identified.
5. The RBAC engine evaluates the employee's business role.
6. Appropriate entitlements are determined.
7. Access requests are submitted when additional permissions are required.
8. Approval workflows evaluate access requests.
9. The provisioning engine applies approved access changes to target applications.
10. Governance controls evaluate access through certification and SoD checks.
11. Important activities are recorded in audit logs.

This sequence represents the intended workflow. Individual components will be implemented and tested incrementally.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Programming | Python 3.12 |
| Directory Services | Microsoft Active Directory |
| Automation | PowerShell |
| Data Exchange | CSV and JSON |
| Version Control | Git |
| Repository | GitHub |
| Documentation | Markdown |
| Development Environment | Visual Studio Code |
| Testing | Python unittest |

The initial implementation will prioritize Python standard-library modules and existing Windows capabilities to avoid unnecessary dependencies.

## 6. SailPoint Conceptual Mapping

| IGA Simulator | SailPoint IdentityIQ | SailPoint Identity Security Cloud |
|---|---|---|
| HR CSV | Authoritative Application | Authoritative Source |
| Identity Engine | Identity Model | Identity Model |
| Application Catalogue | Application | Source |
| Account Records | Link | Account |
| Entitlement Catalogue | Managed Attributes / Entitlements | Entitlements |
| RBAC Engine | Roles / Bundles | Roles / Access Profiles |
| Access Request Engine | Identity Request | Access Request |
| Approval Engine | Approval Workflow | Approval Workflow |
| Certification Engine | Certification | Access Review |
| Provisioning Engine | Provisioning | Provisioning |
| Audit Engine | Audit Events | Audit Events |

These mappings represent conceptual similarities and are not exact one-to-one architectural equivalents.

The simulator is independently developed using Python and PowerShell. No actual SailPoint product implementation is claimed.

## 7. Security and Governance Considerations

The simulator will incorporate the following security principles:

- Least Privilege.
- Role-Based Access Control.
- Separation of Duties.
- Approval-based access management.
- Access reviews.
- Identity lifecycle controls.
- Auditability and accountability.
- Timely access revocation.

## 8. Project Limitations

This is an educational IGA simulator developed using free tools.

It does not provide the complete feature set of a commercial enterprise IGA platform.

SailPoint integrations are conceptual unless explicitly demonstrated through actual product access, which is outside this project's scope.

## 9. Expected Outcome

The completed project will demonstrate a simulated enterprise IGA solution covering identity lifecycle management, access governance, provisioning, compliance checks and audit reporting.

The project is intended to demonstrate practical understanding of enterprise IGA workflows and support IAM/IGA Analyst portfolio development.