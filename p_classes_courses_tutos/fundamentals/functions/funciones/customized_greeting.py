
''' 
Haz un programa con una función que muestre un saludo. 
dado la bienvenidad al usuario, utilizando su nombre, 
el cual se ha pedido antes de llamar a la función. 

La función no devuelve nada (es decir, devuelve None). 
Definir la función con un parámetro (el nombre del usuario). 
''' 


def greeting(username, passcode): 
    username = username.upper() 

    if username == 'JKALI': 
        if passcode == '1234': 
            print('\n********* Admitted Access *********')
            print('|                                 |')
            print("***********************************")
            print("|                                 |")
            print("|            START  PAGE          |") 
            print("|              WELCOME            |") 
            print("|               {}             |".format(username))
            print("|                                 |") 
            print("***********************************")
            print('\n') 

        else: 
            print('\n¡Access denied!\n¡Incorrect Passcode!') 
    else: 
        print('\n¡Access denied!\n¡Unrecognized Username!') 

    return None



if __name__ == '__main__': 
    username = input('\n>>>> Insert your username please: ') 
    passcode = input('>>>> Insert your passcode please: ')

    print(f'Function type: {greeting(username, passcode)}\n')




