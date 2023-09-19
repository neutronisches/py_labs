'''
Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
Параметры функции:
  •	size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
  •	value — значение элементов списка (по-умолчанию 0).
'''

import sys

def make_matrix(size: tuple[int, int] | int, value = 0) -> list[list]:
    w, h = size if isinstance(size, tuple) else (size,) * 2
    return [[value] * w for _ in range(h)]

if __name__ == '__main__':
    try:
        print(make_matrix(tuple(map(int, input().split())), input()))
    except KeyboardInterrupt:
        sys.exit()
