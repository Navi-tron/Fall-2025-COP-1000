# input statements
salary = float(input('What is your salary? '))
numDependents = float(input('How many dependents do you have? '))

# calculate taxes here
stateTax = float(salary * 0.065)
federalTax = float(salary * .28)
dependentDeduction = float(salary * (numDependents * .025))
totalWithholding = float(stateTax + federalTax + dependentDeduction)
takeHomePay = salary - totalWithholding

# output statements
print('State Tax: $' + str(stateTax))
print('Federal Tax: $' + str(federalTax))
print('Dependent Deduction: $' + str(round(dependentDeduction,1)))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
