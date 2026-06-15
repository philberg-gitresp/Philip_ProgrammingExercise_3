# Philip_ProgrammingExercise_3
In this program, it tells the user to make a list for their money expenses. Once the user tells the program a list of their expenses and their prices, it will then analyze the prices for each expense listed and choose the ones that have the highest or lowest price in them.

## Function: get_expenses
Gets the expenses that the user inputs, as well as the money.

Parameters:
None

Variables:
expenses (This stores all the expenses in a list.)
expense_type (A given type of expense that the user adds to the list.)
amount (A given price amount for the expense that the user gives to it.)

Logic:
1. The program welcomes the user and asks them to input a name for their expense to put in the list.
2. After the item was put in, it will then ask for the price amount of that expense.
3. The expense type and the amount would be put on the list as they program will ask the user to either input another expense type or press “enter” to start analyzing the list.

Returns:
expenses



## Function: analyze_expenses
This analyzes the expense types and their amounts to find the ones that have the highest or lowest amount.

Parameters:
expenses (The expenses that were given in a list by the user’s input to be analyzed by the program.)

Variables:
total (Gives out the total from all the given expenses in the list.)
highest (Decides which expense has the highest amount.)
lowest (Decides which expense has the lowest amount.)

Logic:
1. The program adds all the expenses that were given by the user to show the total amount of expenses all together.
2. The program chooses the expense with the highest amount on the list.
3. The program chooses the expense with the lowest amount on the list.

Returns:
total
highest
lowest


## Function: display_results
Displays the results that the user has inputted, including analyzing the total and amounts that are either the highest or the lowest

Parameters:
expenses (Displays all the expense types in the list given by the user.)
total (Displays the total amount of expenses added up all together in the list.)
highest (Displays the expense that has the highest amount.)
lowest (Displays the expense that has the lowest amount.)

Variables:
e (The item type of that expense.)
label (Gives out the label for that expense, whether they have the highest or lowest amount.)

Logic:
1. After the user has inputted all the information in the program, it will display the results using the list the user has written for it.
2. The program analyzes the total and the expenses that have the highest or lowest in their amounts.
3. It will give labels to the expenses that have the highest and lowest amounts.

Returns:
None


## Function: main
The program will tell the viewer to make a list of expense types with their amounts. After it has been inputted by the user, it will add up the total and analyze the amounts that have the highest and lowest amounts in the list. Finally, it will show the list of what the results were given.

Parameters:
None

Variables:
expenses (Receives the expense types given by the user.)
total (Receives the total amount of the added up expenses from that list.)
highest (Receives the expense that has the highest amount.)
lowest (Receives the expense that has the lowest amount.)

Logic:
1. The program tells the user to input expense types, including the amounts, to add to the list for the program to analyze.
2. As the program analyzes the list of expenses, it will add up all the expenses for its total.
3. The program will also find and label the expenses that have the highest amount or the lowest amount.
3. After analyzing the list, the program will end by displaying the final results of what the user had inputted.

Returns:
None

