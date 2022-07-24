# Ejercicio 49: Mostrar los archivos de un directorio especifico 


from os import listdir 
from os.path import isfile, join 

ruta = r'/Users/cristophervanegas/Documents/Projects/Python/python_hub_and_exercises/mostrar_archivos_de_un_directorio_especifico' 

def listar_directorio(ruta): 
    """
    Lista el contenido de *archivos* de un directorio específico 
    """
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))] 

    return archivos 

 
if __name__ == '__main__':
    listado_archivos = listar_directorio(ruta) 
    print(listado_archivos) 
    print(len(listado_archivos)) 



