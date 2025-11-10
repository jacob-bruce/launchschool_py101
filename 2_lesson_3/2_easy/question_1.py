# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
new_list = []

# Method 1: Custom for loop
for number in numbers:
    new_list.insert(0, number)

print(new_list)
print(numbers)

# Method 2: Slicing
reversed_numbers = numbers[::-1]

print(reversed_numbers)

# Method 3: Reversed Function
reversed_numbers_2 = list(reversed(numbers))

print(reversed_numbers_2)