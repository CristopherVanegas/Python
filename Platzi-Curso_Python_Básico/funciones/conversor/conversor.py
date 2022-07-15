# money conversor
# convención => funciones antes de lógica


def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


opcion = int(input("Elige una opción => 1 / 2 / 3 : "))
if opcion == 1:
    conversor("colomianos", 3875)

elif opcion == 2:
    conversor("argentinos", 65)

elif opcion == 3:
    conversor("mexicanos", 24)

else:
    print("Ingresa una opción correcta por favor!")

