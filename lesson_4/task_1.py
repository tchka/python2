# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# Выбираем задачу 9 из урока 3: Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Тестируем на квадратной матрице размера n

import random
import timeit
import cProfile


def get_martix(n):
    MIN_ITEM = 0
    MAX_ITEM = 100
    return [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)] for _ in range(n)]


def func_1(n):
    matrix = get_martix(n)
    # print(*matrix, sep='\n')
    result = None
    min_column = matrix[0]

    for idl, line in enumerate(matrix):
        for idx, item in enumerate(line):
            if item < min_column[idx]:
                min_column[idx] = item
            if idl == n - 1 and (result is None or min_column[idx] > result):
                result = min_column[idx]
    return result


def func_2(n):
    matrix = get_martix(n)
    # print(*matrix, sep='\n')
    result = None

    for idx in range(len(matrix[0])):
        min_ = matrix[0][idx]
        for idl in range(len(matrix)):
            if matrix[idl][idx] < min_:
                min_ = matrix[idl][idx]
        if result is None or min_ > result:
            result = min_
    return result


def func_3(n):
    matrix = get_martix(n)
    # print(*matrix, sep='\n')
    column = [0] * len(matrix)
    min_column = [0] * len(matrix[0])

    for idx in range(len(matrix[0])):
        for idl in range(len(matrix)):
            column[idl] = matrix[idl][idx]
        min_column[idx] = min(column)
    result = max(min_column)
    return result


print(timeit.timeit('func_1(32)', number=100, globals=globals()))  # 1.03300183
print(timeit.timeit('func_1(64)', number=100, globals=globals()))  # 3.8149726540000004
print(timeit.timeit('func_1(128)', number=100, globals=globals()))  # 18.512164081

cProfile.run('func_1(32)')  # 5352 function calls in 0.013 seconds
cProfile.run('func_1(64)')  # 21583 function calls in 0.052 seconds
cProfile.run('func_1(128)')  # 86400 function calls in 0.201 seconds

print(timeit.timeit('func_2(32)', number=100, globals=globals()))  # 0.9092914550000017
print(timeit.timeit('func_2(64)', number=100, globals=globals()))  # 3.743389400999998
print(timeit.timeit('func_2(128)', number=100, globals=globals()))  # 20.050942620999997

cProfile.run('func_2(32)')  # 5468 function calls in 0.012 seconds
cProfile.run('func_2(64)')  # 21678 function calls in 0.046 seconds
cProfile.run('func_2(128)')  # 86469 function calls in 0.180 seconds

print(timeit.timeit('func_3(32)', number=100, globals=globals()))  # 0.7657035500000049
print(timeit.timeit('func_3(64)', number=100, globals=globals()))  # 3.632640925000004
print(timeit.timeit('func_3(128)', number=100, globals=globals()))  # 17.279106467999995

cProfile.run('func_3(32)')  # 5464 function calls in 0.014 seconds
cProfile.run('func_3(64)')  # 21700 function calls in 0.049 seconds
cProfile.run('func_3(128)')  # 86577 function calls in 0.213 seconds
#
#     4096    0.017    0.000    0.035    0.000 random.py:200(randrange)
#     4096    0.009    0.000    0.044    0.000 random.py:244(randint)
#     4096    0.013    0.000    0.018    0.000 random.py:250(_randbelow_with_getrandbits)

#
# Выводы
# Алгоритмы ведут себя как квадратичные и мало чем отличаются.
# Как я понимаю, основная нагрузка - это генерация диапазонов range. А она общая для всех трех вариантов.
