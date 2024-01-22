
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


def ask_to_play_again():
    system('clear')
    answer = input('>>> Do you want to play again?? ( y / n ) ')
    return answer


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


def game_logic(word, attemps, word_list, guessing):
    # WHILE CONDITIONAL TO START THE PROGRAM
    while attemps > 0 and word_list != guessing: #and attemps != attemps or attemps == attemps:
        system('clear')
        
        # CONSOLE INTERFACE TO SHOW DETAILS OF THE WORD TO GUESS
        print('>>> The Word to guess has {} spaces! {}'.format(len(word), word))
        print('|_/ You have {} attemps'.format(attemps))
        print('The word is: {}'.format(guessing))            
        
        # LOGIC TO ASK FOR A CHAR AND COMPARE
        try:
            char = input(">>> enter a character you think it's part of the word: ")
            assert char.isalpha(), '>>> Please enter a correct alpha character!'

            # COMPARES
            for x in range(len(word_list)):
                if char == word_list[x]:
                    guessing[x] = char

            if char not in word_list and word_list != guessing:
                attemps -= 1
            
            # THIS COULD BE OBVIATED
            # elif word_list != guessing:
            #   continue

            elif word_list == guessing:
                system('clear')
                print('>>> CONGRATULATIONS YOU DID IT!!! YOU WON!!!')
                for x in range(1, 4):
                    print(f'{x}... \n')
                    sleep(1)
                
                while_key = False
                while while_key == False:
                    try:
                        answer = ask_to_play_again()
                        assert answer.isalpha(), '>>> The answer must be ( y / n )!'

                        if answer.strip() == 'y':
                            while_key = True
                            # console_interface()
                            print('play again')

                        if answer.strip() == 'n':
                            while_key = True
                            end_program()
                
                    except AssertionError as ae:
                        print(ae)
                        # while_key = while_key
                        # ask_to_play_again
                    

                # ask_to_play_again()


        except AssertionError as ae:
            print(ae)
            sleep(1)


# STORAGE SECTION
# This is the route to the data file where it's kept the words
DATA_ROUTE = '/Users/cristophervanegas/Documents/Docs/Projects/Python/Platzi-Intermediate_Python_Course/Projects/hangman_game/rsrcs/data_b/data.txt'
attemps = 10 # ATTEMPS
word_list = list(get_the_word(DATA_ROUTE)) # THE WORD TO GUESS CONVERTED TO A LIST
guessing = ['_' for x in range(len(word_list))] # THE LIST TO FILL OUT AND VERIFY IF IT'S THE SAME TO THE GUESSING WORD


def run():
    game_logic(word_list, attemps, word_list, guessing)


if __name__ == '__main__':
    run()
