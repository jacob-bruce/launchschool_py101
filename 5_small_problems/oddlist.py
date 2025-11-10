"""
Write a function that returns a list that contains every other element 
of a list that is passed in as an argument. The values in the returned 
list should be those values that are in the 1st, 3rd, 5th, and so on elements
of the argument list.

Problem:
- Given a list, return another list with only the odd elements starting 
with the first

Example:
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

Data:
- Input: List
- Output: List

Algorithm
- Create an empty list
- Take the list given as argument
- Add the first element of the list
- Loop through the list -- if % 2 = 0, then add the element because of 0 indexing

"""

def oddities(lst):
    result = []
    for idx in range(0, len(lst), 2):
        result.append(lst[idx])
    return result

print(oddities([2, 3, 4, 5, 6]))
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True