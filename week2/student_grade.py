students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["John", 77, 88, 66]
]

def calculate_grade(average: float):
    if 70 <= average <= 100:
        return 'A'
    elif 60 <= average <= 69:
        return 'B'
    elif 50 <= average <= 59:
        return 'C'
    elif 45 <= average <= 49:
        return 'D'
    elif 40 <= average <= 44:
        return 'E'
    elif 0 <= average <= 39:
        return 'F'
    else:
        return ''

for student in students:
    name, score1, score2, score3 = student
    average = f"{((score1 + score2 + score3) / 3):.2f}"
    grade = calculate_grade(float(average))

    print(f"{name} -> Average: {average} -> Grade: {grade}")