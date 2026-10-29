def replace_colons(text: str) -> None:
    count = text.count(':')
    new_text = text.replace(':', '-')
    print(f"Количество замен: {count}")
    print(f"Новая строка: {new_text}")
if __name__ == "__main__":
    user_input = input("Введите строку: ")
    replace_colons(user_input)
