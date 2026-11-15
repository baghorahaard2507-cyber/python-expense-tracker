from datetime import datetime
from itertools import count

class Expense:
    id_counter = count(1)
    def __init__(self, title, amount, category, date):

        self.date = self._validate_date(date)
        self.title = self._validate_title(title)
        self.amount = self._validate_amount(amount)
        self.category = self._validate_category(category)
        self.id = next(Expense.id_counter)

    def _validate_title(self, title):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        return title.strip()

    def _validate_amount(self, amount):
        try:
            amount = float(amount)
        except (ValueError):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount cannot be zero or negative.")
        return amount

    def _validate_category(self, category):
        if not category.strip():
            raise ValueError("Category cannot be empty.")
        return category.strip()

    def _validate_date(self, date):
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
    

    
    def update(self, title=None, amount=None, category=None, date=None):
        new_title = self.title
        new_amount = self.amount
        new_category = self.category
        new_date = self.date

        if title is not None:
            new_title = self._validate_title(title)
        if amount is not None:
            new_amount = self._validate_amount(amount)
        if category is not None:
            new_category = self._validate_category(category)
        if date is not None:
            new_date = self._validate_date(date)

        self.title = new_title
        self.amount = new_amount
        self.category = new_category
        self.date = new_date