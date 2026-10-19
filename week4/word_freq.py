def count_words(words: list[str]) -> dict[str, int]:
    output = {}
    cleaned_words = [word.lower() for word in words]
    for word in cleaned_words:
        output[word] = cleaned_words.count(word)
    return output


def get_words(sentence: str) -> list[str]:
    word = ""
    words = []

    for ch in sentence:
        if ch.isalpha():
            word += ch
        elif ch == " ":
            words.append(word)
            word = ""

    if word != "":
        words.append(word)

    return words

def most_freq(freq: dict[str, int]) -> tuple[str, int]:
    longest_word, highest = "", -1

    for word, count in freq.items():
        if count > highest:
            longest_word = word
            highest = count

    return longest_word, highest

freq = count_words(get_words("Python is fun, and Python is powerful!"))
word, word_count = most_freq(freq)
print(f"Most frequent word: {word} ({word_count})")
