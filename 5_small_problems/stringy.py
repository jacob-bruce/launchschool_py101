#Write a function that takes one argument, a positive integer, 
# and returns a string of alternating '1's and '0's, always 
# starting with a '1'. The length of the string should match the given integer.

"""
Example:
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

Algorithm:
- start with a 1
- can use a for loop to print 1 on even loops
"""

def stringy(n):
    result = ''
    for _ in range(n):
        if _ % 2:
            result += '0'
        else:
            result += '1'
    return result

print(stringy(6))
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True