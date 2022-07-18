import time 

def cuentaRegresiva(n): 
    if (n == -6): 
        return 0

    print(n) 
    time.sleep(1/2)
    cuentaRegresiva(n - 1) 

if(__name__ == '__main__'):
    tiempo_1 = time.time() 
    print(tiempo_1)
    cuentaRegresiva(5)

    tiempo_2 = time.time()
    print(tiempo_2)