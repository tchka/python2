# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [i for i in range(2, 10)]
b = [i for i in range(2, 100)]

for j in a:
    result = 0
    for i in b:
        if i % j == 0:
            result += 1
    print(f'В массиве b эелементов кратных {j}: {result} ')
