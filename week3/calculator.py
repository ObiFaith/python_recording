def calculate(operand1,operator, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            return "Cannot divide by zero"
        return operand1 / operand2
    else:
        return "Invalid operator"

result = 0.0
prev_numbers = [0.0]

while True:
    user_input = input("Input: ").strip(" ")

    if user_input.lower() == "undo" and len(prev_numbers) > 1:
        prev_numbers.pop()
        result = prev_numbers[-1]
        print(result)
        continue

    try:
        operator, operand = user_input.split(" ")
        result = calculate(result, operator, float(operand))
        print("Result: ", result)

        if isinstance(result, float):
            prev_numbers.append(result)
        else:
            result = prev_numbers[-1]
    except:
        print("Invalid format (eg; + 5)")
