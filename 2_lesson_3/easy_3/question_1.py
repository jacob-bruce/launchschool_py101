# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers)

numbers = [1, 2, 3, 4]

for number in numbers:
    numbers.remove(number)
    print(numbers)

