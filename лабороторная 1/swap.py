first_room = input('аудитория 1:')
second_room = input('аудитория 2:')
print('Исходные значения:', first_room, second_room)

third_room = first_room
first_room = second_room
second_room = third_room
print('После обмена:', first_room, second_room)
