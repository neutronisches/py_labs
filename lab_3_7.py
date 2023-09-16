'''
Разработайте функцию month, которая принимает номер месяца и
обозначение языка ("ru", "en") и возвращает название заданного месяца в заданном языке с
заглавной буквы.
'''

import sys

def month(num, lang):
    if lang.lower() == 'eu':
        d = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
             7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        print(d[num])
    elif lang.lower() == 'ru':
        d = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
             7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
        print(d[num])

if __name__ == '__main__':
    try:
        num, lang = int(input()), input()
        print(month(num, lang))
    except KeyboardInterrupt:
        sys.exit()
