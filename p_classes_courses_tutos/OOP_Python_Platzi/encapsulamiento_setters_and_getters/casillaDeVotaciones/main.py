
# @property son para getters 
# @'propiedad'.setter para los setters 


class CasillaDeVotaciones: 

    def __init__(self, identificador, pais): 
        self.__identificador = identificador 
        self.__pais = pais 
        self.__region = None 

    # El ' @property ' define que esta función es una propiedad por lo que solo se podrá llamar con un setter 
    @property 
    def region(self): 
        return self.__region 

    # Este decorador ' setter ' permite modificar la función  
    @region.setter 
    def region(self, region): 
        if region in self.__pais: 
            self.__region = region 

        else: 
            raise ValueError(f'La region {region} no es valida en {self.__pais}') 

        
if __name__ == '__main__': 
    casilla = CasillaDeVotaciones(123, ['Ciudad de Mexico', 'Morelos']) 
    casilla.region 

    casilla.region = 'Ciudad de Mexico' 
    print(f'{casilla.region}\n')

    casilla.region = 'GYE' 
    casilla.region 


