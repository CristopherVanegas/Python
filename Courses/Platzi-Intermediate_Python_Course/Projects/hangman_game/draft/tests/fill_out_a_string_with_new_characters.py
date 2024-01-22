from os import system

word = 'interesting'
verify = list(word)
guessing_attemp_word = ['_' for x in range(len(verify))]


def game():
    system('clear')
    char = input('insert a character: ')

    print(f'{verify}\n{guessing_attemp_word}')

    # VERIFY
    for x in range(len(verify)):
        if char == verify[x]:
            guessing_attemp_word[x] = char

    print(guessing_attemp_word)

    if guessing_attemp_word == verify:
        return True
    else:
        return False


def run():
    if game() == True and guessing_attemp_word == verify:
        pass
    else:
        game()


if __name__ == '__main__':
    run()
    
        
