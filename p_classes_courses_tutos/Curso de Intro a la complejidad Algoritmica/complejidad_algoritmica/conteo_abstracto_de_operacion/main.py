
# f(x): 1002 + x + 2x^2 

def f(x): 

    respuesta = 0   # 1 

    print('\n')
    for i in range(1000):   # 1000 
        respuesta += 1 
    print(f'>>> First Loop: {respuesta}') 

    for i in range(x):  # x 
        respuesta += x 
    print(f'>>> Second Loop: {respuesta}')

    print('>>> Third Loop: ')
    print('\n') 
    for i in range(x):  # 2x^2 
        for j in range(x): 
            respuesta += 1 
            respuesta += 1 
            print(j)

    print('\n') 
    return respuesta    # 1 


print(f'>>> Final Answer: {f(2)}') 
print('\n') 

