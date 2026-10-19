def run_length_encoding(data: str) -> str:
    count = 1
    output = []

    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            output.extend([data[i], str(count)])
            count = 1

    output.extend([data[-1], str(count)])
    return "".join(output)

def run_length_decoding(data: str):
    output = []
    for i in range(1, len(data), 2):
        l = [data[i - 1]] * int(data[i])
        output.extend(l)
    return "".join(output)



print(run_length_decoding("a3b2c1"))
print(run_length_decoding("a1b1c1d1"))
print(run_length_decoding("a3"))
print(run_length_decoding("a2b2a2"))
# print(run_length_encoding("aaabbc"))
# print(run_length_encoding("abcd"))
# print(run_length_encoding("aaa"))
# print(run_length_encoding("aabbaa"))
