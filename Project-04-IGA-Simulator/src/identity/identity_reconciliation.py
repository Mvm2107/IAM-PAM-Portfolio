
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from identity.identity_reader import load_hr_employees
from identity.lifecycle_detector import detect_lifecycle_events


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SNAPSHOT_PATH = (
    PROJECT_ROOT / "data" / "identities" / "identity_snapshot.json"
)

EVENTS_PATH = (
    PROJECT_ROOT / "data" / "audit" / "lifecycle_events.json"
)


def load_json_file(file_path):
    """Load and return JSON data from a file."""

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json_atomic(file_path, data):
    """Save JSON through a temporary file before replacing the original."""

    temp_path = file_path.with_suffix(file_path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    temp_path.replace(file_path)


def create_identity_map(employees):
    """Convert employee records into an ID-keyed dictionary."""

    return {
        employee["employee_id"]: employee
        for employee in employees
    }


def generate_event_id(event, previous_sync):
    """Generate a stable ID to prevent duplicate event recording."""

    event_data = {
        "previous_sync": previous_sync,
        "event": event
    }

    serialized = json.dumps(event_data, sort_keys=True)

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def run_reconciliation(hr_csv_path=None):
    """Run initial bootstrap or normal identity reconciliation."""

    # Step 1: Load and validate current HR records
    employees = load_hr_employees(hr_csv_path)

    current_identities = create_identity_map(employees)

    # Step 2: Load existing snapshot and event history
    snapshot = load_json_file(SNAPSHOT_PATH)
    event_log = load_json_file(EVENTS_PATH)

    if not isinstance(snapshot.get("identities"), dict):
        raise ValueError("Invalid identity snapshot structure.")

    if not isinstance(event_log.get("events"), list):
        raise ValueError("Invalid lifecycle event log structure.")

    # Step 3: Initial bootstrap
    if not snapshot.get("initialized", False):

        snapshot["identities"] = current_identities
        snapshot["initialized"] = True
        snapshot["last_successful_sync"] = (
            datetime.now(timezone.utc).isoformat()
        )

        save_json_atomic(SNAPSHOT_PATH, snapshot)

        return {
            "mode": "BOOTSTRAP",
            "employees_processed": len(employees),
            "events_detected": 0,
            "events_recorded": 0
        }

    # Step 4: Detect lifecycle events
    previous_identities = snapshot["identities"]

    detected_events = detect_lifecycle_events(
        employees,
        previous_identities
    )

    # Step 5: Prevent duplicate event recording
    existing_event_ids = {
        event.get("event_id")
        for event in event_log["events"]
    }

    previous_sync = snapshot.get("last_successful_sync")

    new_events = []

    for event in detected_events:
        event_id = generate_event_id(event, previous_sync)

        if event_id in existing_event_ids:
            continue

        event_record = {
            **event,
            "event_id": event_id,
            "detected_at": datetime.now(timezone.utc).isoformat()
        }

        new_events.append(event_record)
        existing_event_ids.add(event_id)

    # Step 6: Record events before updating the snapshot
    if new_events:
        event_log["events"].extend(new_events)
        save_json_atomic(EVENTS_PATH, event_log)

    # Step 7: Merge current records with previous snapshot
    # Missing HR records are retained, not treated as Leavers.
    updated_identities = {
        **previous_identities,
        **current_identities
    }

    # Step 8: Update snapshot after successful event recording
    snapshot["identities"] = updated_identities
    snapshot["last_successful_sync"] = (
        datetime.now(timezone.utc).isoformat()
    )

    save_json_atomic(SNAPSHOT_PATH, snapshot)

    return {
        "mode": "RECONCILIATION",
        "employees_processed": len(employees),
        "events_detected": len(detected_events),
        "events_recorded": len(new_events)
    }


if __name__ == "__main__":
    try:
        result = run_reconciliation()

        print("\nIdentity reconciliation completed successfully.")
        print(json.dumps(result, indent=4))

    except (ValueError, FileNotFoundError, json.JSONDecodeError, OSError) as error:
        print(f"\nIdentity reconciliation failed: {error}")
