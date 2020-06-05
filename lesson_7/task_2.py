# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr, first, last):
    if first >= last:
        return arr

    middle = first + (last - first) // 2 + 1

    merge_sort(arr, first, middle - 1)
    merge_sort(arr, middle, last)

    result = []

    i = first
    j = middle

    while i < middle and j <= last:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    result.extend(arr[i: middle])
    result.extend(arr[j: last + 1])
    # print(result)
    arr[first: last + 1] = result[:]


my_array = [round(random.random() * 50, 3) for i in range(10)]
print(my_array)


merge_sort(my_array, 0, len(my_array) - 1)
print(my_array)
