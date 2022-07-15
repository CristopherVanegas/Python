class Computadora:

    def __init__(self, pantalla, teclado, mouse, parlantes):
        self.pantalla = pantalla
        self.teclado = teclado
        self.mouse = mouse
        self.parlantes = parlantes

        self._memoria = '16GB'
        self._almacenamiento = '500GB'
        self._procesador = 'i5_8vaGEN'

        self._arquitectura = '64_Bits'


    def imprimir(self, valor=False):
        self.valor = valor

        if valor == True:
            print(self.pantalla)
            print(self.teclado)
            print(self.mouse)
            print(self.parlantes) 

        else: 
            print('Valor = False')



class Funcionamiento:

    def estado_procesador(self, arquitectura, estado, turboBoost=False):
        self.arquitectura = '64_Bits'
        self.turboBoost = '3.6Ghz'
        self.estado = False

        self._velocidad = '2.0GHz'
        self._temperatura = '39 Grados'



if __name__ == '__main__':
    mi_computadora = Computadora(
        '13_inches', 'Mecanico', 'Meetion-MT-c500', 'Estereos')
    print(mi_computadora.imprimir(True))

