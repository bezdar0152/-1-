price = int(input('Введите цену одной тетради:'))
count = int(input('Введите количество тетрадей:'))
paid = int(input('Введите переданную сумму:'))

total_cost = price * count
change = paid - total_cost

print('Стоимость:', total_cost, ',сдача:', change)
