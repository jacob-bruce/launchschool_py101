"""
Given a string that consists of some words and an assortment 
of non-alphabetic characters, write a function that returns 
that string with all of the non-alphabetic characters replaced 
by spaces. If one or more non-alphabetic characters occur in a 
row, you should only have one space in the result (i.e., the
result string should never have consecutive spaces).

P:
- Take a string
- Remove all non-alpha characters and replace with one space

E:
print(clean_up("---what's my +*& line?") == " what s my line ") # True

D:
- Input: String
- O: String

A:
- Check if the character isalpha
    - if it isalpha, add it to result
- if the character is not alpha
    - if it and the last character are not a space
- replace it with a space


- Use a for loop to loop through the string
- Check if each char is alpha using .isalpha
- I think we need to check the previous character as well to make sure there aren't two spaces
"""

def clean_up(s):
    prev = None
    result = ''
    
    for char in s:
        if char.isalpha():
            result += char
            prev = char
        elif not char.isalpha() and prev != ' ':
            result += ' '
            prev = ' '
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
