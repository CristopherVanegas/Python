
# binary search with a counter of steps 

import random

counter = 0
def binary_search(list, start, end, objective):
    global counter # Just to use the counter in this function 
    counter += 1 # It add 1 to the variable for each step when the script it's trying to find the objetive. 
    medium_point = (start + end)//2 # This it's done due to the fact of how this algorithm works
                                    # Divides the array by the half and starts searching and repeating the loop until
                                    # Objective it's found
                                    
    print(f'   . Searching objetive {objetive} in index from {start} to {end}')
    print(f'     |___/. Index\'s Medium Point is: {list[medium_point]}')
    print(f'     |___/. Total of elements in the list: {len(list)}')
    print(f'     |___/. Counter: {counter}')

    # If the start pint value exceeds the end value list, It's not found so it returns False.
    if start > end:
        return False
    
    # If the medium_point value it's equal to objetive, It's found so it returns True.
    if list[medium_point] == objective:
        return True
    
    # If value objetive it's higher than the medium_point value, It calls again the function to start searching now since meidum + 1 to end = n.
    elif objective > list[medium_point]:
        return binary_search(list, medium_point + 1, end, objective)
    
    # If value objetive it's lower that the medium_point value, It call again the function to start searching now since start = 0 tp medium - 1.
    elif objective < list[medium_point]:
        return binary_search(list, start, medium_point - 1, objective)



if __name__ == '__main__':
    size_list = int(input('\n>>> Enter the size of your list: ')) # Define the array's size 
    objetive = int(input('>>> Enter the number to find: ')) # Enter the number to find 
    print('\n')

    list = sorted([random.randint(0, 100) for i in range(size_list)]) # This expression let put a random int into each space of the array and then sorted it
    print(f'>>> List Generated: {list}\n') # prints the sorted list 

    print('>>> Running:')    
    answer = binary_search(list, 0, len(list) - 1, objetive) 
    print('\n')

    print(f'>>> Your number {objetive} {"have" if answer else "have not" } been found \n')
    print(f'>>> {counter} was the number of steps to solve this Binary Search!')


