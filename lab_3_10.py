'''
Напишите декоратор answer, который преобразует функцию, 
принимающую неограниченное число позиционных и именованных параметров и 
возвращает её результат с припиской "Результат функции: <значение>".
'''

def answer(func):
    def decorator(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return decorator

@answer
def f(arg):
    return arg

print(f(input()))
