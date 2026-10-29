def sum_digits(number: int) -> int:
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total
def average(numbers: list) -> float | None:

    if not numbers:
        return None
    return sum(numbers) / len(numbers)
def normalize_text(text: str) -> str:
    text = text.lower()
    words = text.split()
    return " ".join(words)
