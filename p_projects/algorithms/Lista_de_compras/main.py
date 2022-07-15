  
# First step
# dinero_available = 1000

from ast import Pass
from contextlib import nullcontext


class Compra:
    hogar = {"muebles": 100, "cortinas": 30, "aparadores": 80}
    cocina = {"cocina": 1200, "nevera": 1300, "tostador": 50}
    electronicos = {"celular": 800, "audifonos": 200, "reloj": 300}
    deportes = {"googles": 20, "aletas": 30, "zapatos": 119}
    comida = {"manzanas": 0.25, "bananas": 0.25, "kiwis": 0.50, "sandias": 1.25}

    # En los parámetros agregar una lista que contenga los artículos
    def __init__(self, lista_productos, dinero_available):
        self.lista_productos = lista_productos
        self.lista_productos = lista_productos
        self.dinero_available = dinero_available

    def comprar(self, lista_productos, dinero_available):
        pass 

    def total_precio(self, list_products):
        pass 

    def contador_de_artículos():
        pass 



class Main: 

    def __init__(self): 
        pass 

    def answer(): 
        i = input('>>> Please select one by introducing just a number from 1 - 5. \n>>> Answer: ')  

        return int(i)  


    def main(): 
        
        print('Good Morning / Afternoon / Night dear, "\n"Tell me, how could I help you? "\n"') 

        list_products = [] 
        # compra.cocina, compra.electronicos, compra.deportes, compra.comida 

        print('We own these product classes: \n     1. home\n     2. kitchen\n     3. Electronics\n     4. Sports\n     5. Food\n')

        Main.main() if answer < 5 and answer <= 0 else None

        """
        answer = Main.answer()
        if answer <= 0 and answer > 5: 
            print('\nWrong value entered...') 
            #Main.answer() 

        else: pass 
        """ 


    def for_in_products(self, dictionary): 
        for x in dictionary: 
            print('>>> List of items in the selected product class: ') 
            print(f'    - {x}: precio: {dictionary[x]}\n-----------------------------------\n\n')
         



if __name__ == '__main__':
    Main.main()
