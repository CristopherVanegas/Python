
# 1. Starts making comparisons of the abyacent elements.
# 2. Repear the loop until the array it's sorted.


def bubbleSort(array):
    n = len(array)
    #cambio = False

    # First loop, which it's duty is to iterate the array in order to carry the second loop.
    for i in range(n):
        cambio = False
        print(array)
        # Second loop, which it's duty is to compare two spaces in the array.
        for j in range(0, n-i-1):
            # Comparison conditional
            if array[j] > array[j+1]:
                # Change of position in rising mode
                array[j], array[j+1] = array[j+1], array[j]
                cambio = True
                #print(cambio)
        
        # If it is NOT "TRUE"
        if not cambio:
            break
                    
            """
            [0, 1, 2, 3, 4, 5]
            n = 6
            for loop = 0
            y = n - i -1
            y = 6 - 0 - 1
            y = 5

            [0, 1, 2, 3, 4, 5]
            for loop = 3
            y = n - i -1
            y = 6 - 3 - 1
            y = 2
            """


#array = [190, 1200, 1, 3 , 5, 7, 55, 1000, 0, 9, 11]
array = [190, 1200, 1, 2, 4, 55, 1000, 6, 800]
bubbleSort(array)
print("\n>>> The sorted Array in rising way is: ", array)


