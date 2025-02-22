
expenses = []

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")  
    description = input("Enter the description: ")  
    amount = float(input("Enter the amount: "))    
    expenses.append({"date": date, "description": description, "amount": amount})  
    print("Expense added successfully!")  


def view_expenses():
    print("\nExpenses:")  
    for i, expense in enumerate(expenses, 1):  
        print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: ₦{expense['amount']:.2f}")

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)  
    print(f"Total Expenses: ₦{total:.2f}")  
    
while True:
    print("\nWelcome to Semicolon Expense Tracker App")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")  

    if choice == "1":
        add_expense()  
    elif choice == "2":
        view_expenses()  
    elif choice == "3":
        calculate_total()  
    elif choice == "4":
        print("Exiting the app. Goodbye!")  
        break  
    else:
        print("Invalid choice. Please try again.")  
