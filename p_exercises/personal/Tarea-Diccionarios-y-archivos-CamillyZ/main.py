#1

archivo = open("imdb.csv")
d = {}
for linea in archivo:
  listas = linea.split(";")
  d[listas[0]] = listas[6]
 

#2
#FUNCION

def categoricePeli(d,Films):
  peliculas = d.keys()
  categorias = d.values()
  cantPelis = len(peliculas)
  
  if cantPelis > 50:
    print("Es popular")

  else:
    print("No es popular")

  
#PP
categoricePeli(d,"Film")


#3
archivo= open("imdb.csv")
def pelisXTipo(archivo):
  d2 = {}
  peli = []
  for linea in archivo:
    listas = linea.split(";")
    pelicula = listas[0]
    type = listas[-8:0]
    if pelicula and type in listas:
      peli.append(pelicula)
      d2[type] = peli

  return d2

#pp
variable = pelisXTipo("imdb.csv")



#4

archivo = open("imdb.csv")
d3 = {}
for linea in archivo:
  lista = linea.split(";")
  d3[lista[0]] = lista[4]

  

#5
  
def categoricePeli(d3,pelicula):
  generos = d3.values()
  cantGeneros = len(generos)
  if cantGeneros > 2:
    print("VARIADO")
  else:
    print("SIMPLE")

  peliculas = d3.keys()
  if peliculas not in d3:
    print("No existe la pelicula")

    
#PP
categoricePeli(d3,"The Guilty")


#6

def pelisXcertificado(imdb.csv)


