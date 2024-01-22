
def apply(num, f): 
    return f(num) 

def double(num): 
    return num * 2 

print(apply(5, double)) 

# Arrow func - Python 
print(apply(5, lambda num: 2 * num)) 



