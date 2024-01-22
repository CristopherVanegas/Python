from random import randint

def get_the_word():
    lines = 0
    words = []

    file = open('/Users/cristophervanegas/Documents/Projects/Python/Platzi-Intermediate_Python_Course/Projects/hangman_game/rsrcs/data_b/data.txt', 'r', encoding='utf-8')
    obj_2 = file.readlines()

    # JUST COUNT THE FILE'S LINES.
    for index in file:
        lines += 1

    a_file = file.read()
    file_list = a_file.splitlines()
    
    file.close()
    print(obj_2)
    print(lines)
    print(file_list)
        
        




if __name__ == '__main__':
    get_the_word()

