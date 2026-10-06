total_seconds = int(input('Введите количество секунд:'))
clock = total_seconds // 3600
minuts = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(clock, 'ч', minuts, 'мин', seconds, 'с')
