import json
from expense import Expense

def save_expenses(expenses):
    storage = []
    for expense in expenses:
        storage.append({
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date.strftime("%Y-%m-%d")
        })

    with open('expenses.json', 'w') as f:
        json.dump(storage, f, indent=4)

def load_expenses():
    with open('expenses.json', 'r') as f:
        storage = json.load(f)
    expenses = []
    for item in storage:
        expense = Expense(
            title=item["title"],
            amount=item["amount"],
            category=item["category"],
            date=item["date"]
        )
        expense.id=item["id"]

        expenses.append(expense)

    return expenses