a = 0
num = 0

while num <= 0:
    num = int(input('Введите положительное число:'))
    if num <= 0:
        a = a + 1

S = num**2

print('Квадрат:', S)
print('Отклоненных попыток:', a)
