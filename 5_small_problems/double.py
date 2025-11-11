"""
Write a function that returns the number provided as an argument 
multiplied by two, unless the argument is a double number. If the 
argument is a double number, return the double number as-is.

"""

def twice(n):
    len_n = len(str(n))
    midpoint = len_n // 2
    str_n = str(n)

    left_side = str_n[:midpoint]
    right_side = str_n[midpoint:]

    if left_side == right_side:
        return n
    else:
        return n * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True