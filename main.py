from expense_manager import ExpenseManager

manager = ExpenseManager()
manager.load()

while True:
    print("\nExpense Manager")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

    operation = int(input("What do you want to do? : "))

    if operation == 1:
        title = input("Enter the title of your expense: ")
        amount = input("Enter the amount: ")
        category = input("Enter the category of your expense: ")
        date = input("Enter the date: ")

        try:
            manager.add_expense(
                title,
                amount,
                category,
                date
            )
        except ValueError as e:
            print(f"Error: {e}")
            continue

        manager.save()
        print("Expense added successfully!")

    elif operation == 2:
        if manager.expenses:
            for expense in manager.expenses:
                print("----All Expenses----")
                print("ID:", expense.id)
                print("Title:", expense.title)
                print("Amount:", expense.amount)
                print("Category:", expense.category)
                print("Date:", expense.date)
                print("--------------------")
        else:
            print("There are no expenses, add an expense first.")
            continue

    elif operation == 3:
        try:
            expense_id = int(input("Enter expense ID: "))

            title = input("New title (leave blank to skip): ")
            amount = input("New amount (leave blank to skip): ")
            category = input("New category (leave blank to skip): ")
            date = input("New date (leave blank to skip): ")

            updated_expense = manager.update_expense(
                expense_id,
                title or None,
                float(amount) if amount else None,
                category or None,
                date or None
            )

        except ValueError as e:
            print(f"Error: {e}")
            continue

        if updated_expense is None:
            print("Expense ID is not found.")
        else:
            manager.save()
            print("Expense updated!")

    elif operation == 4:
        try:
            expense_id = int(input("Enter the ID of the expense to delete: "))

            deleted = manager.delete_expense(expense_id)

            if deleted:
                manager.save()
                print("Expense deleted successfully!")
            else:
                print("Expense ID not found.")

        except ValueError as e:
            print(f"Error: {e}")
            continue

    elif operation == 5:
        print("Thank you for using Expense Manager!")
        break

    else:
        print("Invalid option. Please choose between 1 and 5.")