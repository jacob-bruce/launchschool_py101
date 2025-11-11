"""
Write a function that takes two arguments, a string and a positive integer, 
then prints the string as many times as the integer indicates.

P:
- take two arguments: string, and positive int
- print string as many times as the integer

E:
repeat('Hello', 3)
Hello
Hello
Hello

D:
- input: string, int
- output: string 

A:
- use for loop
- go through int times
"""

def repeat(s, num):
    for _ in range(num):
        print(s)

repeat('Hello', 3)
