"""
Write a function that computes the sum of all numbers 
between 1 and some other number, inclusive, that are 
multiples of 3 or 5. For instance, if the supplied number is 20,
 the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

Problem:
- Given a number
- Find all the numbers between one and that number inclusive that are divisible by 3 and 5
- Find the sum of these numbers

Example:
- Input: 20
- Output: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20

Data Structure:
- Add all numbers divisible by 3 or 5 to a list

Algorithm:
- Create an empty list
- Loop through all numbers between 1 and the number
- Add the numbers to the list
- Sum the list

"""

def multisum(user_num):
    num_lst = []
    for num in range(1, user_num + 1):
        if num % 5 == 0 or num % 3 == 0:
            num_lst.append(num)
    return sum(num_lst)

print(multisum(20))