# This code it's a demonstration of how filter() works.
# This code select the odd number and creates another list with it.

import os

def list_comphrenhension(my_list):  # Function for list_comphrenhension
    odd = [x for x in my_list if x % 2 != 0]
    return odd


def for_loop(my_list):  # Function dedicated to for loop
    odd = []
    for x in my_list:
        if x % 2 == 1:
            odd.append(x)
    return odd


def run(my_list):   # main function
    # List comphrehension
    print(f'>>> list comphrenhension: {for_loop(my_list)}')

    """
                            This doesn't work:
    lambda my_list: my_list = my_list[x for x in my_list if x % 2 != 0]
    odd = [lambda: x for x in my_list if x % 2 != 0]
    print(f'>>> lambda function: {odd}')
    """

    # For loop
    print(f'>>> for loop: {for_loop(my_list)}')

    # Using Filter
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(f'>>> filter (higher order function): {odd}')
    """
        A Higher Order Function is a function that receives another function.
        In this case -> filter(lambda or another function, another function)
        This function return an iterable with could be transformed into a 
        list with the list() function.
    """


if __name__ == '__main__':  # Entry point
    os.system('clear')
    my_list = [1, 4, 5, 6, 9, 13, 16, 21]

    run(my_list)

