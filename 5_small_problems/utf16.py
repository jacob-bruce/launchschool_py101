"""
Write a function that determines and returns the UTF-16 string value 
of a string passed in as an argument. The UTF-16 string value is the 
sum of the UTF-16 values of every character in the string. (You may use 
ord to determine the UTF-16 value of a character.)

Problem:
- Take a string
- Find the UTF-16 values of each character in the string
- Find sum of those string values

Assumptions:
- Only string inputs

Example:
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

Data Structure:
- Need empty list to store string UTF values

Algoritm
- Loop through the string
- For each character, find the UTF-16 value
- Append the UTF-16 value to a list
- Sum the list

"""

def utf16_value(user_string):
    utf_lst = []
    for char in user_string:
        utf_lst.append(ord(char))
    return sum(utf_lst)

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)