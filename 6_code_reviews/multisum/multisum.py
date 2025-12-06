"""
Write a function that computes the sum of all numbers between 1 and some other number, 
inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, 
the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

PROBLEM:
- Write a function that adds up multiples of 3 or 5 between 0 and a given number.

EXAMPLE:
- If the user inputs "20" the function would add up 3, 5, 6, 9, 10, 12, 15, 18, 20 = 98

ALGORITHM:
- We could just use a for loop with modulus and a range object to loop through, and a tracker
variable
- I think this could also be done with the sum function and a comprehension
"""
def multisum(end_num):
    return sum([num for num in range(1, end_num + 1) if num % 3 == 0 or num % 5 ==0])

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)