total = int(input('Введите количество заданий: '))
capacity = int(input('Введите количество заданий в комплекте: '))

filled_units = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity if total > 0 else 0

print(f'Полностью заполненных комплектов: {filled_units}')
print(f'Остаток заданий: {remainder}')
print(f'Минимальное число комплектов: {min_units}')
