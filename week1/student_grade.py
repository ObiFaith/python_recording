students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],

    
    ["Faith", 45, 60, 28],
]

def get_grade(average: float) -> str:
    result = ''
    if 70 <= average <= 100:
        result = 'A'
    elif 60 <= average <= 69:
        result = 'B'
    elif 50 <= average <= 59:
        result = 'C'
    elif 45 <= average <= 49:
        result = 'D'
    elif 40 <= average <= 49:
        result = 'E'
    elif 0 <= average <= 39:
        result = 'F'
    return result

for student in students:
    name, score_1, score_2, score_3 = student
    average = f"{((score_1 + score_2 + score_3) / 3):.2f}"
    grade = get_grade(float(average))
    print(f"{name} - Average: {average} - Grade: {grade}")