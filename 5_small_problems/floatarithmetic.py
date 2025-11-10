"""
P:
- Prompt user for two floats
- Check to ensure they are floats
- Perform addition, subtraction, product, quotient, floor quotient, remainder, and power. 
-Print result of each

Example:
==> Enter the first number:
3.141592
==> Enter the second number:
2.718282
==> 3.141592 + 2.718282 = 5.859874
==> 3.141592 - 2.718282 = 0.4233100000000003
==> 3.141592 * 2.718282 = 8.539732984944001
==> 3.141592 / 2.718282 = 1.1557270364149121
==> 3.141592 // 2.718282 = 1.0
==> 3.141592 % 2.718282 = 0.4233100000000003
==> 3.141592 ** 2.718282 = 22.45914942746313

Data:
- input: floats
- outpur: float

Algorithm
- Use input to get float from user
- Use try except to ensure it is actually a float
- Use series of f-strings to print results

"""

def float_retriever(prompt):
    while True:
        user_str = input(prompt)
        try:
            return float(user_str)
        except ValueError:
            print("Please enter a valid number.")

def float_operations():
    user_float1 = float_retriever('==> Enter the first number: ')
    user_float2 = float_retriever('==> Enter the second number: ')

    print(f"==> {user_float1} + {user_float2} = {user_float1 + user_float2}\n"
          f"==> {user_float1} - {user_float2} = {user_float1 - user_float2}\n"
          f"==> {user_float1} * {user_float2} = {user_float1 - user_float2}\n"
          f"==> {user_float1} / {user_float2} = {user_float1 / user_float2}\n"
          f"==> {user_float1} // {user_float2} = {user_float1 // user_float2}\n"
          f"==> {user_float1} % {user_float2} = {user_float1 % user_float2}\n"
          f"==> {user_float1} ** {user_float2} = {user_float1 ** user_float2}\n"
    )

float_operations()