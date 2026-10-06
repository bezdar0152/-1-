num1 = float(input('Введите первое число:'))
num2 = float(input('Введите второе число:'))
operator = input('Введите операцию (+, -, *, /):')

if operator == '+':
    print(f'{num1 + num2: .2f}')
elif operator == '-':
    print(f'{num1 - num2: .2f}')
elif operator == '*':
    print(f'{num1 * num2: .2f}')
elif operator == '/':
    if num2 == 0:
        print('Деление на ноль запрещено:')
    else:
        print(f'{num1 / num2: .2f}')
else:
    print('Неизвестная операция')
