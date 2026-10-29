def check_palindrome_loop(text: str) -> None:
    cleaned = ''.join(ch.lower() for ch in text if ch != ' ')
    if not cleaned:
        print("Нет текста")
        return
    n = len(cleaned)
    is_palindrome = True

    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
if __name__ == "__main__":
    user_input = input("Введите текст: ")
    check_palindrome_loop(user_input)
