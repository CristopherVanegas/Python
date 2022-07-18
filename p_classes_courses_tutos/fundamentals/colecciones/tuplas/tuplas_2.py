# Familiarizarse con las tuplas 

Tuple = (45, 55, 3, [21, 7, 2004], "Hola", "Mundo", "!",3) 
List = list(Tuple) 
ListToTuple = tuple(List)

List = ["Hello", "World", "!", "List", "to", "Tuple", 21, 7, 2004]

print(f'\n>>>> Position {Tuple.index("Hola")} in the tuple')      # Returns the position of the value especified but the first that it founds. 
print(f'\n>>>> Data repeated {Tuple.count(45)} times')            # Returns the times that a data was repeated. 
print(f'\n>>>> Number of Data {len(Tuple)}')

print(f'\n>>>> Print List: {List}')
print(f'\n>>>> List to tuple: {ListToTuple}')
print(f'\n>>>> {List}') 


