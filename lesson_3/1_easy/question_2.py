# How can you determine whether a given string ends with an exclamation mark (!)? 
# Write some code that prints True or False depending on whether the string 
# ends with an exclamation mark.

def find_exclamation(your_string):
    if your_string[-1] == '!':
        print("Yep, there's an exclamation point!") 
    else:
        print("Doesn't look like there's an exclamation point.")

greeting = 'Howdy!'
other_greeting = 'Hi there'

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

find_exclamation(greeting)
find_exclamation(other_greeting)
find_exclamation(str1)
find_exclamation(str2)

# Better solution:
# print(str1.endswith("!"))  # True
# print(str2.endswith("!"))  # False