
"""
    GIVEN A NUMBER RETURN THE MULTIPLICATION TABLES FROM 1 TO 10 USING A FOR LOOP.
"""


def tablas_de_multiplicar(num):
    for index in range(1, 11):
        result = num * index
        print(f'Tabla de multiplicar del {index} por {num} es igual a {result}')


def run():
    # print(tablas_de_multiplicar(5, 7))
    num = int(input('Enter a number: '))
    print(type(num), end='\n')
    tablas_de_multiplicar(num)


if __name__ == '__main__':
    run()


