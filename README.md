# Python Expense Tracker

A command-line expense tracker built using Python and Object-Oriented Programming (OOP).

This project allows users to manage their daily expenses and store their records locally using JSON.

## Features

- Add new expenses
- View all recorded expenses
- Update existing expenses
- Delete expenses
- Validate expense details (title, amount, category, and date)
- Automatically assign unique expense IDs
- Save and load expense records using JSON

## Technologies Used

- **Python 3** – Core programming language
- **OOP** – Organizing expense records and management operations
- **JSON** – Local data storage

## Project Structure

```text
Python_project2/
│
├── expense.py
├── expense_manager.py
├── storage.py
├── main.py
├── expenses.json
└── README.md
```

## File Description

| File | Responsibility |
|---|---|
| `expense.py` | Defines the Expense class and handles validation and updates. |
| `expense_manager.py` | Manages expense records and CRUD operations. |
| `storage.py` | Handles saving and loading expense data. |
| `main.py` | Provides the command-line interface. |
| `expenses.json` | Stores expense records locally. |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/baghorahaard2507-cyber/python-expense-tracker.git
```

### 2. Navigate to the project directory

```bash
cd python-expense-tracker
```

### 3. Run the application

```bash
python3 main.py
```

## How to Use

After running the application, you'll see the following menu:

```text
Expense Manager

1. Add Expense
2. View all Expenses
3. Update Expense
4. Delete Expense
5. Exit
```

Choose an option and follow the instructions displayed in the terminal.

## Data Storage

Expense records are stored in `expenses.json`.

The application converts expense objects into JSON-compatible data before saving them. When the application starts, previously saved records are loaded automatically.

## Version

**v1.0**

## Learning Objectives

This project was developed to practice:

- Python Object-Oriented Programming
- Classes and objects
- Working with multiple Python modules
- Exception handling and input validation
- File handling
- JSON serialization and deserialization

---

**Note:** This is a beginner-level project built as a practical exercise in Python and OOP.
