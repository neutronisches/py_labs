'''
Напишите простую утилиту, которая очищает заданный файл от:
•	повторяющихся пробелов;
•	повторяющихся символов перевода строки;
•	табуляций,
•	излишних пробелов в начале и конце строк.
'''

import re

with open('1.txt', 'r', encoding='utf-8') as f:
    s = f.read()

try:
    s = re.sub(r'\n+', '\n', s)
    s = re.sub(r'[ ]+', ' ', s)
    s = s.replace('\t', '')
    print('\n'.join(i.strip() for i in s.split('\n') if s.strip()))

finally:
    f.close()    
