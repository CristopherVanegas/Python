# Operations with Sets 

# a = set() only for empty Sets 

a = {1, 2, 3} 
b = {3, 4, 5} 

c = {1, 2, 3, 4, 5}


print(f'\n>>>> Is \'a\' equal to \'b\'?\n  |>  ans: {a == b}') 
print(f'\n>>>> The set \'a\' has {len(a)} items and the set \'b\' has {len(b)} -- \'Len()\' Function')    


# Make a Junction between set 'a' and set 'b'  
ab_junction = a | b 
print(f'\n>>>> Junction between \'a\' and \'b\': {ab_junction}') 

# Make an Intersection between set 'a' and set 'a' 
ab_intersection = a & b
print(f'>>>> Intersection between \'a\' and \'b\': {ab_intersection}') 

# Make a difference from 'a' to 'b' 
ab_difference = a - b 
print(f'>>>> Difference between \'a\' hacia \'b\': {ab_difference}') 

# Make a Simetric Difference between 'a' and 'b' 
ab_symmetricDifference = a ^ b 
print(f'>>>> Symmetric Difference between: {ab_symmetricDifference}') 


### SUBSETS ### 

# Verify subsets 
if a.issubset(c) and b.issubset(c): 
    print(f'\n>>>> A and B are subsets of C.\n  |> A:{a.issubset(c)} B: {a.issubset(c)}') 
else: 
    print(f'\n>>>> C is subset of A or B. ') 


# Verify supersets 
print(f'\n>>>> C is superset of A')if c.issuperset(a) and c.issuperset(b) else print(f'\n>>>>C is NOT superset of A and B') 


# Verify if sets are disjoint 
print(f'\n>>>> Are A or B disjoint?:\n  |> A: {a.isdisjoint(b)}\n  |> B: {b.isdisjoint(a)}') 


# Inmutable Sets 
d = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}      # To make ir inmutable, try: d = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) 
print(f'\n>>>> D set: {d}') 
d.add(11)
print(f'>>>> Interger 11 added to the D set: {d}\n') 
