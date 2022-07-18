a = 7
b = 5 

print(f'\n|| Simple form\n    >>>>  global values are {a}, {b}\n') 
print('|| Complete form\n    >>>>  global values are a = {} and b = {}\n'.format(a, b))

def main():
    print(f'|| Into the main function: ')

    global a 
    global b 
    a = 5 
    
    print(f'    >>>> a es menor\n') if a < b else print(f'    >>>> a & b son iguales\n') if a == b  else print(f'    >>>> a es mayor')   # Ternary Operator 


if __name__ == '__main__': 
    main()


