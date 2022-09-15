import os

def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda i: i % 2 !=  0, my_list))  # (i % 2 !=  0) -> Returns a boolean value (it's a comparator) 
                                                        #  and (my_list) it's the list where the filter function will iterate.
    print(f'>>> Odd list: {odd}')


if __name__ == '__main__':
    os.system('clear')
    run()

