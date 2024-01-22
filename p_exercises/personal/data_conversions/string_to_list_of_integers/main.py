
'''
    String S = "1 2 3 4 5" 
        Convert 

    List of Integers I = [1, 2, 3, 4, 5]
        
'''  


S = '1 2 3 4 5' 
s = S.split(' ')       # this splits the string by the separator that was indicated and put each item into a list in the variable. 
print(f'\n>>>> {s}, this splits the string by the separator that was indicated and put each item into a list in the variable. \n') 

A = list(map(int, S.split(' ')))    # this converts s' list items into integers and adds it into a new variable list. 

print(f'>>>> {A}, prints the new list A. ')    # prints the new list A. 


