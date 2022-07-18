"""
    THIS CODE SIMULATES A MEDICAL SYSTEM

    Actions:
        1. Set names and surnames of a patient and select the specialty
        in which wants to assist. [DONE]

        2. Specialties are: 
            PEDIATRICS $50
            CARDIOLOGY %70
            DERMATOLOGY %50
        
        3. At the end of the program when it stops of entering patients,
           there should be appear the quantity of collected money.
"""


from os import system


specialties_dict = {
    "[A]: pediatrics": 50,
    "[B]: cardiology": 70,
    "[C]: dematology": 50
}

patients = []
specialties = []
money = 0


"""
    for index in specialties.keys():
        print(f'keys: {index}, value: {specialties[index]}')
"""


def set_names():
    global patients, specialties, specialties_dict, money

    while len(patients) < 3:
        patients.append(input(f'Please enter the patient\'s name - Available [{len(patients)} / 3]: '))
        system('clear')

        print("The specialties and it's costs are:")
        for index in specialties_dict.keys():
            print(f'Specialties: {index} - Value: {specialties_dict[index]}')
        
        specialties.append(input(f'Please write down the speacialty [A, B or C] you want to assist! '))
        system('clear')
    
    for index in specialties:
        if index == 'A':
            money += 50
        elif index == 'B':
            money += 70
        elif index == 'C':
            money += 50
    
    print(f'Money Collected: {money}')


def run():
    set_names()


if __name__ == '__main__':
    system('clear')
    run()

