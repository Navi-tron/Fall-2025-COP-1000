# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here
myCurrentAge = int(input('What is your current age? '))
currentYear = int(input('What is the current year? '))

myNewAge = myCurrentAge + (2050 - currentYear)
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")