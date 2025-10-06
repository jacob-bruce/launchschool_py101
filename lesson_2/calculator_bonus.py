# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
LANGUAGE = 'zh'
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def get_message(message, LANGUAGE):
    return MESSAGES[LANGUAGE][message]

prompt(get_message('welcome', LANGUAGE))

while True:
    prompt(get_message('first_number', LANGUAGE))
    number1 = input()

    while invalid_number(number1):
        prompt(get_message('invalid_number', LANGUAGE))
        number1 = input()

    prompt(get_message('second_number', LANGUAGE))
    number2 = input()

    while invalid_number(number2):
        prompt(get_message('invalid_number', LANGUAGE))
        number2 = input()

    prompt(get_message('choose_operation', LANGUAGE))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(get_message('reject_operation', LANGUAGE))
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'{get_message('result', LANGUAGE)} {output}')

    # Ask user if they would like to perform another operation
    prompt(get_message('another_operation', LANGUAGE))
    answer = input()
    while answer not in ['1', '2']:
        prompt(get_message('invalid_choice', LANGUAGE))
        answer = input()

    if answer != '1':
        break