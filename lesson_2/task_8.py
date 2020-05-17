# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def func(figure, number, repeat_res=0):
    if number // 10 == 0:
        repeat_in_number = 1 if number == figure else 0
        repeat_res += repeat_in_number
        return repeat_res
    else:
        repeat_in_number = 1 if number % 10 == figure else 0
        repeat_res += repeat_in_number
        number = number // 10
        return func(figure, number, repeat_res)


figure = int(input("Какую цифру будем считать? "))
repeat = 0

while True:

    number = int(input("Введите натуральное число (0 для окончания ввода чисел): "))
    if number == 0:
        break
    repeat = repeat + func(figure, number)

ending = ''
if repeat % 10 in (2, 3, 4) and repeat % 100 not in (12, 13, 14):
    ending = 'а'

print(f'Во введенной последовательности чисел цифра {figure} встречается {repeat} раз{ending}')
