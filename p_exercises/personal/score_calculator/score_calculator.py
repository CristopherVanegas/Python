
def main(): 
    score_calculator()


def score_calculator(): 
    score = 10 
    for x in range(1, 10): 
        answer = int(input(f'Is it correct or incorrect question {x}?: \n   >>>> Please, answer 1 or 0 \n')) 
        print('\n')1

        if answer != 1: 
            score = score - 1 
        
        print(f'The score is: {score}')

if __name__ == '__main__': 
    main()



