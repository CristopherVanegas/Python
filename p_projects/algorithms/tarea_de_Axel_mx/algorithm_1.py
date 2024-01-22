
lista = [4, 5, -1, 3, -4, 0]  
valores_en_la_lista = len(lista) 

def busquedaLineal(A, n, x): 
    encontrado = -1 

    for k in range(n): 
        if x == A[k]: 
            encontrado = k 
    
    return encontrado 


print(busquedaLineal(lista, valores_en_la_lista, -1))