"""
Write a function that determines the mean (average) of the three 
scores passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'

P:
- take three integers
- find average
- return letter grade

E:
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

D:
- input: three integers
- output: string (grade)

A:
- Use if/elif/else tree to assign average grade to letter grade
"""

def get_grade(grade1, grade2, grade3):
    score = (grade1 + grade2 + grade3) / 3

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'D'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True