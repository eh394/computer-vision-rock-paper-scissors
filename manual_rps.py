import random


def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice():
    user_choice = input('Please enter Rock, Paper or Scissors: ')
    return user_choice

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print('You lost')
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
        print('You won!')
    else:
        print('It is a tie!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()


# import random

# choices = ['rock', 'paper', 'scissors']

# def get_computer_choice():
#     computer_choice = random.choice(choices)
#     print(computer_choice)
#     return computer_choice

# def get_user_choice():
#     while True:
#         user_choice = input('Please enter rock, paper or scissors: ')
#         if user_choice.lower() not in choices:
#             print('Invalid entry. Please enter rock, paper, or scissors.')
#         else:
#             user_choice = user_choice.lower()
#             print(user_choice)
#             break    
#     return user_choice

# get_computer_choice()
# get_user_choice()
