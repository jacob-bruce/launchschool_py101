def get_positive_int():
    while True:
        user_input = input('Please enter an integer greater than 0: ').strip()
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print('Please enter an integer greater than 0.')
        except ValueError:
            print('Invalid input.')

def get_operation():
    while True:
        operation = input('Enter "s" to compute the sum, or "p" to compute the product. ').strip().lower()
        if operation not in ('s', 'p'):
            print("Invalid input! Please enter 's' for sum or 'p' for product. ")
            continue
        else:
            return operation

def do_operation(choice, user_int):
    if choice == 's':
        return sum(range(1, user_int + 1))
    elif choice == 'p':
        product = 1
        for num in range(1, user_int + 1):
            product *= num
        return product
    else:
      raise ValueError('choice must be "s" or "p"')

user_value = get_positive_int()
user_operation = get_operation()
result = do_operation(user_operation, user_value)

label = 'sum' if user_operation == 's' else 'product'
print(f'The {label} of the integers between 1 and {user_value} is {result}.')