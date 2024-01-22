# This code makes a class with methods that let to buy but 
# there's a price which cnnot be changed due to the facts its 
# a private varible using '__.' 

""" 
    Basicamente el convertir una variable en privada usando ' .__ ' 
    No podemos editar su valor ni instanciando la clase y sus variables. 
    Solo se lo logre si y solo si se modifica internamente en la clase 

    Pero para esto tmb se puede modificar una técnica de programación llamada programación defensiva, 
    la cual me permite declarar cuando y como podré modificar los métodos de una clase por lo que sus atributos tmb. 
""" 

class Computer: 
        def __init__(self): 
            self.__maxprice = 900 
            self.__interger = None 

        def sell(self): 
            print(f'El precio de venta es: {self.__maxprice}') 
            self.__interger = 50; 
            print(self.__interger)

        def set_maxprice(self, price): 
            self.__maxprice = price 

if __name__ == '__main__': 
        c = Computer() 
        c.sell() 

        # Change the price 
        c.__maxprice = 1000
        c.__interger = 900  

        c.sell() 
""" 
    Cuando se crea una variable con dos guiones bajos '__' 
    significa que esta será privada en su totalidad (por lo que
    entiendo solo se podrá modificar dentro de la clase donde se creo)
    a diferencia de con un solo guión bajo '_', así solo se identifican como privados 
    por covención (internamente en la memoria no lo son). 
""" 


