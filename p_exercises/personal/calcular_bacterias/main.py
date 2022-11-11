
import math

def calc(t):
    q = ((3**t)/math.log(3))+ 9.090
    return round(q)

if __name__ == '__main__':
    t = int(input('Ingrese su numero t: '))
    print(calc(t))

