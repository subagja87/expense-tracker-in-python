# Expense Tracker CLI

A simple command-line expense tracker built with Python. This application allows users to manage daily expenses, store records in a JSON file, and generate expense summaries.

This project is based on the [Expense Tracker project from roadmap.sh](https://roadmap.sh/projects/expense-tracker).

## Features

- **Add Expense:** Add a new expense with a description and amount.
- **Update Expense:** Update the description and/or amount of an existing expense.
- **Delete Expense:** Delete an expense using its unique ID.
- **List Expenses:** Display all recorded expenses.
- **Expense Summary:** Calculate the total amount of all expenses.
- **Monthly Summary:** Calculate total expenses for a specified month in the current year.
- **Input Validation:** Reject invalid amounts, IDs, and months.
- **JSON Storage:** Automatically create and update a JSON file to store expenses.

## Requirements

- Python 3.8 or later
- No external libraries required

The application uses Python's built-in modules:

- `argparse`
- `json`
- `os`
- `datetime`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/subagja87/expense-tracker-in-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd expense-tracker-in-python
   ```

3. Run the application:

   ```bash
   python app.py --help
   ```

## Usage

### 1. Add an Expense

Add a new expense by providing a description and amount.

```bash
python app.py add --description "Lunch" --amount 20
```

Short version:

```bash
python app.py add -d "Lunch" -a 20
```

Example output:

```text
Expense added successfully (ID: 1)
```

### 2. Update an Expense

Update an existing expense using its ID.

```bash
python app.py update --id 1 --description "Dinner" --amount 25
```

Short version:

```bash
python app.py update -i 1 -d "Dinner" -a 25
```

Example output:

```text
Expense updated successfully (ID: 1)
```

You can also update only the description or amount.

### 3. Delete an Expense

Delete an expense using its ID.

```bash
python app.py delete --id 1
```

Short version:

```bash
python app.py delete -i 1
```

Example output:

```text
Expense deleted successfully
```

### 4. List All Expenses

Display all saved expenses.

```bash
python app.py list
```

Example output:

```text
ID: 1  Date: 2026-11-07  Description: Lunch  Amount: 20.0
ID: 2  Date: 2026-11-07  Description: Coffee  Amount: 5.0
```

### 5. View Total Expense Summary

Calculate the total amount of all recorded expenses.

```bash
python app.py summary
```

Example output:

```text
Total expenses: $25.00
```

### 6. View Monthly Expense Summary

Calculate total expenses for a specific month of the current year.

```bash
python app.py summary --month 11
```

Short version:

```bash
python app.py summary -m 11
```

Example output:

```text
Total expenses for November: $25.00
```

Month values must be between 1 and 12.

## Data Storage

Expenses are stored locally in a file named `expenses.json`.

The file is automatically created when the first expense is added.

Example JSON structure:

```json
[
    {
        "ID": 1,
        "Date": "2026-11-07",
        "Description": "Lunch",
        "Amount": 20.0
    },
    {
        "ID": 2,
        "Date": "2026-11-07",
        "Description": "Coffee",
        "Amount": 5.0
    }
]
```

Each expense contains:

| Field | Description |
|---|---|
| `ID` | Unique expense identifier |
| `Date` | Date when the expense was added (YYYY-MM-DD) |
| `Description` | Expense description |
| `Amount` | Expense amount |

When a new expense is added, the application reads the existing JSON data, appends the new record, and saves the updated list.

## Input Validation

The application validates user inputs to prevent invalid expense records.

Examples:

**Negative amount:**

```bash
python app.py add -d "Lunch" -a -20
```

**Invalid expense ID:**

```bash
python app.py delete -i 999
```

**Invalid month:**

```bash
python app.py summary -m 13
```

The application displays an error message when invalid input is provided.

## Project Structure

```text
expense-tracker/
├── app.py
├── expenses.json
└── README.md
```

- `app.py` — Main Python application.
- `expenses.json` — Local expense data storage, generated automatically.
- `README.md` — Project documentation.

## Limitations

- Expenses are stored locally in a JSON file rather than a database.
- No graphical user interface (GUI).
- No expense categories or budget management.
- No CSV export functionality.
- Monthly summaries use the current calendar year.
- Currency is displayed using the `$` symbol without currency conversion.

## Future Improvements

- Add expense categories.
- Filter expenses by category.
- Set monthly budgets.
- Display warnings when expenses exceed the budget.
- Export expense reports to CSV.
- Add support for custom expense dates.
- Add automated unit tests.

## License

This project is created for educational purposes as part of the [roadmap.sh Expense Tracker project](https://roadmap.sh/projects/expense-tracker).
