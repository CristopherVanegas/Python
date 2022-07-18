"""
    CREATE A FOR LOOP TO COUNT FROM 1 TO 100.
"""

def count():
    for index in range(1, 101):
        print(f'>>> Number {index}')


def run():
    count()


if __name__ == '__main__':
    run()


