"""
Ejercicio: Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40. 

Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0 

"""


horas_trabajadas = int(input(" > Introdusca sus horas trabajadas: "))
salario_hora = int(input(" > Introduzca su salario por hora (pista -> 10): "))
salario = int(input(" > Introduzca su salario: ")) 


def calculo(horas_trabajadas): 
    if (horas_trabajadas > 40): 
        horas_extras = horas_trabajadas - 40 
        salario_horas_extras = horas_extras * salario_hora 
        
        return salario_horas_extras 



if (__name__ == '__main__'): 
    print(end='\n')
    print(f' --> Su salario extra es de: {calculo(horas_trabajadas)}\n --> Su salario por las horas extras trabajadas son: {calculo(horas_trabajadas) + 475}') 
    print(end='\n') 


