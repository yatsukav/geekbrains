# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a = int(input('Введите сторону A: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')
