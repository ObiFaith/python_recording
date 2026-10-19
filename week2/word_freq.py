word_dict = {}
words = input("Input: ")

for word in words.split():
    word_lower = word.lower()
    word_dict[word_lower] = word_dict.get(word_lower, 0) + 1

print("\nOutput:\n")
for word, count in word_dict.items():
    print(f"{word}: {count}\n")
