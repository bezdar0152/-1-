from functions import sum_digits, average, normalize_text, select_numbers

def to_int_list(s):
    if not s.strip():
        return 
    try:
        return [int(v) for v in s.split()]
    except ValueError:
        return 
if __name__ == "__main__":
    n_str = input("Число: ")
    try:
        n = int(n_str)
        print("Сумма цифр:", sum_digits(n))
    except ValueError:
        print("Не число")
    nums_str = input("Числа через пробел: ")
    nums = to_int_list(nums_str)
    avg = average(nums)
    if avg is None:
        print("Нет данных")
    else:
        print("Среднее:", avg)
    txt = input("Текст: ")
    print("Нормализованный текст:", normalize_text(txt))
    th_str = input("Порог: ")
    try:
        th = int(th_str)
        if th < 0:
            print("Порог должен быть >= 0")
        else:
            print("Отфильтрованный список:", select_numbers(nums, th))
    except ValueError:
        print("Не число")
