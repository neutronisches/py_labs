'''
С клавиатуры вводится строка. Напишите выражение для генерации
словаря, который содержит информацию о частоте употребления букв в заданной строке.
При анализе не учитывайте регистр, а ключами словаря сделайте использованные в строке
буквы в нижнем регистре.
'''

string = input().lower()
alphabet = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъёфывапролджэячсмитьбю'
d = {}
for i in set(string):
    if i in alphabet:
        d[i] = string.count(i)
print(string, d, sep='\n')
