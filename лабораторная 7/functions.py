def sum_digits(n):
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
def average(nums):
    if not nums:
        return None
    return sum(nums) / len(nums)
def normalize_text(t):
    return " ".join(t.lower().split())
def select_numbers(nums, t):
    res = 
    for x in nums:
        if abs(x) <= t:
            res.append(x)
    return res
