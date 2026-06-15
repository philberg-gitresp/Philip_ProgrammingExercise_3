# For this program, it tells the user to make a list
# for their monthly expenses. First, they will name the
# item. Then, they will have to give that item an expense
# price. After they made their list and type "done", they
# will get their summary of expense types while also selecting
# the ones from the highest to lowest.

# This code will get the expenses of what the user will input.
def get_expenses():
    expenses = []
    print("=========== The Monthly Expense Management Program ===========")
    print("- Please enter your monthly expenses.")
    print(f'- When you have your list, type the "enter" key to continue.')
    print("==============================================================")

    while True:
        expense_type = input("Enter an expense type: ").strip()
        if expense_type.lower() == '':
            if len(expenses) == 0:
                print("No expenses were made.")
                print("Please enter at least one to continue.")
                continue
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: $"))
            if amount <= 0:
                print("Please enter an amount that is greater than zero.")
                continue
            expenses.append({"type": expense_type, "amount": amount})
            print(f"{expense_type} (${amount:.2f}) has been added to the list.\n")
            print(f'You may add another expense type or type the "enter" key when finished.')
        except ValueError:
            print("You cannot put an invalid number. Please try again.\n")

    return expenses

# This code will analyze the expenses from highest to lowest
# depending on their prices.
def analyze_expenses(expenses):
    total = round(sum(map(lambda e: e["amount"], expenses)), 2) if False else \
            round(__import__("functools").reduce(lambda acc, e: acc + e["amount"], expenses, 0), 2)
    highest = __import__("functools").reduce(lambda acc, e: e if e["amount"] > acc["amount"] else acc, expenses)
    lowest = __import__("functools").reduce(lambda acc, e: e if e["amount"] < acc["amount"] else acc, expenses)
    return total, highest, lowest

# After analyzing, this code will display the results that
# the user has inputted to see the list of expenses, including
# the total, highest, and lowest of these types of expenses.
def display_results(expenses, total, highest, lowest):
    print("==============================================")
    print("The Monthly Expense Management Program:")
    print("FINAL RESULTS")
    print("- We finally finished analyzing your expenses.")
    print("- Here are the results of your summary:")
    print("==============================================")
    print("List of Expenses:")
    for e in expenses:
        label = ""
        if e == highest:
            label = " [Highest]"
        if e == lowest:
            label = " [Lowest]"

        print(f"{e['type']:<20} ${e['amount']:>10.2f} {label}")
    print("==============================================")
    print(f"{'Total Expense':<20} ${total:>10.2f}")
    print(f"{'Highest Expense':<20} ${highest['amount']:>10.2f} ({highest['type']})")
    print(f"{'Lowest Expense':<20} ${lowest['amount']:>10.2f} ({lowest['type']})")
    print("==============================================")
    print("Thanks for using this program!")
    print("==============================================")

# The Main Program Itself.
def main():
    expenses = get_expenses()
    total, highest, lowest = analyze_expenses(expenses)
    display_results(expenses, total, highest, lowest)

main()
