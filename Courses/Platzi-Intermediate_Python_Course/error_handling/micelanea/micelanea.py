# This code sums up everything learned with error_handling

from os import system

def divisors(num):
    '''divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)'''
    try:
        divisors = [index for index in range(1, num + 1) if num % index == 0]
        print(divisors)
        # return divisors
    except NameError:
        print('Dear Developer, plz check the for loop\'s index variable!')

    # return 


def run():
    try:
        num = int(input('Enter a number: '))
        divisors(num)
        print('End of program')
    except ValueError:
        print('You need to enter a number')


if __name__ == '__main__':
    system('clear')
    run()

