# DRAFT #2

# Import many libraries
from os import system
from pynput import keyboard
from random import randint
from time import sleep


# First interface
def console_interface():
    system('clear')
    system('figlet HANGMAN')
    system('figlet GAME   v 1 . 0')
    print()

    try:
        answer = input('>>> Start? ( y / n ): ')
        assert answer.isalpha(), '>>> The answer must be ( y / n )!'

        # Makes the answer a string and verifies if it's 'y' or 'n'
        if answer == 'y':   # answer.strip()
            game(word_list, attemps, word_list, guessing)
            # return True

        elif answer == 'n': # answer.strip()
            end_program(True)

        
        else:
           raise AssertionError('>>> The answer must be ( y / n )!')
        

    except AssertionError as ae:
        print(ae)
        sleep(1)
        console_interface()


def game(word, attemps, word_list, guessing):
    system('clear')

    # FIRST CONDITIONAL TO END THE PROGRAM
    if attemps == 0:
        system('clear')
        print('Sorry, you lost the game!!!')
        sleep(1/2)
        print('Good luck in the next one! ;)')
        sleep(1/2)
        print('Program Finished')
        sleep(2)
        system('clear')
        print('Byeee')
        sleep(2)
        system('exit')
        return True
    
    # SECOND CONDITIONAL TO START THE PROGRAM
    elif attemps > 0 and attemps != attemps or attemps == attemps:
        # CONSOLE INTERFACE TO SHOW DETAILS OF THE WORD TO GUESS
        print(
                """
    >>> The Word to guess has {} spaces! {}
    |_/ You have {} attemps

    The word is: {}
                """.format(len(word), word, attemps, guessing)
            )
        
        # LOGIC TO ASK FOR A CHAR AND COMPARE
        try:
            char = input(">>> enter a character you think it's part of the word: ")
            assert char.isalpha(), '>>> Please enter a correct alpha character!'

            # COMPARES
            for j in range(len(word_list)):
                if char == word_list[j]:
                    guessing[j] = char
                else:
                    continue
            
            if word_list == guessing:
                # ask_to_play_again()
                return False

            elif char not in word_list:
                attemps -= 1
                game(word, attemps, word_list, guessing)
            
            elif word_list != guessing:
                game(word, attemps, word_list, guessing)


        except AssertionError as ae:
            print(ae)
            sleep(1)
            game(word, attemps, word_list, guessing)
    
    if game(word, attemps, word_list, guessing):
        system(exit)


def end_program():
    system('clear')
    print('Program Finished')
    sleep(0.5)
    print('Byeee')
    sleep(1)
    system('exit')


def get_the_word(DATA_ROUTE):
    # COUNT THE LINES
    file = open(DATA_ROUTE, 'r', encoding='utf-8')
    lines = 0

    for index in file:
        lines += 1
    file.close()

    # CREATE THE LIST
    file = open(DATA_ROUTE, 'r', encoding='utf-8')
    file_read = file.read()
    file_list = file_read.splitlines()
    file.close()

    # GET RANDOM WORD AND RETURNS IT
    random_word = randint(0, lines -1)
    print(len(file_list))
    print(random_word)

    return file_list[random_word]


def ask_to_play_again():
    try:
        system('clear')
        print('>>> CONGRATULATIONS YOU DID IT!!! YOU WON!!!')

        for x in range(1, 4):
            print(f'{x}... \n')
            sleep(1)

        system('clear')
        answer = input('>>> Do you want to play again?? ( y / n ) ')
        assert answer.isalpha(),'>>> The answer must be ( y / n )! '

        if answer == 'y':
            game(get_the_word(DATA_ROUTE), attemps, word_list, guessing)
        
        if answer == 'n':
            end_program()

    except AssertionError as ae:
        print(ae)
        ask_to_play_again()


# STORAGE SECTION
# This is the route to the data file where it's kept the words
DATA_ROUTE = '/Users/cristophervanegas/Documents/Docs/Projects/Python/Platzi-Intermediate_Python_Course/Projects/hangman_game/rsrcs/data_b/data.txt'
attemps = 10 # ATTEMPS
word_list = list(get_the_word(DATA_ROUTE)) # THE WORD TO GUESS CONVERTED TO A LIST
guessing = ['_' for x in range(len(word_list))] # THE LIST TO FILL OUT AND VERIFY IF IT'S THE SAME TO THE GUESSING WORD
print(word_list)
print(guessing)


def run():
    console_interface()


if __name__ == '__main__':
    system('clear')
    run()


