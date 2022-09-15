
# DRAFT #1

# This code it's to perform the hangman game.
# Final project to finish Second Course - Python Intermediate [Platzi]


from os import system
from random import randint
from time import sleep


DATA_ROUTE = '/Users/cristophervanegas/Documents/Docs/Projects/Python/Platzi-Intermediate_Python_Course/Projects/hangman_game/rsrcs/data_b/data.txt'
ATTEMPS = 10

def console_interface(word=str, attemps=int, word_completing=str, boolean=bool):
    if attemps >= 1:

        '''if boolean:
            word_completing = word_completing
        else:'''
        word_completing = '_' * len(word)

        system('clear')
        system('figlet HANGMAN')
        system('figlet GAME   v 1 . 0')
        print(
            """
>>> The Word to guess has {} spaces! {}
|_/ You have {} attemps
The word is: {}
            """.format(
                len(word),
                word_completing,
                attemps,
                word
            )
        )

        try:
            answer = input('  >>> Enter a letter: ')
            if answer.isnumeric():
                raise ValueError('  >>> You need to enter a letter, not a number!')

            booleans = verify_char(answer, word)
            for index in booleans:
                if index == answer:
                    word_completing = list(word_completing)
                    word_completing[index] = answer
                    console_interface(word, attemps, word_completing, True)

                else:
                    console_interface(word, attemps-1, word_completing, False)

            # FOR NOW
                
            # I NEED TO CHECK IF THE WORD IS FOUND IN THE STRING CONVERTED INTO LIST.
            # IF IT'S TRUE, SO I NEED TO CLEAR THE CONSOLE AND FILL THE BLANKS.
            # IF IT'S FALSE, SO I NEED TO REST -1 TO THE ATTEMPS AND TRY AGAIN.

            # IF ATTEMPS ARE 0 THE GAME ENDS.

            # COMMENT THE CODE.

            
        except ValueError as ve:
            print(ve)
            sleep(1)
            console_interface(word, attemps)

    else:
        system('clear')
        print('>>> You\'ve reached your limit of attemps!!!')
        print(f' |_// Attemps: {attemps}')
        print('>>> So, you lost the game...')
        print('>>> Good luck in the next one!')
        sleep(1)
        end_program()


def get_the_word(DATA_ROUTE):
    # COUNT THE LINES
    file = open(DATA_ROUTE, 'r', encoding='utf-8')
    lines = 0
    for index in file:
        lines += 1
    file.close()
    # print(lines)

    # CREATE THE LIST
    file = open(DATA_ROUTE, 'r', encoding='utf-8')
    file_r = file.read()
    file_list = file_r.splitlines()
    file.close()
    # print(file_list)

    # GET A RANDOM AND SELECT ONE FROM THE LIST
    random_index = randint(0, lines-1)

    # RETURNS THE RANDOM WORD
    return file_list[random_index]


def verify_char(answer, word):
    booleans = []
    for index in word:
        if answer.strip() == index:
            booleans.append(True)
        else: 
            booleans.append(False)
    return booleans


def end_program():
    print('program finished')


def run():
    system('clear')

    try:
        answer = input('>>> Start? ( y / n ): ')
        assert not answer.isnumeric(), '>>> The answer must be ( y / n )!: '

        if answer.strip() == 'y':
            console_interface(get_the_word(DATA_ROUTE), ATTEMPS, boolean = False)
            
        elif answer.strip() == 'n':
            end_program()


    except AssertionError as assertion_error:
        print(assertion_error)
        sleep(1)
        run()


if __name__ == '__main__':
    run()

