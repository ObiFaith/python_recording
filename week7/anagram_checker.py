def anagram_checker(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    str1_dict, str2_dict = {}, {}

    for i in range(len(str1)):
        cleaned_char1, cleaned_char2 = str1[i].lower(), str2[i].lower()
        str1_dict[cleaned_char1] = str1_dict.get(cleaned_char1, 0) + 1
        str2_dict[cleaned_char2] = str2_dict.get(cleaned_char2, 0) + 1

    return str1_dict == str2_dict

str1 = "hello"
str2 = "world"

output = "Anagram" if anagram_checker(str1, str2) else "Not an anagram"
print(output)
