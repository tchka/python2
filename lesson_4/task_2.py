# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

# 1. Используем алгоритм "решето Эратосфена"
# Асимптотический закон распределения простых чисел:
# доля простых среди первых N чисел 1 / ln N

import math
import timeit
import cProfile


def test_f(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i, item in enumerate(lst):
        assert func(i + 1) == item
        print(f'Ok for {i}')


def func_sieve(p):
    n = 4  # размер необходимого "решета" для нахождения i-го простого числа, 4 - начальное минималное значение
    while True:
        if n / math.log(n) > p + 1:
            break
        n += 1

    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    assert (len(res)) >= p
    return res[p - 1]


def simple_test(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def func_simple(p):
    current_res = 1
    current_number = 2
    while current_res < p:
        current_number += 1
        if simple_test(current_number):
            current_res += 1

    return current_number


test_f(func_sieve)

test_f(func_simple)

print(timeit.timeit('func_sieve(32)', number=100, globals=globals()))  # 0.07809982299999998
print(timeit.timeit('func_sieve(64)', number=100, globals=globals()))  # 0.20245436900000002
print(timeit.timeit('func_sieve(128)', number=100, globals=globals()))  # 0.53653028
print(timeit.timeit('func_sieve(256)', number=100, globals=globals()))  # 1.1610632259999998
print(timeit.timeit('func_sieve(512)', number=100, globals=globals()))  # 2.650680726
print(timeit.timeit('func_sieve(1024)', number=100, globals=globals()))  # 6.4470352140000005
print(timeit.timeit('func_sieve(2048)', number=100, globals=globals()))  # 13.477910737000002
print(timeit.timeit('func_sieve(10000)', number=100, globals=globals()))  # 61.709286383

cProfile.run('func_sieve(32)')  # 174 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 task_1.py:20(func_sieve)
# 167    0.000    0.000    0.000    0.000 {built-in method math.log}

cProfile.run('func_sieve(64)')  # 392 function calls in 0.002 seconds
# 1    0.001    0.001    0.002    0.002 task_1.py:20(func_sieve)
# 385    0.001    0.000    0.001    0.000 {built-in method math.log}

cProfile.run('func_sieve(128)')  # 878 function calls in 0.004 seconds
# 1    0.003    0.003    0.004    0.004 task_1.py:20(func_sieve)
# 871    0.001    0.000    0.001    0.000 {built-in method math.log}

cProfile.run('func_sieve(256)')  # 1951 function calls in 0.016 seconds
# 1    0.011    0.011    0.016    0.016 task_1.py:20(func_sieve)
# 1944    0.004    0.000    0.004    0.000 {built-in method math.log}

cProfile.run('func_sieve(512)')  # 4295 function calls in 0.025 seconds
# 1    0.018    0.018    0.025    0.025 task_1.py:20(func_sieve)
# 4288    0.005    0.000    0.005    0.000 {built-in method math.log}

cProfile.run('func_sieve(1024)')  # 9379 function calls in 0.066 seconds
# 1    0.048    0.048    0.065    0.065 task_1.py:20(func_sieve)
# 9372    0.013    0.000    0.013    0.000 {built-in method math.log}

cProfile.run('func_sieve(2048)')  # 20330 function calls in 0.118 seconds
# 1    0.088    0.088    0.118    0.118 task_1.py:20(func_sieve)
# 20323    0.023    0.000    0.023    0.000 {built-in method math.log}


print(timeit.timeit('func_simple(32)', number=100, globals=globals()))  # 0.11367712799999907
print(timeit.timeit('func_simple(64)', number=100, globals=globals()))  # 0.7892450649999994
print(timeit.timeit('func_simple(128)', number=100, globals=globals()))  # 1.99896824
print(timeit.timeit('func_simple(256)', number=100, globals=globals()))  # 10.530562493000001
print(timeit.timeit('func_simple(1024)', number=100, globals=globals()))  # 236.41571414500004
print(timeit.timeit('func_simple(2048)', number=100, globals=globals()))  # 1007.110128453

cProfile.run('func_simple(32)')  # 133 function calls in 0.001 seconds
# 129    0.001    0.000    0.001    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(64)')  # 313 function calls in 0.004 seconds
# 309    0.003    0.000    0.003    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(128)')  # 721 function calls in 0.016 seconds
# 717    0.015    0.000    0.015    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(256)')  # 1621 function calls in 0.086 seconds
# 1617    0.083    0.000    0.083    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(512)')  # 3673 function calls in 0.512 seconds
# #3669    0.504    0.000    0.504    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(1024)')  # 8163 function calls in 2.518 seconds
# 8159    2.497    0.000    2.497    0.000 task_1.py:43(simple_test)

cProfile.run('func_simple(2048)')  # 17865 function calls in 10.689 seconds
# 17861   10.641    0.001   10.641    0.001 task_1.py:43(simple_test)

# Выводы
# Алгоритм с решетом похож на линейный.
# Хотя есть вложенный цикл, и можно было бы ожидать нечто среднее между линейной и кадратичной зависимостями
# Выбрнная оценка размера решета сверху требует решения логарифмического уравнения.
# Можно дальше пробовать другие оценки, возможно они окажутся менее затратными.
# Второй алгоритм тоже похож на линейный. Несколько портит картину 5-й результат (строка 109)
# При этом, если условно предположить, что алгоритмы линейные, то у второго коэффициент выше примерно в 2-2.5 раза.
# Соответственно, алгоритм с решетом быстрее.
