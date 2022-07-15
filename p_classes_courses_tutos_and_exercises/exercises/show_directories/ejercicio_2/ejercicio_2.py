# Ejercicio 2 - Listar archivos 
# Own Code 


from os import listdir 
from os.path import isfile, join 

path = r'/Users/cristophervanegas/Documents'

def list_docs(path): 

    # List all the documents those are in the define path 

    list_files = [x for x in listdir(path) if join(path, x)] 

    return list_files 


if __name__ == '__main__': 

    files_listed = list_docs(path) 
    files_listed.sort()

    print('\n')
    for x in files_listed: print(f'>>>> {x}')



