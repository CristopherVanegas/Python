
# linear seach with countdown

import random

count = 0

def linear_search(list, objetive):
    global count
    match = False

    for element in list:
        count += 1
        if element == objetive:
            match = True
            break
    
    return match


if __name__ == '__main__':
    size_list = int(input('>>> Enter the size of your list: '))
    objetive = int(input('>>> Enter the number to find: '))
    print('\n')

    list = [random.randint(0, 100) for i in range(size_list)]
    print(f'\n{list}\n')

    answer = linear_search(list, objetive)
    print(f'>>> Your number {"have" if answer else "have not" } been found \n')

    print(f'\n{sorted(list)}\n')
    print(f'>>> {count} was the number of steps to solve this linear search!')