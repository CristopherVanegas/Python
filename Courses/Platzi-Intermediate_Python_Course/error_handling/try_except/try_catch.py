# ERROR_HANDLING
# TRY, EXCEPT

from os import system


def palindrome(string):
    return string == string[::-1]

def run():
    try:
        print('First input')
        print(f'>>> Is it a Palindrome? -> {palindrome(input(">>> Ingrese una cadena de caracteres o string: "))}')
        print()

        print('Second input - this time default')
        print(f'>>> Is it a Palindrome? -> {palindrome(1)}')
        
    except TypeError:
        print('>>> Just strings plz!', end='\n\n')


if __name__ == '__main__':
    system('clear')
    run()
