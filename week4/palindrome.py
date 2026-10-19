def is_letter(ch: str)-> bool:
    return ch.isalpha()

def is_palindrome(text: str) -> bool:
    cleaned_texts = [ch.lower() for ch in text if is_letter(ch)]
    cleaned_text = "".join(cleaned_texts)
    i, j = 0, len(cleaned_text) - 1

    while i < j:
        if cleaned_text[i] != cleaned_text[j]:
            return False
        i += 1
        j -= 1

    return True

print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Hello, World!"))
