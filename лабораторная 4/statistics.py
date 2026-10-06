n = int(input('Введите n:'))

total_sum = 0
positive_count = 0
first = int(input('Введите число:'))
max = first
total_sum += first

if first > 0:
    positive_count += 1

for _ in range(n - 1):
    num = int(input('Введите число:'))
    total_sum += num
    if num > 0:
        positive_count += 1
    if num > max:
        max = num

print(f'сумма: {total_sum}')
print(f'положительных: {positive_count}')
print(f'максимум: {max}')
