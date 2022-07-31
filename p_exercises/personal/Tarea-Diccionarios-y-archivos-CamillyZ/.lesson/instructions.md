* Se le pide hacer un análisis del archivo `imdb.csv` que tiene datos de películas. Cada línea tiene datos de una película con ciertas características:

```
Name;Date;Rate;Votes;Genre;Duration;Type;Certificate;Episodes;Nudity;Violence;Profanity;Alcohol;Frightening
```

1. creaDiccionario(nombreArchivo) que recibe el nombre de un archivo y retorna un diccionario que tiene el siguiente formato:

```python
{ Name1 : Type1,
Name2: Type2,
#........
NameN: TypeN 
}
```
Ejemplo:
```
{ 'No Time to Die': "Film",
  'The Guilty': "Film",
  ...
}
``` 
2. Implementar la función `categoricePeli`, recibe el diccionario del tema 1 y una categoria (Film/Series/..). La función retorna el mensaje 'Es Popular' si existe más de 50 películas de esa categoria, de lo contrario retornará el mensaje 'No es popular'. Si la categoría no está en el diccionario retornar 'No existe la categoría'.
Ejemplo:
```python
mensaje = categoricePeli(diccTema1, 'Film')
# mensaje tendrá 'No es Popular'
``` 
3. Implementar la función `pelisXTipo`, recibe el nombre del archivo y retorna un diccionario de la siguiente forma:

```python
{ Tipo1: [peli1, peli2,.., peliN ],
  Tipo2: [peli3, peli4,..., peliY],
  #...
 }
```
Ejemplo:
```
{ 'Film':['No time to die', 'Venom','Dune',...],
  'Series':[ 'Ted Lasso','House of the Dragon', ...]
   ....
}
``` 

4. creaDiccionario(nombreArchivo) que recibe el nombre de un archivo y retorna un diccionario que tiene el siguiente formato:

```python
{ Name1 : Genre1,
Name2: Genre2,
#........
NameN: GenreN 
}
```
5. Implementar la función `categoricePeli`, recibe el diccionario del tema 4 y una película. La función retorna el mensaje 'Variado' si tiene más de dos géneros (GENRE), de lo contrario retornará el mensaje 'Simple'. Si la película no está en el diccionario retornar 'No existe la película'.

6. Implementar la función `pelisXcertificado`, recibe el nombre del archivo y retorna un diccionario de la siguiente forma:

```python
{ certificado1: [peli1, peli2,.., peliN ],
  certificado2: [peli3, peli4,..., peliY],
  #...
 }
```

7. Utilizando el diccionario que retorna la funcion 6. Encuentre cual es el/los certificado(s) que tiene el mayor número de películas.

5. Implementar la función `pelisXAnio`, recibe el nombre del archivo y retorna un diccionario de la siguiente forma:

```python
{ anio1: {peli1, peli2, peli3,...} ,
  anio2: {peli4, peli8, peli2,...},
  #...
 }
```

6. Utilizando el diccionario del tema anterior, mostrar los años ordenados de menor a mayor con su  total de películas publicadas en cada año


7. Crear una función generoEstadistica que reciba el diccionario del tema 4 y genere otro diccionario donde se cuente el total de películas por Género. Ej:

```python
{
  'Action':100,
  'Adventure':342,
  'Sci-Fi':23,
  ....
}
```

