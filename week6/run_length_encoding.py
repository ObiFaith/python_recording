def run_length_encoding(data: str) -> str:
    count = 1
    output = []

    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            output.append(f"{data[i]}{count}")
            count = 1

    output.append(f"{data[-1]}{count}")
    return "".join(output)

def run_length_decoding(data: str):
    output = []
    for i in range(1, len(data), 2):
        output.append(data[i - 1] * int(data[i]))
    return "".join(output)



print(run_length_decoding("a3b2c1"))
print(run_length_decoding("a1b1c1d1"))
print(run_length_decoding("a3"))
print(run_length_decoding("a2b2a2"))
# print(run_length_encoding("aaabbc"))
# print(run_length_encoding("abcd"))
# print(run_length_encoding("aaa"))
# print(run_length_encoding("aabbaa"))
