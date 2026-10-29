if __name__ == "__main__":
    user_input = input("Введите целые числа одной строкой: ").strip()
    try:
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        print("Ошибка: введены не целые числа")
        exit()
    filtered = [n for n in numbers if 10 <= n <= 20]
    count = len(filtered)
    total = sum(filtered)
    sorted_filtered = sorted(filtered)
    print(filtered)
    print(count)
    print(total)
    print(sorted_filtered)
