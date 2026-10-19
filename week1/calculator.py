first_number = int(input("First number: "))
operator = input("Operator: ")
second_number = int(input("Second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("Result:", result)
