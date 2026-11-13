# 04 – Group Management in Microsoft Entra ID

## 1. Objective

To understand and implement group-based access management in Microsoft Entra ID using Security Groups.

This practical exercise covers:
- Creating a Security Group.
- Assigning group owners.
- Adding users to groups.
- Removing users from groups.
- Verifying membership changes.
- Monitoring group activities through Audit Logs.

## 2. Lab Environment

| Component | Configuration |
|---|---|
| Platform | Microsoft Entra ID |
| Portal | Microsoft Entra Admin Center |
| Directory | Default Directory |
| Group Name | GRP-IT-Operations |
| Group Type | Security |
| Membership Type | Assigned |
| Member | Arun Kumar |
| Owner | Manivannan M |

## 3. Practical Implementation

### Step 1: Create a Security Group

Navigated to:

Microsoft Entra Admin Center → Groups → All Groups → New Group

Configured the following:

- Group Type: Security
- Group Name: GRP-IT-Operations
- Description: Security group for IT Operations employees
- Membership Type: Assigned

Added a user as a group member and assigned an owner.

**Observation:** The Security Group was successfully created.

### Step 2: Verify Group Membership

Navigated to:

Groups → GRP-IT-Operations → Members

Verified that Arun Kumar appeared under Direct Members.

Also checked the Owners section to confirm the assigned group owner.

**Observation:** The group contained one direct member and one owner.

### Step 3: Remove a User from the Group

Selected Arun Kumar from the Members section and performed the Remove operation.

**Observation:**
- The portal confirmed that the member was successfully removed.
- The Direct Members section showed zero members.

### Step 4: Verify Removal Through Audit Logs

Navigated to:

GRP-IT-Operations → Audit Logs

Located the corresponding activity.

| Field | Recorded Value |
|---|---|
| Activity | Remove member from group |
| Category | GroupManagement |
| Status | Success |
| Date | 13 November 2026 |

Reviewed the audit event details.

**Observation:** The audit record confirmed the successful removal operation.

### Step 5: Restore Group Membership

Navigated back to:

GRP-IT-Operations → Members → Add Members

Selected Arun Kumar and added the user back to the group.

**Observation:** Arun Kumar appeared again under Direct Members.

### Step 6: Verify Addition Through Audit Logs

Located the latest event in the group's Audit Logs.

| Field | Recorded Value |
|---|---|
| Activity | Add member to group |
| Category | GroupManagement |
| Status | Success |
| Date | 13 November 2026 |
| Time | 8:44 PM |

Reviewed all three audit log sections:

**Activity**
- Confirmed the operation type and success status.

**Target(s)**
- Identified the affected user.
- Identified the target Security Group.

**Modified Properties**
- Verified the associated Group Object ID.
- Verified the group display name: GRP-IT-Operations.

**Observation:** The audit log confirmed that the user was successfully added back to the Security Group.

## 4. Key IAM Concepts Learned

### Security Groups

Security Groups are used to organize users, devices and other identities for access management and permission assignment.

### Assigned Membership

Assigned membership means administrators manually add or remove members from a group.

### Group Owner

A group owner is responsible for managing the group, including its membership and configuration, depending on their permissions.

### Group Membership Removal vs Account Deletion

Removing a user from a group does not delete or disable their account.

- **Remove from group:** Removes the user's membership in that particular group.
- **Disable account:** Prevents the account from signing in.
- **Delete account:** Removes the user account from the directory.

### Audit Logs

Audit Logs provide records of directory activities, including group creation, membership addition and membership removal.

They help IAM administrators investigate access changes and maintain accountability.

## 5. Practical Results

Successfully completed the following operations:

- [x] Created a Security Group.
- [x] Assigned a group owner.
- [x] Added a user as a member.
- [x] Verified direct membership.
- [x] Removed a user from the group.
- [x] Verified removal through Audit Logs.
- [x] Restored group membership.
- [x] Verified addition through Audit Logs.
- [x] Examined Activity, Target(s) and Modified Properties.

## 6. Conclusion

This exercise provided practical experience with Security Group administration in Microsoft Entra ID.

It demonstrated how IAM administrators manage group memberships, verify access changes and use audit records to maintain visibility and accountability.

These operations are fundamental to Joiner, Mover and Leaver (JML) identity lifecycle management.
