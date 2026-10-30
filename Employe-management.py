from datetime import datetime

# Employee records and yearly leave balances
employees = {
    "E101": {
        "name": "Amit",
        "Casual": 12,
        "Sick": 10,
        "Earned": 15
    }
}

def view_balance(emp_id):
    """Display the remaining leave balance."""
    if emp_id not in employees:
        print("Invalid employee ID.")
        return

    emp = employees[emp_id]
    print(f"\nLeave Balance for {emp_id} ({emp['name']}):")
    print(f"Casual Leave: {emp['Casual']}")
    print(f"Sick Leave: {emp['Sick']}")
    print(f"Earned Leave: {emp['Earned']}")


def apply_leave():
    """Apply for leave and approve or reject the request."""
    emp_id = input("Enter Employee ID: ").strip().upper()

    if emp_id not in employees:
        print("Invalid employee ID.")
        return

    leave_type = input(
        "Enter Leave Type (Casual/Sick/Earned): "
    ).strip().title()

    if leave_type not in ("Casual", "Sick", "Earned"):
        print("Invalid leave type.")
        return

    from_date = input("Enter From Date (YYYY-MM-DD): ").strip()
    to_date = input("Enter To Date (YYYY-MM-DD): ").strip()

    # Validate and parse the dates
    try:
        start = datetime.strptime(from_date, "%Y-%m-%d").date()
        end = datetime.strptime(to_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format or date.")
        return

    # The end date cannot be before the start date
    if end < start:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    # Count both the start date and end date
    days = (end - start).days + 1

    employee = employees[emp_id]
    available = employee[leave_type]

    if days <= available:
        employee[leave_type] -= days
        print(
            f"Leave approved: {days} days {leave_type} | "
            f"Balance {leave_type}: {employee[leave_type]}"
        )
    else:
        print(
            f"Leave rejected. Requested: {days} days | "
            f"Available: {available} days"
        )


def main():
    """Display the menu and run the application."""
    while True:
        print("\n===== Employee Leave Management System =====")
        print("1. Apply for Leave")
        print("2. View Leave Balance")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            apply_leave()
        elif choice == "2":
            emp_id = input("Enter Employee ID: ").strip().upper()
            view_balance(emp_id)
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()