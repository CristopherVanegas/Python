# DEBUGGING

from os import system

def divisors(num):
    '''divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)'''
    
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print('>>> End of program')


if __name__ == '__main__':
    system('clear')
    run()

