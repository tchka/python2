# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def func(number, figure_sum=0):
    if number // 10 == 0:
        figure_sum += number
        return figure_sum
    else:
        figure_sum += number % 10
        number = number // 10
        return func(number, figure_sum)


max_sum
max_number = 0

while True:

    number = int(input("Введите натуральное число (0 для окончания ввода чисел): "))
    if number == 0:
        break

    current_sum = func(number)
    if current_sum > max_sum:
        max_sum = current_sum
        max_number = number


print(f'Во введенной последовательности число с максимальной суммой цифр: {max_number}, сумма его цифр равна {max_sum}')
