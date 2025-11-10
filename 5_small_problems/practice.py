# You’re given a list of student grade records. Each record is a dictionary with a student name and a list of their scores. Write a function that:
#     1.    Loops through the records
#     2.    Calculates the average grade for each student
#     3.    Stores the result in a new dictionary: {name: average_score}
#     4.    Returns the dictionary

import statistics

students = [
    {"name": "Alice", "scores": [80, 90, 100]},
    {"name": "Bob", "scores": [70, 85]},
    {"name": "Charlie", "scores": [60, 65, 70, 75]}
]

def avg_grade_calc(grades: dict):
    avg_grades = {}
    for student_record in grades:
        avg_grades[student_record["name"]] = statistics.mean(student_record['scores'])

    return avg_grades

print(avg_grade_calc(students))

