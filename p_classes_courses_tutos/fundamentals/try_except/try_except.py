
def tryCatch():  

    try: 
        # f= open('hello.txt', 'r') 
        # Always copy the large path         
        f = open('/Users/cristophervanegas/Documents/Projects/Python_Projects/python_hub_and_exercises/try_except/resources/hello.txt', 'r') 
        print(f.read()) 
        f.close()

    except: 
        #print(f'\n An error occurred \n') 
        raise Exception("¡An exception ocurred!")

    # else block code - it runs if nothing has went wrong 
    else: 
        print(f'None error has ocurred')

    # finally blocks executes regardless if the try block raises an error or not 
    finally: 
        print(f'\nFinally the program has ended\n') 

    
if __name__ == '__main__': 
    tryCatch()

 