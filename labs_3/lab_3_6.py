'''
Разработайте функцию number_lenght, которая принимает одно целое
число и возвращает его длину без учёта знака.
'''

import sys

def number_lenght(x: int) -> int:
    return len(str(abs(x)))

if __name__ == '__main__':
    try:
        print(number_lenght(int(input())))
    except KeyboardInterrupt:
        sys.exit()
