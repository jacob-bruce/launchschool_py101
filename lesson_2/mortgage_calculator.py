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

def get_loan_amount():
    prompt('what_is_loan_amount')
    loan_amount = input()

    while invalid_negative_number(loan_amount):
        prompt('invalid_number')
        loan_amount = input()

    loan_amount = float(loan_amount)
    return loan_amount

def get_interest_rate():
    prompt('what_is_annual_rate')
    monthly_rate = input()

    while invalid_positive_number(monthly_rate):
        prompt('invalid_number')
        monthly_rate = input()

    monthly_rate = float(monthly_rate) / 12
    return monthly_rate

def get_loan_duration():
    prompt('what_is_loan_duration')
    monthly_loan_duration = input()

    while invalid_negative_number(monthly_loan_duration):
        prompt('invalid_number')
        monthly_loan_duration = input()

    monthly_loan_duration = float(monthly_loan_duration)
    return monthly_loan_duration

def calculate_payment(amount, rate, duration):
    if rate > 0:
        monthly_payment = amount * (
            rate /
            (1 - (1 + rate) ** (-duration))
        )
    else:
        monthly_payment = amount / duration
    return monthly_payment

def print_result(loan_duration, monthly_payment):
    start_date = date.today()
    payoff_date = (
        start_date
        + relativedelta(months =+int(loan_duration))
        )
    print(
        f"{MORTGAGE_MESSAGES[USER_LANGUAGE]['your_payment_amount']}"
        f"${monthly_payment:,.2f}.\n"
        f"{MORTGAGE_MESSAGES[USER_LANGUAGE]['your_payoff_date']} "
        f"{payoff_date.strftime('%B %Y')}\n"
    )

def perform_another_calculation():
    prompt('another_operation')
    answer = input()
    while answer not in ['1', '2']:
        prompt('invalid_choice')
        answer = input()
    return answer

# Select language
print("""==> Select language
        1) English 
        2) Espanol 
        3) 中文""")

language_choice = input()

while language_choice not in ['1', '2', '3']:
    print(MORTGAGE_MESSAGES[DEFAULT_LANGUAGE]['invalid_language'])
    language_choice = input("==> ")

match language_choice:
    case '1':
        USER_LANGUAGE = 'English'
    case '2':
        USER_LANGUAGE = 'Spanish'
    case '3':
        USER_LANGUAGE = 'Mandarin'

# Welcome the user
prompt('welcome')

# Main loop
while True:
    user_loan_amount = get_loan_amount()
    user_monthly_rate = get_interest_rate()
    user_monthly_loan_duration = get_loan_duration()
    user_monthly_payment = calculate_payment(
        user_loan_amount,
        user_monthly_rate,
        user_monthly_loan_duration
        )
# Print monthly payment
    print_result(user_monthly_loan_duration, user_monthly_payment)
# Ask user if they would like to perform another operation
    if perform_another_calculation() !=  '1':
        break