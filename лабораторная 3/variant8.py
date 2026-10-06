x = int(input())

if x < 0 or x > 100:
    print("Ошибка диапазона")
elif 0 <= x <= 39:
    print("Есть места")
elif 40 <= x <= 79:
    print("Группа набирается")
else:
    print("Почти заполнена")
