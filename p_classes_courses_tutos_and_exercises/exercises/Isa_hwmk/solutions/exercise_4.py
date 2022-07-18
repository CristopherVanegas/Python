"""
    Create a loop that sums numbers between 100 to 200
"""


def sum():
    result = 0
    for index in range(100, 201):
        result += index
        print(f'>>> Index: {index}, The result is: {result}')

    """
    result = 0
    for index in range(1, 6):
        result += index
        print(f'>>> Index: {index}, result: {result}')
    """


def run():
    sum()


if __name__ == '__main__':
    run()


