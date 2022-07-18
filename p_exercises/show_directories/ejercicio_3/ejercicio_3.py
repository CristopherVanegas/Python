# Third exercise, list files using: 
#  1. listdir() 
#  2. isfile() 
#  3. join() 


from time import sleep  # Manage Time 
from os import listdir  # List files in a directory 
from os.path import isfile, join    # iffile --> To accurate whether is a file, join --> To join al the strings in a tuple into one string separating al the items by a character or not. 


def printFileDirectories(path): 
    list_dirs = listdir(path) 

    return list_dirs 



if __name__ == '__main__': 

    path =  r'/Users/cristophervanegas/Downloads' 
    print(printFileDirectories(path)) 


    myTuple = ("111", "222", "333")
    print(myTuple)

    x = ",".join(myTuple) 
    print(x)

    x = x.split(",")
    print(x) 
    
    for x in x: 
        sleep(1)
        print(x)


