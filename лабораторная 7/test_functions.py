from functions import sum_digits, average, normalize_text, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-587) == 20

assert average() is None
assert average([2, 4, 6]) == 4

assert normalize_text("  ПРИВЕТ   МИР  ") == "привет мир"
assert normalize_text("   ") == ""

# Тесты для варианта 8: abs(x) <= threshold
assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]
assert select_numbers(, 2) == 
assert select_numbers([-2, 2], 2) == [-2, 2]
assert select_numbers([-3, 3], 2) == 
assert select_numbers([2, 2, -2, -2, 3], 2) == [2, 2, -2, -2]

orig = [-5, 0, 2, 5]
orig_copy = orig[:]
select_numbers(orig, 2)
assert orig == orig_copy

print("Все проверки пройдены")
