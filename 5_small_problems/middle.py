"""
Write a function that takes a non-empty string argument and returns 
the middle character(s) of the string. If the string has an odd length, 
you should return exactly one character. If the string has an even length, 
you should return exactly two characters.

Problem:
- Take a string (assume string, non-empty)
- return the middle character or characters

Example:
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x") 

Data:
- Input: string
- Output: string

Algorithm:
- Get the string using input which ensures string
- Count the length of the string. Save as variable.
- If its odd return the middle character using slicing and division
"""

def center_of(s):
    len_s = len(s)
    if len_s % 2 == 0:
        middle_char = len_s // 2
        return s[middle_char - 1:middle_char + 1]
    else:
        middle_char = (len_s // 2)
    return s[middle_char]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x") 