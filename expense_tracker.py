import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


# Add Expense
def add_expense():
    try:
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        note = input("Enter Note (optional): ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("\nExpense added successfully!\n")

    except ValueError:
        print("\nInvalid amount. Please enter a numeric value.\n")


# View Expenses
def view_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== Expense Records =====")

        for row in reader:
            print(f"""
Date      : {row['Date']}
Category  : {row['Category']}
Amount    : ₹{row['Amount']}
Note      : {row['Note']}
-----------------------------
""")
            total += float(row["Amount"])

    print(f"Total Expense: ₹{total:.2f}\n")


# Category Summary
def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    print("\n===== Category-wise Summary =====")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

    print()


# Main Menu
initialize_file()

while True:

    print("""
========== Expense Tracker ==========
1. Add Expense
2. View Expenses
3. Category-wise Summary
4. Exit
=====================================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.\n")