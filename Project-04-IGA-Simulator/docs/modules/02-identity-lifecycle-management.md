# Day 2 – Identity Lifecycle Management and Reconciliation

## 1. Objective

The objective of Day 2 was to implement the initial identity lifecycle management and reconciliation engine for the TechNova Solutions IGA Simulator.

The module reads employee information from an authoritative HR CSV file, compares it with a previously stored identity snapshot, detects Joiner–Mover–Leaver (JML) events, and records detected events in an audit log.

## 2. Business Scenario

TechNova Solutions needs a consistent way to identify employee lifecycle changes and maintain accurate identity information.

The simulator uses an HR employee CSV as its authoritative source. It compares the latest employee information against a previously processed identity snapshot to identify changes.

The three primary lifecycle events are:

| Event | Business meaning | Simulator behaviour |
|---|---|---|
| JOINER | A new employee joins | Detects a new active employee |
| MOVER | An employee changes department, job title, or manager | Detects changes to configured employment attributes |
| LEAVER | An employee leaves the organization | Detects an Active-to-Terminated status change |

## 3. Architecture and Data Flow

The Day 2 reconciliation process follows this sequence:

1. Read employee records from the HR CSV.
2. Validate required employee attributes.
3. Load the existing identity snapshot and lifecycle event log.
4. Check whether the simulator requires initial bootstrap.
5. Compare current HR records against previously stored identities.
6. Detect lifecycle events.
7. Generate event IDs and prevent duplicate event recording.
8. Record new lifecycle events in the audit log.
9. Update the identity snapshot after successful processing.

### Data files

| File | Purpose |
|---|---|
| `data/identities/hr_employees.csv` | Authoritative employee information |
| `data/identities/identity_snapshot.json` | Previously processed identity records |
| `data/audit/lifecycle_events.json` | Historical lifecycle event records |

## 4. Python Components

### 4.1 identity_reader.py

**Purpose:** Read and validate employee records from the HR CSV.

Key functionality:
- Reads CSV records using `csv.DictReader`.
- Supports an optional CSV path for testing with fixture files.
- Validates required columns.
- Rejects missing employee IDs.
- Rejects missing employment status.
- Rejects duplicate employee IDs.
- Handles UTF-8 BOM encoded CSV files.

### 4.2 lifecycle_detector.py

**Purpose:** Identify Joiner, Mover and Leaver events by comparing current employee records with previous identity records.

The configured Mover attributes are:

- Department
- Job title
- Manager ID

Lifecycle detection rules:

| Condition | Result |
|---|---|
| New employee with Active status | JOINER |
| New employee with Terminated status | Validation error |
| Existing Active employee becomes Terminated | LEAVER |
| Existing Terminated employee becomes Active | JOINER / reactivation |
| Active employee's configured employment attributes change | MOVER |
| No relevant changes | No event |

An employee missing from the latest HR CSV is not automatically classified as a Leaver. The simulator requires an explicit Terminated status.

### 4.3 identity_reconciliation.py

**Purpose:** Coordinate the reconciliation process.

Key functionality:
- Loads HR employee records.
- Creates an employee-ID-based identity map.
- Loads the previous snapshot and audit log.
- Performs initial bootstrap when required.
- Invokes lifecycle event detection.
- Generates SHA-256-based event IDs.
- Prevents duplicate event recording.
- Updates the audit log and identity snapshot.
- Reports reconciliation results.

## 5. Identity Correlation

The simulator uses `employee_id` as the unique identity correlation key.

This allows the reconciliation engine to compare the same employee across different HR exports and identify changes to their employment attributes.

Using a stable employee identifier is important because names, departments and job titles can change over time.

## 6. Initial Bootstrap and Normal Reconciliation

### Initial bootstrap

During the first execution, the simulator stores the existing eight HR employee records in the identity snapshot.

It does not generate eight artificial JOINER events for employees who already exist in the organization.

### Normal reconciliation

After bootstrap, the simulator compares current HR records with the previous identity snapshot.

Only relevant lifecycle changes generate events. Unchanged employee records do not create unnecessary audit entries.

## 7. Audit and Data Integrity Controls

The Day 2 implementation includes the following controls:

- Required employee attribute validation.
- Duplicate employee ID detection.
- Explicit employment status validation.
- Stable employee correlation using employee ID.
- SHA-256-based event identifiers for duplicate event protection.
- Temporary-file replacement when saving individual JSON files.
- Snapshot updates after successful event recording.
- Retention of employees missing from the latest HR export rather than automatically treating them as Leavers.

**Important implementation detail:** The audit log and identity snapshot are saved as separate files. Temporary-file replacement protects individual file writes, but it does not provide a single atomic transaction across both files.

## 8. Manual Testing and Validation

The following scenarios were manually tested using the original HR dataset and controlled test fixtures.

| Test scenario | Expected result | Observed result |
|---|---|---|
| Read original HR CSV | Load 8 employees | Passed |
| Read test fixture | Load fixture records | Passed |
| Initial bootstrap | 8 identities, 0 lifecycle events | Passed |
| Normal sync without changes | 0 events | Passed |
| New Active employee | JOINER | Passed |
| Department, job title and manager changes | MOVER | Passed |
| Active to Terminated | LEAVER | Passed |
| Unchanged employee | No event | Passed |
| Missing employee ID | Reject input | Passed |
| Duplicate employee ID | Reject input | Passed |
| Invalid employment status | Reject input | Passed |
| Repeat reconciliation | Prevent duplicate event | Passed |
| Employee missing from HR export | Retain previous identity | Passed |
| Validation failure | Do not modify snapshot or audit files | Passed |

These were manual functional checks. An automated Python `unittest` suite has not yet been implemented.

## 9. Current Limitations

The current module focuses on identity reconciliation and lifecycle event detection.

It does not yet:
- Disable Active Directory accounts when a Leaver event is detected.
- Remove application accounts or revoke entitlements.
- Automatically provision access for Joiners.
- Recalculate access when a Mover event occurs.
- Implement a full-export versus partial-export validation mechanism.
- Guarantee an atomic transaction across the audit log and identity snapshot.
- Execute automated regression tests.

The current implementation should therefore be treated as an educational IGA simulator, not a production identity governance platform.

## 10. SailPoint Conceptual Mapping

The simulator demonstrates concepts commonly found in IGA platforms such as SailPoint IdentityIQ and Identity Security Cloud.

| Simulator component | Related IGA concept |
|---|---|
| HR employee CSV | Authoritative source |
| Identity snapshot | Identity data and aggregation state |
| Identity correlation | Identity correlation |
| Lifecycle detector | Lifecycle event processing |
| JOINER / MOVER / LEAVER | Identity lifecycle management |
| Lifecycle event log | Audit history |
| Reconciliation engine | Identity aggregation and reconciliation workflow |

This is a conceptual mapping only. The project does not use an actual SailPoint product or SailPoint APIs.

## 11. Execution

From the project root, run:

```powershell
python -m identity.identity_reconciliation
```

The command executes the reconciliation module and displays the processing mode, number of employees processed, number of events detected and number of events recorded.

## 12. Day 2 Outcome

Day 2 established the initial identity lifecycle management and reconciliation functionality.

The simulator can now:

- Read and validate authoritative HR employee records.
- Maintain an identity snapshot.
- Detect Joiner, Mover and Leaver events.
- Record lifecycle events in an audit log.
- Prevent duplicate event recording during reconciliation retries.
- Preserve identities missing from an HR export.

**Day 2 status: Implementation and manual validation completed.**