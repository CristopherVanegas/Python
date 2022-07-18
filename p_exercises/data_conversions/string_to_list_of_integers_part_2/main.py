
''' 
    Create a variable that has as value an input that wait for a
    string of numbers and then convert it in integers by splitting
    it and mapping it... 

''' 

def identifyType(): 
    stringNums = input('\n>>>> Insert de string numbers separated by one space ' ': ') 
    print('>>>> variable type: {}'.format(type(stringNums))) 

    stringToInteger(stringNums)


def stringToInteger(string): 
    stringList = string.split(' ') 
    print('\n>>>> Splitted string of numbers: {}\n'.format(stringList)) 

    stringInt = list(map(int, stringList)) 
    for x in range(0, len(stringList)): 
        print('>>>> Items converted to intergers: {}'.format(stringInt[x]))

    print('\n')




if __name__ == '__main__': 
    identifyType() 




