# Get acquainted with Sets, add and discard 

Set = set() 
Set = {1, 2, 3, 4, 5, "Hello", "World", "!"} 

def printSet(Set):
    print(f'>>>> Set: {Set}')  


if __name__ == '__main__': 
    printSet(Set)       # Calls the "printSet" function. 

    Set.add("My")       # Adds "My" to 'Set'. 
    printSet(Set) 
    
    Set.discard("My")   # Discards "My" to 'Set'.   
    printSet(Set) 

    print(f'\n>>>>{3 in Set}') 
    print(f'>>>>{5 in Set}')
    print(f'>>>>{10 in Set}') 
    print(f'>>>>{5 not in Set}\n')


