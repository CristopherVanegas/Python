# Ask for numbers until a negative numbers it's entered.
# At the end show the quantity of numbers, without counting the negative number.

# exercise 2
num = 0
counter = 0

while num >= 0:
	num = int(input('Enter a number: '))
	# counter = counter + 1
	if num >= 0:
		counter = counter + 1

# counter = counter - 1
print(f'{counter} numbers were entered.')
	
