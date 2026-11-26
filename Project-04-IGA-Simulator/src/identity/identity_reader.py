
import csv
from pathlib import Path


def load_hr_employees(csv_file_path=None):
    """
    Read employee records from the HR CSV
    and validate essential identity attributes.

    An alternative CSV path can be supplied for testing.
    """

    project_root = Path(__file__).resolve().parents[2]

    if csv_file_path is None:
        csv_path = (
            project_root / "data" / "identities" / "hr_employees.csv"
        )
    else:
        csv_path = Path(csv_file_path)

    if not csv_path.is_absolute():
        csv_path = project_root / csv_path

    if not csv_path.exists():
        raise FileNotFoundError(f"HR employee file not found: {csv_path}")

    employees = []
    employee_ids = set()

    with csv_path.open(
        mode="r", encoding="utf-8-sig", newline=""
    ) as file:

        reader = csv.DictReader(file)

        required_columns = {"employee_id", "employment_status"}

        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError("HR CSV is missing required columns.")

        for row_number, row in enumerate(reader, start=2):

            employee_id = (row.get("employee_id") or "").strip()
            employment_status = (
                row.get("employment_status") or ""
            ).strip()

            if not employee_id:
                raise ValueError(
                    f"Missing employee ID at CSV row {row_number}."
                )

            if not employment_status:
                raise ValueError(
                    f"Missing employment status for {employee_id}."
                )

            if employee_id in employee_ids:
                raise ValueError(
                    f"Duplicate employee ID found: {employee_id}"
                )

            employee_ids.add(employee_id)

            employees.append({
                key: value.strip() if value else ""
                for key, value in row.items()
            })

    return employees
