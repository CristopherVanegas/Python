
# binary search algorythm
# this search asumes that the data is sorted

import random

def busqueda_binaria(list, comienzo, final, objetive):
    print(f'buscando {objetive} entre {list[comienzo]} y {list[final - 1]}')
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2        # euclidian divisition

    if list[medio] == objetive:
        return True

    elif list[medio] < objetive:
        return busqueda_binaria(list, medio + 1, final, objetive)
    elif list[medio] > objetive:
        return busqueda_binaria(list, comienzo, medio - 1, objetive)


if __name__ == '__main__':
    size_list = int(input('>>> How large will be the list?: '))
    objetive  = int(input('>>> What number do you want to find?: '))
    print('\n')

    list = sorted([random.randint(0, 100) for i in range(size_list)])
    
    encontrado = busqueda_binaria(list, 0, len(list), objetive)
    
    print(f'\n{list}\n')
    print(f'>>> The element {objetive} {"is" if encontrado else "is not"} in the list\n')

