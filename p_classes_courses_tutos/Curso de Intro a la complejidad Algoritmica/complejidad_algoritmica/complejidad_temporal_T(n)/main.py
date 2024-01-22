
# this code makes an aproximation to calculate the time of a process T(n)


import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

        return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 10000000000
    comienzo = time.time()
    print(f'>>> normal factorial: {factorial(n)}')
    final = time.time()
    print(f'>>> time used: {final - comienzo}')

    print('\n')

    comienzo = time.time()
    print(f'>>> recursive factorial: {factorial_r(n)}')
    final = time.time()
    print(f'>>> time used: {final - comienzo}')

    print('\n') 

