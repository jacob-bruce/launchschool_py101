"""
Write a function that takes a string argument and returns 
a new string that contains the value of the original string 
with all consecutive duplicate characters collapsed into a single character.

P:
- Take a string
- Return new string that eliminates the repeated letteres

E:
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

D:
- input: string
- Ouput: string

A:
- We could loop through and compare the an index with the previous index


"""

def crunch(text):
    if not text:
        return ''
    result = [text[0]]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            result.append(text[i])
    return ''.join(result)

print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')