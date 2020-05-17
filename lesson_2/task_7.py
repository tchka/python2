# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def summa(n, result=0):
    if n == 1:
        result += n
        return result
    else:
        result += n
        n -= 1
        return summa(n, result)

n = int(input("Введите натуральное число: "))

summa_n = summa(n)
summa_formula = n * (n + 1) / 2

if (summa_formula == summa_n):
    print(f"Формула верна для числа {n}")
else:
    print(f"Формула не верна для числа {n}")
