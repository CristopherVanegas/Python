# Ask for two numbers and show every pair numbers between both.

num_1 = int(input('Enter the first number: '))
num_2 = num_1  # num_1 value assigned to num_2 to enter this comprobation loop
while num_2 <= num_1:	# If num_2 is minor/equal to num_1, do this:  
	num_2 = int(input('Enter the second number: '))	# Asks for a value for num_2

for n in range(num_1, num_2 + 1):
	if n % 2 == 0:
		print(f'{n}')

