"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

charge = 0.00
numChars = int(input('Enter # of chars:'))
woodType = str(input('Enter wood type:'))
color = str(input('Enter color:'))

# Write assignment and if statements here as appropriate.

charge = charge + 35.00

if numChars > 5:
    digitCost = (numChars - 5) * 4.0
    charge = charge + digitCost

if woodType == 'oak':
    charge = charge + 20.0

if color == 'gold':
    charge = charge + 15.0



# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))

