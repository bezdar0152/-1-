n = int(input())
count = 0
total = 0

for _ in range(n):
    x = int(input())
    if abs(x) > 5:
        count += 1
        total += x

print(count, total)
