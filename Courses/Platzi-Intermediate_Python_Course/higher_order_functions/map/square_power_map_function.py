# This code elevates items from a list by using map() function

import os

if __name__ == '__main__':
    os.system('clear')
    my_list = [1, 2, 3, 4, 5]
    square_list = list(map(lambda x: x**2, my_list))
    print(f'>>> My root list: {my_list}')
    print(f'>>> My square list using map() is: {square_list}')


