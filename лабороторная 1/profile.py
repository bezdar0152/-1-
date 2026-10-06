sername = input('Введите фамилию:')
name = input('Введите имя:')
group = input('Введите группу:')
city = input('Ведите город:')
age = int(input('Введите возраст:'))
subject = input('Введите любимый предмет:')
clock = float(input('Введите количество часов подготовки в неделю:'))

new_name = name + " " + sername
new_age = age + 4
clock_weeks = clock * 4
clock_day = clock / 7

print('\n' + '=' * 20)
print('КАРТОЧКА СТУДЕНТА')
print('=' * 20)
print('Полное имя:', new_name)
print('Возраст через 4 года:', new_age)
print('Группа:', group)
print('Город:', city)
print('Любимый предмет:', subject)
print('Время подготовки: {:.2f} ч.'.format(clock_weeks))
print('Среднее время: {:.2f} ч.'.format(clock_day))
print('=' * 20)
