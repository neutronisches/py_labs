'''
Вводятся строки, пока не будет введена строка «ФИНИШ». Требуется 
выполнить простой частотный анализ: выяснить, какой символ встречается в тексте чаще 
всего.
'''

from collections import Counter
import sys

def func(text: str) -> str:
    count = Counter(text)
    ms = count.most_common(1)
    mf = ms[0]
    return mf[0]

if __name__ == '__main__':
    try:
        print(func(''.join([str(x) for x in input().split()])))
    except KeyboardInterrupt:
        sys.exit()
