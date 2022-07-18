num_notas_finales = input('¿Cuantas notas desea ingresar?:')
num_notas_finales= int(num_notas_finales)

sumador= 0
contador= 1

while contador <= num_notas_finales:
    nota = input('ingresar notas:')
    nota = float(nota)
    sumador = sumador + nota
    contador = contador + 1

promedio= sumador / num_notas_finales

print('El promedio de las notas es:{}'.format(promedio))