num1 = input("Input: ")
operator = input("Operator: ")
num2 = input("Input: ")

def calculator(num1: int, num2: int, operator: str):
    if operator == '*':
        return num1 * num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

try:
    n1, n2 = int(num1), int(num2)
    print("Result:", calculator(n1, n2, operator))
except:
    print("One or both input aren't valid numbers")