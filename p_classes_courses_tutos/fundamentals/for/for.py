# For loops and collections  

tuple_collection = {1, 2, 3, 4, 5, "Cr"} 
dictionary = {"Cr": 12, "Mc": 20, "Apple": 18, "OS": "k"}

    # FOR LOOPS #
print('\n|---- FOR LOOPS ----|\n')
print('@FOR LOOP IN TUPLE COLLECTION@')
for i in tuple_collection: 
    print(f'>>>> Hello World!.\n  |> Elemento: {i}\n') 



    # DICTIONARY #
print('\n@FOR LOOP IN DICTIONARY COLLECTION@')
# EASIEST FORM #
for clave,valor in dictionary.items():
    print(f'>>>> Elements in dictionary:\n  |> Key: {clave} -> Value: {valor}\n')



# REDUNDANCY METHOD # 
for x in dictionary: 
    print(f'{x}: {dictionary[x]}')


    # STRING #
print('\n@FOR LOOP IN STRING@\n') 
Str = 'Cr.k12' 
print('>>>> Str =', end=' ')
for x in Str: 
    print(f'{x}', end='')

 

