alphabets = { "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,"s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

def make_shifter(shift: int):
    def shift_word(word: str) -> str:
        shifted_ch = []

        for char in word:
            ch = char.lower()
            if alphabets.get(ch, None) == None:
                shifted_ch.append(ch)
                continue

            idx = (alphabets[ch] + shift) % 26

            idx_key = next((k for k, v in alphabets.items() if v == idx))
            if char.isupper():
                idx_key = idx_key.upper()
            shifted_ch.append(idx_key)

        return "".join(shifted_ch)

    return shift_word

print(make_shifter(1)("hello"))
print(make_shifter(2)("xyz"))
print(make_shifter(3)("hello, world!"))
print(make_shifter(-26)("aIfmmp"))