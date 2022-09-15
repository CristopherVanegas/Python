# This code elevates each item in a list to the square power by using lambda funtion.

import os

if __name__ == '__main__':
    os.system('clear')
    
    my_list = [1, 2, 3, 4, 5]
    
    print(f'>>> Root list: {my_list}')
    square_list = lambda my_list: list(x**2 for x in my_list)
    print(f'>>> Square power by lambda: {square_list(my_list)}')

