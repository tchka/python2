# https://drive.google.com/file/d/1AZeJid7-L7oOViVZwAV1UrpPa6WsZjTD/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа.

def func(a, odd=0, even=0):
    if a // 10 == 0:
        odd += a % 2
        even += a % 2 - 1
        return f'Во введенном числе нечетных цифр: {odd}, четных цифр: {even}'
    else:
        odd += a % 10 % 2
        even += 1 - a % 10 % 2
        a = a // 10
        return func(a, odd, even)


number = int(input("Введите натуральное число: "))
print(func(number))
