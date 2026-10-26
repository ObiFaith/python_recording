def remove_space_and_capitalise(sentence: str):
    first_letter = sentence[0].upper()
    capitalised, removed_space = [first_letter], [first_letter]

    i = 1
    while i < len(sentence):
        capitalised.append(sentence[i])

        if sentence[i] != ' ':
            removed_space.append(sentence[i])

        if sentence[i] == ' ' and 'a' <= sentence[i+1] <= 'z':
            letter = chr(ord(sentence[i+1]) - 32)
            capitalised.append(letter)
            removed_space.append(letter)

            i += 2
        else:
            i += 1
    return "".join(capitalised), "".join(removed_space)

capitalised, removed_space_in_capitalised = remove_space_and_capitalise("hello world from python")
print(f'Capitalized: "{capitalised}"', f'No Spaces: "{removed_space_in_capitalised}"', sep="\n")
