# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_A = 6
SIZE_B = 5
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_B)] for _ in range(SIZE_A)]
print(*matrix, sep='\n')

min_column = [MAX_ITEM] * SIZE_B
print(min_column)

result = MIN_ITEM
for idl, line in enumerate(matrix):
    for idx, item in enumerate(line):
        if item < min_column[idx]:
            min_column[idx] = item
        if idl == SIZE_A - 1 and min_column[idx] > result:
            result = min_column[idx]

print(result)
