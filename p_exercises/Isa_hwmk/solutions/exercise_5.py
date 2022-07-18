"""
    WRITE A PROGRAM THAT ASK YOU FOR THE LOWER AND UPPER LIMIT 
    OF A RANGE.

    1.- IF THE LOWER LIMIT IS GREATER THAN THE UPPER ONE,
    THE PROGRAM SHOULD ASK FOR A NEW VALUE FOR THE LOWER LIMIT.

    2.- NEXT, THE NUMBERS ARE ENTERED UNTIL A 0 IT'S ENTERED.
    
    3.- THEN IT'S PRINTED:
        A. THE SUM OF THE NUMBERS INNER THE RANGE.
        B. THE COUNT OF NUMBERS OUT OF THE RANGE.
        C. INFORM IF HAVE BEEN ENTERED ANY NUMBER EQUAL TO LIMITS.
"""


""" LIBRARIES SECTION """
from os import system
from time import sleep


""" VARIABLE SECTION """
lower_limit = 0
upper_limit = 0
limits = []
list_values = [lower_limit, upper_limit]
range_values = []
sum_of_range_values = 0
list_numbers_out = []
repeated_values = []
repeated_lim = 0


def ask_for_limits():
    global lower_limit, upper_limit, list_values, limits
    lower_limit = int(input('--- Please enter a value for the lower limit: '))
    #sleep(1/2)
    system('clear')
    upper_limit = int(input('--- Please enter a value for the upper limit: '))
    #sleep(1/2)
    system('clear')

    while lower_limit > upper_limit:
        print(f'Sory but your lower_limit is greater than the upper_limit!')
        sleep(1)
        print(f'Please enter new values!', end='\n\n')
        sleep(1)

        ask_for_limits()

    list_values = [lower_limit, upper_limit]
    limits = [lower_limit, upper_limit]
    system('clear')


def asked_values_for_list():
    value = None
    while value != 0:
        value = int(input('--- Please enter values (When you enter a 0 the program will stop asking for values): '))
        list_values.append(value)
        system('clear')


def sum_values_in_range(lower_limit, upper_limit):
    global range_values, list_values, limits, sum_of_range_values
    list_values.sort()

    for index in list_values:
        if index > lower_limit and index < upper_limit:
            range_values.append(index)
    # print(range_values)

    for index in range_values:
        sum_of_range_values += index
    print(f' [1]. The sum of the range values is: {sum_of_range_values}.')
    print(f'      Because range values are: {range_values}')
    print('\n')


def numbers_out(list_values, limits):
    global list_numbers_out
    for index in list_values:
        if index < lower_limit or index > upper_limit:
            list_numbers_out.append(index)
    print(f' [2]. Numbers out of the range are {len(list_numbers_out)} and those are: {list_numbers_out}')
    print(f'      Because limits are {limits}')
    print('\n')


def verify_repeated_lim(list_values, limits, lower_limit, upper_limit, repeated_lim):
    global repeated_values
    for index in list_values:
        if index == lower_limit or index == upper_limit:
            repeated_values.append(index)
            repeated_lim += 1
    #print(repeated_values)
    
    if repeated_lim == 0:
        print(f' [3]. No, there are no limit repeated in list of values.')
    else:
        print(f' [3]. Yes, there are limits repeated in list of values and those are {repeated_lim}.')
        print(f'      Verification: {list_values}, limits: {limits}')
        print('\n')


def run():
    system('clear')
    ask_for_limits()
    asked_values_for_list()
    #print(list_values)
    sum_values_in_range(lower_limit, upper_limit)
    numbers_out(list_values, limits)
    verify_repeated_lim(list_values, limits, lower_limit, upper_limit, repeated_lim)
    print('\n\n')


if __name__ == '__main__':
    run()

