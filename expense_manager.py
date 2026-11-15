from expense import Expense
from storage import save_expenses , load_expenses

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, title, amount, category, date):
        expense = Expense(title, amount, category, date)
        ID = expense.id
        if self.expenses:
            expense.id = max(expense.id for expense in self.expenses) + 1
        else:
            expense.id = ID
        self.expenses.append(expense)
        return expense

    def get_expenses(self):
        return self.expenses

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def delete_expense(self, expense_id):
        expense = self.get_expense_by_id(expense_id)
        if expense:
            self.expenses.remove(expense)
            return True
        return False

    def update_expense(self, expense_id, title=None, amount=None, category=None, date=None):
        expense = self.get_expense_by_id(expense_id)
        if expense:
            expense.update(title, amount, category, date)
            return expense
        return None

    def save(self):
        save_expenses(self.expenses)
 
    def load(self):
        self.expenses = load_expenses()