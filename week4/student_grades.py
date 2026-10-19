students = [
    {
        "name": "Sam",
        "scores": [80, 90]
    },
    {
        "name": "David",
        "scores": [55, 60]
    }
]

def get_student_grade(average: float):
    if 70 <= average <= 100:
        return "A"
    elif 60 <= average <= 69:
        return "B"
    elif 50 <= average <= 59:
        return "C"
    elif 45 <= average <= 49:
        return "D"
    elif 40 <= average <= 45:
        return "E"
    elif 0 <= average <= 39:
        return "F"

student_names = [student["name"] for student in students if "name" in student]
students_average = list(map(lambda student: sum(student["scores"]) / len(student["scores"]), students))
student_grade = list(map(lambda student_average: get_student_grade(student_average), students_average))


for i in range(len(students)):
    print(f"{student_names[i]} -> Average: {students_average[i]} -> Grade: {student_grade[i]}")
