import re
def normalize_text(text: str):
    stripped = text.strip()    
    normalized = re.sub(r'\s+', ' ', stripped)    
    return normalized
if __name__ == "__main__":
    input_text = input("Введите строку: ")   
    original_length = len(input_text)
    normalized_text = normalize_text(input_text)
    new_length = len(normalized_text)
    word_count = len(normalized_text.split())    
    print(f"Исходная длина: {original_length}")
    print(f"Новая длина: {new_length}")
    print(f"Нормализованный текст: {normalized_text}")
    print(f"Количество слов: {word_count}")
