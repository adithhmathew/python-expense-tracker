import csv
expenses = []

try:
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            expense = {
                "amount": float(row[0]),
                "category": row[1],
                "description": row[2]
            }
            expenses.append(expense)
except FileNotFoundError:
    pass

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again")
        return
    category = input("Enter category: ")
    desc = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": desc
    }

    expenses.append(expense)

    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, desc])

    print("Expenses added")

def view_expenses():
    for expense in expenses:
        print(f"Amount: ₹{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print("-" * 20)

def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses: ", total)

def category_summary():
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    for cat, amt, in summary.items():
        print(cat, ":", amt)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Category Summary")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expenses()
    elif choice == 4:
        category_summary()
    else:
        print("Invalid choice. Try again")





