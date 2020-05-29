# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter, deque

firms = Counter()
number = int(input('Введите количество предприятий: '))
total = 0
for idx in range(number):
    name = input(f'Введите название предприятия {idx + 1}: ')
    profit = float(input('Введите прибыль за 1 квартал: '))
    profit += float(input('Введите прибыль за 2 квартал: '))
    profit += float(input('Введите прибыль за 3 квартал: '))
    profit += float(input('Введите прибыль за 4 квартал: '))
    firms[name] = profit
    total += profit


profit_average = total / number

print(f'Средняя прибыль по предприятиям: {profit_average}')
earn = deque()
loss = deque()

for firm in firms:
    if firms[firm] >= profit_average:
        earn.append(firm)
    else:
        loss.append(firm)

print('Прибыльные предприятия :')
for item in earn:
    print(item)

print('Убыточные предприятия :')
for item in loss:
    print(item)