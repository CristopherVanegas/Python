# This code is to verify if a string it's a Palindrome
# pr not, this it's done by a lambda function.

import os   # This os import let me clear the console

def run(string):
    palindrome = lambda string: string == string[::-1]
    if palindrome(string):
        print('>>> It is a palindrome')
    else:
        print('>>> It is not a palindrome')


if __name__ == '__main__':
    os.system('clear')  # Clear the console
    string = str(input('>>> Pls enter a string: ')).lower().replace(' ', '')
    #string = string.lower().replace(' ', '')
    run(string)


