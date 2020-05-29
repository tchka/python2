# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.

from collections import Counter, deque

def add_hex(figure_1, figure_2, plus_bit):
    figures_hex = deque([ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])
    idx = figures_hex.index(figure_1) + figures_hex.index(figure_2) + plus_bit
    idx, high_bit = idx % 16, idx // 16
    return figures_hex[idx], high_bit

def string_to_deque(my_str):
    my_deque = deque()
    for figure in my_str:
        my_deque.append(figure)
    return my_deque

a_as_string = input('Введите первое число в шестнадцатеричной форме: ')
b_as_string = input('Введите второй число в шестнадцатеричной форме: ')

a_as_deque = string_to_deque(a_as_string)
b_as_deque = string_to_deque(b_as_string)

max_len = max(len(a_as_deque), len(b_as_deque))
if len(a_as_deque) < max_len:
    a_as_deque.extendleft(['0'] * (max_len - len(a_as_deque)))
if len(b_as_deque) < max_len:
    b_as_deque.extendleft(['0'] * (max_len - len(b_as_deque)))

a_as_deque.reverse()
b_as_deque.reverse()

result = deque()
plus_bit = 0

for idx in range(max_len):
    result_bit, plus_bit = add_hex(a_as_deque[idx], b_as_deque[idx], plus_bit)
    result.append(result_bit)

if (plus_bit):
    result.append(1)

result.reverse()
print('Результат сложения чисел: ', end='')
for item in result:
    print(item, end='')







