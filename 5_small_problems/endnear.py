"""
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.

Problem:
- You are given a string.
- Find the next to last word
- Don't include non-blank characters
- Anything can be a word, except non-blank
- Assume at least two words

Example:
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

Data Type:
- Input: string
- Intermediary: List
- Output: string

Algorithm:
- Create an empty list
- Assign the different words of the string to the list using split
- return list[-2]
"""

def penultimate(s):
    word_lst = []
    word_lst = s.split(' ')
    return word_lst[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")