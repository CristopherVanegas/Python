# Search the minor number in the array
# Create sub-arrays to take over the algortyhm
# Print the result

import sys

from numpy import arange
array = [20, 5, 21, 6, 23, 7, 34, 999, 68]

def selectionSort(array):
    # Iterate the whole array
    for i in range(len(array)):
        # Search the minor substract value in the disordered array
        idxDes = i
        for j in range(i+1, len(array)):
            count = 1
            print("swapp ")
            if array[idxDes] > array[j]:
                idxDes = j
        # Then with the search, we have to change it by the first value of our disordered array
        array[i], array[idxDes] = array[idxDes], array[i]

# Execute the function
print(">>> Array: ", array)
selectionSort(array)
print(">>> Sorted array: ", array)
for i in range(len(array)):
    print(" ", array[i])




