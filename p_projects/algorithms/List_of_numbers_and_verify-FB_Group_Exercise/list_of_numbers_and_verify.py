from random import randint  # del módulo 'random' importa la función 'randint'

numbers = [randint(-100, 100) for x in range(10)]   # aplicando list_comphrenhension agrego enteros aleatorios en un rango de 10 para tener esa cardinalidad del conjunto numbers donde guardo esa lista.
pos = 0    # positivos = 0
neg = 0    # negativos = 0
zero = 0   # ceros = 0

pos_l = [x for x in numbers if x > 0]     # aplicando list_comphrenhensions agrego todos los enteros positivos si la implicaicón de x es mayor a 0 es cierta.
neg_l = [x for x in numbers if x < 0]     # aplicando list_comphrenhensions agrego todos los enteros negativos si la implicaicón de x es menor a 0 es cierta.
zero_l = [x for x in numbers if x == 0]   # aplicando list_comphrenhensions agrego todos los enteros que cumplan la implicaicón de x es 0.


for x in numbers:   # hago un recorrido en la lista numbers
    if x > 0:       # si es mayor ( + )
        pos += 1    # sumo 1 a pos
        
    elif x < 0:     # si es menor ( - )
        neg += 1    # sumo 1 a neg
        
    elif x == 0:    # si es 0
        zero += 1   # sumo 1 a zero

print(f'>>> cantidad de positivos: {len(pos_l)}')   # imprimo la cantidad de positivos aplicando un len() en la lista de positivos.
print(f'>>> cantidad de negativos: {len(neg_l)}')   # imprimo la cantidad de negativos aplicando un len() en la lista de negativos.
print(f'>>> cantidad de ceros: {len(zero_l)}')      # imprimo la cantidad de ceros aplicando un len() en la lista de ceros.
print(f'')
print(f'>>> listas: ')
print(f'           {pos_l} ')   # imprimo la lista de positivos.
print(f'           {neg_l} ')   # imprimo la lista de negativos.


