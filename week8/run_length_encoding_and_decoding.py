def rle_encode(text: str) -> str:
    if not text:
        return text

    i, count, output = 0, 1, []

    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            count += 1
        else:
            output.append(f"{text[i]}{count}")
            count = 1
        i += 1

    output.append(f"{text[i]}{count}")
    return "".join(output)

# print(rle_encode("aaabbc"))
# print(rle_encode("aaaaaaaaaaaab"))
# print(rle_encode(""))

def rle_decode(encoded: str):
    if not encoded:
        return encoded

    i = count = 0
    char, output = "", []

    while i < len(encoded):
        ch = encoded[i]
        if ch.isdigit():
            count = (count * 10) + int(ch)
        else:
            output.append(char * count)
            char, count = ch, 0
        i += 1

    output.append(char * count)
    return "".join(output)


print(rle_decode("a12b1"))
print(rle_decode("a3b2c1"))
