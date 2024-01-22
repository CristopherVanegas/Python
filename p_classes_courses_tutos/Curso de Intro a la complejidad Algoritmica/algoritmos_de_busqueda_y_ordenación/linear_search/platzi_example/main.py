
# linear search

import random 

def linear_search(list, objetive): 
    match = False

    for element in list:
        if element == objetive:
            match = True
            break

    return match


if __name__ == '__main__':
    size_list = int(input('>>> How large will be the list?: '))
    objetive  = int(input('>>> What number do you want to find?: '))
    print('\n')

    list = [random.randint(0, 100) for i in range(size_list)]
    
    encontrado = linear_search(list, objetive)
    
    list.sort()
    print(f'{list}\n')
    print(f'>>> The element {objetive} {"is" if encontrado else "is not"} in the list\n')



