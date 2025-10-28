# Write a function that takes one integer argument and 
# returns True when the number's absolute value is odd, 
# False otherwise.

def odd_number_identifer(user_integer):
    if user_integer % 2 != 0:
        return True
    else:
        return False

print(odd_number_identifer(303))    # True
print(odd_number_identifer(1000))   # False