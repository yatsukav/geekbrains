# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю
# о невозможности деления на ноль, если он ввел 0 в качестве делителя.


repeat_main = True
while repeat_main:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    get_operator = True
    while get_operator:
        op = input('Введите оператор или 0: ')
        if op == '0':
            get_operator = False
            repeat_main = False  # выходим из приложения
        elif op == '+':
            print(f'{a} {op} {b} = {a + b}')
            get_operator = False  # выводим результат
        elif op == '-':
            print(f'{a} {op} {b} = {a - b}')
            get_operator = False  # выводим результат
        elif op == '*':
            print(f'{a} {op} {b} = {a * b}')
            get_operator = False  # выводим результат
        elif op == '/':
            print(f'{a} {op} {b} = {a / b}')
            get_operator = False  # выводим результат
        else:
            print('Не верный оператор')

print('До свидания!')
