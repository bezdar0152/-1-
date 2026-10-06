name1 = input('название первого предмета:')
count1 = int(input('Количество занятия по первому предмету в неделю:'))
duration1 = int(input('Длительность занятия:'))

name2 = input('Название второго предмета:')
count2 = int(input('Количество занятия по второму предмету в неделю:'))
duration2 = int(input('Длительность занятия:'))
available_clock = float(input('Доступное время на неделюв часах:'))

time1 = count1 * duration1
time2 = count2 * duration2
total_min = time1 + time2
total_clock = total_min / 60
free_clock = available_clock - total_clock
load_weeks = total_clock * 4

print('\n' + '=' * 40)
print('УЧЕБНАЯ НАГРУЗКА')
print('=' * 45)
print(f"Время на '{name1}': {time1} мин")
print(f"Время на '{name2}': {time2} мин")
print(f'Общая нагрузка: {total_min} мин. ({total_clock: .2f} ч.)')
print(f'Остаток свободного времени: {free_clock: .2f} ч.')
print(f'Нагрузка: {load_weeks: .2f} ч.')
print('=' * 40)
