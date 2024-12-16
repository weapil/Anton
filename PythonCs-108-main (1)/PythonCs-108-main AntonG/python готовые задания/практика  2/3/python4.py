def average_grade(Student):
    return sum(Student['grades']) / len(Student['grades'])
student = {
    'name': 'Islam Moldabaev',
    'age': 20,
    'grades': [88, 92, 79, 85, 90]
}
average_student_grade = average_grade(student)
print("Средняя оценка студента:", average_student_grade)
