
class Rectangulo: 
    def __init__(self, altura, base): 
        self.altura = altura 
        self.base = base 
        
    def area(self): 
        return self.base * self.altura 


class Cuadrado(Rectangulo): 
    def __init__(self, lado):           # initial function - this mean what object features represent 
        super().__init__(lado, lado)    # initialize the super.method.rectangle.function and give as the parameters to height and base each side size 



if __name__ == '__main__': 
    rectangulo = Rectangulo(5, 8) 
    print(rectangulo.area()) 

    cuadrado = Cuadrado(7) 
    print(cuadrado.area()) 


