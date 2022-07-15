
option = int(input('Elige una opción (1, 2, 3: '))

def conversacion(mensaje):
    print('Hola!')
    print('Cómo estás?')
    print(mensaje)
    print('Adiós!')

if option == 1:
    conversacion('Elegiste la opción 1!')
elif option == 2:
    conversacion('Elegiste la opción 2!')
elif option == 3:
    conversacion('Elegiste la opción 3!')
else:
    print('Elige una opción correcta!')

