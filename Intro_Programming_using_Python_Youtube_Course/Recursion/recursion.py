# To define something in terms of itself || A function that calls itself
# fib(n) = fib(n-1) + fib(n-2)
# The seq stars with 0 and 1

"""
 A FUNCTION CAN BE:
    > base case => Stop
    > resursive case => Calls itself to solve a problem

"""


import os

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 0, 1, 2, 3, 4, 5

if __name__ == '__main__':
    os.system('clear')
    print(fibonacci(5))


