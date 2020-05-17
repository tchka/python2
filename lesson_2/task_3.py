# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

def func(a, result=0):
    if a // 10 == 0:
        result *= 10
        result += a
        # print(f'1 {result}')
        return result
    else:
        result *= 10
        result += a % 10
        a = a // 10
        return func(a, result)

number = int(input("Введите натуральное число: "))
print(func(number))