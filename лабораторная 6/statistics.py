def calculate_stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    minimum = numbers[0]
    maximum = numbers[0]
    for n in numbers[1:]:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    average = total / count
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")
if __name__ == "__main__":
    user_input = input("Введите целые числа одной строкой: ").strip()
    if not user_input:
        print("Нет данных")
    else:
        try:
            numbers = [int(x) for x in user_input.split()]
            if not numbers:
                print("Нет данных")
            else:
                calculate_stats(numbers)
        except ValueError:
            print("Ошибка: введены не целые числа")
