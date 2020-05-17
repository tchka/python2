# https://drive.google.com/file/d/18aEzzMoVyhGi9VjPBf_--2t-aVXVIvkW/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите целое трехзначное число: '))
number = abs(number)
n0 = number % 10
print(n0)
number = number // 10
n1 = number % 10
print(n1)
n2 = number // 10
print(n2)

product = n0 * n1 * n2
sum = n0 + n1 + n2

print(f'Произведение цифр: {product}')
print(f'Сумма цифр: {sum}')
