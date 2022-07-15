
#conjunto --- set()
conjunto = set()
conjunto = {5, 4, 3, 2, 1, "Hola", "Mundo", "!", "1.15"} 

# Conjuntos --- Sets 
def conjuntos(): 
    global conjunto 
    return f'>>>> {conjunto}'

# List to Set 
def list_to_set(): 
    Lista_1 = [13, 33, 55, 23, 4] 
    return set(Lista_1) 


if __name__ == '__main__':
    print(f'\n>>>> List converted to Set: {list_to_set()}')
    print(f'\n>>>> Global Set: {conjunto}')
    print(f'\n>>>> def conjuntos: {conjuntos()}')




