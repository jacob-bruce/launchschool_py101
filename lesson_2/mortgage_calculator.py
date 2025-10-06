# Import json and datetime
import json
from datetime import date
from dateutil.relativedelta import relativedelta

# Import language file
with open('mortgage_messages.json', 'r') as file:
    MORTGAGE_MESSAGES = json.load(file)

# Establish default language
DEFAULT_LANGUAGE = 'English'

# Define functions to get messages from language file
def get_message(language_key, message_key):
    return MORTGAGE_MESSAGES[language_key][message_key]

def prompt(message_key):
    message = get_message(USER_LANGUAGE, message_key)
    print(f'==> {message}')

# Define functions to be used multiple times
def invalid_negative_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

def invalid_positive_number(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

# Select language
print("""==> Select language
        1) English 
        2) Espanol 
        3) 中文""")

language_choice = input()

while language_choice not in ['1', '2', '3']:
    prompt('invalid_language')
    language_choice = input()

match language_choice:
    case '1':
        USER_LANGUAGE = 'English'
    case '2':
        USER_LANGUAGE = 'Spanish'
    case '3':
        USER_LANGUAGE = 'Mandarin'

# Welcome the user
prompt('welcome')

# Ask the user for the loan amount and convert to float
while True:
    prompt('what_is_loan_amount')
    loan_amount = input()

    while invalid_negative_number(loan_amount):
        prompt('invalid_number')
        loan_amount = input()

    loan_amount = float(loan_amount)

# Ask the user for the APR and convert to float
    prompt('what_is_annual_rate')
    monthly_rate = input()

    while invalid_positive_number(monthly_rate):
        prompt('invalid_number')
        monthly_rate = input()

    monthly_rate = float(monthly_rate) / 12

# Ask the user for the loan duration and convert to float
    prompt('what_is_loan_duration')
    monthly_loan_duration = input()

    while invalid_negative_number(monthly_loan_duration):
        prompt('invalid_number')
        monthly_loan_duration = input()

    monthly_loan_duration = float(monthly_loan_duration)

# Calculate the monthly payment
    if monthly_rate > 0:
        monthly_payment = loan_amount * (
            monthly_rate /
            (1 - (1 + monthly_rate) ** (-monthly_loan_duration))
        )
    else:
        monthly_payment = loan_amount / monthly_loan_duration

# Print monthly payment
    start_date = date.today()
    payoff_date = (
        start_date
        + relativedelta(months =+int (monthly_loan_duration))
        )
    print(
        f"{MORTGAGE_MESSAGES[USER_LANGUAGE]['your_payment_amount']}"
        f"${monthly_payment:,.2f}.\n"
        f"{MORTGAGE_MESSAGES[USER_LANGUAGE]['your_payoff_date']} "
        f"{payoff_date.strftime('%B %Y')}\n"
    )

# Ask user if they would like to perform another operation
    prompt('another_operation')
    answer = input()
    while answer not in ['1', '2']:
        prompt('invalid_choice')
        answer = input()

    if answer != '1':
        break