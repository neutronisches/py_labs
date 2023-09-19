'''
Напишите рекурсивную функцию recursive_digit_sum, которая находит 
сумму всех цифр натурального числа.
'''

import sys

def recursive_digit_sum(n: int) -> int:
    if n == 0: return 0
    return n % 10 + recursive_digit_sum(n // 10)
    
if __name__ == '__main__':
    try:
        print(recursive_digit_sum(int(input())))
    except KeyboardInterrupt:
        sys.exit()
