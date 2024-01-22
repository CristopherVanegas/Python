'''
    > Create the lists 'all_python_devs' and 'all_Platzi_workers'
    using one combination of 'filter' and 'map' higher order functions.

    > Create the list 'old_people' and 'adults' using 'list_comprehensions'.

'''


from concurrent.futures.thread import _worker
from os import system


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def python_devs_and_platzi_workers():
    print(">>> 'All_Python_Devs' and 'All_Platzi_Workers' lists using 'filter' and 'map'")
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))                 # HIGH ORDER FUNCTION > filter
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))                         # HIGH ORDER FUNCTION > map
    for worker in all_python_devs:
       print(f'Python Devs: {worker}')
    print('')

    # all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]    # LIST COMPHRENHENSION 
    all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))          # HIGH ORDER FUNCTION > filter
    all_Platzi_workers = list(map(lambda worker: worker['name'], all_Platzi_workers))                   # HIGH ORDER FUNCTION > map
    for worker in all_Platzi_workers:
       print(f'Platzi Workers: {worker}')
    print('\n')


def old_people_and_adults():
    global DATA
    
    print(">>> 'Old_People' and 'Adults' lists using 'list comprehensions'")

    # creates the old_people's list using list comprehension.
    old_people = [worker for worker in DATA if worker['age'] >= 70]
    print('Old Workers:')
    for worker in old_people:
       print(f"    Worker: {worker['name']} -> {worker['age']}")

    # Adds a new key for a boolean value in the 'old' key.
    DATA = [worker | {'old': worker['age'] >= 70} for worker in DATA]
    print(f"\nDATA MODIFIED - NEW KEY {'{OLD}'} ADDED TO DATA_BACKUP")
    for index in DATA:
        print(f"    Worker: {index['name']} is old: {index['old']}")
    print('\n', end='')

    # creates the adults' list using list comprehension.
    adults = [worker for worker in DATA if worker['age'] > 18 and worker['age'] < 70]
    print('Adult workers: ')
    for worker in adults:
        print(f"    {worker['name']} -> age: {worker['age']}") # -> age: {adults['age']}")
    print('\n', end='')


def print_DATA(DATA):
    for index in DATA:
        print(f"    DATA_BACKUP: {index}")
    print('\n', end='')
    

def run():
    # [complete] > Create the lists 'all_python_devs' and 'all_Platzi_workers' using one combination of 'filter' and 'map' higher order functions. 
    python_devs_and_platzi_workers()
    old_people_and_adults()
    # print_DATA(DATA)


if __name__ == '__main__':
    system('clear')
    run()


