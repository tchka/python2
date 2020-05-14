# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

five_0 = 5 % 2
five_1 = 5 // 2 % 2
five_2 = 5 // 4 % 2

six_0 = 6 % 2
six_1 = 6 // 2 % 2
six_2 = 6 // 4 % 2

and_0 = five_0 * six_0
and_1 = five_1 * six_1
and_2 = five_2 * six_2

or_0 = 1 if (five_0 + six_0 > 0) else 0
or_1 = 1 if (five_1 + six_1 > 0) else 0
or_2 = 1 if (five_2 + six_2 > 0) else 0

xor_0 = 1 if (five_0 + six_0 == 1) else 0
xor_1 = 1 if (five_1 + six_1 == 1) else 0
xor_2 = 1 if (five_2 + six_2 == 1) else 0

not_five_0 = 1 - five_0
not_five_1 = 1 - five_1
not_five_2 = 1 - five_2

not_six_0 = 1 - six_0
not_six_1 = 1 - six_1
not_six_2 = 1 - six_2

left_2_five_0 = 0
left_2_five_1 = 0
left_2_five_2 = five_0
left_2_five_3 = five_1
left_2_five_4 = five_2

right_2_five_0 = five_2

result_and = and_2 * 4 + and_1 * 2 + and_0
result_or = or_2 * 4 + or_1 * 2 + or_0
result_xor = xor_2 * 4 + xor_1 * 2 + xor_0
not_five = not_five_2 * 4 + not_five_1 * 2 + not_five_0
not_six = not_six_2 * 4 + not_six_1 * 2 + not_six_0
left_2_five = left_2_five_4 * 16 + left_2_five_3 * 8 + left_2_five_2 * 4 + left_2_five_1 * 2 + left_2_five_0
right_2_five = right_2_five_0

print(f'Побитовое И: {result_and}')
print(f'Побитовое ИЛИ: {result_or}')
print(f'Побитовое исключающее ИЛИ: {result_xor}')
print(f'Побитовое НЕ от 5: {not_five}')
print(f'Побитовое НЕ от 6: {not_six}')
print(f'Cдвиг влево от 5: {left_2_five}')
print(f'Cдвиг вправо от 5: {right_2_five}')
