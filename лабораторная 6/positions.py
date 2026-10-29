def find_max_indices(numbers):
    max_value = numbers[0]
    for n in numbers[1:]:
        if n > max_value:
            max_value = n
    indices = [i for i, n in enumerate(numbers) if n == max_value]
    return indices
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
                result = find_max_indices(numbers)
                print(result)
        except ValueError:
            print("Ошибка: введены не целые числа")
