def variant_8(text: str) -> None:
    raw_words = text.split()
    cleaned_words = []  
    for w in raw_words:
        cleaned = w.strip(".,!?;:")
        if cleaned:
            cleaned_words.append(cleaned.lower())
    result = [w for w in cleaned_words if w.count('а') == 1]
    if not result:
        print("нет совпадений")
        print(0)
    else:
        for w in result:
            print(w)
        print(len(result))
if __name__ == "__main__":
    user_input = input("Введите строку: ")
    variant_8(user_input)
