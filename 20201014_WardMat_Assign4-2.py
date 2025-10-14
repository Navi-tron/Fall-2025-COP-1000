empName = str(input('Enter Employee Name: '))
numShifts = int(input('Enter number of shifts: '))
numTrans = int(input('Enter number of transactions: '))
transDollVal = float(input('Enter transaction dollar value: '))

productivityScore = 0
bonus = 0

productivityScore = (transDollVal/numTrans)/numShifts

if productivityScore <= 30:
    bonus = bonus + 50
elif productivityScore >= 31 and productivityScore <= 69:
    bonus = bonus + 75
elif productivityScore >= 70 and productivityScore <= 199:
    bonus = bonus + 100
else: 
    bonus = bonus + 200

bonus1 = float(bonus)
print('Employee Name:', empName)
print('Employee Bonus: $' + str(bonus1))
    
