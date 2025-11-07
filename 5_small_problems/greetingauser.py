"""
Write a program that asks for user's name, then greets the user. 
If the user appends a ! to their name, the computer will yell the 
greeting (print it using all uppercase).

Problem:
- Take input from the user "What is your name?"
- Make sure it's a string
- If there is an explamation point, respond in all caps

Questions?
- Empty string?
- Input of non-strings? Can we assume input is a string?

Example:
What is your name? Sue
Hello Sue.

What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?

Data:
- input: string
- output: string

Algorithm:
- Input
- Check to make sure is a string
- If string, check for exclamation point (use .find)
- If exclamation point reponse in all caps
"""

def greeting():
    name = input("What is your name? ").strip()
    if name.endswith('!'):
        print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
    else:
        print(f'Hello {name}.')

greeting()

