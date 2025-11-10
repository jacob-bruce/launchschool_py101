def factors(number):
    divisor = 1
    result = []
    while divisor <= number:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor += 1
    return result

print(factors(20))