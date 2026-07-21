# ==============================
#      EXPENSE TRACKER
# ==============================

expenses = []


# Add Expense
def add_expense():
    print("\n----- Add Expense -----")

    name = input("Enter Expense Name: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expenses.append([name, category, amount])

    print("Expense Added Successfully!")


# View Expenses
def view_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    print("\n----------- Expense List -----------")
    print("No.\tName\t\tCategory\tAmount")

    for i in range(len(expenses)):
        print(i + 1, "\t", expenses[i][0], "\t\t", expenses[i][1], "\t\t₹", expenses[i][2])


# Total Expense
def total_expense():

    total = 0

    for expense in expenses:
        total = total + expense[2]

    print("\nTotal Expense = ₹", total)


# Search Expense
def search_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    search = input("Enter Expense Name: ")

    found = False

    for expense in expenses:

        if expense[0].lower() == search.lower():

            print("\nExpense Found")
            print("Name     :", expense[0])
            print("Category :", expense[1])
            print("Amount   : ₹", expense[2])

            found = True

    if found == False:
        print("Expense Not Found!")


# Delete Expense
def delete_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    view_expense()

    number = int(input("\nEnter Expense Number to Delete: "))

    if number >= 1 and number <= len(expenses):

        deleted = expenses.pop(number - 1)

        print(deleted[0], "Deleted Successfully!")

    else:
        print("Invalid Number!")


# Update Expense
def update_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    view_expense()

    number = int(input("\nEnter Expense Number to Update: "))

    if number >= 1 and number <= len(expenses):

        print("\nEnter New Details")

        name = input("Enter Expense Name: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expenses[number - 1] = [name, category, amount]

        print("Expense Updated Successfully!")

    else:
        print("Invalid Number!")


# Show Highest Expense
def highest_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense[2] > highest[2]:
            highest = expense

    print("\nHighest Expense")
    print("Name     :", highest[0])
    print("Category :", highest[1])
    print("Amount   : ₹", highest[2])


# Main Menu
while True:

    print("\n================================")
    print("        EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search Expense")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Highest Expense")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        update_expense()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        highest_expense()

    elif choice == "8":
        print("\nThank You for Using Expense Tracker!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")