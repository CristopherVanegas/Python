myArray = [1, 2, 3, 4, 7]
greatest = 0
count = 0 
index = 0

def checkTheGreatest(myArray, greatest, count, index):
	while(count < len(myArray)):
		index = count

		if(greatest < myArray[index]):
			greatest = myArray[index]
			count += 1
			checkTheGreatest(myArray, greatest, count, index)
	return greatest

def print_result(result):
	print(f'>>> The greatest is {result}.')

result = checkTheGreatest(myArray, greatest, count, index)
print_result(result)
