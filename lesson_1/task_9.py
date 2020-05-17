# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).другого

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if b > c:
        result = b
    else:
        if c > a:
            result = a
        else:
            result = c
else:
    if c > a:
        if b > c:
            result = c
        else:
            result = b
    else:
        result = a

print(f'Среднее число: {result}')

