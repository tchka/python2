# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = float(input('Введите длину первой стороны: '))
b = float(input('Введите длину второй стороны: '))
c = float(input('Введите длину третьей стороны: '))

if a + b <= c or b + c <= a or c + a <= b:
    result = 'Треугольник не существует'
else:
    if a == b:
        if b == c:
            result = 'Треугольник равносторонний'
        else:
            result = 'Треугольник равнобедренный'
    else:
        if c == a:
            result = 'Треугольник равнобедренный'
        else:
            if b == c:
                result = 'Треугольник равнобедренный'
            else:
                result = 'Треугольник разносторонний'

print(result)

