def count_letters(text: str) -> tuple[int, int]:
    vowels, consonants = 0, 0

    for char in text:
        lower_char = char.lower()
        if 'a' <= lower_char <= 'z':
            if lower_char in {"a", "e", "i", "o", "u"}:
                vowels += 1
            else:
                consonants += 1

    return (vowels, consonants)

print(count_letters("Hello, World 123"))
print(count_letters("AEIOU"))
print(count_letters("rhythm"))
print(count_letters(""))
