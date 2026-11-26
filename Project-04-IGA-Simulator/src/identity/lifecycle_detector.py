
MOVER_ATTRIBUTES = ("department", "job_title", "manager_id")

VALID_STATUSES = {"Active", "Terminated"}


def detect_lifecycle_events(current_employees, previous_identities):
    """
    Detect Joiner, Mover and Leaver events by comparing
    current HR records with the previous identity snapshot.

    Returns a list of detected lifecycle events.
    """

    events = []

    for employee in current_employees:
        employee_id = employee["employee_id"]
        current_status = employee["employment_status"]

        previous = previous_identities.get(employee_id)

        # Validate employment status
        if current_status not in VALID_STATUSES:
            raise ValueError(
                f"Invalid employment status for {employee_id}: "
                f"{current_status}"
            )

        # New employee
        if previous is None:
            if current_status == "Active":
                events.append({
                    "employee_id": employee_id,
                    "event_type": "JOINER",
                    "reason": "New active employee"
                })
            else:
                raise ValueError(
                    f"New employee {employee_id} has Terminated status."
                )

            continue

        previous_status = previous.get("employment_status")

        # Leaver: existing employee is now terminated
        if previous_status == "Active" and current_status == "Terminated":
            events.append({
                "employee_id": employee_id,
                "event_type": "LEAVER",
                "reason": "Employment terminated"
            })
            continue

        # Rehire / reactivation handling
        if previous_status == "Terminated" and current_status == "Active":
            events.append({
                "employee_id": employee_id,
                "event_type": "JOINER",
                "reason": "Previously terminated employee reactivated"
            })
            continue

        # Mover: important employment attributes changed
        changed_attributes = {}

        if current_status == "Active":
            for attribute in MOVER_ATTRIBUTES:
                old_value = previous.get(attribute, "")
                new_value = employee.get(attribute, "")

                if old_value != new_value:
                    changed_attributes[attribute] = {
                        "old": old_value,
                        "new": new_value
                    }

        if changed_attributes:
            events.append({
                "employee_id": employee_id,
                "event_type": "MOVER",
                "reason": "Employment attributes changed",
                "changes": changed_attributes
            })

    return events
