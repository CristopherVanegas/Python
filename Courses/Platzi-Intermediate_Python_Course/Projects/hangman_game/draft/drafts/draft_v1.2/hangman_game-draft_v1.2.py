# DRAFT #3 (FINAL)

# Import many libraries
from os import system
from random import randint
from time import sleep


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

    return file_list[random_word]


def ask_to_play_again():
    system('clear')
    answer = input('>>> Do you want to play again?? ( y / n ) ')    
    try:
        assert answer.isalpha(), '>>> The answer must be ( y / n )!'
        if answer.strip() == 'y':
            return True

        if answer.strip() == 'n':
            return False

        else:
            raise AssertionError('>>> The answer must be ( y / n )!')
    

    except AssertionError as ae:
        print(ae)
        ask_to_play_again()


# STORAGE SECTION
# This is the route to the data file where it's kept the words
DATA_ROUTE = '/Users/cristophervanegas/Documents/Docs/Projects/Python/Platzi-Intermediate_Python_Course/Projects/hangman_game/rsrcs/data_b/data.txt'
attemps = 10 # ATTEMPS
word = get_the_word(DATA_ROUTE)
word_list = list(word) # THE WORD TO GUESS CONVERTED TO A LIST
guessing = ['_' for x in range(len(word_list))] # THE LIST TO FILL OUT AND VERIFY IF IT'S THE SAME TO THE GUESSING WORD
key = True
play_again = False


def game(word_f, attemps_f, word_list_f, guessing_f):
    global key, play_again

    # WHILE CONDITIONAL TO START THE PROGRAM
    while attemps_f > 0 and word_list_f != guessing_f: #and attemps != attemps or attemps == attemps:
        system('clear')
        
        # CONSOLE INTERFACE TO SHOW DETAILS OF THE WORD TO GUESS
        print('>>> The Word to guess has {} spaces!'.format(len(word_f)))
        print('|_/ You have {} attemps'.format(attemps_f))
        print('The word is: {}'.format(guessing_f))            


        # LOGIC TO ASK FOR A CHAR AND COMPARE
        try:
            char = input(">>> enter a character you think it's part of the word: ")
            assert char.isalpha(), '>>> Please enter a correct alpha character!'

        except AssertionError as ae:
            print(ae)
            sleep(1)
        
        
        # COMPARES
        for x in range(len(word_list_f)):
            if char == word_list_f[x]:
                guessing_f[x] = char
        

        if char not in word_list_f and word_list_f != guessing_f:
            attemps_f -= 1
            if attemps_f < 1:
                system('clear')
                print('Sorry, you lost!')
                print(f'attemps = {attemps_f}')
                sleep(2)
                key, play_again = False, False
                # end_program()
        

        if word_list_f == guessing_f:
            system('clear')
            print('>>> CONGRATULATIONS YOU DID IT!!! YOU WON!!!')
            for x in range(1, 4):
                sleep(1/2)
                print(f'{x}... \n')
            sleep(1/2)
            
            if ask_to_play_again() == True:
                play_again, key = True, True
            
            else:
                play_again, key =  False, False


# First interface
def console_interface():
    global key
    system('clear')
    system('figlet HANGMAN')
    system('figlet GAME   v 1 . 2')
    print()

    answer = input('>>> Start? ( y / n ): ')
    assert answer.isalpha(), '>>> The answer must be ( y / n )!'
    try:
        # Makes the answer a string and verifies if it's 'y' or 'n'
        if answer.strip() == 'y':  
            game(word, attemps, word_list, guessing)

        elif answer.strip() == 'n':
            key = False

        else:
           raise AssertionError('>>> The answer must be ( y / n )!')
    

    except AssertionError as ae:
        print(ae)
        sleep(1)
        console_interface()


def run():
    global key, play_again

    while key == True:
        if key == False:
            break
        
        elif key == True:
            console_interface()
            
            if play_again == True:
                attemps = 10 # ATTEMPS
                word = get_the_word(DATA_ROUTE)
                word_list = list(word) # THE WORD TO GUESS CONVERTED TO A LIST
                guessing = ['_' for x in range(len(word_list))] # THE LIST TO FILL OUT AND VERIFY IF IT'S THE SAME TO THE GUESSING WORD
                
                game(word, attemps, word_list, guessing)

            elif play_again == False:
                key = False


    end_program()


if __name__ == '__main__':
    run()


