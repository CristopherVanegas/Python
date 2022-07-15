
# This code verifies if a input string is a palindrome

def palindrome(string):
    string = string.lower()
    string = string.replace(' ', '')
    string_reversed = string[::-1]

    # for x in string[::-1]:
    # string_reversed.append(x)a
    
    print('> string: {}'.format(list(string)))
    print('> string reversed: {}'.format(list(string_reversed)))
    if string_reversed != string:
        return False
    else:
        return True


def run():
    string = input('>>> Pls Enter a word or phrase to verify if it is a palindrome: ')

    if palindrome(string) == True:
        print(">>> It's a palindrome")
    else:
        print(">>> It's not a palindrome")




if __name__ == '__main__':
    run()


