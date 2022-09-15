# This code is just done for showing purpouses.
# Summed up, this shows how dictionaries can contain lists and vice versa.

def run():
    list = [1, 'Hello World', 15, 3.14]
    dict = {
        'First Name': 'Cristopher',
        'Last Name': 'Vanegas'
    }

    super_list = [
        {'First Name': 'Cristopher', 'Last Name': 'Vanegas'},
        {'First Name': 'Alondra', 'Last Name': 'Vanegas'},
        {'First Name': 'Damian', 'Last Name': 'Vanegas'}
    ]

    super_dict = {
        'Natural_nums': [1, 2, 3, 4, 5],
        'Integer_nums': [-2, -1, 0, 1, 2],
        'Floating_nums': [1.2, 4.5, 5.5, 7.2, 10.2]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    print()

    for x in super_list:
        key, value = x.items()
        print(key, '-', value)



if __name__ == '__main__':
    run()
