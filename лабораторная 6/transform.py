def transform_numbers(numbers):
    transformed = [abs(n) if n < 0 else n for n in numbers]
    return transformed
if __name__ == "__main__":
    user_input = input("Введите целые числа одной строкой: ").strip()
    if not user_input:
        print("Исходный список: []")
        print("Новый список: []")
    else:
        try:
            numbers = [int(x) for x in user_input.split()]
            transformed = transform_numbers(numbers)
            print(f"Исходный список: {numbers}")
            print(f"Новый список: {transformed}")
        except ValueError:
            print("Ошибка: введены не целые числа")
