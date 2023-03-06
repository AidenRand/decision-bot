import random

def make_game_response(message):
    user_input = message.strip().lower()

    # generate random computer choice
    num = random.randint(1, 3)
    match num:
        case 1:
            comp_choice = 'rock'
        case 2:
            comp_choice = 'paper'
        case 3:
            comp_choice = 'scissors'

    # compare user input and computer choice
    if (user_input == comp_choice):
            result = 'Tie!'
    elif (user_input == 'rock' and comp_choice == 'scissors'
        or user_input == 'paper' and comp_choice == 'rock'
        or user_input == 'scissors' and comp_choice == 'paper'):
        result = 'You Win :-]'
    elif (user_input == 'scissors' and comp_choice == 'rock'
        or user_input == 'rock' and comp_choice == 'paper'
        or user_input == 'paper' and comp_choice == 'scissors'):
         result = 'You lost :-['

    return result