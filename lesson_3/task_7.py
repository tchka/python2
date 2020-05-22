# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_value_1 = MAX_ITEM
min_value_2 = MAX_ITEM

for value in array:
    if value < min_value_1:
        min_value_2 = min_value_1
        min_value_1 = value
    elif value < min_value_2:
        min_value_2 = value

print(min_value_1, min_value_2)
