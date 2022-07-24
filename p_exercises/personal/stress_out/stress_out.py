
from os import system


stress_out = False

system('clear')
ans = input('>>> Stress is True or False? (t / f): ')

if ans == 't':
    stress_out = True
    
if ans == 'f':
    stress_out = False


def drink_coffee():
    system('clear')
    print('Drinking Coffee')


def cont():
    system('clear')
    print('Doing...')


func = lambda stress_out: drink_coffee() if stress_out == True else cont()
func(stress_out)

