# input statements
salary = 1250.0
numDependents = 2

# calculate taxes here
stateTax = float(salary * 0.065)
federalTax = float(salary * .28)
dependentDeduction = float(salary * (numDependents * .025))
totalWithholding = float(stateTax + federalTax + dependentDeduction)
takeHomePay = salary - totalWithholding

# output statements
print('State Tax: $' + str(stateTax))
print('Federal Tax: $' + str(federalTax))
print('Dependent Deduction: $' + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
