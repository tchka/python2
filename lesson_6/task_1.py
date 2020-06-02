# lesson 2 task 2
# Посчитать четные и нечетные цифры натурального числа.
import random
import sys
from _collections import deque

number = random.randint(0, 100000)
print(number)


def func(a, odd=0, even=0, memory=0):
    if a // 10 == 0:
        memory += sys.getsizeof(a)
        odd += a % 2
        memory += sys.getsizeof(odd)
        even += a % 2 + 1
        memory += sys.getsizeof(even)
        print(f'Во введенном числе нечетных цифр: {odd}, четных цифр: {even}')
        return memory
    else:
        odd += a % 10 % 2
        even += 1 - a % 10 % 2
        a = a // 10
        return func(a, odd, even)


def show(object):
    print(f'object_type = {type(object)}, size= {sys.getsizeof(object)}, object = {object}')
    if hasattr(object, '__iter__'):
        if hasattr(object, 'item'):
            for key, value in object.items():
                show(key)
                show(value)
        elif not isinstance(object, str):
            for item in object:
                show(item)


def calculate_zise(object):
    memory_size = sys.getsizeof(object)
    if hasattr(object, '__iter__'):
        if hasattr(object, 'item'):
            for key, value in object.items():
                memory_size += sys.getsizeof(key)
                memory_size += sys.getsizeof(value)
        elif not isinstance(object, str):
            for item in object:
                memory_size += sys.getsizeof(item)
    return memory_size


# Вариант 1
print(f'Var1. Allocated memory size: {sys.getsizeof(number) + func(number)}')

# Вариант 2

number2 = number
number_as_list = []

while True:
    number_as_list.append(number2 % 10)
    if number2 // 10 == 0:
        break
    number2 = number2 // 10

odd = 0
even = 0
for i in number_as_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Во введенном числе нечетных цифр: {odd}, четных цифр: {even}')
print(
    f'Var2. Allocated memory size: {sys.getsizeof(number2) + calculate_zise(number_as_list) + calculate_zise(odd) + calculate_zise(even)}')

# Вариант 3
number3 = number
number_as_deque = deque()

while True:
    number_as_deque.append(number3 % 10)
    if number3 // 10 == 0:
        break
    number3 = number3 // 10

odd = 0
even = 0
for i in number_as_deque:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Во введенном числе нечетных цифр: {odd}, четных цифр: {even}')
print(
    f'Var2. Allocated memory size: {sys.getsizeof(number3) + calculate_zise(number_as_deque) + calculate_zise(odd) + calculate_zise(even)}')

# print(func(number))
# show([1,2,3,4,5])
# print(calculate_zise([1,2,3,4,5]))
