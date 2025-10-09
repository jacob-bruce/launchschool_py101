import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if((player == 'scissors' and (computer == 'paper' or computer == 'lizard')) or
       (player == 'paper' and (computer == 'rock' or computer == 'spock')) or
       (player == 'rock' and (computer == 'lizard' or computer == 'scissors')) or
       (player == 'lizard' and (computer == 'spock' or computer == 'paper')) or
       (player == 'spock' and (computer == 'scissors' or computer == 'rock'))):
        prompt('You win!')
    elif ((player == 'scissors' and (computer == 'spock' or computer == 'rock')) or
       (player == 'paper' and (computer == 'scissors' or computer == 'lizard')) or
       (player == 'rock' and (computer == 'paper' or computer == 'spock')) or
       (player == 'lizard' and (computer == 'scissors' or computer == 'rock')) or
       (player == 'spock' and (computer == 'paper' or computer == 'lizard'))):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner(choice, computer_choice)
    
    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("Please enter 'y' or 'n'")
        answer = input().lower()
    
    if answer[0] == 'n':
        break