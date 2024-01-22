
# I define a super class called 'Persona' and this is to create a sub-class that extends that methods and atributes 
# that 'Persona' contains and also this sub-class 'Ciclista' modifies method 'avanzar' (that action of modifie methods depending on the situation it's called polimorphism) 
# then the program it's runned by a start point (if name is equal to main). 

class Persona: 
    def __init__(self,  nombre): 
        self.nombre = nombre 

    def avanzar(self, nombre): 
        print(f'Hola! soy {nombre}, Ando caminando') 


class Ciclista(Persona):    # Extends the super class 
    def __init__(self, nombre): # Initialize the constructor 
        super().__init__(nombre)    # send the parameter 'nombre' to the initializer into the super class 

    def avanzar(self, nombre): 
        print(f'Hola! soy {nombre}, Ando moviendome en mi bicicleta') 


def main(): 
    persona = Persona('David') 
    persona.avanzar(persona.nombre) 

    ciclista = Ciclista('Daniel') 
    ciclista.avanzar(ciclista.nombre) 


if __name__ == '__main__': 
    main() 

