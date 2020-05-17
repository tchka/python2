# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (number) вводится с клавиатуры.

n = 1  # начальное число последовательности
k = -0.5  # коэффициент постедовательности


def func(n, k, number, result=0):
    if number == 1:
        result += n
        return result
    else:
        number -= 1
        result += n * k ** number
        return func(n, k, number, result)


number = int(input("Введите натуральное число: "))
print(func(n, k, number))
