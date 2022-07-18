
t = 1, True, "Hola" 
t_2 = (3, "hola", False) 
t_3 = (1, False, "I'm Learning...", [1, 2, 3, 4, 5]) 
list_1 = [5, 2, 3, 1] 

def main(): 
    print('\n', ">>>> ", t, "Tupla 1", sep='') 
    print(">>>> ", type(t_2), "Tupla 2\n") 
    print(f'>>>> Valor de la tupla 2 en -1: {t_2[-1]}')
    print(f'>>>> Todos los valores por slizing de la tupla 3 a partir del valor 1: {t_3[1:]} ')

    print(">>>> ", end='') 
    print(t[1], t_2[1], "Integrantes de la 2da posición en ambas tuplas...", sep=', ') 

    # t[0] = 0      # Tuplas cannot have reassigments 
    print(">>>> ", end='')
    print(list_1[2], "Integrante 3 de la lista...\n", sep=', ')

    # print(t_3[3[]]) 

    list_1.append("I don't know what to do...") 
    print(f'>>>> El valor ha sido agregado en la última posición de la lista \n     -->El resultado es: \'{list_1}\'\n') 
    print(f'>>>> \'{list_1.pop()}\' ha sido el último elemento de la lista eliminado.')
    print(f'>>>> Quedan estos valores: \'{list_1}\'\n')


if __name__ == '__main__': 
    main() 
    print(f'\n¡TheProgramHaveFinished!\n')

