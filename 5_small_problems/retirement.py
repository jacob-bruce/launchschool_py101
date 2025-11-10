"""
Build a program that displays when the user will retire and 
how many years she has to work till retirement.


What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!

Problem:
- Take input from the user: age, retirment age
- Take today's year
- print retirement statement

Example:
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!

Data Type:
- Input: string
- Output: string

Algorithm:
- Use datetime for the current year

"""
from datetime import date

current_year = date.today().year

def get_age():
    while True:
        age = input("What is your age? ")
        try:
            return int(age)
        except ValueError:
            print("Please enter a valid age!")

def get_retirment_age():
    while True:
        retirement_age = input("At what age would you like to retire? ")
        try:
            return int(retirement_age)
        except ValueError:
            print("Please enter a valid retirement age!")

user_age = get_age()
user_retirement_age = get_retirment_age()
years_left = user_retirement_age - user_age
print(f"It's {current_year}. You will retire in {current_year + years_left}.\n"
      f"You have only {years_left} years of work to go!")