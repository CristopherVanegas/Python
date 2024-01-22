# This code is the challenge of the micelanea class
# Use the key-words TRY, EXCEPT and RAISE to raise an error is the user enters a negative number.

from os import system
from string import ascii_letters


def divisors(num):
    try:
        if num < 0:
            raise Exception('You cannot enter negative values!')
        
        divisors = [index for index in range(1, num + 1) if num % index == 0]
        print(divisors)

    except ValueError:
        print('Plz enter a number!')
        ask()
    except NameError:
        print('Dear Developer, plz check the for loop\'s index variable!')
        ask()
    except Exception as exception:
        print(exception)
        ask()


def ask():
    try:
        answer = input('Do u want to reboot the program or just quit? (R to reboot / Q to quit) ').capitalize().strip()
        # answer = answer.capitalize().strip() 
        # run() if answer == 'R' else print('Ok, bye!')

        if answer == 'R':
            run()
        elif answer == 'Q':
            print('Ok, bye!')
        else:
            raise Exception('Pls write Q or R')

    except Exception as exception:
        print(exception)
        ask()


def run():
    system('clear')
    try:
        num = int(input('Enter a number: '))        
        divisors(num)
        print('End of program')

    except ValueError:
        print('Plz enter a number!')
        ask()


if __name__ == '__main__':
    run()

