# ERROR_HANDLING
# TRY, EXCEPT and RAISE

from os import system


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacía!')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        print(palindrome(input('>>> Enter a string: ')))
    except TypeError:
        print('Solo se pueden ingresar strings')


if __name__ == '__main__':
    system('clear')
    run()

