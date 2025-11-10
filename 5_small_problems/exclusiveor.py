"""
The or operator returns a truthy value if either or both of its operands 
are truthy, a falsy value if both operands are falsy. The and operator 
returns a truthy value if both of its operands are truthy, and a falsy value 
if either operand is falsy. This works great until you need only one of two 
conditions to be truthy, the so-called exclusive or, also known as xor 
(pronounced "ECKS-or").

In this exercise, you will write an xor function that takes two arguments, 
and returns True if exactly one of its arguments is truthy, False otherwise.

Problem:
- Write a function that take two arguments
- Retrun true if just one of the arguments is truthy, otherwise false

Example
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

Data
- input: Anything
- Output: Boolean

Algorithm:
- Boolean values are just 0s and 1s
- We can return true is the sum of the values is 1
- Add the values togther using bool()
- Return true if the sum is 1

"""

def xor(thing1, thing2):
    if sum([bool(thing1), bool(thing2)])== 1:
        return True
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)