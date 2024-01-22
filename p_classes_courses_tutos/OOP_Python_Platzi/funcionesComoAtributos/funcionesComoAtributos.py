
def saludo(nombre): 
    return f"Hola mi nombre es {nombre}"

def estudiemos_juntos(otro_nombre):
    return f"Hola {otro_nombre}, estudiemos juntos"


def funcionComoParametro(funcion_entrante_a, funcion_entrante_b): 
    print(funcion_entrante_a("Cristopher"))
    print(funcion_entrante_b("Dayanna")) 
    #return None


if __name__ == '__main__': 
    funcionComoParametro(saludo, estudiemos_juntos) 


