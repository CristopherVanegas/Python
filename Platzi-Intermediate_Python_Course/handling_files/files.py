from os import system

names = [
    'Melva',
    'Francisco',
    'Alondra',
    'Damián',
    'Cristopher',
    'Sabrina',
    'Paula'
]


def read():
    numbers = []
    with open('/Users/cristophervanegas/Documents/Projects/Python/Platzi-Intermediate_Python_Course/handling_files/archivos/numbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)


def write():
    global names
    with open('/Users/cristophervanegas/Documents/Projects/Python/Platzi-Intermediate_Python_Course/handling_files/archivos/names.txt', 'w', encoding='utf-8') as file:
        for name in names:
            file.write(name)
            file.write('\n')


def append_files():
    global names
    names = [
        'Jessica',
        'Emily'
    ]
    with open('/Users/cristophervanegas/Documents/Projects/Python/Platzi-Intermediate_Python_Course/handling_files/archivos/names.txt', 'a', encoding='utf-8') as file :
        for name in names:
            file.write(name)
            file.write('\n')



def run():
    read()
    write()
    append_files()


if __name__ == '__main__':
    system('clear')
    run()
