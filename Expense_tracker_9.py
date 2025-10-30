# Start Housekeeping Loop
# Module for current date and time
from datetime import datetime
tracker_date = datetime.now().strftime('%Y-%m-%d %H:%M')
print('Today is:', tracker_date)

# Module for creating storage area for user entries
#idNum = []
kind = []
expenses = []
payees = []

# Module for entering expenses   
def entExpenses():
        #i = 1
        # Expense Type - String from list
        while True:
                expTyp = input('\nPlease choose an expense type: Travel, Lodging, or Food: ').strip().lower()
                if expTyp in {'travel', 'lodging', 'food'}:
                    expenseType = expTyp.title()
                    break
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
        #idNum.append(i)
        kind.append(expenseType)
        expenses.append(expenseAmount)
        payees.append(payeeName)
        #i += 1

# Module for summing total expenses   
def add_expenses(expenses):
    return sum(expenses)
       
# Module for printing summary to screen
def printToScreen():
    if not expenses:
        print('No entries have been made.')
        return
    print('\nYour expenses for', tracker_date, 'are:\n')        
    print('{a:8s}\t{b:10s}\t{c:6s}'.format(a='Expense',b='Payee',c='Amount'))
    print('========================================')
    for i in range(len(expenses)):
        print(f'{kind[i]:<8}\t{payees[i]:<15}\t${expenses[i]:.2f}')
    total_expenses = add_expenses(expenses)
    form_total_exp = f"{total_expenses:.2f}"
    print('\nYour total entered expenses are: $', form_total_exp)

# Module to remove last item entered
def clearLast():
    kind.pop()
    expenses.pop()
    payees.pop()
    print('The last entry has been cleared.')

# Module for clearing entires
def clearAll():
    kind.clear()
    expenses.clear()
    payees.clear()
    print('All entries have been cleared.')

# Module for option to print to file
def saveToFile():
    with open(f'expenses.{tracker_date}.txt', 'w') as file:
        file.write('Expense Tracker Entry Date: ')
        file.write(tracker_date + '\n')
        file.write('\nYour Expense Tracker entries are:\n')        
        file.write('\n{a:8s}\t{b:15s}\t{c:6s}\n'.format(a='Expense',b='Payee',c='Amount'))
        file.write('========================================\n')
        for i in range(len(kind)):
            file.write(f'{kind[i]:<8}\t{payees[i]:<15}\t${expenses[i]:.2f}')
        total_expenses = add_expenses(expenses)
        form_total_exp = f"{total_expenses:.2f}"
        file.write(f'\n\nYour total entered expenses are: ${form_total_exp}')
        print(f'Your expenses have been saved to the file: expenses.{tracker_date}.txt')
# End Housekeeping Loop

# Start Detail Loop
while True: 
    # Opening Menu - Yes or no string
    print('\nChoose an action from the following menu:')
    print('1. Add Expense \n2. View Summary \n3. Clear Last Entry \n4. Clear All Entries \n5. Print to file \n6. Exit')
    promptAns = input('\nMenu Chosen: ')
    if promptAns == '1': entExpenses()
    elif promptAns == '2': printToScreen()
    elif promptAns == '3': clearLast()
    elif promptAns == '4': clearAll()
    elif promptAns == '5': saveToFile()
    elif promptAns == '6':
        print("Don't forget to submit your expenses to accounting!")
        break
    else:
        print('Please choose a valid menu number.')
# End Detail Loop
        
# Start End of Job Loop
# End End of Job Loop
