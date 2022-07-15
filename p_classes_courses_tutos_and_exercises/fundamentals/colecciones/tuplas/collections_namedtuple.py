# creación de tuplas 
# las tuplas son como arreglos, la diferencia cae 
# en que los arreglos utilizan ' [ ] ' y son un tipo *diferente*
# de dato, las tuplas utilizan ' ( ) ' y por lo general representan 
# puntos para graficar. 


from matplotlib import pyplot as plt 
from collections import namedtuple 

coordenada = namedtuple('punto', ['x', 'y']) 

coordenada_1 = coordenada(3, 4)
coordenada_2 = coordenada(5, -2) 

plt.scatter(coordenada_1[0], coordenada_1[1]) 
plt.scatter(coordenada_2[0], coordenada_2[1])
plt.show()

