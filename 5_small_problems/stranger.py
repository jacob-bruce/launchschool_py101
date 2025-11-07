"""
Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, 
will produce a person's name. The dictionary will contain two keys, "title" 
and "occupation", and the appropriate values. Your function should return 
a greeting that uses the person's full name, and mentions the person's title.

Problem:
- Take a list and a dictionary
- List is someone;s name
- Dicionary is their title
- Return a greeting with the person's full name and title

Assumptions:
- List will have 2+ elements that when joined with spaces form a person's name
- Dictionary has two keys title and occupation

Example:
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

Data:
- input: list and dictionary
- output: string

Algorithm:
- Can actually just do return value as an f-string

"""

def greetings(full_name_lst, occupation_dict):
    return (f"Hello, {' '.join(full_name_lst)}! Nice to have a "
            f"{occupation_dict['title']} {occupation_dict['occupation']} around.")

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)