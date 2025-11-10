import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
computer_score = 0
player_score = 0
ties = 0

def prompt(message):
    print(f'==> {message}')

def get_choice():
    while True:
        prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
        selection = input().lower().strip()

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
        elif selection.startswith('sp'):
            selection = 'spock'
            return selection
            break
        elif selection.startswith('sc'):
            selection = 'scissors'
            return selection
            break
        elif selection.startswith('s'):
            prompt(
                "Sorry—can't tell if you meant 'spock' or 'scissors.'" 
                "Try 'sp' for 'spock' and 'sc' for 'scissors'?")
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

def keep_score(player, computer):
    global computer_score 
    global player_score
    global ties

    if((player == 'scissors' and (computer == 'paper' or computer == 'lizard')) or
       (player == 'paper' and (computer == 'rock' or computer == 'spock')) or
       (player == 'rock' and (computer == 'lizard' or computer == 'scissors')) or
       (player == 'lizard' and (computer == 'spock' or computer == 'paper')) or
       (player == 'spock' and (computer == 'scissors' or computer == 'rock'))):
       player_score += 1
    elif ((player == 'scissors' and (computer == 'spock' or computer == 'rock')) or
       (player == 'paper' and (computer == 'scissors' or computer == 'lizard')) or
       (player == 'rock' and (computer == 'paper' or computer == 'spock')) or
       (player == 'lizard' and (computer == 'scissors' or computer == 'rock')) or
       (player == 'spock' and (computer == 'paper' or computer == 'lizard'))):
        computer_score += 1
    else:
        ties += 1

def print_score():
    global computer_score 
    global player_score
    global ties

    player_score_string = ''
    computer_score_string = ''
    score_string = ''

    if player_score == 1:
        player_score_string = f"You have {player_score} point."
    else:
        player_score_string = f"You have {player_score} points."

    if computer_score == 1:
        computer_score_string = f"The computer has {computer_score} point."
    else:
        computer_score_string = f"The computer has {computer_score} points."

    prompt(f"{player_score_string} {computer_score_string}")

def play_again():
    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("Please enter 'y' or 'n'")
        answer = input().lower()
    
def computer_wins():
    global computer_score 
    global player_score
    global ties

    prompt(
        f"Ah too bad! The computer wins {computer_score} to {player_score}. "
        f"You tied {ties} times."
        )
    
    play_again()

def player_wins():
    global computer_score 
    global player_score
    global ties

    prompt(
        f"The force is strong with this one! "
        f"You beat the computer {player_score} to {computer_score}. "
        f"You tied {ties} times."
        )
    
    play_again()

prompt("*** Welcome to best of five rock, paper, scissors, lizard, spock! Good luck! ***")

while computer_score < 3 and player_score < 3:
    choice = get_choice()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner(choice, computer_choice)

    keep_score(choice, computer_choice)
    
    print_score()

if computer_score == 3:
    computer_wins()
else:
    player_wins