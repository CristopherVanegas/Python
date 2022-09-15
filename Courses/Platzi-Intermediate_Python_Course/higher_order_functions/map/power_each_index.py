# This code elevates each item in a list to the square power by list_comphrenhensions.

import os

def run(my_list):
    squares_p = [i**2 for i in my_list]
    
    print(f'>>> This is the root list: {my_list}')
    print(f'>>> Converted to 2nd power: {squares_p}')
    return 


if __name__ == '__main__':
    os.system('clear')
    
    my_list = [1, 2, 3, 4, 5]
    run(my_list)

