"""
    PRINT NUMBERS FROM 1 TO 10 UPSIDE DOWN USING FOR LOOP.
"""

def upside_down_count():
    num = 10
    for index in range(10):
        print(f'>>> UPSIDE DOWN COUNT: {num}')
        num -= 1


def run():
    upside_down_count()


if __name__ == '__main__':
    run()

