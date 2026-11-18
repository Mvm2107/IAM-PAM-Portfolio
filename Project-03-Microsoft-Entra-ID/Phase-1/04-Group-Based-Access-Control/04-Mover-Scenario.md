# Mover Scenario – Department Transfer

## 1. Objective

Demonstrate the Identity Lifecycle Management (JML) Mover process by updating an employee's attributes and modifying group memberships following a department transfer.

## 2. Scenario

An employee, Arun Kumar, transfers from IT Operations to Finance Operations.

**Change request:** Department transfer

**Employee ID:** EMP1001

## 3. Initial State

| Attribute | Previous value |
|---|---|
| Department | IT Operations |
| Job Title | IT Support Analyst |
| Group | GRP-IT-Operations |

## 4. Activities Performed

### Step 1 – Update User Attributes

Updated the following properties in Microsoft Entra ID:

| Attribute | Previous value | New value |
|---|---|---|
| Department | IT Operations | Finance Operations |
| Job Title | IT Support Analyst | Finance Operations Analyst |
| Office Location | Chennai | Chennai |

### Step 2 – Create Finance Security Group

Created a new security group:

- Group Name: GRP-Finance-Operations
- Group Type: Security
- Membership Type: Assigned
- Source: Cloud

### Step 3 – Update Group Membership

- Removed Arun Kumar from GRP-IT-Operations.
- Added Arun Kumar to GRP-Finance-Operations.

## 5. Verification

Verified the updated user profile and group memberships in Microsoft Entra Admin Center.

| Verification | Expected result | Actual result |
|---|---|---|
| Department update | Finance Operations | Successful |
| Job title update | Finance Operations Analyst | Successful |
| Old group membership | Removed | Confirmed |
| New group membership | Added | Confirmed |

## 6. Audit Log Verification

Verified the following events under Microsoft Entra Audit Logs:

| Activity | Category | Status |
|---|---|---|
| Update user | UserManagement | Success |
| Remove member from group | GroupManagement | Success |
| Add member to group | GroupManagement | Success |

## 7. Security and IAM Concepts Learned

- Employee department transfers require access reviews and group membership updates.
- Group-based access control simplifies access administration.
- Audit logs provide evidence of identity lifecycle changes.
- Access to the previous department's resources should be removed when no longer required.

## 8. Conclusion

Successfully completed the Mover scenario using Microsoft Entra ID cloud-only identity management. Updated employee attributes, transferred group membership, and verified all changes through audit logs.
