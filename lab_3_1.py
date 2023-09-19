'''
Вводятся строки, пока не будет введена строка «ФИНИШ». Требуется 
выполнить простой частотный анализ: выяснить, какой символ встречается в тексте чаще 
всего.
'''

import sys

def func(text: str) -> str:
    alphabet = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъёфывапролджэячсмитьбю'
    d = {}
    for i in set(text):
        if i in alphabet:
            d[i] = text.count(i)
    return sorted(d.items(), key=lambda x: x[1])[-1][0]

if __name__ == '__main__':
    try:
        s = ''
        while True:
            a = input().lower()
            if a == 'финиш':
                break
            s += a
        print(func(s))
    except KeyboardInterrupt:
        sys.exit()
