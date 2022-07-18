# Exercise 
# Create a tupla and then convert to a string and split it,
# to create a list of string and print it by a for. 

from os.path import join 


myTuple = ("123", "555", "21072004", "Cristopher", "21") 

def convertTupleToString(myTuple): 

    myTuple = ",".join(myTuple) # Join all items in a tuple into a String and separates each item by a comma. 
    print(f'>>>> Tuple into string = {myTuple}') 
    

    myTuple = myTuple.split(',') # This makes a list of String after split it. 
    print(f'>>>> Tuple converted to list of string: {myTuple}\n')


    print(f'>>>> Print myTuple list of string by a for: ')

    for x in myTuple: 
        print(f'  |>    {x}')



if __name__ == '__main__': 

    print(f'\n>>>> {myTuple}') 
    convertTupleToString(myTuple)


