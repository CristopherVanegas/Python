
class Automovi:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo 
        self.marca = marca 
        self.color = color 
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4) 


    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida': 
            self._motor.inyecta_gasolina(10)
        else: 
            self._motor.inyecta_gasolinna(3)

        self.estado = 'En movimiento' 



class Motor:

    def __init__(self, cilindro, tipo = 'gasolina'): 
        self.cilindros = cilindros 
        self.tipo = tipo 
        self._temperatura = 0 


    def inyecta_gasolinna(self, cantidad): 
        pass 



