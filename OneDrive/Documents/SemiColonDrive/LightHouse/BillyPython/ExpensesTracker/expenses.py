# Step 1: Create an empty list to store expenses
expenses = []

# Step 2: Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")  # Ask for the date
    description = input("Enter the description: ")  # Ask for the description
    amount = float(input("Enter the amount: "))    # Ask for the amount
    expenses.append({"date": date, "description": description, "amount": amount})  # Add to the list
    print("Expense added successfully!")  # Tell the user it worked

# Step 3: Function to view all expenses
def view_expenses():
    print("\nExpenses:")  # Show a header
    for i, expense in enumerate(expenses, 1):  # Loop through the list
        print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: ₦{expense['amount']:.2f}")

# Step 4: Function to calculate total expenses
def calculate_total():
    total = sum(expense['amount'] for expense in expenses)  # Add up all amounts
    print(f"Total Expenses: ₦{total:.2f}")  # Show the total

# Step 5: Main program loop
while True:
    print("\nWelcome to Semicolon Expense Tracker App")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")  # Ask the user to choose

    if choice == "1":
        add_expense()  # Call the add_expense function
    elif choice == "2":
        view_expenses()  # Call the view_expenses function
    elif choice == "3":
        calculate_total()  # Call the calculate_total function
    elif choice == "4":
        print("Exiting the app. Goodbye!")  # Say goodbye
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")  # Handle invalid input