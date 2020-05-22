# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
min_value = MAX_ITEM
max_value = MIN_ITEM

for idx, value in enumerate(array):
    if value > max_value:
        idx_max = idx
        max_value = value
    if value < min_value:
        idx_min = idx
        min_value = value

print(idx_min, idx_max)
array[idx_max], array[idx_min] = array[idx_min], array[idx_max]

print(array)
