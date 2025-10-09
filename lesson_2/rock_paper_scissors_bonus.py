import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def prompt(message):
    print(f'==> {message}')

def get_choice():
    while True:
        prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
        selection = input().lower()

        if selection in VALID_CHOICES:
            return selection
            break
        elif selection.startswith('r'):
            selection = 'rock'
            return selection
            break
        elif selection.startswith('l'):
            selection = 'lizard'
            return selection
            break
        elif selection.startswith('p'):
            selection = 'paper'
            return selection
            break
        elif selection.startswith('s'):
            prompt("Sorry—can't tell if you meant 'spock' or 'scissors.' Try again?")
            continue
        else:
            prompt("That's not a valid choice.")
            continue

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

prompt("*** Welcome to best of five rock, paper, scissors, lizard, spock! ***")

while True:
    choice = get_choice()

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