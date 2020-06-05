# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# Лучше бы реализовать что-то поинтереснее, но времени уже нет. На вторую задачу часов 6 ушло... Не знаю, почему так много. Вроде все понятно, пока не начинаю код писать

import random


def half_sort(array):
    n = 1
    while n < len(array)//2 + 2:
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        print(array)
        n += 1


HALF = 10

my_array = [random.randint(-100, 99) for i in range(2 * 10 + 1)]
print(my_array)

print(half_sort(my_array))
print(my_array[HALF])
