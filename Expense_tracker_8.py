# Start Housekeeping Loop
# Module for setting up output text file
from datetime import datetime
tracker_date = datetime.now().strftime('%Y-%m-%d %H:%M')
print('Today is:', tracker_date)

# Module for creating storage area for user entries
kind = []
expenses = []
payees = []

# Module for entering expenses   
def entExpenses():
        # Expense Type - String from list
        while True:
                expTyp = input('\nPlease choose an expense type: Travel, Lodging, or Food: ').strip().lower()
                if expTyp in {'travel', 'lodging', 'food'}:
                    expenseType = expTyp.title()
                else:
                    print('Please enter a valid response')
        # Expense Amount Menu - Float entry
        while True:
            try: 
                expenseAmount = float(input('\nPlease input the expense amount with no commas or $ sign: '))
                break
            except ValueError:
                print('Please enter a valid expense amount')
        # Payee Menu - String open to user   
        payNme = str(input('\nEnter the name of the payee Company: '))
        payeeName = payNme.title()
        kind.append(expenseType)
        expenses.append(expenseAmount)
        payees.append(payeeName)

# Module for summing total expenses   
def add_expenses(expenses):
    return sum(expenses)
       
# Module for printing summary to screen
def printToScreen():
    if not expenses:
        print('No entries have been made.')
        return
    print('\nYour expenses for', tracker_date, 'are:\n')        
    print('\033[4mExpense Type\tPayee\t\tAmount\033[0m')
    for i in range(len(expenses)):
        print(f'{kind[i]}\t\t{payees[i]}\t\t${expenses[i]:.2f}')
    total_expenses = add_expenses(expenses)
    form_total_exp = f"{total_expenses:.2f}"
    print('\nYour total entered expenses are: $', form_total_exp)

# Module for clearing entires
def clearFile():
    kind.clear()
    expenses.clear()
    payees.clear()
    print('All entries have been cleared.')

# Module for option to print to file
def saveToFile():
    with open(f'expenses.{tracker_date}.txt', 'w') as file:
        file.write('Expense Tracker Entry Date: ')
        file.write(tracker_date + '\n')
        file.write('\nYour Expense Tracker entries are:')        
        file.write('\n\nExpense Type:\tPayee:\t\tAmount:') 
        for i in range(len(kind)):
            file.write(f'\n{kind[i]}\t\t{payees[i]}\t\t${expenses[i]:.2f}')
        total_expenses = add_expenses(expenses)
        form_total_exp = f"{total_expenses:.2f}"
        file.write(f'\n\nYour total entered expenses are: ${form_total_exp}')
        print(f'Your expenses have been saved to the file: expenses.{tracker_date}.txt')
# End Housekeeping Loop

# Start Detail Loop
while True: 
    # Opening Menu - Yes or no string
    print('\nChoose an action from the following menu:')
    print('1. Add Expense 2. View Summary 3. Clear Entries 4. Print to file 5. Exit')
    promptAns = input('Menu Chosen: ')
    if promptAns == '1': entExpenses()
    elif promptAns == '2': printToScreen()
    elif promptAns == '3': clearFile()
    elif promptAns == '4': saveToFile()
    elif promptAns == '5':
        print('Have a wonderful day!')
        break
    else: print('Please choose a valid menu number.')
# End Detail Loop
        
# Start End of Job Loop
# End End of Job Loop
